import os
from functools import partial

from PySide2.QtCore import QPoint, Qt, QTimer
from PySide2.QtGui import QFontMetrics
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QTextEdit

from attachment_label import AttachmentLabel
from ui_extend import Ui_MainWindow_Extend

class MainWindow(QMainWindow):
    def __init__(self, model, logic):
        QMainWindow.__init__(self)

        self.model = model
        self.logic = logic

        self.ui = Ui_MainWindow_Extend()
        self.ui.setupUi(self)

        self.ui.receiver_file_label.setVisible(False)

        compulsory_list = []
        compulsory_list.append(self.ui.column_name_entry)
        compulsory_list.append(self.ui.receiver_file_label)
        compulsory_list.append(self.ui.my_password_entry)
        compulsory_list.append(self.ui.my_email_entry)
        
        optional_list = []
        optional_list.append(self.ui.subject_entry)
        optional_list.append(self.ui.msg_entry)
        

        # listen for ui event signals
        self.ui.msg_entry.cursorPositionChanged.connect(self.adjust_slider)
        self.ui.send_mail_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.mail_page))
        self.ui.status_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.status_page))

        
        # connect ui to logic
        self.fm = QFontMetrics(self.font())

        self.ui.my_email_entry.setFocus()
        self.hide_error_message()

        self.ui.browse_file_btn.clicked.connect(self.browse_file)
        self.ui.attach_btn.clicked.connect(self.attach_file)
        self.ui.send_btn.clicked.connect(lambda : self.send_email(compulsory_list, optional_list, True))

        getattr(self.logic, 'signal_' + str(4)).connect(lambda : self.show_no_subject_pop_up(compulsory_list, optional_list))
        getattr(self.logic, 'signal_' + str(0)).connect(self.show_email_column_error)
        getattr(self.logic, 'signal_' + str(1)).connect(self.show_receiver_email_error)
        getattr(self.logic, 'signal_' + str(2)).connect(self.show_password_error)
        getattr(self.logic, 'signal_' + str(3)).connect(self.show_my_email_error)

        # listen for model event signals

    def focus_on_attachment(self):
        position = self.ui.scrollArea.verticalScrollBar().maximum()
        self.ui.scrollArea.verticalScrollBar().setValue(position)
        # self.ui.scrollArea.verticalScrollBar().setValue(self.ui.attachment_grid.contentsRect().bottom())

    def adjust_slider(self):
        # expand height to remove scroll bar of QTextEdit
        height = self.ui.msg_entry.document().size().height()
        self.ui.msg_entry.setMinimumHeight(height)
        
        position = self.ui.msg_entry.cursorRect()
        # wait for 1 millisecond (for scroll bar height to re-adjust) before setting vertical scroll bar value
        QTimer.singleShot(1, partial(self.ui.scrollArea.ensureVisible, position.x(), position.y(), 0, 30))
        # less ideal method try next line
        # self.ui.scrollArea.verticalScrollBar().setValue(self.ui.msg_entry.cursorRect().top())


    def get_compulsory_text(self, compulsory_list):
        compulsory_text = []
        for ele in compulsory_list:
            compulsory_text.append(ele.text())
        return compulsory_text

    def get_optional_text(self, optional_list):
        optional_text = []
        for ele in optional_list:
            if isinstance(ele, QTextEdit):
                optional_text.append(ele.toPlainText())
            else:
                optional_text.append(ele.text())
        return optional_text

    def browse_file(self):
        receiver_file_name, _ = QFileDialog.getOpenFileName(self, 'Select A File',
                                                            os.path.join(os.environ["HOMEPATH"], "Desktop"),
                                                            "excel files (*.xlsx)")
        self.model.receiver_file_name = receiver_file_name
        label_width = self.ui.to_email_label.width()
        self.ui.to_email_label.setText(self.fm.elidedText(receiver_file_name.split('/')[-1],
                                                            Qt.ElideRight, label_width))
        self.ui.receiver_file_label.setText(receiver_file_name)

    def attach_file(self):
        attach_file_name, _ = QFileDialog.getOpenFileName(self, 'Select A File',
                                                            os.path.join(os.environ["HOMEPATH"], "Desktop"),
                                                            "all files (*.*)")
        if not attach_file_name:
            return
        attachment_label = AttachmentLabel(attach_file_name)
        self.ui.attachment_grid.addWidget(attachment_label)
        # wait for 10 milliseconds (for scroll bar ui to update) before setting vertical scroll bar value
        QTimer.singleShot(10, self.focus_on_attachment)

    def hide_error_message(self):
        self.ui.email_address_error.setVisible(False)
        self.ui.no_password_error.setVisible(False)
        self.ui.to_error.setVisible(False)
        self.ui.invalid_col_error.setVisible(False)
        

    def send_email(self, compulsory_list, optional_list, send_with_subject):
        self.hide_error_message()
        compulsory_text = self.get_compulsory_text(compulsory_list)
        optional_text = self.get_optional_text(optional_list)

        self.logic.send_email(compulsory_text, optional_text, send_with_subject)

    def show_email_column_error(self):
        self.ui.invalid_col_error.show()
        self.ui.column_name_entry.setFocus()

    def show_receiver_email_error(self):
        self.ui.to_error.show()

    def show_password_error(self):
        self.ui.no_password_error.show()
        self.ui.my_password_entry.setFocus()

    def show_my_email_error(self):
        self.ui.email_address_error.show()
        self.ui.my_email_entry.setFocus()

    def show_no_subject_pop_up(self, compulsory_list, optional_list):
        button_clicked = self.ui.show_no_subject_pop_up()
        if button_clicked == QMessageBox.Yes:
            self.send_email(compulsory_list, optional_list, False)