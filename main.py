# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartUpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings
import urllib.request
from playsound import playsound
import pyttsx3 as ptts
import speech_recognition as sr
import random, os, webbrowser, time, wikipedia, datetime, smtplib, sys, time, wikipedia, subprocess
import youtube_search as ys
import wikipedia as w
from distutils.util import strtobool
from pynput.keyboard import Key, Controller


class Assistant_details(object):
    try:
        icon_display = "stark-logo"
        click_sound = 'resources\\audio\\button_click.mp3'
        start_sound = 'resources\\audio\\on.mp3'
        stop_sound = 'resources\\audio\\off.mp3'

        current_date = datetime.date.today().strftime('%d-%m-%Y')
        current_year = datetime.date.today().strftime('%Y')
        date_created = '01-06-2020'

        personal_settings = QSettings('PyQt5Application', 'Stark')
        owner = personal_settings.value('Name')
        dob = personal_settings.value('DOB')
        gender = personal_settings.value('Gender')
        nickname = personal_settings.value('Nickname')
        email = personal_settings.value('Email')

        assistant_feedback_status = strtobool(personal_settings.value('assistant_feedback_status'))
        click_sound_status = strtobool(personal_settings.value('click_sound_status'))
        start_stop_sound_status = strtobool(personal_settings.value('start_stop_sound_status'))

        music_folder = personal_settings.value('music_folder')
        voice_type = personal_settings.value('voice_type')

        if gender == 'Male':
            denotation = 'Sir'
        else:
            denotation = "Ma'am"

    except Exception as e:
        pass


