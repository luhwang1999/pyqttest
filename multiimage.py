import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

from functools import cached_property
import sys

from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets


class App(QWidget):
    def __init__(self):
        super().__init__()

        pic = QLabel(self)
        pic.setPixmap(QPixmap("test.png"))
        pic.resize(250, 250)
        pic.move(220, 90)
        pic.show()

        pic1 = QLabel(self)
        pic1.setPixmap(QPixmap("test.png"))
        pic1.resize(250, 250)
        pic1.move(20, 90)
        pic1.show()

        self.show()

        self.playlist.addMedia(
            QtMultimedia.QMediaContent(
                QtCore.QUrl(
                    "http://techslides.com/demos/sample-videos/small.mp4")
            )
        )

    def player(self):
        return QtMultimedia.QMediaPlayer()


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
