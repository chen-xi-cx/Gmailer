# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'close_windowaWXZLJ.ui'
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


class Ui_CloseWindow(object):
    def setupUi(self, CloseWindow):
        if not CloseWindow.objectName():
            CloseWindow.setObjectName(u"CloseWindow")
        CloseWindow.resize(531, 105)
        CloseWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(CloseWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        CloseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CloseWindow)

        QMetaObject.connectSlotsByName(CloseWindow)
    # setupUi

    def retranslateUi(self, CloseWindow):
        CloseWindow.setWindowTitle(QCoreApplication.translate("CloseWindow", u"Closing program", None))
        self.label.setText(QCoreApplication.translate("CloseWindow", u"Cleaning up program and terminating. Please Wait", None))
    # retranslateUi

