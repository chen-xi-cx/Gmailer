import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QFontMetrics)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fm = QFontMetrics(self.font())

        self.ui.my_email_entry.setFocus()
        UIFunctions.hide_error_message(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.browse_file_btn.clicked.connect(lambda: UIFunctions.browse_file(self))
        self.ui.send_btn.clicked.connect(lambda: UIFunctions.send_email(self))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())