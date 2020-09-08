import logging
import smtplib
import ssl

import numpy as np
import pandas as pd
from PySide2.QtCore import QObject, QThreadPool, Signal

from email_thread import EmailThread

class Logic(QObject):
    signal_0 = Signal() # email column
    signal_1 = Signal() # receiver file
    signal_2 = Signal() # password
    signal_3 = Signal() # my email
    signal_4 = Signal() # subject
    sending_start = Signal()
    fail_email = Signal(str)
    success_email = Signal(str)
    sending_done = Signal()
    send_progress = Signal(int)

    def __init__(self, model):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.model = model
        self.is_valid_field_dict = dict()
        self.is_valid_field_dict['is_valid_email_column'] = False
        self.is_valid_field_dict['is_valid_receiver_file'] = False
        self.is_valid_field_dict['is_valid_password'] = False
        self.is_valid_field_dict['is_valid_my_email'] = False
        self.successful_email_counter = 0
        self.unsuccessful_list = []
        self.threadpool = QThreadPool()
        num_email_threads = 5
        self.threadpool.setMaxThreadCount(num_email_threads)
        self.total_email = 0

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
        except smtplib.SMTPAuthenticationError:
            self.signal_2.emit()
            self.signal_3.emit()
            return
        except:
            self.logger.exception("SMTP error")

        email_input = {'my_email' : my_email, 'password' : password,
                'subject' : subject, 'body' : body_msg}


        self.total_email = len(emails)
        num_email_threads = min(5, len(emails))
        emails = np.array_split(emails, num_email_threads)

        self.successful_email_counter = 0
        self.unsuccessful_list = []

        self.sending_start.emit()
        for sublist in emails:
            email_thread = EmailThread(sublist, email_input)
            email_thread.signal.invalid_email_column.connect(self.show_invalid_email_error)
            email_thread.signal.fail_email.connect(self.update_fail_email)
            email_thread.signal.success_email.connect(self.update_successful_email)
            self.threadpool.start(email_thread)

        print('number of active thread', self.threadpool.activeThreadCount())


    def is_sending_done(self):
        num_email_processed = len(self.unsuccessful_list) + self.successful_email_counter
        self.send_progress.emit(num_email_processed / self.total_email * 100)
        if num_email_processed == self.total_email:
            self.sending_done.emit()
            
            unsuccessful_file = open('unsuccessful_emails.txt', 'w')
            unsuccessful_file_string = '\n'.join(self.unsuccessful_list)
            unsuccessful_file.write(unsuccessful_file_string)
            unsuccessful_file.close()
            
            self.logger.info(unsuccessful_file_string)

    def show_invalid_email_error(self):
        self.is_sending_done()
        self.signal_0.emit()

    def update_fail_email(self, email):
        self.unsuccessful_list.append(email)
        self.fail_email.emit(email)
        self.is_sending_done()

    def update_successful_email(self, email):
        self.successful_email_counter += 1
        self.success_email.emit(email)
        self.is_sending_done()

    def check_valid_field(self, compulsory_text):
        is_valid_field = True
        idx = 0
        
        for email_input in self.is_valid_field_dict:
            if compulsory_text[idx]:
                self.is_valid_field_dict[email_input] = True
            else:
                self.is_valid_field_dict[email_input] = False
                getattr(self, 'signal_' + str(idx)).emit()
                is_valid_field = False
            idx += 1
        
        return is_valid_field
