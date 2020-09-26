from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox

from flow_layout import FlowLayout
from ui_main import Ui_MainWindow

class Ui_MainWindow_Extend(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.attachment_grid = FlowLayout()
        self.attachment_grid.setObjectName(u"attachment_grid")

        self.verticalLayout_6.addLayout(self.attachment_grid)

        

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
                            "	width: 50px;\n"
                            "	height: 20px;\n"
                            "	padding: 10px;\n"
                            "}\n"
                            "\n"
                            "QPushButton:hover{\n"
                            "	border: 2px solid;\n"
                            "	border-color: rgb(85, 85, 255);\n"
                            "}\n"
                            "QMessageBox{\n"
                            "	background-color: rgb(255, 255, 255);\n"
                            "}")
        msg.setIconPixmap(QPixmap(":/icons/images/help-circle.svg"))
        msg.setText('Are you sure you want to send without a subject?')
        msg.setWindowTitle('Empty subject')

        return msg.exec_()

    def show_exit_confirmation(self):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setStyleSheet(u"QPushButton{\n"
                            "	background-color: rgb(85, 170, 255);\n"
                            "	color: rgb(255, 255, 255);\n"
                            "	border: 2px solid;\n"
                            "	border-color: none;\n"
                            "	border-radius: 10px;\n"
                            "	width: 50px;\n"
                            "	height: 20px;\n"
                            "	padding: 10px;\n"
                            "}\n"
                            "\n"
                            "QPushButton:hover{\n"
                            "	border: 2px solid;\n"
                            "	border-color: rgb(85, 85, 255);\n"
                            "}\n"
                            "QMessageBox{\n"
                            "	background-color: rgb(255, 255, 255);\n"
                            "}")
        msg.setIconPixmap(QPixmap(":/icons/images/help-circle.svg"))
        msg.setText('Emails are being sent. Are you sure you want to quit?')
        msg.setWindowTitle('Close program')

        return msg.exec_()

    def show_cleaning_up_message(self):
        msg = QMessageBox()
        msg.setStandardButtons(0)
        msg.setStyleSheet(u"QPushButton{\n"
                            "	background-color: rgb(85, 170, 255);\n"
                            "	color: rgb(255, 255, 255);\n"
                            "	border: 2px solid;\n"
                            "	border-color: none;\n"
                            "	border-radius: 10px;\n"
                            "	width: 50px;\n"
                            "	height: 20px;\n"
                            "	padding: 10px;\n"
                            "}\n"
                            "\n"
                            "QPushButton:hover{\n"
                            "	border: 2px solid;\n"
                            "	border-color: rgb(85, 85, 255);\n"
                            "}\n"
                            "QMessageBox{\n"
                            "	background-color: rgb(255, 255, 255);\n"
                            "}")
        msg.setText('Please wait for the program to clean up and terminate')
        msg.setWindowTitle('Closing program')

        return msg.exec_()