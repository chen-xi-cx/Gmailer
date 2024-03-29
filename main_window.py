import logging
import os
from functools import partial
from typing import Optional

import pandas as pd
from numpy.ma.core import count
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QFontMetrics, QTextCursor
from PySide2.QtWidgets import (QApplication, QComboBox, QFileDialog,
                               QMainWindow, QMessageBox, QTextEdit)

from attachment_label import AttachmentLabel
from ui_close_window import Ui_CloseWindow
from ui_extend import Ui_MainWindow_Extend
from ui_message_preview import Ui_MessagePreview


class CloseWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_CloseWindow()
        self.ui.setupUi(self)
        flag = Qt.WindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(flag)

class PreviewWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MessagePreview()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self, model, logic):
        QMainWindow.__init__(self)
        

        self.logger = logging.getLogger(__name__)

        self.model = model
        self.logic = logic

        self.ui = Ui_MainWindow_Extend()
        self.ui.setupUi(self)

        self.close_window = CloseWindow()
        self.preview_window = PreviewWindow()

        self.ui.receiver_file_label.setVisible(False)
        self.ui.status.setText('You haven\'t sent anything!')

        self.fm = QFontMetrics(self.ui.to_email_label.font()) # for setting text ellipsis
        # self.ui.msg_entry.installEventFilter(self)

        compulsory_list = []
        compulsory_list.append(self.ui.email_column_combo)
        compulsory_list.append(self.ui.receiver_file_label)
        compulsory_list.append(self.ui.my_password_entry)
        compulsory_list.append(self.ui.my_email_entry)
        
        optional_list = []
        optional_list.append(self.ui.subject_entry)
        optional_list.append(self.ui.msg_entry)
        optional_list.append(self.ui.personalised_att_combo)
        

        # listen for ui event signals
        self.ui.msg_entry.cursorPositionChanged.connect(self.adjust_slider)
        self.ui.send_mail_btn.clicked.connect(self.switch_to_email_pg)
        self.ui.status_btn.clicked.connect(self.switch_to_status_pg)

        
        # connect ui to logic
        self.ui.my_email_entry.setFocus()
        self.hide_error_message()

        self.ui.browse_file_btn.clicked.connect(self.browse_file)
        self.ui.attach_btn.clicked.connect(self.attach_file)
        self.ui.send_btn.clicked.connect(lambda : self.send_email(compulsory_list, optional_list, True))
        self.ui.preview_btn.clicked.connect(lambda : self.open_preview_window(compulsory_list, optional_list))

        # listen for logic event signals
        getattr(self.logic, 'signal_' + str(4)).connect(lambda : self.show_no_subject_pop_up(compulsory_list, optional_list))
        getattr(self.logic, 'signal_' + str(0)).connect(self.show_email_column_error)
        getattr(self.logic, 'signal_' + str(1)).connect(self.show_receiver_email_error)
        getattr(self.logic, 'signal_' + str(2)).connect(self.show_password_error)
        getattr(self.logic, 'signal_' + str(3)).connect(self.show_my_email_error)
        self.logic.attachment_limit_reached.connect(self.ui.invalid_byte_size_error.show)
        self.logic.sending_start.connect(self.show_sending_start)
        self.logic.success_email.connect(self.update_successful_status)
        self.logic.fail_email.connect(self.update_fail_status)
        self.logic.sending_done.connect(self.show_sending_finish)
        self.logic.send_progress.connect(self.update_progress_bar)
        self.logic.estimate_time_finish.connect(self.update_estimated_time_finish)

    def update_estimated_time_finish(self, duration):
        num_hour = int(duration / 3600)
        num_minute = int((duration % 3600) / 60)

        if duration == 0:
            self.ui.estimated_time_finish_label.setText("")
        elif duration < 60:
            self.ui.estimated_time_finish_label.setText('Estimated time remaining: less than 1 minute')
        elif num_hour == 0:
            self.ui.estimated_time_finish_label.setText(f'Estimated time remaining: {num_minute} minute(s)')
        else:
            self.ui.estimated_time_finish_label.setText(f'Estimated time remaining: {num_hour} hour(s) {num_minute} minute(s)')

    def open_preview_window(self, compulsory_list, optional_list):
        self.hide_error_message()
        self.preview_window.show()
        compulsory_text = self.get_compulsory_text(compulsory_list)
        optional_text = self.get_optional_text(optional_list)
        subject_preview, message_preview = self.logic.show_preview(compulsory_text, optional_text)
        self.preview_window.ui.subject_preview.setText(subject_preview)
        self.preview_window.ui.msg_preview.setText(message_preview)

    def switch_to_email_pg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.mail_page)
        self.ui.label.setText("Send Email")

    def switch_to_status_pg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.status_page)
        self.ui.label.setText("Send Status")

        

    def closeEvent(self, event):
        if self.logic.threadpool.activeThreadCount() > 0:
            button_clicked = self.ui.show_exit_confirmation()
            if button_clicked == QMessageBox.Yes:
                self.logger.info("User terminate program")
                self.close_window.show()
                self.hide()
                QApplication.processEvents()
                self.logic.kill_thread()
                while self.logic.threadpool.activeThreadCount() != 0:
                    QApplication.processEvents()
                self.close_window.close()
                event.accept()
            else:
                event.ignore()
        else:
            self.logger.info('Close program without active thread')
            event.accept()


    def update_progress_bar(self, progress):
        self.ui.progress_bar.setValue(progress)

    def show_sending_finish(self, num_success, num_fail, csv_path):
        self.ui.send_btn.setEnabled(True)
        self.ui.status.moveCursor(QTextCursor.End)
        self.ui.status.insertHtml(('<br>All emails sent!'
                                   '<br><b>Number of successful sends: {}'
                                   '<br>Number of fail sends: {}</b>'
                                   '<br>Failed emails saved to {}')
                                   .format(num_success, num_fail, csv_path))
        self.ui.status.moveCursor(QTextCursor.End)


    def show_sending_start(self):
        self.ui.progress_bar.setValue(0)
        self.ui.send_btn.setDisabled(True)
        self.ui.status.setText('Sending emails...')
        self.ui.status_btn.click()
        self.ui.stackedWidget.setCurrentWidget(self.ui.status_page)

    def update_successful_status(self, email):
        self.ui.status.moveCursor(QTextCursor.End)
        self.ui.status.insertPlainText('\nsuccess: {}'.format(email))
        self.ui.status.moveCursor(QTextCursor.End)

    def update_fail_status(self, email):
        self.ui.status.moveCursor(QTextCursor.End)
        self.ui.status.insertPlainText('\nfail: {}'.format(email))
        self.ui.status.moveCursor(QTextCursor.End)


    def focus_on_attachment(self):
        position = self.ui.scrollArea.verticalScrollBar().maximum()
        self.ui.scrollArea.verticalScrollBar().setValue(position)
        # self.ui.scrollArea.verticalScrollBar().setValue(self.ui.attachment_grid.contentsRect().bottom())

    def truncate_email_label_text(self):
        email_label = os.path.basename(self.ui.receiver_file_label.text())
        label_width = self.ui.to_email_label.width()
        self.ui.to_email_label.setText(self.fm.elidedText(email_label,
                                                          Qt.ElideRight, label_width))


    # def eventFilter(self, source, event):
    #     # adjust msg_entry height when it is resized by maximising or minimising window
    #     if event.type() == QEvent.Resize and source is self.ui.msg_entry:
    #         self.adjust_height()
    #     return super().eventFilter(source, event)

    # overrides resizeEvent of QMainWindow
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_height()
        self.truncate_email_label_text()
        
    def adjust_slider(self):
        self.adjust_height()
        position = self.ui.msg_entry.cursorRect()
        # wait for 1 millisecond (for scroll bar height to re-adjust) before setting vertical scroll bar value
        QTimer.singleShot(1, partial(self.ui.scrollArea.ensureVisible, position.x(), position.y(), 0, 30))
        # less ideal method
        # self.ui.scrollArea.verticalScrollBar().setValue(self.ui.msg_entry.cursorRect().top())

    def adjust_height(self):
        # expand height to remove scroll bar of QTextEdit
        height = self.ui.msg_entry.document().size().height()
        self.ui.msg_entry.setMinimumHeight(height)


    def get_compulsory_text(self, compulsory_list):
        compulsory_text = []
        for ele in compulsory_list:
            if isinstance(ele, QComboBox):
                compulsory_text.append(ele.currentText())
            else:
                compulsory_text.append(ele.text())
        return compulsory_text

    def get_optional_text(self, optional_list):
        optional_text = []
        for ele in optional_list:
            if isinstance(ele, QTextEdit):
                optional_text.append(ele.toHtml())
            elif isinstance(ele, QComboBox):
                optional_text.append(ele.currentText())
            else:
                optional_text.append(ele.text())
        return optional_text

    def browse_file(self):
        receiver_file_name, _ = QFileDialog.getOpenFileName(self, 'Select A File',
                                                            os.path.join(os.environ["HOMEPATH"], "Desktop"),
                                                            "excel files (*.xlsx)")
        if not receiver_file_name:
            return
        self.model.receiver_file_name = receiver_file_name
        label_width = self.ui.to_email_label.width()
        self.ui.to_email_label.setText(self.fm.elidedText(receiver_file_name.split('/')[-1],
                                                            Qt.ElideRight, label_width))
        self.ui.receiver_file_label.setText(receiver_file_name)
        receiver_df = pd.read_excel(receiver_file_name)
        self.update_combo_box(self.ui.email_column_combo, receiver_df.columns)
        self.update_combo_box(self.ui.personalised_att_combo, receiver_df.columns)

    def update_combo_box(self, combo_box, column_names):
        if combo_box.count() > 1:
            for idx in range(combo_box.count() - 1, 0, -1):
                combo_box.removeItem(idx)

        combo_box.addItems(column_names)

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
        self.ui.invalid_byte_size_error.setVisible(False)
        

    def send_email(self, compulsory_list, optional_list, send_with_subject):
        self.hide_error_message()
        compulsory_text = self.get_compulsory_text(compulsory_list)
        optional_text = self.get_optional_text(optional_list)

        self.logic.send_email(compulsory_text, optional_text, send_with_subject)

    def show_email_column_error(self):
        self.ui.invalid_col_error.show()

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
