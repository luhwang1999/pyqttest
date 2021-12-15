from functools import cached_property
import sys

from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(self.video_widget)

        self.viewer.show()

        self.player.setVideoOutput(
            [self.video_widget.videoSurface(), self.viewer.videoSurface()]
        )
        self.player.setPlaylist(self.playlist)

        self.playlist.addMedia(
            QtMultimedia.QMediaContent(
                QtCore.QUrl(
                    "http://techslides.com/demos/sample-videos/small.mp4")
            )
        )
        self.player.play()

    @cached_property
    def player(self):
        return QtMultimedia.QMediaPlayer()

    @cached_property
    def video_widget(self):
        return QtMultimediaWidgets.QVideoWidget()

    @cached_property
    def viewer(self):
        view = QtMultimediaWidgets.QVideoWidget()
        view.setWindowFlags(view.windowFlags() |
                            QtCore.Qt.WindowStaysOnTopHint)
        view.setMinimumSize(480, 360)
        view.setWindowTitle("VR Therapy")
        return view

    @cached_property
    def playlist(self):
        return QtMultimedia.QMediaPlaylist()


app = QtWidgets.QApplication(sys.argv)

w = MainWindow()
w.resize(640, 480)
w.show()

sys.exit(app.exec_())
