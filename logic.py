import logging
import os
import smtplib
import ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
from PySide2.QtCore import QObject, Signal

from attachment_label import AttachmentLabel

class Logic(QObject):
    signal_0 = Signal() # email column
    signal_1 = Signal() # receiver file
    signal_2 = Signal() # password
    signal_3 = Signal() # my email
    signal_4 = Signal() # subject

    def __init__(self, model):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.model = model
        self.is_valid_field_dict = dict()
        self.is_valid_field_dict['is_valid_email_column'] = False
        self.is_valid_field_dict['is_valid_receiver_file'] = False
        self.is_valid_field_dict['is_valid_password'] = False
        self.is_valid_field_dict['is_valid_my_email'] = False

    def send_email(self, compulsory_text, optional_text, send_with_subject):
        is_valid_field = self.check_valid_field(compulsory_text)
        
        if not is_valid_field:
            return
        
        email_column, receiver_email_file, password, my_email = compulsory_text
        subject, body_msg = optional_text
        
        if send_with_subject and not subject:
            self.signal_4.emit()
            return

        try:
            receiver_df = pd.read_excel(receiver_email_file)
            emails = receiver_df[email_column].to_numpy()
        except KeyError:
            self.signal_0.emit()
            return

        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls(context=context)
            server.login(my_email, password)
            unsuccessful_list = []

            counter = 1

            emails = [emails[i:i + 50] for i in range(0, len(emails), 50)]

            for sublist in emails:
                if counter != 1:
                    time.sleep(61)
                for email in sublist:
                    try:
                        msg = MIMEMultipart()
                        msg["From"] = my_email
                        msg["To"] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body_msg, "plain"))
                        
                        for filename in AttachmentLabel.attachment_list:
                            attachment_name = os.path.basename(filename)
                            with open(filename, "rb") as attachment:
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attachment.read())
                            
                            encoders.encode_base64(part)
                            
                            part.add_header(
                                "Content-Disposition",
                                f"attachment; filename= {attachment_name}",
                            )
                        
                            msg.attach(part)
                        
                        server.sendmail(my_email, email, msg.as_string())
                        print("{}. success: {}".format(counter, email))
                        counter = counter + 1
                    except smtplib.SMTPRecipientsRefused:
                        self.logger.exception("Recipient refused")
                        self.signal_0.emit()
                        unsuccessful_list.append(email)
                    except:
                        self.logger.exception("Message Send Error")
                        print("fail: {}".format(email))
                        unsuccessful_list.append(email)
                    
            server.quit()
            print('finish sending')
        except smtplib.SMTPAuthenticationError:
            self.signal_2.emit()
            self.signal_3.emit()
            return
        
        except:
            self.logger.exception("SMTP error")

    def check_valid_field(self, compulsory_text):
        is_valid_field = True
        idx = 0
        
        for input in self.is_valid_field_dict:
            if compulsory_text[idx]:
                self.is_valid_field_dict[input] = True
            else:
                self.is_valid_field_dict[input] = False
                getattr(self, 'signal_' + str(idx)).emit()
                is_valid_field = False
            idx += 1
        
        return is_valid_field
