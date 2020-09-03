from main import *
import os

class UIFunctions(MainWindow):

    def browse_file(self):
        global to_file_name
        to_file_name, _ = QFileDialog.getOpenFileName(self, 'Select A File', os.path.join(os.environ["HOMEPATH"], "Desktop"),
                                                        "excel files (*.xlsx);;all files (*.*)")
        label_width = self.ui.to_email_label.width()
        self.ui.to_email_label.setText(self.fm.elidedText('To ' + to_file_name.split('/')[-1], Qt.ElideLeft, label_width))

    def hide_error_message(self):
        self.ui.email_address_error.setVisible(False)
        self.ui.no_password_error.setVisible(False)
        self.ui.to_error.setVisible(False)
        self.ui.invalid_col_error.setVisible(False)

    def send_email(self, has_subject = True):
        UIFunctions.hide_error_message(self)
        UIFunctions.check_valid_field(self, has_subject)

    def check_valid_field(self, has_subject):
        my_email = self.ui.my_email_entry.text()
        my_email_password = self.ui.my_password_entry.text()
        to_email = self.ui.to_email_label.text()
        email_column_name = self.ui.column_name_entry.text()
        subject = self.ui.subject_entry.text()
        body = self.ui.msg_entry.toPlainText()

        if not subject and has_subject:
            UIFunctions.show_no_subject_pop_up(self)

        if not email_column_name:
            self.ui.invalid_col_error.show()
            self.ui.column_name_entry.setFocus()

        if to_email == 'To':
            self.ui.to_error.show()

        if not my_email_password:
            self.ui.no_password_error.show()
            self.ui.my_password_entry.setFocus()

        if not my_email:
            self.ui.email_address_error.show()
            self.ui.my_email_entry.setFocus()

    def show_no_subject_pop_up(self):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-color: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid;\n"
"	border-color: rgb(85, 85, 255);\n"
"}")
        
        msg.setIcon(QMessageBox.Question)
        msg.setText('Are you sure you want to send without a subject?')
        msg.setWindowTitle('Empty subject')

        button_clicked = msg.exec_()
        if button_clicked == QMessageBox.Yes:
            UIFunctions.send_email(self, False)