# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainelaAyf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMinimumSize(QSize(1000, 750))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.navigation_frame = QFrame(self.centralwidget)
        self.navigation_frame.setObjectName(u"navigation_frame")
        self.navigation_frame.setMinimumSize(QSize(220, 0))
        self.navigation_frame.setMaximumSize(QSize(220, 16777215))
        self.navigation_frame.setStyleSheet(u"background-color: rgb(51, 51, 76);")
        self.navigation_frame.setFrameShape(QFrame.NoFrame)
        self.navigation_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.navigation_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.navigation_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 75))
        self.logo_frame.setStyleSheet(u"background-color: rgb(39, 39, 58);")
        self.logo_frame.setFrameShape(QFrame.NoFrame)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.logo_frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Microsoft Sans Serif")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.logo_frame)

        self.btn_frame = QFrame(self.navigation_frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setFrameShape(QFrame.NoFrame)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.btn_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.send_mail_btn = QPushButton(self.btn_frame)
        self.side_button_group = QButtonGroup(MainWindow)
        self.side_button_group.setObjectName(u"side_button_group")
        self.side_button_group.addButton(self.send_mail_btn)
        self.send_mail_btn.setObjectName(u"send_mail_btn")
        self.send_mail_btn.setMinimumSize(QSize(0, 60))
        self.send_mail_btn.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.send_mail_btn.setFont(font1)
        self.send_mail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_mail_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(51, 51, 76);\n"
"	border: 0px solid;\n"
"	text-align:left;\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/send_mail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_mail_btn.setIcon(icon)
        self.send_mail_btn.setIconSize(QSize(25, 25))
        self.send_mail_btn.setCheckable(True)
        self.send_mail_btn.setChecked(True)

        self.verticalLayout_2.addWidget(self.send_mail_btn)

        self.status_btn = QPushButton(self.btn_frame)
        self.side_button_group.addButton(self.status_btn)
        self.status_btn.setObjectName(u"status_btn")
        self.status_btn.setMinimumSize(QSize(0, 60))
        self.status_btn.setMaximumSize(QSize(16777215, 60))
        self.status_btn.setFont(font1)
        self.status_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(51, 51, 76);\n"
"	border: 0px solid;\n"
"	text-align:left;\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/time.png", QSize(), QIcon.Normal, QIcon.Off)
        self.status_btn.setIcon(icon1)
        self.status_btn.setIconSize(QSize(25, 25))
        self.status_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.status_btn)


        self.verticalLayout.addWidget(self.btn_frame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.navigation_frame)

        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.content_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 75))
        self.title_frame.setMaximumSize(QSize(16777215, 75))
        self.title_frame.setStyleSheet(u"QFrame#title_frame{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: none;\n"
"    background: #F8F8F8;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #CCCCCC;\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line {\n"
"    border: none;\n"
"    background: none;\n"
"}")
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.title_frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(231, 233, 231);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mail_page = QWidget()
        self.mail_page.setObjectName(u"mail_page")
        self.mail_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.mail_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.mail_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: none;\n"
"    background: #F8F8F8;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #CCCCCC;\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line {\n"
"    border: none;\n"
"    background: none;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 50))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(500, 0))
        self.frame_3.setMaximumSize(QSize(500, 16777215))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"images/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.my_email_entry = QLineEdit(self.frame_3)
        self.my_email_entry.setObjectName(u"my_email_entry")
        self.my_email_entry.setMinimumSize(QSize(0, 0))
        self.my_email_entry.setFont(font1)
        self.my_email_entry.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);")
        self.my_email_entry.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.my_email_entry, 0, 1, 1, 1)

        self.email_address_error = QLabel(self.frame_3)
        self.email_address_error.setObjectName(u"email_address_error")
        font3 = QFont()
        font3.setPointSize(10)
        self.email_address_error.setFont(font3)
        self.email_address_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.email_address_error, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(500, 0))
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.my_password_entry = QLineEdit(self.frame_4)
        self.my_password_entry.setObjectName(u"my_password_entry")
        self.my_password_entry.setMinimumSize(QSize(0, 0))
        self.my_password_entry.setFont(font1)
        self.my_password_entry.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);")
        self.my_password_entry.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.my_password_entry, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u"images/lock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.no_password_error = QLabel(self.frame_4)
        self.no_password_error.setObjectName(u"no_password_error")
        self.no_password_error.setFont(font3)
        self.no_password_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.no_password_error, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 50))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.browse_file_btn = QPushButton(self.frame_5)
        self.browse_file_btn.setObjectName(u"browse_file_btn")
        self.browse_file_btn.setMinimumSize(QSize(150, 40))
        self.browse_file_btn.setMaximumSize(QSize(100, 16777215))
        self.browse_file_btn.setFont(font1)
        self.browse_file_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_file_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-color: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid;\n"
