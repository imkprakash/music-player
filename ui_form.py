# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(950, 200)
        Widget.setMinimumSize(QSize(950, 200))
        Widget.setMaximumSize(QSize(950, 200))
        Widget.setStyleSheet(u"Widget {\n"
"	background-color: #212121;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #1db954;\n"
"     width: 1px;\n"
"}\n"
"QLabel{\n"
"	color: #ffffff;\n"
"	background-color: #535353;\n"
"	border-radius: 5px;\n"
"}\n"
"QProgressBar{\n"
"	color: #000000;\n"
"	background-color: #535353;\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.playingLabel = QLabel(Widget)
        self.playingLabel.setObjectName(u"playingLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playingLabel.sizePolicy().hasHeightForWidth())
        self.playingLabel.setSizePolicy(sizePolicy)
        self.playingLabel.setMinimumSize(QSize(930, 100))
        self.playingLabel.setMaximumSize(QSize(930, 100))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setStyleStrategy(QFont.NoAntialias)
        self.playingLabel.setFont(font)
        self.playingLabel.setStyleSheet(u"background-image: image")
        self.playingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.playingLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.songPosition = QLabel(Widget)
        self.songPosition.setObjectName(u"songPosition")
        self.songPosition.setMinimumSize(QSize(40, 20))
        self.songPosition.setMaximumSize(QSize(40, 20))
        self.songPosition.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.songPosition)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.progressBar.setFont(font1)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout.addWidget(self.progressBar)

        self.songDuration = QLabel(Widget)
        self.songDuration.setObjectName(u"songDuration")
        self.songDuration.setMinimumSize(QSize(40, 20))
        self.songDuration.setMaximumSize(QSize(40, 20))
        self.songDuration.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.songDuration)

        self.start = QPushButton(Widget)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 35))
        self.start.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.start)

        self.startOver = QPushButton(Widget)
        self.startOver.setObjectName(u"startOver")
        self.startOver.setEnabled(False)
        self.startOver.setMinimumSize(QSize(0, 35))
        self.startOver.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.startOver)

        self.play = QPushButton(Widget)
        self.play.setObjectName(u"play")
        self.play.setEnabled(False)
        self.play.setMinimumSize(QSize(0, 35))
        self.play.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.play)

        self.pause = QPushButton(Widget)
        self.pause.setObjectName(u"pause")
        self.pause.setEnabled(False)
        self.pause.setMinimumSize(QSize(0, 35))
        self.pause.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.pause)

        self.mute = QPushButton(Widget)
        self.mute.setObjectName(u"mute")
        self.mute.setMinimumSize(QSize(0, 35))
        self.mute.setSizeIncrement(QSize(0, 35))

        self.horizontalLayout.addWidget(self.mute)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 20))
        self.label.setMaximumSize(QSize(100, 20))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.audio = QSlider(Widget)
        self.audio.setObjectName(u"audio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.audio.sizePolicy().hasHeightForWidth())
        self.audio.setSizePolicy(sizePolicy1)
        self.audio.setMinimumSize(QSize(100, 20))
        self.audio.setMaximumSize(QSize(100, 20))
        self.audio.setSizeIncrement(QSize(0, 0))
        self.audio.setCursor(QCursor(Qt.OpenHandCursor))
        self.audio.setMouseTracking(True)
        self.audio.setMaximum(100)
        self.audio.setOrientation(Qt.Horizontal)
        self.audio.setInvertedAppearance(False)
        self.audio.setInvertedControls(False)

        self.verticalLayout.addWidget(self.audio)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.playingLabel.setText(QCoreApplication.translate("Widget", u"NOW PLAYING - Select a song to play", None))
        self.songPosition.setText(QCoreApplication.translate("Widget", u"--/--", None))
        self.progressBar.setFormat("")
        self.songDuration.setText(QCoreApplication.translate("Widget", u"--/--", None))
        self.start.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.startOver.setText(QCoreApplication.translate("Widget", u"Start Over", None))
        self.play.setText(QCoreApplication.translate("Widget", u"Play", None))
        self.pause.setText(QCoreApplication.translate("Widget", u"Pause", None))
        self.mute.setText(QCoreApplication.translate("Widget", u"Mute", None))
        self.label.setText(QCoreApplication.translate("Widget", u"VOLUME", None))
    # retranslateUi

