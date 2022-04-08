import logging
import smtplib
import ssl
import os
import re

import numpy as np
import pandas as pd
from PySide2.QtCore import QObject, QThreadPool, Signal

from attachment_label import AttachmentLabel
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
    sending_done = Signal(int, int, str)
    send_progress = Signal(int)
    estimate_time_finish = Signal(int)

    attachment_limit_reached = Signal()
    attachment_byte_limit = 20000000 #20 MB


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
        self.thread_list = []

    def send_email(self, compulsory_text, optional_text, send_with_subject):
        is_valid_field = self.check_valid_field(compulsory_text)
        
        if not is_valid_field:
            return
        
        email_column, receiver_email_file, password, my_email = compulsory_text
        subject, body_msg, personalised_att = optional_text

        if send_with_subject and not subject:
            self.signal_4.emit()
            return

        receiver_df = pd.read_excel(receiver_email_file)
        if email_column not in receiver_df.columns:
            self.signal_0.emit()
            return

        # try:
        #     receiver_df = pd.read_excel(receiver_email_file)
        #     emails = receiver_df[email_column].to_numpy()
        # except KeyError:
        #     self.signal_0.emit()
        #     return
        
        self.logger.info('Start sending')

        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls(context=context)
            server.login(my_email, password)
            server.quit()
        except smtplib.SMTPAuthenticationError:
            self.signal_2.emit()
            self.signal_3.emit()
            return
        except:
            self.logger.exception("SMTP error")

        email_input = {'my_email' : my_email, 'password' : password,
                'subject' : subject, 'body' : body_msg, 'email_column' : email_column,
                'personalised_att' : personalised_att}


        self.total_email = len(receiver_df)
        num_email_threads = min(1, len(receiver_df))
        receiver_df = np.array_split(receiver_df, num_email_threads)

        self.successful_email_counter = 0
        self.unsuccessful_list = []

        self.sending_start.emit()
        for sublist in receiver_df:
            email_thread = EmailThread(sublist, email_input)
            email_thread.signal.invalid_email_column.connect(self.show_invalid_email_error)
            email_thread.signal.fail_email.connect(self.update_fail_email)
            email_thread.signal.success_email.connect(self.update_successful_email)
            email_thread.signal.duration.connect(self.update_estimated_time_finish)
            self.thread_list.append(email_thread)
            self.threadpool.start(email_thread)

    def kill_thread(self):
        for thread in self.thread_list:
            thread.kill()

    def update_estimated_time_finish(self, duration):
        time_remaining = duration * (self.total_email - len(self.unsuccessful_list) - self.successful_email_counter)
        self.estimate_time_finish.emit(int(time_remaining))

            
    def is_sending_done(self):
        num_email_processed = len(self.unsuccessful_list) + self.successful_email_counter
        self.send_progress.emit(num_email_processed / self.total_email * 100)
        if num_email_processed == self.total_email:
            # output excel file to desktop
            unsuccessful_df = pd.DataFrame(self.unsuccessful_list)
            save_path = os.path.join(os.path.expanduser("~"), "Desktop", "unsuccessful_emails.xlsx")
            unsuccessful_df.to_excel(save_path, index=False)
            
            self.sending_done.emit(self.successful_email_counter, len(self.unsuccessful_list), save_path)
            self.thread_list = []
            
            self.logger.info('Send finished')

    def show_invalid_email_error(self):
        self.is_sending_done()
        self.signal_0.emit()

    def update_fail_email(self, email, data_row):
        self.unsuccessful_list.append(data_row)
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
            if not compulsory_text[idx] or compulsory_text[idx] == 'Select email column':
                self.is_valid_field_dict[email_input] = False
                getattr(self, 'signal_' + str(idx)).emit()
                is_valid_field = False
            else:
                self.is_valid_field_dict[email_input] = True
            idx += 1

        if AttachmentLabel.attachment_list_byte_size > Logic.attachment_byte_limit:
            self.attachment_limit_reached.emit()
            is_valid_field = False

        return is_valid_field

    def show_preview(self, compulsory_text, optional_text):
        is_valid_field = self.check_valid_field(compulsory_text)

        if not is_valid_field:
            return ['', 'Unable to preview message. Please fill in all compulsory fields']

        try:
            receiver_email_file= compulsory_text[1]
            receiver_df = pd.read_excel(receiver_email_file)
            first_row_data = receiver_df.iloc[0]

            subject_preview = self.process_placeholder(first_row_data, optional_text[0])
            message_preview = self.process_placeholder(first_row_data, optional_text[1])

            return [subject_preview, message_preview]
        except:
            return ['', 'Excel file is not in correct format. Please amend it.']


    def process_placeholder(self, row, msg):
        for placeholder, key in re.findall("({{(.+?)}})", msg):
            msg = msg.replace(placeholder, row.get(key, placeholder))
        return msg