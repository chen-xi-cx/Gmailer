import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from PySide2.QtWidgets import QApplication

from logic import Logic
from main_window import MainWindow
from model import Model

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.logic = Logic(self.model)
        self.mainWindow = MainWindow(self.model, self.logic)
        self.mainWindow.show()


if __name__ == '__main__':
    try:
        os.mkdir('log file')
    except:
        pass
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = RotatingFileHandler('log file/app.log', maxBytes=100000, backupCount=10)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # logging.basicConfig(filename='app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Start')
    app = App(sys.argv)
    sys.exit(app.exec_())
