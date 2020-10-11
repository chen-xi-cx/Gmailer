import time

from PySide2.QtCore import QRunnable, Slot, QThreadPool
from email_thread import EmailThread

class StartThread(QRunnable):
    def __init__(self, logic, receiver_df, email_input):
        super().__init__()
        self.logic = logic
        self.receiver_df = receiver_df
        self.email_input = email_input

    @Slot()
    def run(self):
        for sublist in self.receiver_df:
            email_thread = EmailThread(sublist, self.email_input)
            email_thread.signal.invalid_email_column.connect(self.logic.show_invalid_email_error)
            email_thread.signal.fail_email.connect(self.logic.update_fail_email)
            email_thread.signal.success_email.connect(self.logic.update_successful_email)
            self.logic.threadpool.start(email_thread)
            time.sleep(5)