class Ui_AboutAssistant(object):
    def setupUi(self, AboutAssistant):
        AboutAssistant.setObjectName("AboutAssistant")
        AboutAssistant.setWindowModality(QtCore.Qt.NonModal)
        AboutAssistant.setFixedSize(600, 450)

        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        AboutAssistant.setFont(font)
        AboutAssistant.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutAssistant.setWindowIcon(icon)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(AboutAssistant)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(215, 360, 366, 74))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.SupportVericalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.SupportVericalLayout.setContentsMargins(0, 0, 0, 0)
        self.SupportVericalLayout.setObjectName("SupportVericalLayout")
        self.SupportLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.SupportLabel.setFont(font)
        self.SupportLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SupportLabel.setObjectName("SupportLabel")
        self.SupportVericalLayout.addWidget(self.SupportLabel)
        self.SocialMediaLayout = QtWidgets.QHBoxLayout()
        self.SocialMediaLayout.setObjectName("SocialMediaLayout")

        self.YoutubeIcon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.YoutubeIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.YoutubeIcon.setText("")
        self.YoutubeIcon.setIcon(QtGui.QIcon("resources/application/youtube.png"))
        self.YoutubeIcon.setObjectName("YoutubeIcon")
        self.SocialMediaLayout.addWidget(self.YoutubeIcon)
        self.YoutubeIcon.setStyleSheet("border: none")
        self.YoutubeIcon.setIconSize(QtCore.QSize(45, 45))

        self.InstagramIcon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.InstagramIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InstagramIcon.setText("")
        self.InstagramIcon.setIcon(QtGui.QIcon("resources/application/instagram.png"))
        self.InstagramIcon.setObjectName("InstagramIcon")
        self.SocialMediaLayout.addWidget(self.InstagramIcon)
        self.InstagramIcon.setStyleSheet("border: none")
        self.InstagramIcon.setIconSize(QtCore.QSize(35, 35))

        self.GithubIcon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.GithubIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GithubIcon.setText("")
        self.GithubIcon.setIcon(QtGui.QIcon("resources/application/github.svg"))
        self.GithubIcon.setObjectName("GithubIcon")
        self.SocialMediaLayout.addWidget(self.GithubIcon)
        self.GithubIcon.setStyleSheet("border: none")
        self.GithubIcon.setIconSize(QtCore.QSize(35, 35))

        self.QuoraIcon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.QuoraIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QuoraIcon.setText("")
        self.QuoraIcon.setIcon(QtGui.QIcon("resources/application/quora.webp"))
        self.QuoraIcon.setObjectName("QuoraIcon")
        self.SocialMediaLayout.addWidget(self.QuoraIcon)
        self.QuoraIcon.setStyleSheet("border: none")
        self.QuoraIcon.setIconSize(QtCore.QSize(35, 35))

        self.LinkedinIccon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.LinkedinIccon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LinkedinIccon.setText("")
        self.LinkedinIccon.setIcon(QtGui.QIcon("resources/application/linkedin.webp"))
        self.LinkedinIccon.setObjectName("LinkedinIccon")
        self.SocialMediaLayout.addWidget(self.LinkedinIccon)
        self.LinkedinIccon.setStyleSheet("border: none")
        self.LinkedinIccon.setIconSize(QtCore.QSize(35, 35))

        self.FacebookIcon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FacebookIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FacebookIcon.setText("")
        self.FacebookIcon.setIcon(QtGui.QIcon("resources/application/facebook.png"))
        self.FacebookIcon.setObjectName("FacebookIcon")
        self.SocialMediaLayout.addWidget(self.FacebookIcon)
        self.FacebookIcon.setStyleSheet("border: none")
        self.FacebookIcon.setIconSize(QtCore.QSize(35, 35))

        self.BloggerIcon = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.BloggerIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BloggerIcon.setStatusTip("")
        self.BloggerIcon.setText("")
        self.BloggerIcon.setIcon(QtGui.QIcon("resources/application/blogger.png"))
        self.BloggerIcon.setObjectName("BloggerIcon")
        self.SocialMediaLayout.addWidget(self.BloggerIcon)
        self.BloggerIcon.setStyleSheet("border: none")
        self.BloggerIcon.setIconSize(QtCore.QSize(35, 35))

        self.SupportVericalLayout.addLayout(self.SocialMediaLayout)
        self.InformationLabel = QtWidgets.QLabel(AboutAssistant)
        self.InformationLabel.setGeometry(QtCore.QRect(30, 128, 541, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.InformationLabel.setFont(font)
        self.InformationLabel.setScaledContents(False)
        self.InformationLabel.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.InformationLabel.setWordWrap(True)
        self.InformationLabel.setObjectName("InformationLabel")
        self.CopyrightLabel = QtWidgets.QLabel(AboutAssistant)
        self.CopyrightLabel.setGeometry(QtCore.QRect(12, 362, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.CopyrightLabel.setFont(font)
        self.CopyrightLabel.setScaledContents(False)
        self.CopyrightLabel.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.CopyrightLabel.setWordWrap(True)
        self.CopyrightLabel.setObjectName("CopyrightLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AboutAssistant)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(95, 10, 439, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HeadingHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HeadingHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HeadingHorizontalLayout.setObjectName("HeadingHorizontalLayout")
        self.StarkIcon = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.StarkIcon.setMaximumSize(QtCore.QSize(100, 100))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.HeadingHorizontalLayout.addWidget(self.StarkIcon)
        self.HeadingLayout = QtWidgets.QVBoxLayout()
        self.HeadingLayout.setObjectName("HeadingLayout")
        self.StarkLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(40)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.StarkLabel.setFont(font)
        self.StarkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkLabel.setObjectName("StarkLabel")
        self.HeadingLayout.addWidget(self.StarkLabel)
        self.StarkMotto = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(25)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.StarkMotto.setFont(font)
        self.StarkMotto.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkMotto.setObjectName("StarkMotto")
        self.HeadingLayout.addWidget(self.StarkMotto)
        self.HeadingHorizontalLayout.addLayout(self.HeadingLayout)

        self.retranslateUi(AboutAssistant)
        QtCore.QMetaObject.connectSlotsByName(AboutAssistant)

        self.YoutubeIcon.clicked.connect(lambda: self.open_link('youtube'))
        self.InstagramIcon.clicked.connect(lambda: self.open_link('instagram'))
        self.GithubIcon.clicked.connect(lambda: self.open_link('github'))
        self.QuoraIcon.clicked.connect(lambda: self.open_link('quora'))
        self.LinkedinIccon.clicked.connect(lambda: self.open_link('linkedin'))
        self.FacebookIcon.clicked.connect(lambda: self.open_link('facebook'))
        self.BloggerIcon.clicked.connect(lambda: self.open_link('blogger'))

    def retranslateUi(self, AboutAssistant):
        _translate = QtCore.QCoreApplication.translate
        AboutAssistant.setWindowTitle(_translate("AboutAssistant", "About - \'Stark\'"))
        self.SupportLabel.setText(_translate("AboutAssistant", "Support the Developer"))
        self.YoutubeIcon.setToolTip(_translate("AboutAssistant", "Subscribe to YouTube Channel"))
        self.InstagramIcon.setToolTip(_translate("AboutAssistant", "Follow on Instagram"))
        self.GithubIcon.setToolTip(_translate("AboutAssistant", "Github Profile"))
        self.QuoraIcon.setToolTip(_translate("AboutAssistant", "Follow on Quora"))
        self.LinkedinIccon.setToolTip(_translate("AboutAssistant", "Connect on Linkedin"))
        self.FacebookIcon.setToolTip(_translate("AboutAssistant", "Reach at Facebook"))
        self.BloggerIcon.setToolTip(_translate("AboutAssistant", "Read Blog posts"))
        self.InformationLabel.setText(_translate("AboutAssistant",
                                                 "\'Stark\' - The Personal Assistant, is a project application made by Charitra Agarwal. It is a simple GUI based Desktop Application, which can help you carry out some troublesome tasks in a simple way. It cannot perform as good as other personal assistants like Google Assistant or Cortana, but it comes handy, even if you don\'t have internet connection. You can perform some simple tasks even without internet connected, with the help of manual command input functionality. Hope you like this project. It\'ll be a great pleasure, if you all express your love by supporting the developer in the following given links."))
        self.CopyrightLabel.setText(_translate("AboutAssistant", "\'Stark\' - The Personal Assistant\n"
                                                                 "Copyright (c) 2020 - {}\n"
                                                                 "Developer - Charitra Agarwal\n"
                                                                 "India".format(Assistant_details.current_year)))
        self.StarkLabel.setText(_translate("AboutAssistant", "Stark"))
        self.StarkMotto.setText(_translate("AboutAssistant", "The Personal Assistant"))

    def open_link(self, string=False):
        if string:
            if string == 'youtube':
                url = "https://www.youtube.com/channel/UCLeAOMSk1sGxRT8-0r3mY9g"
            if string == 'instagram':
                url = "https://www.instagram.com/everything_computerized/"
            if string == 'github':
                url = "https://github.com/Charitra1022"
            if string == 'quora':
                url = "https://www.quora.com/profile/Charitra-Agarwal-1"
            if string == 'linkedin':
                url = "https://www.linkedin.com/in/charitra1022/"
            if string == 'facebook':
                url = "https://www.facebook.com/charitra.agarwal"
            if string == 'blogger':
                url = "https://everythingcomputerized-ca.blogspot.com/"
            webbrowser.get().open(url)


class Ui_VolumeSelector(object):
    def setupUi(self, VolumeSelector):
        VolumeSelector.setObjectName("VolumeSelector")
        VolumeSelector.setFixedSize(309, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/sound-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VolumeSelector.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(VolumeSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VolumeSlider.setGeometry(QtCore.QRect(47, 46, 191, 21))
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.VolumeDisplay = QtWidgets.QLabel(self.centralwidget)
        self.VolumeDisplay.setGeometry(QtCore.QRect(250, 46, 30, 16))
        self.VolumeSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #bbb;background: white;height: 7px;border-radius: 4px;}"
        "QSlider::sub-page:horizontal {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66e, stop: 1 #bbf);"
        "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1, stop: 0 #bbf, stop: 1 #55f);border: 0px solid #777;height: 10px;border-radius: 4px;}"
        "QSlider::add-page:horizontal {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:0.5 #fff, stop: 1 #d4d4d4);border: 0px solid #777;height: 10px;border-radius: 4px;}"
        "QSlider::handle:horizontal {background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #52307c, stop: 1 #ece6ff);width: 13px;margin-top: -5px;margin-bottom: -5px;border-radius: 4px;}"
        "QSlider::handle:horizontal:hover {background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #bca0dc, stop:1 #e0d6ff);border: 0px solid #444;border-radius: 4px;}"
        "QSlider::sub-page:horizontal:disabled {background: #bbb;border-color: #999;}"
        "QSlider::add-page:horizontal:disabled {background: #eee;border-color: #999;}QSlider::handle:horizontal:disabled {background: #eee;border: 1px solid #aaa;border-radius: 4px;}")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.VolumeDisplay.setFont(font)
        self.VolumeDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.VolumeDisplay.setObjectName("VolumeDisplay")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(75, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CancelButton.setFont(font)
        self.CancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CancelButton.setStyleSheet("background-color:#0162ff; color: white; border-radius:5px")
        self.CancelButton.setObjectName("CancelButton")
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmButton.setGeometry(QtCore.QRect(180, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConfirmButton.setStyleSheet("background-color:#0162ff; color: white; border-radius:5px")
        self.ConfirmButton.setObjectName("ConfirmButton")
        VolumeSelector.setCentralWidget(self.centralwidget)
        self.VolumeSlider.setMinimum(0)
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.valueChanged.connect(self.volume_changed)

        self.CancelButton.clicked.connect(lambda: self.cancel_button(VolumeSelector))
        self.ConfirmButton.clicked.connect(lambda: self.confirm_button(VolumeSelector))

        self.settings = QSettings('PyQt5Application', 'Stark')
        try:
            self.VolumeSlider.setValue(self.settings.value('volume'))
        except:
            self.VolumeSlider.setValue(100)

        self.VolumeDisplay.setText(str(self.VolumeSlider.value()))

        self.retranslateUi(VolumeSelector)
        QtCore.QMetaObject.connectSlotsByName(VolumeSelector)
        VolumeSelector.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

    def retranslateUi(self, VolumeSelector):
        _translate = QtCore.QCoreApplication.translate
        VolumeSelector.setWindowTitle(_translate("VolumeSelector", "Volume Selector"))
        self.CancelButton.setText(_translate("VolumeSelector", "Cancel"))
        self.ConfirmButton.setText(_translate("VolumeSelector", "OK"))
        self.ConfirmButton.setShortcut(_translate("VolumeSelector", "Return"))
        self.CancelButton.setShortcut(_translate("VolumeSelector", "Esc"))

    def volume_changed(self):
        value = self.VolumeSlider.value()
        self.VolumeDisplay.setText(str(value))

    def cancel_button(self, x):
        x.close()

    def confirm_button(self, x):
        value = self.VolumeSlider.value()
        keyboard = Controller()
        for i in range(0, 50):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)

        for i in range(0, int(value / 2)):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
        self.settings.setValue('volume', self.VolumeSlider.value())
        x.close()


########################### Assistant Brain ###################################
class AssistantSpeakAndListen(object):
    @staticmethod
    def speak(string):
        """Makes the Assistant give feedback in the form of spoken words"""
        s = ptts.init()
        AssistantSpeakAndListen.voice_change()
        s.setProperty('rate', 180)
        s.say(string)
        s.runAndWait()

    @staticmethod
    def voice_change():
        s = ptts.init()
        voices = s.getProperty('voices')
        s.setProperty('voice', voices[0].id) if Assistant_details.voice_type == 'Male' else s.setProperty('voice',
                                                                                                          voices[1].id)


class Assistant_main(object):
    @classmethod
    def command_input(cls, command_input):
        """Initiate the Assistant"""
        commands_present = ['hi', 'hello', 'hey', 'stark', 'hay', 'star', 'stock',
                            'launch', 'open', 'start',
                            'google', 'youtube', 'wikipedia',
                            'search', 'find', 'navigate', 'location',
                            'calculate',
                            'help', 'assist',
                            'play', 'music',
                            'time',
                            'is', 'was', 'has', 'had',
                            'send', 'email', 'gmail', 'message',
                            'what', 'how', 'when', 'where', 'who',
                            'increase', 'decrease', 'mute', 'volume', 'full']  # recognize keywords for Assistant
        command = Commands.check_availability(command_input, commands_present)
        if command:
            status = Commands.execute_command(command_input)
            return status
        return False


class Time(object):
    """Returns the current time"""

    @staticmethod
    def current_time(string):
        """Returns the current time"""
        try:
            cur_time = datetime.datetime.now().strftime("%I:%M %p")
            Assistant_details.icon_display = 'time'
            return "The time is " + cur_time
        except:
            return 'Something went wrong'


class OtherCommands(object):
    """Class 'OtherCommands' : It contains all the miscelleneous commands related to the Assistant
    name_Assistant(string) : Speaks the name of Assistant
    age_Assistant(string) : Speaks the age of Assistant
    own_Assistant(string) : Speaks the owner of Assistant
    coder_Assistant(string) : Speaks the manufacturer of Assistant
    """

    @staticmethod
    def name_Assistant(string):
        """Class 'OtherCommands' - name_Assistant(string) : Speaks the name of Assistant"""
        Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
        return 'I\'m Stark, your Personal Assistant!'

    @staticmethod
    def age_Assistant(string):
        """Class 'OtherCommands' - age_Assistant(string) : Speaks the age of Assistant"""
        try:
            dateformat = '%d-%m-%Y'
            d1 = datetime.datetime.strptime(Assistant_details.date_created, dateformat)
            d2 = datetime.datetime.strptime(Assistant_details.current_date, dateformat)
            years = (d2 - d1).days // 365
            months = ((d2 - d1).days - years * 365) // 30
            if years == 0 and months != 0:
                Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
                return 'I\'m {} months old!'.format(str(months))
            if years != 0 and months == 0:
                Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
                return 'I\'m {} years old!'.format(str(years))
            if years != 0 and months != 0:
                Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
                return 'I\'m {} years {} months old!'.format(str(years), str(months))
            Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
            return 'I\'m ' + str((d2 - d1).days) + ' days old!'
        except:
            return 'Something went wrong'

    @staticmethod
    def own_Assistant(string):
        """Class 'OtherCommands' - own_Assistant(string) : Speaks the owner of Assistant"""
        Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
        return str('I work for {}'.format(Assistant_details.owner))

    @staticmethod
    def coder_Assistant(string):
        """Class 'OtherCommands' - coder_Assistant(string) : Speaks the manufacturer of Assistant"""
        Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
        return "I was made by 'Charitra Agarwal'. He coded me and made me worthy of helping you!"

    @staticmethod
    def age_Owner(string):
        """Class 'OtherCommands' - age_Owner(string) : Speaks the age of owner"""
        try:
            dateformat = '%d-%m-%Y'
            d1 = datetime.datetime.strptime(Assistant_details.dob, dateformat)
            d2 = datetime.datetime.strptime(Assistant_details.current_date, dateformat)
            years = (d2 - d1).days // 365
            months = ((d2 - d1).days - years * 365) // 30
            if months != 0:
                Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
                return 'You are {} years {} months old!'.format(str(years), str(months))
            Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
            return 'You are {} years old!'.format(str(years))
        except:
            return 'Something went wrong'

    @staticmethod
    def owner_name(string):
        """Returns owner name"""
        try:
            Assistant_details.icon_display = random.choice(['angel', 'happy', 'heart', 'lol', 'love', 'wink'])
            return 'You are {}'.format(Assistant_details.owner)
        except:
            return 'Something went wrong'


class Search_internet(object):
    """Opens something in the internet"""

    @staticmethod
    def search_google(string):
        """Searches for a query in the internet"""
        try:
            if 'search' in string:
                string = string.replace('search ', "")
            url = 'https://google.com/search?q=' + string
            webbrowser.get().open(url)
            Assistant_details.icon_display = 'google'
            return 'Here is what I got'
        except:
            return 'Something went wrong'

    @staticmethod
    def open_youtube(string=False):
        """Opens youtube and searches for a song if 'string' parameter present"""
        try:
            if 'open youtube' in string:
                string = string.replace('open youtube', '')
            else:
                string = string.replace('youtube', '')
            keywords = string.split()

            if len(keywords) == 0:
                url = "https://youtube.com/"
                webbrowser.get().open(url)
                Assistant_details.icon_display = 'youtube'
                return 'Opening YouTube'

            search_key = ' '.join(keywords)
            Assistant_details.icon_display = 'youtube'
            return PlayMusic.youtube_play(search_key)
        except:
            return 'Somethimg went wrong'

    @staticmethod
    def open_google(string=False):
        """Open 'google.com'"""
        try:
            url = "https://www.google.co.in/"
            webbrowser.get().open(url)
            Assistant_details.icon_display = 'google'
            return 'Opening Google'
        except:
            return 'Something went wrong'

    @staticmethod
    def wikipedia_search(string):
        """Search wikipedia for something"""
        try:
            if 'wikipedia' in string:
                string = string.replace('wikipedia', '')
            try:
                result = w.summary(string, sentences=2)
                AssistantSpeakAndListen.speak(result)
                Assistant_details.icon_display = 'wikipedia'
                return 'This was according to Wikipedia'
            except:
                Assistant_details.icon_display = 'wikipedia'
                return 'Seems like internet is not connected'
        except:
            return 'Something went wrong'


class Location_search(object):
    """Searches google for a location parameter"""

    @staticmethod
    def search_location(string):
        """Searches google for a location parameter"""
        try:
            if 'location' in string:
                string = string.replace('location ', "")
            if 'navigate' in string:
                string = string.replace('navigate ', "")
            url = 'https://google.nl/maps/place/' + string + '/&amp;'
            webbrowser.get().open(url)
            return 'Here is what I got'
        except:
            return 'Something went wrong'


class LaunchApp(object):
    """Launches a registered application"""

    @staticmethod
    def launch_app(string):
        """Checks if an application is installed or not, then opens it"""
        try:
            if 'chrome' in string or 'web browser' in string or 'browser' in string or 'internet' in string:
                try:
                    os.startfile('chrome.exe')
                except:
                    os.startfile('iexplore.exe')
                Assistant_details.icon_display = 'internet'
                return 'Launching Internet Browser'

            elif 'opera' in string:
                try:
                    os.startfile('opera.exe')
                except:
                    os.startfile('iexplore.exe')
                Assistant_details.icon_display = 'internet'
                return 'Launching Internet Browser'

            elif 'internet explore' in string:
                os.startfile('iexplore.exe')
                Assistant_details.icon_display = 'internet'
                return 'Launching Internet Browser'

            elif 'firefox' in string:
                try:
                    os.startfile('firefox.exe')
                except:
                    os.startfile('iexplore.exe')
                Assistant_details.icon_display = 'internet'
                return 'Launching Internet Browser'

            elif 'wordpad' in string or 'wattpad' in string:
                os.startfile('wordpad.exe')
                Assistant_details.icon_display = 'wordpad'
                return 'Launching Wordpad'

            elif 'ms word' in string or 'microsoft word' in string or 'word' in string:
                os.startfile('winword.exe')
                Assistant_details.icon_display = 'word'
                return 'Launching Microsoft Word'

            elif 'ms powerpoint' in string or 'microsoft powerpoint' in string or 'powerpoint' in string or 'presentation' in string or 'ppt' in string:
                os.startfile('powerpnt.exe')
                Assistant_details.icon_display = 'powerpoint'
                return 'Launching Microsoft Powerpoint'

            elif 'ms excel' in string or 'microsoft excel' in string or 'excel' in string or 'spreadsheet' in string:
                os.startfile('excel.exe')
                Assistant_details.icon_display = 'excel'
                return 'Launching Microsoft Excel'

            elif 'ms access' in string or 'microsoft access' in string or 'access' in string:
                os.startfile('msaccess.exe')
                Assistant_details.icon_display = 'access'
                return 'Launching Microsoft Access'

            elif 'settings' in string or 'device settings' in string:
                try:
                    os.system('start ms-settings:')
                    Assistant_details.icon_display = 'settings'
                    return 'Launching Settings'
                except Exception as e:
                    os.startfile('control.exe')
                    Assistant_details.icon_display = 'settings'
                    return 'Launching Control Panel'

            elif 'control panel' in string or 'control' in string or 'panel' in string:
                os.startfile('control.exe')
                Assistant_details.icon_display = 'settings'
                return 'Launching Control Panel'

            elif 'this pc' in string or 'file manager' in string or 'file explorer' in string or 'my files' in string or 'my computer' in string or 'files' in string:
                os.system('explorer.exe /e,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')
                Assistant_details.icon_display = 'files'
                return 'Launching This PC'

            elif 'notepad' in string:
                os.startfile('notepad.exe')
                Assistant_details.icon_display = 'wordpad'
                return 'Launching Notepad'

            elif 'cmd' in string or 'command prompt' in string or 'terminal' in string or 'command' in string or 'prompt' in string:
                os.startfile('cmd.exe')
                Assistant_details.icon_display = 'cmd'
                return 'Launching Microsoft Command Prompt'

            elif 'calculator' in string or 'calculation' in string or 'calc' in string:
                os.startfile('calc.exe')
                Assistant_details.icon_display = 'calculator'
                return 'Launching Calculator'

            elif 'powershell' in string:
                try:
                    os.startfile('powershell.exe')
                    Assistant_details.icon_display = 'powershell'
                    return 'Launching Windows PowerShell'
                except Exception as e:
                    os.startfile('cmd.exe')
                    Assistant_details.icon_display = 'cmd'
                    return 'Launching Microsoft Command Prompt'

            elif 'run' in string:
                os.system('explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}')
                Assistant_details.icon_display = 'run'
                return 'Launching Run'

            elif 'paint' in string or 'mspaint' in string or 'microsoft paint' in string or 'draw' in string or 'colour' in string or 'color' in string:
                os.startfile('mspaint.exe')
                Assistant_details.icon_display = 'paint'
                return 'Launching Microsoft Paint'

            elif 'task manager' in string:
                os.startfile("taskmgr.exe")
                Assistant_details.icon_display = 'task-manager'
                return 'Launching Task Manager'

            elif 'media player' in string or 'music player' in string or 'music' in string or 'song' in string:
                os.startfile("wmplayer.exe")
                Assistant_details.icon_display = 'music'
                return 'Launching Windows Media Player'

            else:
                Assistant_details.icon_display = 'not_found'
                return "Seems like the application is not installed"

        except Exception as e:
            Assistant_details.icon_display = 'not_found'
            return "Seems like the application is not installed"


class PlayMusic(object):
    """Opens a music streamer and plays a desired song"""

    @staticmethod
    def music_search(keywords, song):
        """Searches for a song and returns its path if requested else returns a random music path"""
        try:
            if song:
                found = False
                for root, directories, files in os.walk(Assistant_details.music_folder):
                    for file in files:
                        for keyword in keywords:
                            if not keyword in file.lower():
                                found = False
                                break
                            found = True
                        if found:
                            return root + '\\' + file
                return
            else:
                for root, directories, files in os.walk(Assistant_details.music_folder):
                    music = root + '\\' + str(random.choice(files))
                    while not '.mp3' in music:
                        music = root + '\\' + str(random.choice(files))
                    return music
        except: return

    @staticmethod
    def play_music(string):
        """Opens a music streamer and plays a desired song"""
        if 'play music' in string:
            string = string.replace('play music', '')
        else:
            string = string.replace('play', '')
        if Assistant_details.music_folder != 'None' and Assistant_details.music_folder != '':
            try:
                keywords = string.lower().split()
                if len(keywords) == 0:
                    music_found = PlayMusic.music_search(keywords, False)
                else:
                    music_found = PlayMusic.music_search(keywords, True)

                if music_found:
                    try:
                        wmp = r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"
                        subprocess.Popen([wmp, music_found])
                        Assistant_details.icon_display = 'music'
                        return 'Playing ' + string.title()
                    except:
                        pass
                return PlayMusic.youtube_play(string)
            except:
                return 'Something went wrong'
        else:
            try:
                return PlayMusic.youtube_play(string)
            except:
                return 'Something went wrong'

    @staticmethod
    def youtube_play(string):
        try:
            results = ys.YoutubeSearch(string, max_results=1).to_dict()
            result_dict = results[0]
            title = result_dict['title']
            id = result_dict['id']
            url = "https://m.youtube.com/watch?v=" + id
            webbrowser.get().open(url)
            os.system("taskkill /im wmplayer.exe")
            Assistant_details.icon_display = 'youtube'
            return 'Playing ' + '"' + title + '"'
        except:
            Assistant_details.icon_display = 'internet_error'
            return 'Seems like internet is not connected'


class Commands(object):
    """'Commands' class: Contains functions for starting phase of a command, i.e, initialization, processing
    start_Assistant() : Listen to the commands and return it in string
    check_availability(string_input, commands_present) : checks if a command is acceptable or not
    hello_Assistant() : greets the user
    help_Assistant() : opens up help window
    execute_command(command) : processes the command and calls the required functions"""

    @staticmethod
    def check_availability(string_input, commands_present):
        """In 'Commands' class - check_availability(str_in, commands_present) : Check if a command is available for execution, else return 'None'"""
        for command in commands_present:
            if command in string_input:
                return command
        return

    @staticmethod
    def hello_Assistant():
        """In 'Commands' class - hello_Assistant() : Greetings for first initialization of the Assistant"""
        greet_str = ['Hi There!',
                     "Hello {},".format(Assistant_details.denotation),
                     "I'm before you!",
                     "I'm your Assistant!",
                     "Hola!",
                     "What's up!",
                     "I'm Stark! Your Assistant!"]

        order_str = ["How can I help?",
                     "How can I help you?",
                     "What do you want me to do?",
                     "How do you want me to assist you?",
                     "What do you want me to do?",
                     "I'm waiting eagerly for your orders!"]

        string = str(random.choice(greet_str)) + " " + str(random.choice(order_str))
        return string

    @staticmethod
    def help_Assistant():
        Ui_StarkWindow.helpui = Ui_HelpAssistant()
        Ui_StarkWindow.helpwindow = QtWidgets.QMainWindow()
        Ui_StarkWindow.helpui.setupUi(Ui_StarkWindow.helpwindow)
        Ui_StarkWindow.helpwindow.show()
        Assistant_details.icon_display = 'help_assistant'
        return "Opening Assistant Help"

    @staticmethod
    def execute_command(command_str):
        """In 'Commands' class - execute_command(command_str) : If a command is recognized as acceptable, run the associated task"""
        try:
            ############ Miscelleneous Commands ###################
            if 'what is your name' in command_str or 'who are you' in command_str:
                return OtherCommands.name_Assistant(command_str)

            elif 'what is my name' in command_str or 'who am i' in command_str or 'who i am' in command_str:
                return OtherCommands.owner_name(command_str)

            elif 'what is my age' in command_str or 'how old am i' in command_str or 'how old i am' in command_str or 'how much old am i' in command_str or 'how much old i am' in command_str:
                return OtherCommands.age_Owner(command_str)

            elif 'what is your age' in command_str or 'how much old are you' in command_str or 'how much old you are' in command_str or 'how old are you' in command_str or 'how old you are' in command_str:
                return OtherCommands.age_Assistant(command_str)

            elif 'what is your owner' in command_str or 'who is your owner' in command_str or 'who is your master' in command_str or 'who owns you' in command_str or 'who is owner' in command_str:
                return OtherCommands.own_Assistant(command_str)

            elif 'who made you' in command_str or 'who designed you' in command_str or 'who coded you' in command_str or 'who manufactured you' in command_str or 'who created you' in command_str or 'who wrote you' in command_str:
                return OtherCommands.coder_Assistant(command_str)
            ###########################################################

            ################### Service Commands ######################
            elif 'open google' in command_str or 'google' in command_str:
                return Search_internet.open_google(command_str)

            elif 'increase volume' in command_str or 'decrease volume' in command_str or 'mute volume' in command_str or 'full volume' in command_str:
                return VolumeCommands.volume_control(command_str)

            elif 'open youtube' in command_str or 'youtube' in command_str:
                return Search_internet.open_youtube(command_str)

            elif 'launch' in command_str or 'open' in command_str:
                return LaunchApp.launch_app(command_str)

            elif 'play music' in command_str or 'play' in command_str:
                return PlayMusic.play_music(command_str)

            elif 'time' in command_str:
                return Time.current_time(command_str)

            elif 'search' in command_str or 'what' in command_str or 'where' in command_str or 'how' in command_str or 'who' in command_str or 'when' in command_str:
                return Search_internet.search_google(command_str)

            elif 'location' in command_str or 'navigate' in command_str:
                return Location_search.search_location(command_str)

            elif 'wikipedia' in command_str:
                return Search_internet.wikipedia_search(command_str)

            elif 'hi' in command_str or 'hello' in command_str or 'stark' in command_str or 'hey' in command_str or 'hay' in command_str:
                return Commands.hello_Assistant()

            elif 'help assistant' in command_str:
                return Commands.help_Assistant()
            ##################################################################

            else:
                return Search_internet.search_google(command_str)
            # find command to write
            return status
        except:
            return 'command not found'


class VolumeCommands(object):
    """Controls the volume of the Computer"""
    @staticmethod
    def volume_control(string):
        if 'increase' in string:
            return VolumeCommands.increase_volume()
        if 'decrease' in string:
            return VolumeCommands.decrease_volume()
        if 'mute' in string:
            return VolumeCommands.mute_volume()
        if 'full' in string:
            return VolumeCommands.full_volume()

    @staticmethod
    def increase_volume():
        try:
            keyboard = Controller()
            for i in range(0, 5):
                keyboard.press(Key.media_volume_up)
                keyboard.release(Key.media_volume_up)
            Assistant_details.icon_display = 'volume'
        except Exception as e:
            pass
        return 'Done'

    @staticmethod
    def decrease_volume():
        try:
            keyboard = Controller()
            for i in range(0, 5):
                keyboard.press(Key.media_volume_down)
                keyboard.release(Key.media_volume_down)
            Assistant_details.icon_display = 'volume'
        except Exception as e:
            pass
        return 'Done'

    @staticmethod
    def mute_volume():
        try:
            keyboard = Controller()
            keyboard.press(Key.media_volume_mute)
            keyboard.release(Key.media_volume_mute)
            Assistant_details.icon_display = 'mute'
        except Exception as e:
            pass
        return 'Done'

    @staticmethod
    def full_volume():
        try:
            keyboard = Controller()
            for i in range(0, 50):
                keyboard.press(Key.media_volume_up)
                keyboard.release(Key.media_volume_up)
            Assistant_details.icon_display = 'volume'
        except Exception as e:
            pass
        return 'Done'


################################ UI Elements ######################################

class Ui_HelpAssistant(object):
    def setupUi(self, HelpAssistant):
        HelpAssistant.setObjectName("HelpAssistant")
        HelpAssistant.setFixedSize(547, 389)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpAssistant.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpAssistant)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(171, 10, 301, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StarkTitle.sizePolicy().hasHeightForWidth())
        self.StarkTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setOpenExternalLinks(False)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle_2.sizePolicy().hasHeightForWidth())
        self.PageTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setOpenExternalLinks(False)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(80, 10, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 140, 311, 156))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Help4Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help4Button.setFont(font)
        self.Help4Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help4Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help4Button.setObjectName("Help4Button")
        self.gridLayout.addWidget(self.Help4Button, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.Help2Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help2Button.setFont(font)
        self.Help2Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help2Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help2Button.setObjectName("Help2Button")
        self.gridLayout.addWidget(self.Help2Button, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.Help5Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help5Button.setFont(font)
        self.Help5Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help5Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help5Button.setObjectName("Help5Button")
        self.gridLayout.addWidget(self.Help5Button, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Help3Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help3Button.setFont(font)
        self.Help3Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help3Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help3Button.setObjectName("Help3Button")
        self.gridLayout.addWidget(self.Help3Button, 2, 1, 1, 1)
        self.Help1Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help1Button.setFont(font)
        self.Help1Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help1Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help1Button.setObjectName("Help1Button")
        self.gridLayout.addWidget(self.Help1Button, 0, 1, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(430, 320, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.CloseButton.setFlat(False)
        self.CloseButton.setObjectName("CloseButton")
        HelpAssistant.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpAssistant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 21))
        self.menubar.setObjectName("menubar")
        HelpAssistant.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpAssistant)
        self.statusbar.setObjectName("statusbar")
        HelpAssistant.setStatusBar(self.statusbar)

        self.Help1Button.clicked.connect(lambda: self.help1_button(HelpAssistant))
        self.Help2Button.clicked.connect(lambda: self.help2_button(HelpAssistant))
        self.Help3Button.clicked.connect(lambda: self.help3_button(HelpAssistant))
        self.Help4Button.clicked.connect(lambda: self.help4_button(HelpAssistant))
        self.Help5Button.clicked.connect(lambda: self.help5_button(HelpAssistant))
        self.CloseButton.clicked.connect(lambda: self.close_button(HelpAssistant))

        self.retranslateUi(HelpAssistant)
        QtCore.QMetaObject.connectSlotsByName(HelpAssistant)

    def retranslateUi(self, HelpAssistant):
        _translate = QtCore.QCoreApplication.translate
        HelpAssistant.setWindowTitle(_translate("HelpAssistant", "\'Stark\' - Help"))
        self.StarkTitle.setText(_translate("HelpAssistant", "Stark"))
        self.PageTitle_2.setText(_translate("HelpAssistant", "The Personal Assistant"))
        self.Help4Button.setText(_translate("HelpAssistant", "Information regarding Internet access"))
        self.label_4.setText(_translate("HelpAssistant", "4."))
        self.Help2Button.setText(_translate("HelpAssistant", "What all commands are available?"))
        self.label_2.setText(_translate("HelpAssistant", "2."))
        self.label_3.setText(_translate("HelpAssistant", "3."))
        self.label_5.setText(_translate("HelpAssistant", "5."))
        self.Help5Button.setText(_translate("HelpAssistant", "\'Stark\' Settings and customization"))
        self.label.setText(_translate("HelpAssistant", "1."))
        self.Help3Button.setText(_translate("HelpAssistant", "Shortcut keys into Action"))
        self.Help1Button.setText(_translate("HelpAssistant", "How to use \'Stark\'?"))
        self.CloseButton.setText(_translate("HelpAssistant", "Close"))

    def help1_button(self, x):
    	self.help1_ui = Ui_HelpAssistant1()
    	self.help1_window = QtWidgets.QMainWindow()
    	self.help1_ui.setupUi(self.help1_window)
    	x.close()
    	self.help1_window.show()

    def help2_button(self, x):
    	self.help2_ui = Ui_HelpAssistant2()
    	self.help2_window = QtWidgets.QMainWindow()
    	self.help2_ui.setupUi(self.help2_window)
    	x.close()
    	self.help2_window.show()

    def help3_button(self, x):
    	self.help3_ui = Ui_HelpAssistant3()
    	self.help3_window = QtWidgets.QMainWindow()
    	self.help3_ui.setupUi(self.help3_window)
    	x.close()
    	self.help3_window.show()

    def help4_button(self, x):
    	self.help4_ui = Ui_HelpAssistant4()
    	self.help4_window = QtWidgets.QMainWindow()
    	self.help4_ui.setupUi(self.help4_window)
    	x.close()
    	self.help4_window.show()

    def help5_button(self, x):
    	self.help5_ui = Ui_HelpAssistant5()
    	self.help5_window = QtWidgets.QMainWindow()
    	self.help5_ui.setupUi(self.help5_window)
    	x.close()
    	self.help5_window.show()

    def close_button(self, x):
    	x.close()


class Ui_HelpAssistant1(object):
    def setupUi(self, HelpAssistant1):
        HelpAssistant1.setObjectName("HelpAssistant1")
        HelpAssistant1.setFixedSize(619, 621)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpAssistant1.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpAssistant1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 17, 301, 73))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setSpacing(0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StarkTitle.sizePolicy().hasHeightForWidth())
        self.StarkTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setOpenExternalLinks(False)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle_2.sizePolicy().hasHeightForWidth())
        self.PageTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setOpenExternalLinks(False)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(121, 10, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(512, 550, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.CloseButton.setFlat(False)
        self.CloseButton.setObjectName("CloseButton")
        self.GoBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackButton.setGeometry(QtCore.QRect(24, 550, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.GoBackButton.setFont(font)
        self.GoBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GoBackButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.GoBackButton.setFlat(False)
        self.GoBackButton.setObjectName("GoBackButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(8, 110, 600, 431))
        self.scrollArea.setMaximumSize(QtCore.QSize(600, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color:white;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1451, 579, 1878))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMaximumSize(QtCore.QSize(160, 30))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/images/menubar.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setMaximumSize(QtCore.QSize(250, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("resources/images/mic-prepare.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setMaximumSize(QtCore.QSize(250, 50))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("resources/images/mic-listen.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setMaximumSize(QtCore.QSize(250, 50))
        self.label_11.setStyleSheet("")
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("resources/images/keyboard-input.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setMaximumSize(QtCore.QSize(250, 50))
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("resources/images/keyboard-input1.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_14.setFont(font)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setMaximumSize(QtCore.QSize(200, 130))
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("resources/images/file-menu.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout.addWidget(self.line_9)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_17.setFont(font)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setMaximumSize(QtCore.QSize(210, 130))
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("resources/images/settings-menu.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout.addWidget(self.line_10)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setMaximumSize(QtCore.QSize(400, 120))
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("resources/images/settings-menu1.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_20.setFont(font)
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setScaledContents(True)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setMaximumSize(QtCore.QSize(310, 120))
        self.label_21.setFrameShape(QtWidgets.QFrame.Box)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("resources/images/settings-menu2.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_22.setFont(font)
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setScaledContents(True)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setMaximumSize(QtCore.QSize(195, 120))
        self.label_23.setFrameShape(QtWidgets.QFrame.Box)
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("resources/images/settings-menu3.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout.addWidget(self.line_13)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_24.setFont(font)
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setMaximumSize(QtCore.QSize(290, 120))
        self.label_25.setFrameShape(QtWidgets.QFrame.Box)
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("resources/images/settings-menu4.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.line_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout.addWidget(self.line_14)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_26.setFont(font)
        self.label_26.setTextFormat(QtCore.Qt.AutoText)
        self.label_26.setScaledContents(True)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.verticalLayout.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setMaximumSize(QtCore.QSize(180, 120))
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("resources/images/settings-menu5.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.verticalLayout.addWidget(self.label_27)
        self.line_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout.addWidget(self.line_15)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_29.setFont(font)
        self.label_29.setTextFormat(QtCore.Qt.AutoText)
        self.label_29.setScaledContents(True)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.label_29)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setMaximumSize(QtCore.QSize(295, 120))
        self.label_28.setFrameShape(QtWidgets.QFrame.Box)
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("resources/images/help-menu.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.verticalLayout.addWidget(self.label_28)
        self.line_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout.addWidget(self.line_16)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        HelpAssistant1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpAssistant1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 21))
        self.menubar.setObjectName("menubar")
        HelpAssistant1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpAssistant1)
        self.statusbar.setObjectName("statusbar")
        HelpAssistant1.setStatusBar(self.statusbar)

        self.CloseButton.clicked.connect(lambda: self.close_button(HelpAssistant1))
        self.GoBackButton.clicked.connect(lambda: self.help_menu_button(HelpAssistant1))

        self.retranslateUi(HelpAssistant1)
        QtCore.QMetaObject.connectSlotsByName(HelpAssistant1)

    def retranslateUi(self, HelpAssistant1):
        _translate = QtCore.QCoreApplication.translate
        HelpAssistant1.setWindowTitle(_translate("HelpAssistant1", "\'Stark\' - How to use \'Stark\'"))
        self.StarkTitle.setText(_translate("HelpAssistant1", "Stark"))
        self.PageTitle_2.setText(_translate("HelpAssistant1", "The Personal Assistant"))
        self.CloseButton.setText(_translate("HelpAssistant1", "Close"))
        self.GoBackButton.setText(_translate("HelpAssistant1", "< Go back"))
        self.label.setText(_translate("HelpAssistant1", "1. Below is the \'Stark\' Menubar. Certain features related to \'Stark\' can be accessed from here."))
        self.label_3.setText(_translate("HelpAssistant1", "2. Click on the Microphone Button to give voice commands to \'Stark\'. Note- It requires active internet connection as well as a physical Microphone attached to the system! Once active, it will prepare the system for about a second, and then will start listening to you."))
        self.label_13.setText(_translate("HelpAssistant1", "3. If you don\'t have a Microphone, or don\'t have internet access, don\'t worry. We have a manual command input functionality, by which you can give exactly the same commands, which you would give using the voice input.\n"
"To access that, click on the Keyboard icon. A text input box will appear, where you can type your commands. To execute the command, press \'Enter\' or click on the \'Send\' button"))
        self.label_14.setText(_translate("HelpAssistant1", "4. In the \'File\' menu, there are 3 functions which you could use.\n"
"\'Exit\' - Exits the application\n"
"\'Restart\' -  Restarts the application\n"
"\'Re-configure\' - Starts the application right from the starting point, that is, from the \'Configuration\'"))
        self.label_17.setText(_translate("HelpAssistant1", "5. In the \'Settings\' menu, there are various functions, for customizing the application."))
        self.label_18.setText(_translate("HelpAssistant1", "6. In the \'Sound Settings\', you could change the settings related to Sound output.\n"
"\'Assistant Feedback\' - Turn on/off the voice output of the assistant.\n"
"\'Button Click Feedback\' - Turn on/off the click sounds of the various buttons.\n"
"\'Start/Stop Sound Indication\' - Turn on/off the sound indication for voice command activation.\n"
"          By default, these all are set to \'On\'\n"
"If a parameter is set to \'On\', it will display \'Off\' and vice-versa."))
        self.label_20.setText(_translate("HelpAssistant1", "7. In the \'Folders and Paths Settings\', you could change the default music directory.\n"
"When you\'ll give the command to Play music, \'Stark\' will search for the requested music in this directory. If the music is found, it will play it from here, else, it will play that music on YouTube."))
        self.label_22.setText(_translate("HelpAssistant1", "8. In the \'Personal Settings\', you could update the personal details, like your \'Name\' and other parameters, which you entered during the Setup of \'Stark\'."))
        self.label_24.setText(_translate("HelpAssistant1", "9. In the \'Assistant Settings\', you could alter the settings related to \'Stark\', like, its Voice or its Volume.\n"
"In \'Voice\', there are two Voices - \'Male\' & \'Female\'. By default, \'Male\' is its voice, which you could change to \'Female\' later. Note: On some devices, this setting may not work as expected.\n"
"In \'Volume\', you could select the volume of \'Stark\'. It will set the volume of your computer to the required loudness."))
        self.label_26.setText(_translate("HelpAssistant1", "10. \'Revert to defaults\' will change \'Sound Settings\' and \'Assistant Settings\' to their default value."))
        self.label_29.setText(_translate("HelpAssistant1", "11. In\' Help\' menu, there are 2 options you can choose.\n"
"\'Assistant Help\' - For detailed explanation of \'Stark\' and its functions\n"
"\'About\' - About this application and the developer"))

    def close_button(self, x):
    	x.close()

    def help_menu_button(self, x):
    	self.helpMenuUi = Ui_HelpAssistant()
    	self.helpMenuWindow = QtWidgets.QMainWindow()
    	self.helpMenuUi.setupUi(self.helpMenuWindow)
    	x.close()
    	self.helpMenuWindow.show()


class Ui_HelpAssistant2(object):
    def setupUi(self, HelpAssistant2):
        HelpAssistant2.setObjectName("HelpAssistant2")
        HelpAssistant2.setFixedSize(619, 617)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpAssistant2.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpAssistant2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 17, 301, 73))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setSpacing(0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StarkTitle.sizePolicy().hasHeightForWidth())
        self.StarkTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setOpenExternalLinks(False)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle_2.sizePolicy().hasHeightForWidth())
        self.PageTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setOpenExternalLinks(False)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(121, 10, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(512, 550, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.CloseButton.setFlat(False)
        self.CloseButton.setObjectName("CloseButton")
        self.GoBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackButton.setGeometry(QtCore.QRect(24, 550, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.GoBackButton.setFont(font)
        self.GoBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GoBackButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.GoBackButton.setFlat(False)
        self.GoBackButton.setObjectName("GoBackButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(8, 110, 600, 431))
        self.scrollArea.setMaximumSize(QtCore.QSize(600, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color:white;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -478, 579, 905))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setMaximumSize(QtCore.QSize(561, 130))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_14.setFont(font)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout.addWidget(self.line_9)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_17.setFont(font)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout.addWidget(self.line_10)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_20.setFont(font)
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setScaledContents(True)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_22.setFont(font)
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setScaledContents(True)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_23.setFont(font)
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setScaledContents(True)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_24.setFont(font)
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout.addWidget(self.line_13)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        HelpAssistant2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpAssistant2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 21))
        self.menubar.setObjectName("menubar")
        HelpAssistant2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpAssistant2)
        self.statusbar.setObjectName("statusbar")
        HelpAssistant2.setStatusBar(self.statusbar)

        self.CloseButton.clicked.connect(lambda: self.close_button(HelpAssistant2))
        self.GoBackButton.clicked.connect(lambda: self.help_menu_button(HelpAssistant2))

        self.retranslateUi(HelpAssistant2)
        QtCore.QMetaObject.connectSlotsByName(HelpAssistant2)

    def retranslateUi(self, HelpAssistant2):
        _translate = QtCore.QCoreApplication.translate
        HelpAssistant2.setWindowTitle(_translate("HelpAssistant2", "\'Stark\' - Commands Available"))
        self.StarkTitle.setText(_translate("HelpAssistant2", "Stark"))
        self.PageTitle_2.setText(_translate("HelpAssistant2", "The Personal Assistant"))
        self.CloseButton.setText(_translate("HelpAssistant2", "Close"))
        self.GoBackButton.setText(_translate("HelpAssistant2", "< Go back"))
        self.label.setText(_translate("HelpAssistant2", "1. Audio Control Commands -\n"
"     i. \'Increase Volume\' - Increases system volume by 10 units\n"
"     ii. \'Decrease Volume\' - Decreases system volume by 10 units\n"
"     iii. \'Mute Volume\' - Mutes the system volume\n"
"     iv. \'Full Volume\' - Turns up the system volume to full"))
        self.label_3.setText(_translate("HelpAssistant2", "2. Opening Application - \n"
"     Use \'Launch\' or \'Open\' keyword, along with the name of the application, to open that Application.\n"
"     Ex1- \'Launch Microsoft Word\' - Opens MS Word\n"
"     Ex2- \'Open Chrome\' - Launches Chrome, if installed, else launches any other internet browser."))
        self.label_13.setText(_translate("HelpAssistant2", "     Currently, there is a limited number of applications registered. It will be updated in the future updates.\n"
"     The Applications currently supported by the \'Launch\' command are - "))
        self.label_6.setText(_translate("HelpAssistant2", "Chrome\n"
"Firefox\n"
"Opera\n"
"Internet Explorer\n"
"Internet Browser\n"
"Wordpad"))
        self.label_7.setText(_translate("HelpAssistant2", "Notepad\n"
"Paint\n"
"Calculator\n"
"Windows Media Player\n"
"Task Manager\n"
"Control Panel"))
        self.label_9.setText(_translate("HelpAssistant2", "Command Prompt\n"
"Powershell\n"
"Run\n"
"This PC\n"
"My Files\n"
"My Computer"))
        self.label_5.setText(_translate("HelpAssistant2", "MS Word\n"
"MS Powerpoint\n"
"MS Access\n"
"MS Excel\n"
"Settings\n"
""))
        self.label_14.setText(_translate("HelpAssistant2", "3. Open certain Websites - \n"
"     i. \'Open Google\' - Opens https://www.google.com/\n"
"     ii. \'Open YouTube\' - Opens https://www.youtube.com/"))
        self.label_15.setText(_translate("HelpAssistant2", "4. Search something on Websites - \n"
"     i. \'YouTube <search item>\' - Opens the requested item on YouTube.\n"
"      Ex- \'YouTube Everything Computerized\'- Searches for \'Everything Computerized\' on YouTube.\n"
"\n"
"     ii. \'Search <search item>\'- Searches for the requested item on Google."))
        self.label_16.setText(_translate("HelpAssistant2", "     You can use custom Search commands to search for something in the web\n"
"          Ex-\'Who is the President of India\'\n"
""))
        self.label_17.setText(_translate("HelpAssistant2", "     iii. \'Wikipedia <search item>\'- Accesses Wikipedia and reads out a summary of the search item.\n"
"     iv. \'Location <search item>\'- Locates a place on Google Maps and gives the result."))
        self.label_18.setText(_translate("HelpAssistant2", "5. Play Music Commands - \n"
"     i. \'Play <music name>\'- Plays the requested music either from your computer or on YouTube.\n"
"     ii. \'Play Music\'- Plays any random music from your computer."))
        self.label_20.setText(_translate("HelpAssistant2", "6. System Commands - \n"
"     i. \'Time\' - Gives the current time.\n"
"     ii. \'Exit\' - Exits or closes \'Stark\'."))
        self.label_22.setText(_translate("HelpAssistant2", "7. Fun Commands - \n"
"     i. \'Hello Stark\'\n"
"     ii. \'What is your name\'\n"
"     iii. \'What is your age\'"))
        self.label_23.setText(_translate("HelpAssistant2", "     iv. \'What is my name\'\n"
"     v. \'What is my age\'"))
        self.label_24.setText(_translate("HelpAssistant2", "     vi. \'Who is your owner\'\n"
"     vii. \'Who made you\'"))


    def close_button(self, x):
        x.close()

    def help_menu_button(self, x):
        self.helpMenuUi = Ui_HelpAssistant()
        self.helpMenuWindow = QtWidgets.QMainWindow()
        self.helpMenuUi.setupUi(self.helpMenuWindow)
        x.close()
        self.helpMenuWindow.show()


class Ui_HelpAssistant3(object):
    def setupUi(self, HelpAssistant3):
        HelpAssistant3.setObjectName("HelpAssistant3")
        HelpAssistant3.setFixedSize(621, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpAssistant3.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpAssistant3)
        self.centralwidget.setObjectName("centralwidget")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(515, 351, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.CloseButton.setFlat(False)
        self.CloseButton.setObjectName("CloseButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 130, 561, 171))
        self.scrollArea.setMaximumSize(QtCore.QSize(600, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color:white;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 557, 167))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_31.setFont(font)
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_2.addWidget(self.label_31)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.GoBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackButton.setGeometry(QtCore.QRect(27, 351, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.GoBackButton.setFont(font)
        self.GoBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GoBackButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.GoBackButton.setFlat(False)
        self.GoBackButton.setObjectName("GoBackButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(213, 8, 301, 73))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setSpacing(0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StarkTitle.sizePolicy().hasHeightForWidth())
        self.StarkTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setOpenExternalLinks(False)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle_2.sizePolicy().hasHeightForWidth())
        self.PageTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setOpenExternalLinks(False)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(124, 1, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.Help1Button = QtWidgets.QPushButton(self.centralwidget)
        self.Help1Button.setGeometry(QtCore.QRect(276, 308, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help1Button.setFont(font)
        self.Help1Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help1Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help1Button.setObjectName("Help1Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 310, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        HelpAssistant3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpAssistant3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
        self.menubar.setObjectName("menubar")
        HelpAssistant3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpAssistant3)
        self.statusbar.setObjectName("statusbar")
        HelpAssistant3.setStatusBar(self.statusbar)

        self.CloseButton.clicked.connect(lambda: self.close_button(HelpAssistant3))
        self.GoBackButton.clicked.connect(lambda: self.help_menu_button(HelpAssistant3))
        self.Help1Button.clicked.connect(lambda: self.help1_button(HelpAssistant3))

        self.retranslateUi(HelpAssistant3)
        QtCore.QMetaObject.connectSlotsByName(HelpAssistant3)

    def retranslateUi(self, HelpAssistant3):
        _translate = QtCore.QCoreApplication.translate
        HelpAssistant3.setWindowTitle(_translate("HelpAssistant3", "\'Stark\' - Shortcut keys into Action"))
        self.CloseButton.setText(_translate("HelpAssistant3", "Close"))
        self.label.setText(_translate("HelpAssistant3", "\'Stark\' has some of the functionalities, which can be controlled using some Shortcut keys, to make its use easier.\n"
"\n"
"These are - "))
        self.label_31.setText(_translate("HelpAssistant3", "i. \'Alt + M\' - to activate Voice Command mode (can also be done by clicking Microphone icon)\n"
"ii. \'Alt + K\' - to activate Keyboard Input mode (can also be done by clicking Keyboard icon)\n"
"iii. \'Alt + F4\' - To close the assistant\n"
"iv. \'Ctrl + H\' - To open the \'Help\' menu."))
        self.GoBackButton.setText(_translate("HelpAssistant3", "< Go back"))
        self.StarkTitle.setText(_translate("HelpAssistant3", "Stark"))
        self.PageTitle_2.setText(_translate("HelpAssistant3", "The Personal Assistant"))
        self.Help1Button.setText(_translate("HelpAssistant3", "How to use \'Stark\'?"))
        self.label_2.setText(_translate("HelpAssistant3", "Also have a look on "))

    def close_button(self, x):
        x.close()

    def help_menu_button(self, x):
        self.helpMenuUi = Ui_HelpAssistant()
        self.helpMenuWindow = QtWidgets.QMainWindow()
        self.helpMenuUi.setupUi(self.helpMenuWindow)
        x.close()
        self.helpMenuWindow.show()

    def help1_button(self, x):
    	self.help1_ui = Ui_HelpAssistant1()
    	self.help1_window = QtWidgets.QMainWindow()
    	self.help1_ui.setupUi(self.help1_window)
    	x.close()
    	self.help1_window.show()


class Ui_HelpAssistant4(object):
    def setupUi(self, HelpAssistant4):
        HelpAssistant4.setObjectName("HelpAssistant4")
        HelpAssistant4.setFixedSize(621, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpAssistant4.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpAssistant4)
        self.centralwidget.setObjectName("centralwidget")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(515, 461, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.CloseButton.setFlat(False)
        self.CloseButton.setObjectName("CloseButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(11, 100, 600, 311))
        self.scrollArea.setMaximumSize(QtCore.QSize(600, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color:white;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 596, 307))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setMaximumSize(QtCore.QSize(573, 100))
        self.label.setSizeIncrement(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_31.setFont(font)
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_2.addWidget(self.label_31)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setMaximumSize(QtCore.QSize(400, 150))
        self.label_35.setFrameShape(QtWidgets.QFrame.Box)
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("resources/images/internet-error.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_2.addWidget(self.label_35)
        self.line_22 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_2.addWidget(self.line_22)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.GoBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackButton.setGeometry(QtCore.QRect(27, 461, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.GoBackButton.setFont(font)
        self.GoBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GoBackButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.GoBackButton.setFlat(False)
        self.GoBackButton.setObjectName("GoBackButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(213, 8, 301, 73))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setSpacing(0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StarkTitle.sizePolicy().hasHeightForWidth())
        self.StarkTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setOpenExternalLinks(False)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle_2.sizePolicy().hasHeightForWidth())
        self.PageTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setOpenExternalLinks(False)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(124, 1, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.Help1Button = QtWidgets.QPushButton(self.centralwidget)
        self.Help1Button.setGeometry(QtCore.QRect(276, 418, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help1Button.setFont(font)
        self.Help1Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help1Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help1Button.setObjectName("Help1Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 420, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        HelpAssistant4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpAssistant4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
        self.menubar.setObjectName("menubar")
        HelpAssistant4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpAssistant4)
        self.statusbar.setObjectName("statusbar")
        HelpAssistant4.setStatusBar(self.statusbar)

        self.CloseButton.clicked.connect(lambda: self.close_button(HelpAssistant4))
        self.GoBackButton.clicked.connect(lambda: self.help_menu_button(HelpAssistant4))
        self.Help1Button.clicked.connect(lambda: self.help1_button(HelpAssistant4))

        self.retranslateUi(HelpAssistant4)
        QtCore.QMetaObject.connectSlotsByName(HelpAssistant4)

    def retranslateUi(self, HelpAssistant4):
        _translate = QtCore.QCoreApplication.translate
        HelpAssistant4.setWindowTitle(_translate("HelpAssistant4", "\'Stark\' - Information regarding Internet access"))
        self.CloseButton.setText(_translate("HelpAssistant4", "Close"))
        self.label.setText(_translate("HelpAssistant4", "\'Stark\' can operate offline, but requires internet access for some services. These are listed below - "))
        self.label_3.setText(_translate("HelpAssistant4", "i. To use Voice Command feature.\n"
"ii. To query Google for any information.\n"
"iii. To play a song on YouTube.\n"
"iv. To access the Web for the completion of a command."))
        self.label_31.setText(_translate("HelpAssistant4", "If there is a need for assistant to access the Web, and internet is not connected, it will inform that it requires internet connection to perform that task."))
        self.GoBackButton.setText(_translate("HelpAssistant4", "< Go back"))
        self.StarkTitle.setText(_translate("HelpAssistant4", "Stark"))
        self.PageTitle_2.setText(_translate("HelpAssistant4", "The Personal Assistant"))
        self.Help1Button.setText(_translate("HelpAssistant4", "How to use \'Stark\'?"))
        self.label_2.setText(_translate("HelpAssistant4", "Also have a look on "))

    def close_button(self, x):
        x.close()

    def help_menu_button(self, x):
        self.helpMenuUi = Ui_HelpAssistant()
        self.helpMenuWindow = QtWidgets.QMainWindow()
        self.helpMenuUi.setupUi(self.helpMenuWindow)
        x.close()
        self.helpMenuWindow.show()

    def help1_button(self, x):
    	self.help1_ui = Ui_HelpAssistant1()
    	self.help1_window = QtWidgets.QMainWindow()
    	self.help1_ui.setupUi(self.help1_window)
    	x.close()
    	self.help1_window.show()


class Ui_HelpAssistant5(object):
    def setupUi(self, HelpAssistant5):
        HelpAssistant5.setObjectName("HelpAssistant5")
        HelpAssistant5.setFixedSize(621, 616)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpAssistant5.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpAssistant5)
        self.centralwidget.setObjectName("centralwidget")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(515, 541, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.CloseButton.setFlat(False)
        self.CloseButton.setObjectName("CloseButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(11, 101, 600, 391))
        self.scrollArea.setMaximumSize(QtCore.QSize(600, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color:white;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -1336, 579, 1763))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setMaximumSize(QtCore.QSize(550, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setMaximumSize(QtCore.QSize(250, 50))
        self.label_30.setFrameShape(QtWidgets.QFrame.Box)
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("resources/images/mic-listen.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_2.addWidget(self.label_30)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setMaximumSize(QtCore.QSize(250, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("resources/images/keyboard-input.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_31.setFont(font)
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_2.addWidget(self.label_31)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setMaximumSize(QtCore.QSize(250, 100))
        self.label_32.setStyleSheet("")
        self.label_32.setFrameShape(QtWidgets.QFrame.Box)
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("resources/images/media-player.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_4.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setMaximumSize(QtCore.QSize(250, 100))
        self.label_33.setFrameShape(QtWidgets.QFrame.Box)
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("resources/images/word.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_4.addWidget(self.label_33)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_17 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_2.addWidget(self.line_17)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setMaximumSize(QtCore.QSize(570, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_34.setFont(font)
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_2.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setMaximumSize(QtCore.QSize(200, 130))
        self.label_35.setFrameShape(QtWidgets.QFrame.Box)
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("resources/images/buttons.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_2.addWidget(self.label_35)
        self.line_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_2.addWidget(self.line_18)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_36.setFont(font)
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_2.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setMaximumSize(QtCore.QSize(550, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_37.setFont(font)
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_2.addWidget(self.label_37)
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_50.setMaximumSize(QtCore.QSize(400, 80))
        self.label_50.setFrameShape(QtWidgets.QFrame.Box)
        self.label_50.setText("")
        self.label_50.setPixmap(QtGui.QPixmap("resources/images/mic-listen.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_2.addWidget(self.label_50)
        self.line_19 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_2.addWidget(self.line_19)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_38.setFont(font)
        self.label_38.setTextFormat(QtCore.Qt.AutoText)
        self.label_38.setScaledContents(True)
        self.label_38.setWordWrap(True)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_2.addWidget(self.label_38)
        self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_51.setMaximumSize(QtCore.QSize(195, 120))
        self.label_51.setFrameShape(QtWidgets.QFrame.Box)
        self.label_51.setText("")
        self.label_51.setPixmap(QtGui.QPixmap("resources/images/settings-menu3.png"))
        self.label_51.setScaledContents(True)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_2.addWidget(self.label_51)
        self.line_20 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.verticalLayout_2.addWidget(self.line_20)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_40.setFont(font)
        self.label_40.setTextFormat(QtCore.Qt.AutoText)
        self.label_40.setScaledContents(True)
        self.label_40.setWordWrap(True)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_2.addWidget(self.label_40)
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_52.setFont(font)
        self.label_52.setTextFormat(QtCore.Qt.AutoText)
        self.label_52.setScaledContents(True)
        self.label_52.setWordWrap(True)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_2.addWidget(self.label_52)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setMaximumSize(QtCore.QSize(310, 120))
        self.label_41.setFrameShape(QtWidgets.QFrame.Box)
        self.label_41.setText("")
        self.label_41.setPixmap(QtGui.QPixmap("resources/images/music-play.png"))
        self.label_41.setScaledContents(True)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_2.addWidget(self.label_41)
        self.line_21 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.verticalLayout_2.addWidget(self.line_21)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_42.setFont(font)
        self.label_42.setTextFormat(QtCore.Qt.AutoText)
        self.label_42.setScaledContents(True)
        self.label_42.setWordWrap(True)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_2.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_43.setMaximumSize(QtCore.QSize(383, 120))
        self.label_43.setFrameShape(QtWidgets.QFrame.Box)
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("resources/images/voice-settings.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_2.addWidget(self.label_43)
        self.line_22 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_2.addWidget(self.line_22)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_44.setFont(font)
        self.label_44.setTextFormat(QtCore.Qt.AutoText)
        self.label_44.setScaledContents(True)
        self.label_44.setWordWrap(True)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_2.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_45.setMaximumSize(QtCore.QSize(250, 120))
        self.label_45.setFrameShape(QtWidgets.QFrame.Box)
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("resources/images/volume.png"))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_2.addWidget(self.label_45)
        self.line_23 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.verticalLayout_2.addWidget(self.line_23)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setMaximumSize(QtCore.QSize(550, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_46.setFont(font)
        self.label_46.setTextFormat(QtCore.Qt.AutoText)
        self.label_46.setScaledContents(True)
        self.label_46.setWordWrap(True)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_2.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_47.setMaximumSize(QtCore.QSize(180, 120))
        self.label_47.setFrameShape(QtWidgets.QFrame.Box)
        self.label_47.setText("")
        self.label_47.setPixmap(QtGui.QPixmap("resources/images/settings-menu5.png"))
        self.label_47.setScaledContents(True)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_2.addWidget(self.label_47)
        self.line_24 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.verticalLayout_2.addWidget(self.line_24)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.GoBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackButton.setGeometry(QtCore.QRect(27, 541, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.GoBackButton.setFont(font)
        self.GoBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GoBackButton.setStyleSheet("background-color:#0162ff; color:white; border-radius:7px; border:none;")
        self.GoBackButton.setFlat(False)
        self.GoBackButton.setObjectName("GoBackButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(213, 8, 301, 73))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setSpacing(0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StarkTitle.sizePolicy().hasHeightForWidth())
        self.StarkTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setOpenExternalLinks(False)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle_2.sizePolicy().hasHeightForWidth())
        self.PageTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setOpenExternalLinks(False)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(124, 1, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.Help1Button = QtWidgets.QPushButton(self.centralwidget)
        self.Help1Button.setGeometry(QtCore.QRect(276, 498, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.Help1Button.setFont(font)
        self.Help1Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help1Button.setStyleSheet("border:none; text-decoration:underline; color:blue; text-align:left;")
        self.Help1Button.setObjectName("Help1Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 500, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        HelpAssistant5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpAssistant5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
        self.menubar.setObjectName("menubar")
        HelpAssistant5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpAssistant5)
        self.statusbar.setObjectName("statusbar")
        HelpAssistant5.setStatusBar(self.statusbar)

        self.CloseButton.clicked.connect(lambda: self.close_button(HelpAssistant5))
        self.GoBackButton.clicked.connect(lambda: self.help_menu_button(HelpAssistant5))
        self.Help1Button.clicked.connect(lambda: self.help1_button(HelpAssistant5))

        self.retranslateUi(HelpAssistant5)
        QtCore.QMetaObject.connectSlotsByName(HelpAssistant5)

    def retranslateUi(self, HelpAssistant5):
        _translate = QtCore.QCoreApplication.translate
        HelpAssistant5.setWindowTitle(_translate("HelpAssistant5", "\'Stark\' - Settings and Customization"))
        self.CloseButton.setText(_translate("HelpAssistant5", "Close"))
        self.label.setText(_translate("HelpAssistant5", "1. \'Stark\' comes with a lot of features, which you can even customize to have a better experience."))
        self.label_3.setText(_translate("HelpAssistant5", "2. You can switch between Voice input and Keyboard input, so that you can use it in any circumstances."))
        self.label_31.setText(_translate("HelpAssistant5", "3. In the feedback of your commands, it gives you a Voice Output along with a feedback text and a visual representation of the feedback. You can change the Voice Feedback setting in the \'Sound Settings\' menu, under the \'Assistant Feedback\'.\n"
"By default, it is set to \'On\'.\n"
"Have a look on \'How to use \'Stark\'?\' to know more."))
        self.label_34.setText(_translate("HelpAssistant5", "4. There are 3 response buttons, which gives a Sound feedback when clicked.\n"
"You can turn on/off this sound feedback in \'Sound settings\' under \'Button Click Feedback\'\n"
"By default, this is set to \'On\'.\n"
"Have a look on \'How to use \'Stark\'?\' to know more."))
        self.label_36.setText(_translate("HelpAssistant5", "5. When you are using Voice command mode, there is a dedicated indication feedback, to help you know, when the assistant is ready to get dictated and when the dictation is complete. You can turn this sound feedback on/off in \'Sound Settings\' under \'Start/Stop Indication\'\n"
"By default, it is set to \'On\'.\n"
"Note- This feedback works only in the \'Voice\' command mode.\n"
"Have a look on \'How to use \'Stark\'?\' to know more.\n"
""))
        self.label_37.setText(_translate("HelpAssistant5", "As soon as there is a sound feedback, you can start dictating your commands. When the dictation gets over, there is another sound feedback, which indicates that the dictation is over and \'Stark\' is processing your commands."))
        self.label_38.setText(_translate("HelpAssistant5", "6. \'Stark\' stores some of your personal details like your name, age, email, gender and nickname to assist you in a better way.\n"
"You are asked to enter these details during the setup of \'Stark\' but you can always change these at a later stage in \'Settings\' under \'Personal\'."))
        self.label_40.setText(_translate("HelpAssistant5", "7. \'Stark\' can also play music for you! During the setup of \'Stark\', it will ask you to mention the default music folder, which contains some of your favourite music. When you give it command to play a certain music, it wil search for the music in that folder. If it finds that music, it plays it. If its unable to find the music, it will play that music on YouTube, if internet is connected.\n"
"\n"
"If no music is mentioned, it plays any random music from your music folder."))
        self.label_52.setText(_translate("HelpAssistant5", "You can change the music folder any time you want, under \'Settings\'>\'Folders and Paths\'>\'Music Folder\'."))
        self.label_42.setText(_translate("HelpAssistant5", "8. \'Stark\' comes with two Voices! By default, it speaks in a Male accent. You can change it to \'Female\' at any point of time under \'Settings\'>Assistant Settings\'>\'Voice\'\nNote: On some devices, this setting may not work as expected."))
        self.label_44.setText(_translate("HelpAssistant5", "9. You can even control the volume of your computer from within \'Stark\' under \'Settings\'>\'Assistant Settings\'>\'Volume\'."))
        self.label_46.setText(_translate("HelpAssistant5", "10. Want to reset all the settings you did? \'Revert to defaults\' will do it for you."))
        self.GoBackButton.setText(_translate("HelpAssistant5", "< Go back"))
        self.StarkTitle.setText(_translate("HelpAssistant5", "Stark"))
        self.PageTitle_2.setText(_translate("HelpAssistant5", "The Personal Assistant"))
        self.Help1Button.setText(_translate("HelpAssistant5", "How to use \'Stark\'?"))
        self.label_2.setText(_translate("HelpAssistant5", "Also have a look on "))

    def close_button(self, x):
        x.close()

    def help_menu_button(self, x):
        self.helpMenuUi = Ui_HelpAssistant()
        self.helpMenuWindow = QtWidgets.QMainWindow()
        self.helpMenuUi.setupUi(self.helpMenuWindow)
        x.close()
        self.helpMenuWindow.show()

    def help1_button(self, x):
    	self.help1_ui = Ui_HelpAssistant1()
    	self.help1_window = QtWidgets.QMainWindow()
    	self.help1_ui.setupUi(self.help1_window)
    	x.close()
    	self.help1_window.show()


class Ui_StarkWindow(object):
    helpui=0
    helpwindow=0
    def setupUi(self, StarkWindow):
        StarkWindow.setObjectName("StarkWindow")
        StarkWindow.setFixedSize(780, 585)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StarkWindow.setWindowIcon(icon)

        StarkWindow.setWindowOpacity(1.0)
        StarkWindow.setIconSize(QtCore.QSize(40, 40))
        StarkWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        StarkWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(StarkWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.PageTitle = QtWidgets.QLabel(self.centralwidget)
        self.PageTitle.setGeometry(QtCore.QRect(320, 17, 231, 91))

        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(70)
        font.setWeight(50)
        self.PageTitle.setFont(font)

        self.PageTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle.setObjectName("PageTitle")

        # keyboard button
        self.KeyboardButton = QtWidgets.QPushButton(self.centralwidget)
        self.KeyboardButton.setGeometry(QtCore.QRect(651, 458, 61, 41))
        self.KeyboardButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.KeyboardButton.setStyleSheet("border: none;")
        self.KeyboardButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icons/keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KeyboardButton.setIcon(icon1)
        self.KeyboardButton.setIconSize(QtCore.QSize(50, 50))
        self.KeyboardButton.setFlat(True)
        self.KeyboardButton.setObjectName("KeyboardButton")

        # microphone button
        self.MicrophoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.MicrophoneButton.setGeometry(QtCore.QRect(80, 458, 61, 41))
        self.MicrophoneButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MicrophoneButton.setAutoFillBackground(False)
        self.MicrophoneButton.setStyleSheet("border: none;")
        self.MicrophoneButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/microphone-windows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrophoneButton.setIcon(icon2)
        self.MicrophoneButton.setIconSize(QtCore.QSize(50, 50))
        self.MicrophoneButton.setFlat(True)
        self.MicrophoneButton.setObjectName("MicrophoneButton")

        # command input box
        self.CommandInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CommandInput.setGeometry(QtCore.QRect(150, 455, 440, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.CommandInput.setFont(font)
        self.CommandInput.setObjectName("CommandInput")

        # send commmand button
        self.CommandSendButton = QtWidgets.QPushButton(self.centralwidget)
        self.CommandSendButton.setGeometry(QtCore.QRect(601, 465, 31, 31))
        self.CommandSendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CommandSendButton.setStyleSheet("border: none;")
        self.CommandSendButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CommandSendButton.setIcon(icon3)
        self.CommandSendButton.setIconSize(QtCore.QSize(25, 25))
        self.CommandSendButton.setFlat(True)
        self.CommandSendButton.setObjectName("CommandSendButton")

        # label to display the result
        self.OutputDisplay = QtWidgets.QLabel(self.centralwidget)
        self.OutputDisplay.setGeometry(QtCore.QRect(10, 125, 761, 151))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(30)
        self.OutputDisplay.setFont(font)
        self.OutputDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputDisplay.setWordWrap(True)
        self.OutputDisplay.setIndent(-1)
        self.OutputDisplay.setObjectName("OutputDisplay")

        # assistant status display
        self.CommandStatusDisplay = QtWidgets.QLabel(self.centralwidget)
        self.CommandStatusDisplay.setGeometry(QtCore.QRect(10, 382, 761, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(20)
        self.CommandStatusDisplay.setFont(font)
        self.CommandStatusDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.CommandStatusDisplay.setObjectName("CommandStatusDisplay")

        # microphone input mode active label
        self.DictationModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.DictationModeLabel.setGeometry(QtCore.QRect(150, 455, 490, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.DictationModeLabel.setFont(font)
        self.DictationModeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DictationModeLabel.setObjectName("DictationModeLabel")

        # icon display for result
        self.OutputIconDisplay = QtWidgets.QLabel(self.centralwidget)
        self.OutputIconDisplay.setGeometry(QtCore.QRect(335, 276, 100, 100))
        self.OutputIconDisplay.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OutputIconDisplay.setText("")
        self.OutputIconDisplay.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.OutputIconDisplay.setScaledContents(True)
        self.OutputIconDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputIconDisplay.setObjectName("OutputIconDisplay")

        self.StarkIconDisplay = QtWidgets.QLabel(self.centralwidget)
        self.StarkIconDisplay.setGeometry(QtCore.QRect(240, 10, 91, 91))
        self.StarkIconDisplay.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StarkIconDisplay.setText("")
        self.StarkIconDisplay.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIconDisplay.setScaledContents(True)
        self.StarkIconDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkIconDisplay.setObjectName("StarkIconDisplay")
        StarkWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(StarkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")

        #################### Settings Menu bar ##############################
        self.SettingsMenu = QtWidgets.QMenu(self.menubar)
        self.SettingsMenu.setObjectName("SettingsMenu")

        ####### sound settings #######
        self.SoundSettingsMenu = QtWidgets.QMenu(self.SettingsMenu)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/icons/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SoundSettingsMenu.setIcon(icon4)
        self.SoundSettingsMenu.setObjectName("SoundSettingsMenu")

        # assistant feedback sound settings
        self.AssistantFeedbackSoundSetting = QtWidgets.QMenu(self.SoundSettingsMenu)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/icons/assistant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AssistantFeedbackSoundSetting.setIcon(icon5)
        self.AssistantFeedbackSoundSetting.setObjectName("AssistantFeedbackSoundSetting")

        self.AssistantFeedbackSoundSettingOn = QtWidgets.QAction(StarkWindow)
        self.AssistantFeedbackSoundSettingOn.setObjectName("AssistantFeedbackSoundSettingOn")
        self.AssistantFeedbackSoundSetting.addAction(self.AssistantFeedbackSoundSettingOn)

        self.AssistantFeedbackSoundSettingOff = QtWidgets.QAction(StarkWindow)
        self.AssistantFeedbackSoundSettingOff.setObjectName("AssistantFeedbackSoundSettingOff")
        self.AssistantFeedbackSoundSetting.addAction(self.AssistantFeedbackSoundSettingOff)

        self.SoundSettingsMenu.addAction(self.AssistantFeedbackSoundSetting.menuAction())

        # button click sound settings
        self.ButtonClickSoundSetting = QtWidgets.QMenu(self.SoundSettingsMenu)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icons/click.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonClickSoundSetting.setIcon(icon6)
        self.ButtonClickSoundSetting.setObjectName("ButtonClickSoundSetting")

        self.ButtonClickSoundSettingOn = QtWidgets.QAction(StarkWindow)
        self.ButtonClickSoundSettingOn.setObjectName("ButtonClickSoundSettingOn")
        self.ButtonClickSoundSetting.addAction(self.ButtonClickSoundSettingOn)

        self.ButtonClickSoundSettingOff = QtWidgets.QAction(StarkWindow)
        self.ButtonClickSoundSettingOff.setObjectName("ButtonClickSoundSettingOff")
        self.ButtonClickSoundSetting.addAction(self.ButtonClickSoundSettingOff)

        self.SoundSettingsMenu.addAction(self.ButtonClickSoundSetting.menuAction())

        # start/stop sound settings
        self.StartStopSoundSetting = QtWidgets.QMenu(self.SoundSettingsMenu)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/icons/start-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartStopSoundSetting.setIcon(icon7)
        self.StartStopSoundSetting.setObjectName("StartStopSoundSetting")

        self.StartStopSoundSettingOn = QtWidgets.QAction(StarkWindow)
        self.StartStopSoundSettingOn.setObjectName("StartStopSoundSettingOn")
        self.StartStopSoundSetting.addAction(self.StartStopSoundSettingOn)

        self.StartStopSoundSettingOff = QtWidgets.QAction(StarkWindow)
        self.StartStopSoundSettingOff.setObjectName("StartStopSoundSettingOff")
        self.StartStopSoundSetting.addAction(self.StartStopSoundSettingOff)

        self.SoundSettingsMenu.addAction(self.StartStopSoundSetting.menuAction())

        self.SettingsMenu.addAction(self.SoundSettingsMenu.menuAction())

        ###### folder and path settings ######
        self.FolderSettingsMenu = QtWidgets.QMenu(self.SettingsMenu)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FolderSettingsMenu.setIcon(icon9)
        self.FolderSettingsMenu.setObjectName("FolderSettingsMenu")

        # music folder
        self.MusicFolderSettings = QtWidgets.QAction(StarkWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("resources/icons/music-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MusicFolderSettings.setIcon(icon13)
        self.MusicFolderSettings.setObjectName("MusicFolderSettings")
        self.FolderSettingsMenu.addAction(self.MusicFolderSettings)

        self.SettingsMenu.addAction(self.FolderSettingsMenu.menuAction())

        ######## personal settings #########
        self.PersonalSettingsMenu = QtWidgets.QAction(self.SettingsMenu)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/icons/personal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PersonalSettingsMenu.setIcon(icon8)
        self.PersonalSettingsMenu.setObjectName("PersonalSettingsMenu")

        self.SettingsMenu.addAction(self.PersonalSettingsMenu)

        ############## assistant settings ###########
        self.AssistantSettingsMenu = QtWidgets.QMenu(self.SettingsMenu)
        self.AssistantSettingsMenu.setIcon(icon5)
        self.AssistantSettingsMenu.setObjectName("AssistantSettingsMenu")

        # assistant voice type
        self.VoiceSettings = QtWidgets.QMenu(self.AssistantSettingsMenu)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/icons/voice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VoiceSettings.setIcon(icon10)
        self.VoiceSettings.setObjectName("VoiceSettings")

        self.MaleVoiceSettings = QtWidgets.QAction(StarkWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("resources/icons/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MaleVoiceSettings.setIcon(icon19)
        self.MaleVoiceSettings.setObjectName("MaleVoiceSettings")
        self.VoiceSettings.addAction(self.MaleVoiceSettings)

        self.FemaleVoiceSettings = QtWidgets.QAction(StarkWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("resources/icons/female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FemaleVoiceSettings.setIcon(icon20)
        self.FemaleVoiceSettings.setObjectName("FemaleVoiceSettings")
        self.VoiceSettings.addAction(self.FemaleVoiceSettings)

        self.AssistantSettingsMenu.addAction(self.VoiceSettings.menuAction())

        # volume settings
        self.VolumeSettings = QtWidgets.QAction(StarkWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("resources/icons/audio-signal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeSettings.setIcon(icon18)
        self.VolumeSettings.setObjectName("VolumeSettings")
        self.AssistantSettingsMenu.addAction(self.VolumeSettings)

        self.SettingsMenu.addAction(self.AssistantSettingsMenu.menuAction())

        ############## revert to defaults ##############
        self.RevertToDefaultsSettings = QtWidgets.QAction(StarkWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("resources/icons/revert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RevertToDefaultsSettings.setIcon(icon17)
        self.RevertToDefaultsSettings.setObjectName("RevertToDefaultsSettings")

        self.SettingsMenu.addAction(self.RevertToDefaultsSettings)

        ################################ Help Menu #########################################
        self.HelpMenu = QtWidgets.QMenu(self.menubar)
        self.HelpMenu.setObjectName("HelpMenu")

        ##### assistant help ######
        self.AssistantHelp = QtWidgets.QAction(StarkWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AssistantHelp.setIcon(icon11)
        self.AssistantHelp.setObjectName("AssistantHelp")

        self.HelpMenu.addAction(self.AssistantHelp)

        ##### about help #####
        self.AboutHelp = QtWidgets.QAction(StarkWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutHelp.setIcon(icon12)
        self.AboutHelp.setObjectName("AboutHelp")

        self.HelpMenu.addAction(self.AboutHelp)

        ############################## File Menu #################################
        self.FileMenu = QtWidgets.QMenu(self.menubar)
        self.FileMenu.setObjectName("FileMenu")
        StarkWindow.setMenuBar(self.menubar)

        ##### exit assistant #####
        self.MenuExit = QtWidgets.QAction(StarkWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("resources/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuExit.setIcon(icon14)
        self.MenuExit.setObjectName("MenuExit")

        self.FileMenu.addAction(self.MenuExit)

        ####### restart assistant ######
        self.MenuRestart = QtWidgets.QAction(StarkWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("resources/icons/restart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuRestart.setIcon(icon15)
        self.MenuRestart.setObjectName("MenuRestart")

        self.FileMenu.addAction(self.MenuRestart)

        ####### re-configure assistant ######
        self.MenuRe_Configure = QtWidgets.QAction(StarkWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("resources/icons/reconfig.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuRe_Configure.setIcon(icon16)
        self.MenuRe_Configure.setObjectName("MenuRe_Configure")

        self.FileMenu.addAction(self.MenuRe_Configure)

        self.menubar.addAction(self.FileMenu.menuAction())
        self.menubar.addAction(self.SettingsMenu.menuAction())
        self.menubar.addAction(self.HelpMenu.menuAction())

        self.statusbar = QtWidgets.QStatusBar(StarkWindow)
        self.statusbar.setObjectName("statusbar")
        StarkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StarkWindow)
        QtCore.QMetaObject.connectSlotsByName(StarkWindow)
        StarkWindow.setTabOrder(self.MicrophoneButton, self.KeyboardButton)
        StarkWindow.setTabOrder(self.KeyboardButton, self.CommandInput)
        StarkWindow.setTabOrder(self.CommandInput, self.CommandSendButton)

        ##### function connections #####

        self.MenuExit.triggered.connect(self.exit_assistant)
        self.MenuRestart.triggered.connect(self.restart_assistant)
        self.MenuRe_Configure.triggered.connect(lambda: self.re_config_assistant(StarkWindow))

        self.AssistantFeedbackSoundSettingOn.triggered.connect(self.assistant_feedback_sound_on)
        self.AssistantFeedbackSoundSettingOff.triggered.connect(self.assistant_feedback_sound_off)
        self.ButtonClickSoundSettingOn.triggered.connect(self.button_click_sound_on)
        self.ButtonClickSoundSettingOff.triggered.connect(self.button_click_sound_off)
        self.StartStopSoundSettingOn.triggered.connect(self.start_stop_sound_on)
        self.StartStopSoundSettingOff.triggered.connect(self.start_stop_sound_off)

        self.MusicFolderSettings.triggered.connect(lambda: self.music_folder_selector(StarkWindow))

        self.PersonalSettingsMenu.triggered.connect(lambda: self.re_config_assistant(StarkWindow))

        self.MaleVoiceSettings.triggered.connect(self.voice_type_male)
        self.FemaleVoiceSettings.triggered.connect(self.voice_type_female)
        self.VolumeSettings.triggered.connect(self.volume_settings)
        self.RevertToDefaultsSettings.triggered.connect(self.revert_default_settings)

        self.AssistantHelp.triggered.connect(self.assistant_help)
        self.AboutHelp.triggered.connect(self.about_help)

        self.MicrophoneButton.clicked.connect(self.microphone_button)
        self.KeyboardButton.clicked.connect(self.keyboard_button)
        self.CommandSendButton.clicked.connect(self.command_send_button)

        self.show_microphone() if self.check_internet_connection() else self.show_keyboard()

        self.CommandInput.selectionChanged.connect(lambda: self.CommandStatusDisplay.setText('Type your Commands here'))
        self.CommandInput.textEdited.connect(lambda: self.CommandStatusDisplay.setText('Type your Commands here'))

        try:
            self.assistant_feedback_sound_on() if Assistant_details.assistant_feedback_status == 1 else self.assistant_feedback_sound_off()
            self.button_click_sound_on() if Assistant_details.click_sound_status == 1 else self.button_click_sound_off()
            self.start_stop_sound_on() if Assistant_details.start_stop_sound_status == 1 else self.start_stop_sound_off()
            self.voice_type_male() if Assistant_details.voice_type == 'Male' else self.voice_type_female()
        except Exception as e:
            self.assistant_feedback_sound_on()
            self.button_click_sound_on()
            self.start_stop_sound_on()
            self.voice_type_male()

    Assistant_details()

    def retranslateUi(self, StarkWindow):
        _translate = QtCore.QCoreApplication.translate
        StarkWindow.setWindowTitle(_translate("StarkWindow", "\'Stark\' - The Personal Assistant"))
        self.PageTitle.setText(_translate("StarkWindow", "Stark"))
        self.CommandInput.setPlaceholderText(_translate("StarkWindow", "Type your Commands here"))
        self.CommandSendButton.setShortcut(_translate("StarkWindow", "Return"))
        self.OutputDisplay.setText(_translate("StarkWindow", ""))
        self.CommandStatusDisplay.setText(_translate("StarkWindow", ""))
        self.DictationModeLabel.setText(_translate("StarkWindow", "Tap on the Mic icon"))
        self.SettingsMenu.setTitle(_translate("StarkWindow", "Settings"))
        self.SoundSettingsMenu.setTitle(_translate("StarkWindow", "Sound"))
        self.AssistantFeedbackSoundSetting.setTitle(_translate("StarkWindow", "Assistant Feedback"))
        self.ButtonClickSoundSetting.setTitle(_translate("StarkWindow", "Button Click Feedback"))
        self.StartStopSoundSetting.setTitle(_translate("StarkWindow", "Start/Stop Indication"))
        self.PersonalSettingsMenu.setText(_translate("StarkWindow", "Personal"))
        self.FolderSettingsMenu.setTitle(_translate("StarkWindow", "Folders and Paths"))
        self.AssistantSettingsMenu.setTitle(_translate("StarkWindow", "Assistant Settings"))
        self.VoiceSettings.setTitle(_translate("StarkWindow", "Voice"))
        self.HelpMenu.setTitle(_translate("StarkWindow", "Help"))
        self.FileMenu.setTitle(_translate("StarkWindow", "File"))
        self.AssistantHelp.setText(_translate("StarkWindow", "Assistant Help"))
        self.AssistantHelp.setShortcut(_translate("StarkWindow", "Ctrl+H"))
        self.AboutHelp.setText(_translate("StarkWindow", "About"))
        self.MusicFolderSettings.setText(_translate("StarkWindow", "Music Folder"))
        self.MenuExit.setText(_translate("StarkWindow", "Exit"))
        self.MenuRestart.setText(_translate("StarkWindow", "Restart"))
        self.MenuRe_Configure.setText(_translate("StarkWindow", "Re-configure"))
        self.RevertToDefaultsSettings.setText(_translate("StarkWindow", "Revert to defaults"))
        self.AssistantFeedbackSoundSettingOn.setText(_translate("StarkWindow", "On"))
        self.AssistantFeedbackSoundSettingOff.setText(_translate("StarkWindow", "Off"))
        self.ButtonClickSoundSettingOn.setText(_translate("StarkWindow", "On"))
        self.ButtonClickSoundSettingOff.setText(_translate("StarkWindow", "Off"))
        self.StartStopSoundSettingOn.setText(_translate("StarkWindow", "On"))
        self.StartStopSoundSettingOff.setText(_translate("StarkWindow", "Off"))
        self.VolumeSettings.setText(_translate("StarkWindow", "Volume"))
        self.MaleVoiceSettings.setText(_translate("StarkWindow", "Male"))
        self.FemaleVoiceSettings.setText(_translate("StarkWindow", "Female"))
        self.MenuExit.setShortcut(_translate("StarkWindow", "Alt+F4"))
        self.MicrophoneButton.setShortcut(_translate("StarkWindow", "Alt+M"))
        self.KeyboardButton.setShortcut(_translate("StarkWindow", "Alt+K"))
        self.KeyboardButton.setToolTip(_translate("StarkWindow", "Press 'Alt+K' to enter Keyboard mode"))
        self.MicrophoneButton.setToolTip(_translate("StarkWindow", "Press 'Alt+M' to enter Voice mode"))

    def icon_output(self, string):
        try:
            self.OutputIconDisplay.setPixmap(QtGui.QPixmap("resources/application/{}.png".format(string)))
        except:
            self.OutputIconDisplay.setPixmap(QtGui.QPixmap("resources/application/stark-logo.png"))

    ########## voice input ###############
    def voice_input(self, ask=False):
        """Takes the input from user in the form of voice"""
        try:
            r = sr.Recognizer()
            if ask:
                AssistantSpeakAndListen.speak(ask)
            with sr.Microphone() as source:
                self.CommandStatusDisplay.setText('Wait Preparing...')
                QtCore.QCoreApplication.processEvents()
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                try:
                    if Assistant_details.start_stop_sound_status:
                        playsound('resources\\audio\\on.mp3')
                except Exception as e: pass
                self.CommandStatusDisplay.setText('Listening...')
                QtCore.QCoreApplication.processEvents()
                audio = r.listen(source)
                voice_data = ''
                try:
                    voice_data = r.recognize_google(audio, language="en-in")
                except sr.UnknownValueError:
                    try:
                        if Assistant_details.start_stop_sound_status:
                            playsound('resources\\audio\\off.mp3')
                    except Exception as e:
                        pass
                    return 'Sorry, I didn\'t get that', False
                except sr.RequestError:
                    try:
                        if Assistant_details.start_stop_sound_status:
                            playsound('resources\\audio\\off.mp3')
                    except Exception as e:
                        pass
                    return 'Sorry, my speech service is down', False
                except Exception as e:
                    try:
                        if Assistant_details.start_stop_sound_status:
                            playsound('resources\\audio\\off.mp3')
                    except Exception as e:
                        pass
                    return "Something went wrong"
            try:
                if Assistant_details.start_stop_sound_status:
                    playsound('resources\\audio\\off.mp3')
            except Exception as e: pass
            return voice_data, True
        except OSError as e:
            try:
                if Assistant_details.start_stop_sound_status:
                    playsound('resources\\audio\\off.mp3')
            except Exception as e:
                pass
            return str(e), False
        except Exception as e:
            try:
                if Assistant_details.start_stop_sound_status:
                    playsound('resources\\audio\\off.mp3')
            except Exception as e:
                pass
            print("Error:", e)
            return 'Problem setting up the Voice feature', False

    ############ file menu ##############
    def exit_assistant(self):
        self.quit_assistant()

    def restart_assistant(self):
        try:
            python = sys.executable
            os.execl(python, python, *sys.argv)
        except Exception as e:
            pass

    def re_config_assistant(self, x):
        self.revert_default_settings()
        self.configui = Ui_ConfigureWindow()
        self.configwindow = QtWidgets.QMainWindow()
        self.configui.setupUi(self.configwindow)
        x.close()
        self.configwindow.show()

    ############# help menu #################
    def assistant_help(self):
        Ui_StarkWindow.helpui = Ui_HelpAssistant()
        Ui_StarkWindow.helpwindow = QtWidgets.QMainWindow()
        Ui_StarkWindow.helpui.setupUi(Ui_StarkWindow.helpwindow)
        Ui_StarkWindow.helpwindow.show()

    def about_help(self):
        self.aboutui = Ui_AboutAssistant()
        self.aboutwindow = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.aboutui.setupUi((self.aboutwindow))
        self.aboutwindow.exec_()

    ############# settings menu ############
    def revert_default_settings(self):
        try:
            self.assistant_feedback_sound_on()
            self.button_click_sound_on()
            self.start_stop_sound_on()
            self.voice_type_male()
        except Exception as e:
            pass

    ## assistant feedback sound ##
    def assistant_feedback_sound_on(self):
        try:
            Assistant_details.assistant_feedback_status = True
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('assistant_feedback_status', 'True')
            self.AssistantFeedbackSoundSettingOff.setVisible(True)
            self.AssistantFeedbackSoundSettingOn.setVisible(False)
        except Exception as e:
            pass

    def assistant_feedback_sound_off(self):
        try:
            Assistant_details.assistant_feedback_status = False
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('assistant_feedback_status', 'False')
            self.AssistantFeedbackSoundSettingOff.setVisible(False)
            self.AssistantFeedbackSoundSettingOn.setVisible(True)
        except Exception as e:
            pass

    ## click sound ##
    def button_click_sound_on(self):
        try:
            Assistant_details.click_sound_status = True
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('click_sound_status', 'True')
            self.ButtonClickSoundSettingOff.setVisible(True)
            self.ButtonClickSoundSettingOn.setVisible(False)
        except Exception as e:
            pass

    def button_click_sound_off(self):
        try:
            Assistant_details.click_sound_status = False
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('click_sound_status', 'False')
            self.ButtonClickSoundSettingOff.setVisible(False)
            self.ButtonClickSoundSettingOn.setVisible(True)
        except Exception as e:
            pass

    ## start/stop sound ##
    def start_stop_sound_on(self):
        try:
            Assistant_details.start_stop_sound_status = True
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('start_stop_sound_status', 'True')
            self.StartStopSoundSettingOff.setVisible(True)
            self.StartStopSoundSettingOn.setVisible(False)
        except Exception as e:
            pass

    def start_stop_sound_off(self):
        try:
            Assistant_details.start_stop_sound_status = False
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('start_stop_sound_status', 'False')
            self.StartStopSoundSettingOff.setVisible(False)
            self.StartStopSoundSettingOn.setVisible(True)
        except Exception as e:
            pass

    ############# music folder ##########
    def music_folder_selector(self, x):
        self.musicui = Ui_MusicDialogSelector()
        self.musicwindow = QtWidgets.QMainWindow()
        self.musicui.setupUi(self.musicwindow)
        x.close()
        self.musicwindow.show()

    ############ assistant settings ########

    def voice_type_male(self):
        try:
            Assistant_details.voice_type = 'Male'
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('voice_type', 'Male')
            self.FemaleVoiceSettings.setVisible(True)
            self.MaleVoiceSettings.setVisible(False)
            AssistantSpeakAndListen.voice_change()
        except Exception as e:
            pass

    def voice_type_female(self):
        try:
            Assistant_details.voice_type = 'Female'
            self.settings = QSettings('PyQt5Application', 'Stark')
            self.settings.setValue('voice_type', 'Female')
            self.FemaleVoiceSettings.setVisible(False)
            self.MaleVoiceSettings.setVisible(True)
            AssistantSpeakAndListen.voice_change()
        except Exception as e:
            pass

    def volume_settings(self):
        try:
            self.volumeui = Ui_VolumeSelector()
            self.volumewindow = QtWidgets.QMainWindow()
            self.volumeui.setupUi(self.volumewindow)
            self.volumewindow.show()
        except Exception as e:
            pass

    ####### button functions #########
    def microphone_button(self):
        try:
            if Assistant_details.click_sound_status:
                playsound(Assistant_details.click_sound)
        except:
            pass

        if self.check_internet_connection():
            self.show_microphone()
            self.OutputDisplay.setText("")
            self.DictationModeLabel.setText("Voice mode")
            QtCore.QCoreApplication.processEvents()
            try:
                command, status = self.voice_input()
                if status:
                    self.CommandInput.setText(command)
                    QtCore.QCoreApplication.processEvents()
                    self.command_send_button()
                else:
                    self.OutputDisplay.setText('Error: ' + command)
                self.CommandStatusDisplay.setText('Ready...')
                self.DictationModeLabel.setText("Tap on the Mic icon")
                QtCore.QCoreApplication.processEvents()

            except Exception as e:
                pass

        else:
            self.CommandStatusDisplay.setText('Check your internet connection')
            self.icon_output('internet_error')

    def keyboard_button(self):
        try:
            if Assistant_details.click_sound_status:
                playsound(Assistant_details.click_sound)
        except:
            pass
        self.show_keyboard()

    def command_send_button(self):
        command = self.CommandInput.text()
        if not command == '':
            self.OutputDisplay.setText(command)
            self.CommandInput.setText("")

            if 'quit' in command.lower() or 'exit' in command.lower() or 'leave' in command.lower():
                self.quit_assistant()
            else:
                status = Assistant_main.command_input(command.lower())

            if not status:
                self.OutputDisplay.setText('Sorry, I didn\'t understand\nUse "Help Assistant"')
                self.icon_output('not_found')
                QtCore.QCoreApplication.processEvents()
                if Assistant_details.assistant_feedback_status:
                    AssistantSpeakAndListen.speak('Sorry, I didn\'t understand\nUse "Help Assistant"')

            elif status == 'command not found':
                self.OutputDisplay.setText('It seems I didn\'t get your Command\nUse "Help Assistant"')
                self.icon_output('not_found')
                QtCore.QCoreApplication.processEvents()
                if Assistant_details.assistant_feedback_status:
                    AssistantSpeakAndListen.speak('It seems I didn\'t get your Command\nUse "Help Assistant"')

            else:
                self.OutputDisplay.setText(status)
                self.icon_output(Assistant_details.icon_display)
                QtCore.QCoreApplication.processEvents()
                if Assistant_details.assistant_feedback_status:
                    AssistantSpeakAndListen.speak(status)

    def check_internet_connection(self):
        host = 'https://google.com/'
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    def show_microphone(self):
        self.CommandInput.hide()
        self.CommandSendButton.hide()
        self.DictationModeLabel.show()
        self.icon_output('stark-logo')
        QtCore.QCoreApplication.processEvents()

    def show_keyboard(self):
        self.CommandInput.show()
        self.CommandSendButton.show()
        self.DictationModeLabel.hide()
        self.icon_output('stark-logo')
        QtCore.QCoreApplication.processEvents()
        self.CommandStatusDisplay.setText('Type your Commands here')

    def quit_assistant(self):
        self.OutputDisplay.setText('Thanks for using me!')
        self.CommandStatusDisplay.setText('Exiting')
        QtCore.QCoreApplication.processEvents()

        if Assistant_details.assistant_feedback_status:
            AssistantSpeakAndListen.speak('Thanks for using me!')
        else:
            time.sleep(1)
        sys.exit(0)


# Form Window
class Ui_ConfigureWindow(object):
    def setupUi(self, ConfigureWindow):
        ConfigureWindow.setObjectName("ConfigureWindow")
        ConfigureWindow.setFixedSize(700, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigureWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ConfigureWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(150, 10, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(241, 10, 301, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setObjectName("StarkTitle")
        self.verticalLayout_2.addWidget(self.StarkTitle)

        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.verticalLayout_2.addWidget(self.PageTitle_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 661, 291))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(220, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setUnderline(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(44, 71, 571, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)

        # name input box
        self.nameInput.setFont(font)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameInput)

        self.dateOfBirthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.dateOfBirthLabel.setFont(font)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.genderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.nicknameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.nicknameLabel.setFont(font)
        self.nicknameLabel.setObjectName("nicknameLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.nicknameLabel)

        # nickname input box
        self.nicknameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.nicknameInput.setFont(font)
        self.nicknameInput.setObjectName("nicknameInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.nicknameInput)

        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.emailLabel)

        # email input box
        self.emailInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.emailInput.setFont(font)
        self.emailInput.setObjectName("emailInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.emailInput)

        # date section
        self.datelayout = QtWidgets.QHBoxLayout()
        self.datelayout.setObjectName("datelayout")
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Arial")
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.datelayout.addWidget(self.dateEdit)
        self.dateformat = QtWidgets.QLabel(self.formLayoutWidget)
        self.dateformat.setText("MM-DD-YYYY")
        self.dateformat.setAlignment(QtCore.Qt.AlignCenter)
        font.setPointSize(12)

        self.dateformat.setFont(font)
        self.dateformat.setObjectName("dateformat")
        self.datelayout.addWidget(self.dateformat)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.datelayout)

        # gender selector
        self.GenderSelector = QtWidgets.QComboBox(self.formLayoutWidget)
        self.GenderSelector.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GenderSelector.setEditable(False)
        self.GenderSelector.setCurrentText("")
        self.GenderSelector.setObjectName("GenderSelector")
        self.GenderSelector.addItems(['Male', 'Female'])
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.GenderSelector.setFont(font)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.GenderSelector)

        # submit button
        self.SubmitDetailsButton = QtWidgets.QPushButton(self.groupBox)
        self.SubmitDetailsButton.setGeometry(QtCore.QRect(540, 250, 75, 23))
        self.SubmitDetailsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.SubmitDetailsButton.setFont(font)
        self.SubmitDetailsButton.setObjectName("SubmitDetailsButton")
        self.SubmitDetailsButton.setStyleSheet("background-color:#0162ff; color: white; border-radius:5px")
        self.SubmitDetailsButton.clicked.connect(lambda: self.submit_form(ConfigureWindow))

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 224, 441, 16))
        self.label_2.setObjectName("label_2")

        # warning display
        self.WarningLabel = QtWidgets.QLabel(self.groupBox)
        self.WarningLabel.setGeometry(QtCore.QRect(40, 244, 441, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.WarningLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WarningLabel.setFont(font)
        self.WarningLabel.setObjectName("WarningLabel")
        self.WarningLabel.hide()

        ConfigureWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConfigureWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        ConfigureWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConfigureWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        ConfigureWindow.setStatusBar(self.statusbar)

        self.dateEdit.setDisplayFormat("dd-MM-yyyy")

        self.retranslateUi(ConfigureWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfigureWindow)

    def retranslateUi(self, ConfigureWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigureWindow.setWindowTitle(_translate("ConfigureWindow", "Fill up details"))
        self.StarkTitle.setText(_translate("ConfigureWindow", "Stark"))
        self.PageTitle_2.setText(_translate("ConfigureWindow", "The Personal Assistant"))
        self.groupBox.setTitle(_translate("ConfigureWindow", "Details"))
        self.label.setText(_translate("ConfigureWindow", "Enter your details here"))
        self.nameLabel.setText(_translate("ConfigureWindow", "Name"))
        self.dateOfBirthLabel.setText(_translate("ConfigureWindow", "Date of Birth"))
        self.genderLabel.setText(_translate("ConfigureWindow", "Gender"))
        self.nicknameLabel.setText(_translate("ConfigureWindow", "Nickname"))
        self.emailLabel.setText(_translate("ConfigureWindow", "Email"))
        self.SubmitDetailsButton.setText(_translate("ConfigureWindow", "Submit"))
        self.SubmitDetailsButton.setShortcut(_translate("ConfigureWindow", "Return"))
        self.label_2.setText(_translate("ConfigureWindow", "*You can change these later from within the settings"))
        self.WarningLabel.setText(_translate("ConfigureWindow", "**Please fill up all the details!"))
        self.SubmitDetailsButton.setShortcut(_translate("ConfigureWindow", "Return"))

    def submit_form(self, x):
        self.WarningLabel.hide()
        name = self.nameInput.text()
        dob = self.dateEdit.date().toPyDate().strftime('%d-%m-%Y')
        year = self.dateEdit.date().toPyDate().strftime('%Y')
        gender = self.GenderSelector.currentText()
        nickname = self.nicknameInput.text()
        email = self.emailInput.text()

        if name == '' or dob == '' or gender == '' or nickname == '' or email == '':
            self.WarningLabel.setText("**Please fill up all the details!")
            self.WarningLabel.show()

        elif int(year) >= int(Assistant_details.current_year):
            self.WarningLabel.setText("*Year should be less than {}!".format(Assistant_details.current_year))
            self.WarningLabel.show()

        else:
            self.WarningLabel.hide()
            try:
                self.personal_details = QSettings('PyQt5Application', 'Stark')
                self.personal_details.setValue('Name', name)
                self.personal_details.setValue('DOB', dob)
                self.personal_details.setValue('Gender', gender)
                self.personal_details.setValue('Nickname', nickname)
                self.personal_details.setValue('Email', email)
            except Exception as e:
                pass

            self.form_window = QtWidgets.QMainWindow()
            self.form_ui = Ui_MusicDialogSelector()
            self.form_ui.setupUi(self.form_window)
            x.close()
            self.form_window.show()


# music directory selector window
class Ui_MusicDialogSelector(object):
    def setupUi(self, MusicDialogSelector):
        MusicDialogSelector.setObjectName("MusicDialogSelector")
        MusicDialogSelector.setFixedSize(535, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MusicDialogSelector.setWindowIcon(icon)

        # ignore button
        self.IgnoreButton = QtWidgets.QPushButton(MusicDialogSelector)
        self.IgnoreButton.setGeometry(QtCore.QRect(350, 361, 75, 23))
        self.IgnoreButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IgnoreButton.setObjectName("IgnoreButton")
        self.IgnoreButton.setStyleSheet("background-color:#0162ff; color: white; border-radius:5px")

        # OK button
        self.ConfirmButton = QtWidgets.QPushButton(MusicDialogSelector)
        self.ConfirmButton.setGeometry(QtCore.QRect(440, 361, 75, 23))
        self.ConfirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConfirmButton.setDefault(True)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.ConfirmButton.setStyleSheet("background-color:#0162ff; color: white; border-radius:5px")

        # font styles for the buttons
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.IgnoreButton.setFont(font)

        # Big icon of Stark
        self.StarkIcon = QtWidgets.QLabel(MusicDialogSelector)
        self.StarkIcon.setGeometry(QtCore.QRect(69, 10, 81, 81))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")

        # layout containing Stark title and motto
        self.verticalLayoutWidget = QtWidgets.QWidget(MusicDialogSelector)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 10, 301, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StarkTitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StarkTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.StarkTitleLayout.setObjectName("StarkTitleLayout")

        # stark title
        self.StarkTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(30)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setObjectName("StarkTitle")
        self.StarkTitleLayout.addWidget(self.StarkTitle)

        # stark motto
        self.PageTitle_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(20)
        font.setWeight(50)
        self.PageTitle_2.setFont(font)
        self.PageTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle_2.setObjectName("PageTitle_2")
        self.StarkTitleLayout.addWidget(self.PageTitle_2)

        # frame containing Tre View and Info label
        self.frame = QtWidgets.QFrame(MusicDialogSelector)
        self.frame.setGeometry(QtCore.QRect(20, 96, 491, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # info label
        self.informationLabel = QtWidgets.QLabel(self.frame)
        self.informationLabel.setGeometry(QtCore.QRect(23, 1, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setWeight(50)
        self.informationLabel.setFont(font)
        self.informationLabel.setWordWrap(True)
        self.informationLabel.setObjectName("informationLabel")

        # type for the tree view
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')
        self.indexRoot = self.model.index(self.model.rootPath())
        self.model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)

        # tree view widget
        self.folderTreeView = QtWidgets.QTreeView(self.frame)
        self.folderTreeView.setModel(self.model)
        self.folderTreeView.setRootIndex(self.indexRoot)
        self.folderTreeView.setGeometry(QtCore.QRect(21, 75, 450, 150))
        self.folderTreeView.setObjectName("folderTreeView")
        # tree widget properties
        self.folderTreeView.setAnimated(True)
        self.folderTreeView.setIndentation(20)
        self.folderTreeView.setSortingEnabled(True)
        self.folderTreeView.setColumnHidden(3, True)
        self.folderTreeView.setColumnHidden(1, True)
        self.folderTreeView.setColumnWidth(0, 300)
        self.folderTreeView.clicked.connect(self.display_directory)

        # label to display selected directory and warning
        self.directoryDisplay = QtWidgets.QLabel(self.frame)
        self.directoryDisplay.setGeometry(QtCore.QRect(26, 225, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.directoryDisplay.setFont(font)
        self.directoryDisplay.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.directoryDisplay.setObjectName("directoryDisplay")

        self.retranslateUi(MusicDialogSelector)
        QtCore.QMetaObject.connectSlotsByName(MusicDialogSelector)
        MusicDialogSelector.setTabOrder(self.folderTreeView, self.IgnoreButton)
        MusicDialogSelector.setTabOrder(self.IgnoreButton, self.ConfirmButton)

        # event handlers for Ignore and OK buttons
        self.IgnoreButton.clicked.connect(lambda: self.ignore_selection(MusicDialogSelector))
        self.ConfirmButton.clicked.connect(lambda: self.confirm_selection(MusicDialogSelector))

        self.selected_path = ''

    def retranslateUi(self, MusicDialogSelector):
        _translate = QtCore.QCoreApplication.translate
        MusicDialogSelector.setWindowTitle(_translate("MusicDialogSelector", "Music Directory"))
        self.IgnoreButton.setText(_translate("MusicDialogSelector", "Ignore"))
        self.ConfirmButton.setText(_translate("MusicDialogSelector", "OK"))
        self.ConfirmButton.setShortcut(_translate("MusicDialogSelector", "Return"))
        self.StarkTitle.setText(_translate("MusicDialogSelector", "Stark"))
        self.PageTitle_2.setText(_translate("MusicDialogSelector", "The Personal Assistant"))
        self.informationLabel.setText(_translate("MusicDialogSelector",
                                                 "Choose the folder from where you want to play music. Stark will use this folder to play music when requested. You can change this later from within the settings"))
        self.directoryDisplay.setText(_translate("MusicDialogSelector", ""))

    def display_directory(self, index):
        '''Function for updating the directory display label'''
        indexItem = self.model.index(index.row(), 0, index.parent())
        self.selected_path = str(self.model.filePath(indexItem))
        self.directoryDisplay.setText(self.selected_path)
        self.directoryDisplay.setStyleSheet('color: black;')

    def ignore_selection(self, x):
        '''Button event for the ignore button'''
        try:
            self.music_settings = QSettings('PyQt5Application', 'Stark')
            self.music_settings.setValue('music_folder', 'None')
        except Exception as e:
            pass
        self.starkui = Ui_StarkWindow()
        self.starkwindow = QtWidgets.QMainWindow()
        self.starkui.setupUi(self.starkwindow)
        x.close()
        self.starkwindow.show()

    def confirm_selection(self, x):
        '''Button event for OK button'''
        if self.selected_path == '':
            self.directoryDisplay.setText('*Select a folder containing music!')
            self.directoryDisplay.setStyleSheet('color: red;')
        else:
            music_path = self.selected_path
            music_path = music_path.replace('/', '\\\\')
            try:
                self.music_settings = QSettings('PyQt5Application', 'Stark')
                self.music_settings.setValue('music_folder', music_path)
            except Exception as e:
                pass
            try:
                self.starkui = Ui_StarkWindow()
                self.starkwindow = QtWidgets.QMainWindow()
                self.starkui.setupUi(self.starkwindow)
                x.close()
                self.starkwindow.show()
            except Exception as e:
                pass


# startup window
class Ui_StartUpWindow(object):
    def setupUi(self, StartUpWindow):
        StartUpWindow.setObjectName("StartUpWindow")
        StartUpWindow.setFixedSize(600, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartUpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StartUpWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.StarkTitle = QtWidgets.QLabel(self.centralwidget)
        self.StarkTitle.setGeometry(QtCore.QRect(10, 8, 571, 91))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(70)
        font.setWeight(50)
        self.StarkTitle.setFont(font)
        self.StarkTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkTitle.setObjectName("StarkTitle")

        self.StarkLabel = QtWidgets.QLabel(self.centralwidget)
        self.StarkLabel.setGeometry(QtCore.QRect(10, 78, 581, 91))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(40)
        font.setWeight(50)
        self.StarkLabel.setFont(font)
        self.StarkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StarkLabel.setObjectName("StarkLabel")

        self.ProgressDisplayFrame = QtWidgets.QFrame(self.centralwidget)
        self.ProgressDisplayFrame.setGeometry(QtCore.QRect(10, 310, 581, 131))
        self.ProgressDisplayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProgressDisplayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressDisplayFrame.setObjectName("ProgressDisplayFrame")
        self.ProgressDisplayFrame.hide()

        self.ProgressBar = QtWidgets.QProgressBar(self.ProgressDisplayFrame)
        self.ProgressBar.setGeometry(QtCore.QRect(140, 56, 321, 31))
        self.ProgressBar.setObjectName("ProgressBar")

        self.StarkIcon = QtWidgets.QLabel(self.centralwidget)
        self.StarkIcon.setGeometry(QtCore.QRect(240, 178, 120, 120))
        self.StarkIcon.setText("")
        self.StarkIcon.setPixmap(QtGui.QPixmap("resources/icons/stark-logo.png"))
        self.StarkIcon.setScaledContents(True)
        self.StarkIcon.setObjectName("StarkIcon")

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(235, 360, 130, 40))
        self.StartButton.clicked.connect(lambda: self.get_started_func(StartUpWindow))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color:#0162ff; color: white; border-radius:7px")
        self.StartButton.setObjectName("StartButton")

        StartUpWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(StartUpWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        StartUpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartUpWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        StartUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartUpWindow)
        QtCore.QMetaObject.connectSlotsByName(StartUpWindow)

    def retranslateUi(self, StartUpWindow):
        _translate = QtCore.QCoreApplication.translate
        StartUpWindow.setWindowTitle(_translate("StartUpWindow", "\'Stark\' Start-up"))
        self.StarkTitle.setText(_translate("StartUpWindow", "Stark"))
        self.StarkLabel.setText(_translate("StartUpWindow", "The Personal Assistant"))
        self.StartButton.setText(_translate("StartUpWindow", "Get Started"))
        self.StartButton.setShortcut(_translate("StartUpWindow", "Return"))

    def get_started_func(self, x):
        self.ProgressDisplayFrame.show()
        self.StartButton.hide()
        try:
            self.ProgressBar.setValue(10)
            personal_settings = QSettings('PyQt5Application', 'Stark')
            Assistant_details.owner = personal_settings.value('Name')
            Assistant_details.dob = personal_settings.value('DOB')
            Assistant_details.gender = personal_settings.value('Gender')
            Assistant_details.nickname = personal_settings.value('Nickname')
            Assistant_details.email = personal_settings.value('Email')

            self.ProgressBar.setValue(30)

            if Assistant_details.owner == None or Assistant_details.dob == None or Assistant_details.gender == None or Assistant_details.nickname == None or Assistant_details.email == None:
                raise ValueError('No personal detail registry files found')
            if Assistant_details.gender == 'Male':
                Assistant_details.denotation = 'Sir'
            else:
                Assistant_details.denotation = "Ma'am"

            self.ProgressBar.setValue(50)

            try:
                Assistant_details.assistant_feedback_status = strtobool(
                    personal_settings.value('assistant_feedback_status'))
                Assistant_details.click_sound_status = strtobool(personal_settings.value('click_sound_status'))
                Assistant_details.start_stop_sound_status = strtobool(
                    personal_settings.value('start_stop_sound_status'))
                Assistant_details.voice_type = personal_settings.value('voice_type')

                self.ProgressBar.setValue(70)

                try:
                    Assistant_details.music_folder = personal_settings.value('music_folder')
                    if Assistant_details.music_folder == None:
                        raise ValueError('No music registry files found')

                    self.ProgressBar.setValue(90)

                except Exception as e:
                    self.music_window = QtWidgets.QMainWindow()
                    self.music_ui = Ui_MusicDialogSelector()
                    self.music_ui.setupUi(self.music_window)
                    x.close()
                    self.music_window.show()

            except Exception as e:
                self.sound_settings = QSettings('PyQt5Application', 'Stark')
                self.sound_settings.setValue('assistant_feedback_status', 'True')
                self.sound_settings.setValue('click_sound_status', 'True')
                self.sound_settings.setValue('start_stop_sound_status', 'True')
                self.sound_settings.setValue('voice_type', 'Male')
                Assistant_details.assistant_feedback_status = strtobool(
                    self.sound_settings.value('assistant_feedback_status'))
                Assistant_details.click_sound_status = strtobool(self.sound_settings.value('click_sound_status'))
                Assistant_details.start_stop_sound_status = strtobool(
                    self.sound_settings.value('start_stop_sound_status'))
                Assistant_details.voice_type = self.sound_settings.value('voice_type')

            '''here comes stark window'''
            self.ProgressBar.setValue(100)

            self.starkui = Ui_StarkWindow()
            self.starkwindow = QtWidgets.QMainWindow()
            self.starkui.setupUi(self.starkwindow)
            x.close()
            self.starkwindow.show()

        except Exception as e:
            self.form_window = QtWidgets.QMainWindow()
            self.form_ui = Ui_ConfigureWindow()
            self.form_ui.setupUi(self.form_window)
            x.close()
            self.form_window.show()


class Ui_ActivationWindow(object):
    def setupUi(self, ActivationWindow):
        ActivationWindow.setObjectName("ActivationWindow")
        ActivationWindow.setFixedSize(540, 533)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ActivationWindow.setWindowIcon(icon)
        ActivationWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ActivationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 460, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border:none;background-color:#0162ff;color:white;border-radius:7px")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 291, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 351, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 160, 231, 111))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("resources/images/1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 267, 351, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 231, 111))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("resources/images/2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 300, 231, 111))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("resources/images/3.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 420, 351, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 351, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        ActivationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActivationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        ActivationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActivationWindow)
        self.statusbar.setObjectName("statusbar")
        ActivationWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(lambda: self.activate_stark(ActivationWindow))
        self.warninglabel = QtWidgets.QLabel(self.centralwidget)
        self.warninglabel.setGeometry(QtCore.QRect(20, 480, 351, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setWeight(50)
        self.warninglabel.setFont(font)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.warninglabel.setPalette(palette)
        self.warninglabel.setText("* Connect to internet!")
        self.warninglabel.setObjectName("warninglabel")
        self.warninglabel.hide()

        self.retranslateUi(ActivationWindow)
        QtCore.QMetaObject.connectSlotsByName(ActivationWindow)

    def retranslateUi(self, ActivationWindow):
        _translate = QtCore.QCoreApplication.translate
        ActivationWindow.setWindowTitle(_translate("ActivationWindow", "ActivationWindow"))
        self.pushButton.setText(_translate("ActivationWindow", "Activate Now!"))
        self.label.setText(_translate("ActivationWindow", "You need to activate this software before you can use it!"))
        self.label_2.setText(_translate("ActivationWindow", "Follow the below steps to activate the software:-"))
        self.label_3.setText(_translate("ActivationWindow", "1. Click on the \'Activate Now!\' button."))
        self.label_4.setText(_translate("ActivationWindow", "2. You will be directed to a YouTube channel."))
        self.label_6.setText(_translate("ActivationWindow", "3. You simply need to subscribe the channel."))
        self.label_9.setText(_translate("ActivationWindow", "4. After that, start the application again."))
        self.label_10.setText(_translate("ActivationWindow", "5. And that\'s all! You are good to go!"))
        self.pushButton.setShortcut(_translate("ActivationWindow", "Return"))

    def activate_stark(self, x):
        internet = False
        host = 'https://google.com/'
        try:
            urllib.request.urlopen(host)
            internet =  True
        except:
            internet =  False
        if internet:
            webbrowser.get().open('https://www.youtube.com/everythingcomputerized')
            activation_status = QSettings('PyQt5Application', 'Stark')
            activation_status.setValue('activation', 1)
            time.sleep(1)
            sys.exit(0)
        else:
            self.warninglabel.show()


def main():
    activation_status = QSettings('PyQt5Application', 'Stark')
    status = activation_status.value('activation')

    if status==None or status==0 or status=='0' or status=='False' or status==False:
        app = QtWidgets.QApplication(sys.argv)
        ActivationWindow = QtWidgets.QMainWindow()
        ui = Ui_ActivationWindow()
        ui.setupUi(ActivationWindow)
        ActivationWindow.show()
        sys.exit(app.exec_())
    else:
        app = QtWidgets.QApplication(sys.argv)
        StartUpWindow = QtWidgets.QMainWindow()
        ui = Ui_StartUpWindow()
        ui.setupUi(StartUpWindow)
        StartUpWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
