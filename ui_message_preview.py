# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message_previewLwBNYF.ui'
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


class Ui_MessagePreview(object):
    def setupUi(self, MessagePreview):
        if not MessagePreview.objectName():
            MessagePreview.setObjectName(u"MessagePreview")
        MessagePreview.resize(912, 575)
        self.centralwidget = QWidget(MessagePreview)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(231, 233, 231);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
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
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.subject_preview = QLineEdit(self.frame_8)
        self.subject_preview.setObjectName(u"subject_preview")
        self.subject_preview.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        self.subject_preview.setFont(font)
        self.subject_preview.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-left: 1.5px;\n"
"padding-bottom: 5px;")
        self.subject_preview.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.subject_preview)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.msg_preview = QTextEdit(self.frame_2)
        self.msg_preview.setObjectName(u"msg_preview")
        self.msg_preview.setFont(font)
        self.msg_preview.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-radius: 0px;\n"
"color: rgb(113, 112, 114);\n"
"padding-top: 5px;")
        self.msg_preview.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.msg_preview)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MessagePreview.setCentralWidget(self.centralwidget)

        self.retranslateUi(MessagePreview)

        QMetaObject.connectSlotsByName(MessagePreview)
    # setupUi

    def retranslateUi(self, MessagePreview):
        MessagePreview.setWindowTitle(QCoreApplication.translate("MessagePreview", u"Preview message", None))
        self.subject_preview.setPlaceholderText("")
    # retranslateUi