"	border-color: rgb(85, 85, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.browse_file_btn, 0, 2, 1, 1)

        self.to_email_label = QLabel(self.frame_5)
        self.to_email_label.setObjectName(u"to_email_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_email_label.sizePolicy().hasHeightForWidth())
        self.to_email_label.setSizePolicy(sizePolicy)
        self.to_email_label.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Microsoft Sans Serif")
        font4.setPointSize(12)
        self.to_email_label.setFont(font4)
        self.to_email_label.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-bottom: 5px;\n"
"margin-right: 5px;")

        self.gridLayout_3.addWidget(self.to_email_label, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(40, 16777215))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-bottom: 5px;")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.receiver_file_label = QLabel(self.frame_5)
        self.receiver_file_label.setObjectName(u"receiver_file_label")

        self.gridLayout_3.addWidget(self.receiver_file_label, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.to_error = QLabel(self.frame)
        self.to_error.setObjectName(u"to_error")
        self.to_error.setFont(font3)
        self.to_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_9.addWidget(self.to_error)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.column_name_entry = QLineEdit(self.frame_7)
        self.column_name_entry.setObjectName(u"column_name_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.column_name_entry.sizePolicy().hasHeightForWidth())
        self.column_name_entry.setSizePolicy(sizePolicy1)
        self.column_name_entry.setMinimumSize(QSize(0, 33))
        self.column_name_entry.setFont(font1)
        self.column_name_entry.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-bottom: 5px;")

        self.verticalLayout_7.addWidget(self.column_name_entry)

        self.invalid_col_error = QLabel(self.frame_7)
        self.invalid_col_error.setObjectName(u"invalid_col_error")
        self.invalid_col_error.setFont(font3)
        self.invalid_col_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_7.addWidget(self.invalid_col_error)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.subject_entry = QLineEdit(self.frame_8)
        self.subject_entry.setObjectName(u"subject_entry")
        self.subject_entry.setMinimumSize(QSize(0, 0))
        self.subject_entry.setFont(font1)
        self.subject_entry.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-left: 1.5px;\n"
"padding-bottom: 5px;")

        self.horizontalLayout_8.addWidget(self.subject_entry)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 736, 123))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.msg_entry = QTextEdit(self.scrollAreaWidgetContents)
        self.msg_entry.setObjectName(u"msg_entry")
        self.msg_entry.setMinimumSize(QSize(0, 0))
        self.msg_entry.setFont(font1)
        self.msg_entry.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-top: 5px;")
        self.msg_entry.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.msg_entry.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.msg_entry.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.verticalLayout_6.addWidget(self.msg_entry)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.attach_btn = QPushButton(self.frame_6)
        self.attach_btn.setObjectName(u"attach_btn")
        self.attach_btn.setMaximumSize(QSize(30, 16777215))
        self.attach_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.attach_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(231, 233, 231);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attach_btn.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.attach_btn)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_9)

        self.send_btn = QPushButton(self.frame_6)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setMinimumSize(QSize(100, 30))
        self.send_btn.setMaximumSize(QSize(50, 16777215))
        self.send_btn.setFont(font1)
        self.send_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-color: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid;\n"
"	border-color: rgb(85, 85, 255);\n"
"}")

        self.horizontalLayout_7.addWidget(self.send_btn)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.mail_page)
        self.status_page = QWidget()
        self.status_page.setObjectName(u"status_page")
        self.verticalLayout_8 = QVBoxLayout(self.status_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.status_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: none;\n"
"    background: #F8F8F8;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #CCCCCC;\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line {\n"
"    border: none;\n"
"    background: none;\n"
"}")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)

        self.verticalLayout_8.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.status_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.content_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gmailer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gmailer", None))
        self.send_mail_btn.setText(QCoreApplication.translate("MainWindow", u"  Send Mail", None))
        self.status_btn.setText(QCoreApplication.translate("MainWindow", u"  Send Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton.setText("")
        self.my_email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your email address", None))
        self.email_address_error.setText(QCoreApplication.translate("MainWindow", u"Please enter your email address correctly", None))
        self.my_password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your password", None))
        self.pushButton_2.setText("")
        self.no_password_error.setText(QCoreApplication.translate("MainWindow", u"Please enter your password correctly", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.browse_file_btn.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.to_email_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.receiver_file_label.setText("")
        self.to_error.setText(QCoreApplication.translate("MainWindow", u"Please select email list", None))
        self.column_name_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email column name", None))
        self.invalid_col_error.setText(QCoreApplication.translate("MainWindow", u"Please enter a valid name", None))
        self.subject_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.msg_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.attach_btn.setText("")
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

