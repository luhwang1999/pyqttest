from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QFile, Qt, QUrl
import sys

from functools import cached_property

from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("test.ico"))
        self.setWindowTitle("Controller")
        self.setGeometry(150, 150, 150, 150)

        self.viewer.show()
        self.video_widget.show()
        self.create_player()

    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        controllerwidget = QVideoWidget()

        self.openBtn = QPushButton('Open Video')
        self.openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
        # SP_ArrowForward,SP_ArrowLeft

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)

        vbox = QVBoxLayout()
        vbox.addWidget(controllerwidget)

        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(
            [self.video_widget.videoSurface(), self.viewer.videoSurface()]
        )

        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    @cached_property
    def viewer(self):
        view = QtMultimediaWidgets.QVideoWidget()
        view.setWindowFlags(view.windowFlags() |
                            QtCore.Qt.WindowStaysOnTopHint)
        view.setMinimumSize(480, 360)
        view.setWindowTitle("screen1")
        return view

    @cached_property
    def video_widget(self):
        view = QtMultimediaWidgets.QVideoWidget()
        view.setWindowFlags(view.windowFlags() |
                            QtCore.Qt.WindowStaysOnTopHint)
        view.setMinimumSize(480, 360)
        view.setWindowTitle("test2")
        return view


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
