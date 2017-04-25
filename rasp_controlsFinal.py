# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raspUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 246, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 246, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 246, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(750, 16777215))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.splash = QtGui.QWidget()
        self.splash.setObjectName(_fromUtf8("splash"))
        self.gridLayout_6 = QtGui.QGridLayout(self.splash)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.welcome = QtGui.QLabel(self.splash)
        self.welcome.setObjectName(_fromUtf8("welcome"))
        self.gridLayout_6.addWidget(self.welcome, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.begin = QtGui.QPushButton(self.splash)
        self.begin.setMinimumSize(QtCore.QSize(120, 50))
        self.begin.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.begin.setFont(font)
        self.begin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.begin.setStyleSheet(_fromUtf8("QPushButton#begin{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(85, 255, 127);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#begin::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.begin.setObjectName(_fromUtf8("begin"))
        self.gridLayout_6.addWidget(self.begin, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.splash)
        self.screenLogin = QtGui.QWidget()
        self.screenLogin.setObjectName(_fromUtf8("screenLogin"))
        self.gridLayout_4 = QtGui.QGridLayout(self.screenLogin)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.screenLogin)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passEdit = QtGui.QLineEdit(self.screenLogin)
        self.passEdit.setMinimumSize(QtCore.QSize(450, 40))
        self.passEdit.setMaximumSize(QtCore.QSize(450, 40))
        self.passEdit.setStyleSheet(_fromUtf8("QLineEdit#passEdit{\n"
"    border-style: solid;\n"
"    border-color: rgb(180, 180, 180);\n"
"    border-width:2px;\n"
"    border-radius: 7px;\n"
"    \n"
"}"))
        self.passEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passEdit.setObjectName(_fromUtf8("passEdit"))
        self.horizontalLayout_5.addWidget(self.passEdit)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLogin = QtGui.QGridLayout()
        self.gridLogin.setHorizontalSpacing(6)
        self.gridLogin.setVerticalSpacing(25)
        self.gridLogin.setObjectName(_fromUtf8("gridLogin"))
        self.clearpass = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearpass.sizePolicy().hasHeightForWidth())
        self.clearpass.setSizePolicy(sizePolicy)
        self.clearpass.setMinimumSize(QtCore.QSize(120, 50))
        self.clearpass.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clearpass.setStyleSheet(_fromUtf8("QPushButton#clearpass{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#clearpass::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.clearpass.setIconSize(QtCore.QSize(24, 24))
        self.clearpass.setObjectName(_fromUtf8("clearpass"))
        self.gridLogin.addWidget(self.clearpass, 5, 1, 1, 1)
        self.login = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(120, 50))
        self.login.setFocusPolicy(QtCore.Qt.NoFocus)
        self.login.setStyleSheet(_fromUtf8("QPushButton#login{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#login::pressed{\n"
"background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.login.setIconSize(QtCore.QSize(24, 24))
        self.login.setObjectName(_fromUtf8("login"))
        self.gridLogin.addWidget(self.login, 5, 4, 1, 1)
        self.six = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.six.setFont(font)
        self.six.setFocusPolicy(QtCore.Qt.NoFocus)
        self.six.setStyleSheet(_fromUtf8("QPushButton#six{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#six::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.six.setDefault(False)
        self.six.setFlat(False)
        self.six.setObjectName(_fromUtf8("six"))
        self.gridLogin.addWidget(self.six, 3, 4, 1, 1)
        self.five = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.five.setFont(font)
        self.five.setFocusPolicy(QtCore.Qt.NoFocus)
        self.five.setStyleSheet(_fromUtf8("QPushButton#five{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#five::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.five.setObjectName(_fromUtf8("five"))
        self.gridLogin.addWidget(self.five, 3, 2, 1, 1)
        self.one = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.one.setFont(font)
        self.one.setFocusPolicy(QtCore.Qt.NoFocus)
        self.one.setStyleSheet(_fromUtf8("QPushButton#one{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#one::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.one.setObjectName(_fromUtf8("one"))
        self.gridLogin.addWidget(self.one, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.eight = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.eight.setFont(font)
        self.eight.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eight.setStyleSheet(_fromUtf8("QPushButton#eight{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#eight::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.eight.setObjectName(_fromUtf8("eight"))
        self.gridLogin.addWidget(self.eight, 4, 2, 1, 1)
        self.seven = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.seven.setFont(font)
        self.seven.setFocusPolicy(QtCore.Qt.NoFocus)
        self.seven.setStyleSheet(_fromUtf8("QPushButton#seven{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#seven::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.seven.setObjectName(_fromUtf8("seven"))
        self.gridLogin.addWidget(self.seven, 4, 1, 1, 1)
        self.nine = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.nine.setFont(font)
        self.nine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nine.setStyleSheet(_fromUtf8("QPushButton#nine{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#nine::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.nine.setObjectName(_fromUtf8("nine"))
        self.gridLogin.addWidget(self.nine, 4, 4, 1, 1)
        self.four = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.four.setFont(font)
        self.four.setFocusPolicy(QtCore.Qt.NoFocus)
        self.four.setStyleSheet(_fromUtf8("QPushButton#four{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#four::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.four.setObjectName(_fromUtf8("four"))
        self.gridLogin.addWidget(self.four, 3, 1, 1, 1)
        self.two = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.two.setFont(font)
        self.two.setFocusPolicy(QtCore.Qt.NoFocus)
        self.two.setStyleSheet(_fromUtf8("QPushButton#two{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#two::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.two.setObjectName(_fromUtf8("two"))
        self.gridLogin.addWidget(self.two, 1, 2, 1, 1)
        self.three = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.three.setFont(font)
        self.three.setFocusPolicy(QtCore.Qt.NoFocus)
        self.three.setStyleSheet(_fromUtf8("QPushButton#three{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#three::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.three.setObjectName(_fromUtf8("three"))
        self.gridLogin.addWidget(self.three, 1, 4, 1, 1)
        self.zero = QtGui.QPushButton(self.screenLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.zero.setFont(font)
        self.zero.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero.setStyleSheet(_fromUtf8("QPushButton#zero{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton#zero::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.zero.setObjectName(_fromUtf8("zero"))
        self.gridLogin.addWidget(self.zero, 5, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLogin.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLogin.addItem(spacerItem3, 3, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLogin, 4, 0, 1, 2)
        self.stackedWidget.addWidget(self.screenLogin)
        self.control = QtGui.QWidget()
        self.control.setMinimumSize(QtCore.QSize(750, 450))
        self.control.setObjectName(_fromUtf8("control"))
        self.gridLayout_2 = QtGui.QGridLayout(self.control)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lock_2 = QtGui.QPushButton(self.control)
        self.lock_2.setMinimumSize(QtCore.QSize(100, 50))
        self.lock_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lock_2.setStyleSheet(_fromUtf8("QPushButton#lock_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(180, 180, 180);\n"
"    border-width: 2px;\n"
"    border-color: rgb(180, 180, 180);\n"
"}\n"
"QPushButton#lock_2::pressed{\n"
"    background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"}"))
        self.lock_2.setObjectName(_fromUtf8("lock_2"))
        self.horizontalLayout_4.addWidget(self.lock_2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(779, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.start = QtGui.QPushButton(self.control)
        self.start.setMinimumSize(QtCore.QSize(500, 120))
        self.start.setMaximumSize(QtCore.QSize(500, 120))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.start.setFont(font)
        self.start.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start.setStyleSheet(_fromUtf8("QPushButton#start{\n"
"    background-color: rgb(161, 255, 167);\n"
"    border-style: solid;\n"
"    border-radius: 7px;\n"
"    color: rgb(115, 115, 115);\n"
"    border-width: 3px;\n"
"    border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
""))
        self.start.setObjectName(_fromUtf8("start"))
        self.gridLayout_2.addWidget(self.start, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.line_9 = QtGui.QFrame(self.control)
        self.line_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.horizontalLayout_3.addWidget(self.line_9)
        self.over_2 = QtGui.QPushButton(self.control)
        self.over_2.setEnabled(True)
        self.over_2.setMinimumSize(QtCore.QSize(70, 20))
        self.over_2.setMaximumSize(QtCore.QSize(70, 30))
        self.over_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.over_2.setStyleSheet(_fromUtf8("QPushButton#over_2{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    color: rgb(180, 180, 180);\n"
"}\n"
""))
        self.over_2.setObjectName(_fromUtf8("over_2"))
        self.horizontalLayout_3.addWidget(self.over_2)
        self.line_7 = QtGui.QFrame(self.control)
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_3.addWidget(self.line_7)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.line_8 = QtGui.QFrame(self.control)
        self.line_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout_3.addWidget(self.line_8)
        self.rone_2 = QtGui.QPushButton(self.control)
        self.rone_2.setEnabled(True)
        self.rone_2.setMinimumSize(QtCore.QSize(70, 30))
        self.rone_2.setMaximumSize(QtCore.QSize(100, 30))
        self.rone_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rone_2.setStyleSheet(_fromUtf8("QPushButton#rone_2{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    color: rgb(180, 180, 180);\n"
"}\n"
""))
        self.rone_2.setObjectName(_fromUtf8("rone_2"))
        self.horizontalLayout_3.addWidget(self.rone_2)
        self.line_3 = QtGui.QFrame(self.control)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_3.addWidget(self.line_3)
        self.rtwo_2 = QtGui.QPushButton(self.control)
        self.rtwo_2.setEnabled(True)
        self.rtwo_2.setMinimumSize(QtCore.QSize(70, 20))
        self.rtwo_2.setMaximumSize(QtCore.QSize(70, 30))
        self.rtwo_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rtwo_2.setStyleSheet(_fromUtf8("QPushButton#rtwo_2{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    color: rgb(180, 180, 180);\n"
"}\n"
""))
        self.rtwo_2.setObjectName(_fromUtf8("rtwo_2"))
        self.horizontalLayout_3.addWidget(self.rtwo_2)
        self.line_5 = QtGui.QFrame(self.control)
        self.line_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_3.addWidget(self.line_5)
        self.rthree_2 = QtGui.QPushButton(self.control)
        self.rthree_2.setEnabled(True)
        self.rthree_2.setMinimumSize(QtCore.QSize(70, 20))
        self.rthree_2.setMaximumSize(QtCore.QSize(70, 30))
        self.rthree_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rthree_2.setStyleSheet(_fromUtf8("QPushButton#rthree_2{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    color: rgb(180, 180, 180);\n"
"}\n"
""))
        self.rthree_2.setObjectName(_fromUtf8("rthree_2"))
        self.horizontalLayout_3.addWidget(self.rthree_2)
        self.line_6 = QtGui.QFrame(self.control)
        self.line_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_3.addWidget(self.line_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)
        self.timer_label = QtGui.QLabel(self.control)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_label.sizePolicy().hasHeightForWidth())
        self.timer_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.timer_label.setFont(font)
        self.timer_label.setObjectName(_fromUtf8("timer_label"))
        self.gridLayout_2.addWidget(self.timer_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lcdnum = QtGui.QLCDNumber(self.control)
        self.lcdnum.setMinimumSize(QtCore.QSize(500, 100))
        self.lcdnum.setMaximumSize(QtCore.QSize(500, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lcdnum.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lcdnum.setFont(font)
        self.lcdnum.setStyleSheet(_fromUtf8("QLCDNumber#lcdnum{\n"
"    color:rgb(115, 115, 115);\n"
"    border-style: solid;\n"
"    border-width: 3px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    border-radius: 7px;\n"
"}"))
        self.lcdnum.setFrameShape(QtGui.QFrame.WinPanel)
        self.lcdnum.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdnum.setSmallDecimalPoint(False)
        self.lcdnum.setNumDigits(5)
        self.lcdnum.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdnum.setObjectName(_fromUtf8("lcdnum"))
        self.gridLayout_2.addWidget(self.lcdnum, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtGui.QSpacerItem(779, 37, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 7, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(779, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.control)
        self.error = QtGui.QWidget()
        self.error.setObjectName(_fromUtf8("error"))
        self.gridLayout_3 = QtGui.QGridLayout(self.error)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.errorOccur = QtGui.QLabel(self.error)
        self.errorOccur.setObjectName(_fromUtf8("errorOccur"))
        self.gridLayout_5.addWidget(self.errorOccur, 0, 1, 1, 1)
        self.logo = QtGui.QLabel(self.error)
        self.logo.setMinimumSize(QtCore.QSize(30, 30))
        self.logo.setMaximumSize(QtCore.QSize(30, 30))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/logins/indicator_input_error.png")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.gridLayout_5.addWidget(self.logo, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.errorCode = QtGui.QLabel(self.error)
        self.errorCode.setObjectName(_fromUtf8("errorCode"))
        self.gridLayout_5.addWidget(self.errorCode, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.realError = QtGui.QLabel(self.error)
        self.realError.setObjectName(_fromUtf8("realError"))
        self.gridLayout_5.addWidget(self.realError, 1, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.error)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.error)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RaspControl", None))
        self.welcome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#55ff7f;\"> welcome </span></p></body></html>", None))
        self.begin.setText(_translate("MainWindow", "Start", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#b4b4b4;\">Login Required</span></p></body></html>", None))
        self.clearpass.setText(_translate("MainWindow", "CLEAR", None))
        self.login.setText(_translate("MainWindow", "LOGIN", None))
        self.six.setText(_translate("MainWindow", "6", None))
        self.five.setText(_translate("MainWindow", "5", None))
        self.one.setText(_translate("MainWindow", "1", None))
        self.eight.setText(_translate("MainWindow", "8", None))
        self.seven.setText(_translate("MainWindow", "7", None))
        self.nine.setText(_translate("MainWindow", "9", None))
        self.four.setText(_translate("MainWindow", "4", None))
        self.two.setText(_translate("MainWindow", "2", None))
        self.three.setText(_translate("MainWindow", "3", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.lock_2.setText(_translate("MainWindow", "Lock", None))
        self.start.setText(_translate("MainWindow", "START", None))
        self.over_2.setText(_translate("MainWindow", "E-Stop", None))
        self.rone_2.setText(_translate("MainWindow", "Relay 1", None))
        self.rtwo_2.setText(_translate("MainWindow", "Relay 2", None))
        self.rthree_2.setText(_translate("MainWindow", "Relay 3", None))
        self.timer_label.setText(_translate("MainWindow", "<html><head/><body><p>Timer</p></body></html>", None))
        self.errorOccur.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">error occurred</span></p></body></html>", None))
        self.errorCode.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">error code : </span></p></body></html>", None))
        self.realError.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">error</span></p></body></html>", None))

