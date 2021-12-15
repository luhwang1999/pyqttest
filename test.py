from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QFile, Qt, QUrl
import sys
from functools import cached_property
import sys

from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(self.video_widget)

        self.openBtn = QPushButton('Open Video')
        # self.openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        # self.playBtn.clicked.connect(self.play_video)
        # SP_ArrowForward,SP_ArrowLeft

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        # self.slider.sliderMoved.connect(self.set_position)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.viewer.show()

        self.player.setVideoOutput(
            [self.video_widget.videoSurface(), self.viewer.videoSurface()]
        )
        self.player.setPlaylist(self.playlist)

        self.playlist.addMedia(
            QtMultimedia.QMediaContent(
                QtCore.QUrl.fromLocalFile(
                    "C:\\Users\\Lu\\Downloads\\b3756b8d-43d8-4f8d-bf33-7c7425f83f33.mp4")
            )
        )
        self.player.play()

    @ cached_property
    def player(self):
        return QtMultimedia.QMediaPlayer()

    @ cached_property
    def video_widget(self):
        return QtMultimediaWidgets.QVideoWidget()

    @ cached_property
    def viewer(self):
        view = QtMultimediaWidgets.QVideoWidget()
        view.setWindowFlags(view.windowFlags() |
                            QtCore.Qt.WindowStaysOnTopHint)
        view.setMinimumSize(480, 360)
        view.setWindowTitle("VR Therapy")
        return view

    @ cached_property
    def playlist(self):
        return QtMultimedia.QMediaPlaylist()


app = QtWidgets.QApplication(sys.argv)

w = MainWindow()
w.resize(640, 480)
w.show()

sys.exit(app.exec_())
