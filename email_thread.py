import logging
import mimetypes
import os
import re
import smtplib
import ssl
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PySide2.QtCore import QObject, QRunnable, Signal, Slot

from attachment_label import AttachmentLabel

class EmailThreadSignal(QObject):
    invalid_email_column = Signal(list)
    fail_email = Signal(str, list)
    success_email = Signal(str)
    duration = Signal(float)


class EmailThread(QRunnable):
    def __init__(self, receiver_df, email_input):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.receiver_df = receiver_df
        self.email_input = email_input
        self.signal = EmailThreadSignal()
        self.is_killed = False

    @Slot()
    def run(self):
        context = ssl.create_default_context()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls(context=context)
        server.login(self.email_input['my_email'], self.email_input['password'])
        counter = 0
        start_time_fifty = time.time()
        for _, row in self.receiver_df.iterrows():
            if self.is_killed:
                try:
                    self.logger.info("Thread terminating early")
                    server.quit()
                    return
                except:
                    self.logger.exception("Thread terminating early error")
                    return

            counter += 1

            ## prevent gmail from blocking us
            if counter % 50 == 1 and counter != 1:
                if time.time() - start_time_fifty < 60:
                    time.sleep(60)
                start_time_fifty = time.time()
            try:
                row_dict = row.to_dict()
                receiver_email = row_dict[self.email_input['email_column']]
                msg = MIMEMultipart()
                msg["From"] = self.email_input['my_email']
                msg["To"] = receiver_email
                msg['Subject'] = self.process_placeholder(row_dict, self.email_input['subject'])
                body_msg = self.process_placeholder(row_dict, self.email_input['body'])
                msg.attach(MIMEText(body_msg, "html"))
                
                if self.email_input['personalised_att'] != 'Select personalised attachment (Optional)':
                    personalised_att = row_dict[self.email_input['personalised_att']]
                    personalised_att = re.split('\s*,\s*', personalised_att)
                    self.add_attachments(msg, personalised_att)

                self.add_attachments(msg, AttachmentLabel.attachment_list)
                
                start_time = time.time()
                server.sendmail(self.email_input['my_email'], receiver_email, msg.as_string())
                self.signal.success_email.emit(receiver_email)
                duration = time.time() - start_time
                self.signal.duration.emit(duration)

                if duration < 1:
                    time.sleep(1)

            # except smtplib.SMTPRecipientsRefused:
            #     self.logger.exception("Recipients refused" + str(receiver_email))
            #     self.signal.fail_email.emit(receiver_email)
            except:
                self.logger.exception("Message Send Error: {}".format(receiver_email))
                self.signal.fail_email.emit(receiver_email, row)

        try:
            server.quit()
        except:
            self.logger.exception("Quitting server naturally")

    def kill(self):
        self.is_killed = True

    def process_placeholder(self, row, msg):
        for placeholder, key in re.findall("({{(.+?)}})", msg):
            msg = msg.replace(placeholder, row.get(key, placeholder))
        return msg

    def add_attachments(self, msg, attachment_files):
        for filename in attachment_files:
            attachment_name = os.path.basename(filename)
            mimetype, _ = mimetypes.guess_type(filename)
            _, sub_type = mimetype.split('/', 1)
            with open(filename, "rb") as attachment:
                part = MIMEApplication(attachment.read(), _subtype=sub_type)

            part.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', attachment_name))
            msg.attach(part)