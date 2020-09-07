import os

from PySide2.QtCore import QRect, QSize, Qt
from PySide2.QtGui import QCursor, QIcon
from PySide2.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QWidget

class AttachmentLabel(QWidget):
    attachment_list = []

    def __init__(self, file_name):
        super(AttachmentLabel, self).__init__()
        self.file_name = file_name

        self.attachment_list.append(file_name)

        self.frame = QFrame()
        
        self.frame.setStyleSheet("border: 2px solid;")

        inner_layout = QHBoxLayout(self.frame)
        # self.inner_layout.setContentsMargins(11, 0, 0, 0)

        self.file_name_label = QLabel(self.frame)
        trim_file_name = os.path.basename(file_name)
        self.file_name_label.setText(trim_file_name)
        self.file_name_label.setStyleSheet("border: none;")
        inner_layout.addWidget(self.file_name_label)

        self.delete_btn = QPushButton(self.frame)
        self.delete_btn.setGeometry(QRect(350, 10, 81, 20))
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                        "border: none;")
        icon5 = QIcon()
        icon5.addFile(u"images/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon5)
        inner_layout.addWidget(self.delete_btn)
        outer_layout = QHBoxLayout()
        outer_layout.addWidget(self.frame)

        self.setLayout(outer_layout)

        self.delete_btn.clicked.connect(self.deleteLater)
        self.destroyed.connect(lambda : self.remove_attachment())

    def remove_attachment(self):
        self.attachment_list.remove(self.file_name)
