import logging
import mimetypes
import os
import smtplib
import ssl
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PySide2.QtCore import QObject, QRunnable, Signal, Slot

from attachment_label import AttachmentLabel

class EmailThreadSignal(QObject):
    invalid_email_column = Signal(str)
    fail_email = Signal(str)
    success_email = Signal(str)


class EmailThread(QRunnable):
    def __init__(self, email_list, email_input):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.email_list = email_list
        self.email_input = email_input
        self.signal = EmailThreadSignal()

    @Slot()
    def run(self):
        context = ssl.create_default_context()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls(context=context)
        server.login(self.email_input['my_email'], self.email_input['password'])
        counter = 1
        for receiver_email in self.email_list:
            if counter % 11 == 0 and counter != 1:
                time.sleep(61)
            try:
                msg = MIMEMultipart()
                msg["From"] = self.email_input['my_email']
                msg["To"] = receiver_email
                msg['Subject'] = self.email_input['subject']
                body_msg = self.email_input['body']
                msg.attach(MIMEText(body_msg, "plain"))
                

                for filename in AttachmentLabel.attachment_list:
                    attachment_name = os.path.basename(filename)
                    mimetype, encoding = mimetypes.guess_type(filename)
                    main_type, sub_type = mimetype.split('/', 1)
                    with open(filename, "rb") as attachment:
                        part = MIMEApplication(attachment.read(), _subtype=sub_type)

                    part.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', attachment_name))
                    msg.attach(part)
                
                server.sendmail(self.email_input['my_email'], receiver_email, msg.as_string())
                self.signal.success_email.emit(receiver_email)

            # except smtplib.SMTPRecipientsRefused:
            #     self.logger.exception("Recipient refused")
            #     self.signal.invalid_email_column.emit(receiver_email)
            #     print('fail', receiver_email)
            except:
                self.logger.exception("Message Send Error")
                self.signal.fail_email.emit(receiver_email)

        server.quit()