# This Python file uses the following encoding: utf-8
import sys, os

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QIcon

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.ui.start.clicked.connect(self.playAudio)
        self.ui.mute.clicked.connect(self.volumeMute)
        self.ui.audio.valueChanged.connect(self.volumeChanged)
        self.ui.audio.setValue(50)
        self.muted = False
        self.playing = False
        self.paused = False
        self.player.positionChanged.connect(self.progress)
        self.player.positionChanged.connect(self.songPosition)
        self.player.durationChanged.connect(self.setDuration)
        self.ui.play.clicked.connect(self.playbtn)
        self.ui.pause.clicked.connect(self.pausebtn)
        self.ui.startOver.clicked.connect(self.startOverSong)


    def playAudio(self):
        filepath = QFileDialog.getOpenFileName(self, ("Select song"), "/", ("Audio Files (*.mp3)"))[0]
        song = filepath.split("/")[-1]
        url = QUrl.fromLocalFile(filepath)
        if len(song)>=1:
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(url)
            self.player.play()
            self.ui.playingLabel.setText("NOW PLAYING - " + song)
            self.ui.play.setText("Playing")
            self.playing = True
            self.ui.play.setEnabled(True)
            self.ui.pause.setEnabled(True)
            self.ui.startOver.setEnabled(True)
            self.ui.progressBar.setFormat("Playing")



    def volumeChanged(self):
        self.audioOutput.setVolume(self.ui.audio.value()/100)


    def volumeMute(self):
        self.audioOutput.setMuted(not self.audioOutput.isMuted())
        if self.muted:
            self.ui.mute.setText("Mute")
        else:
            self.ui.mute.setText("Unmute")
        self.muted = not self.muted

    def progress(self):
        self.ui.progressBar.setValue(self.player.position()/self.player.duration()*100)

    def playbtn(self):
        if not self.playing:
            self.player.play()
            self.ui.play.setText("Playing")
            self.ui.pause.setText("Pause")
            self.paused = not self.paused
            self.playing = not self.playing
            self.ui.progressBar.setFormat("Playing")

    def pausebtn(self):
        if not self.paused:
            self.player.pause()
            self.ui.play.setText("Play")
            self.ui.pause.setText("Paused")
            self.paused = not self.paused
            self.playing = not self.playing
            self.ui.progressBar.setFormat("Paused")

    def startOverSong(self):
       self.player.setPosition(0)

    def songPosition(self):
        mili = self.player.position()
        seconds = (mili/1000)%60
        seconds = str(int(seconds))
        if len(seconds) == 1:
            seconds = "0"+seconds
        minutes = (mili/(1000*60))%60
        minutes = str(int(minutes))
        if len(minutes) == 1:
            minutes = "0"+minutes
        self.ui.songPosition.setText(minutes + ":" + seconds)


    def setDuration(self):
        duration = self.player.duration()
        duration_sec = (duration/1000)%60
        duration_sec = str(int(duration_sec))
        if len(duration_sec) == 1:
            duration_sec = "0"+duration_sec
        duration_min = (duration/(1000*60))%60
        duration_min = str(int(duration_min))
        if len(duration_min) == 1:
            duration_min = "0"+duration_min
        self.ui.songDuration.setText(duration_min + ":" + duration_sec)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    myicon = QIcon()
    myicon.addFile("icon.ico")
    widget.setWindowIcon(myicon)
    widget.setWindowTitle("Music Player by Kshitiz Prakash")
    widget.show()
    sys.exit(app.exec())
