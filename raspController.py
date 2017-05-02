import sys
import os
from os import listdir
import subprocess
import time
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
import rasp_controlsFinal
import xml.etree.ElementTree as ET
import random


    

class controller(QtGui.QMainWindow, rasp_controlsFinal.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        #have the +
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        # parses the xml file
        parse = ET.parse('cript.xml')
        root = parse.getroot()
        stored = root[0][0].text

        self.states = []

        if len(root) == 5:
            for i in range(len(root)):
                self.states.append(root[i][0].text)
                i += 1
        else:
            self.stackedWidget.setCurrentIndex(3)
            self.errorOccur.setText("An Error Occurred")
            self.errorCode.setText("<b>Error Code</b>" + " :445")
            self.realError.setText("Error Parsing the xml file")

        # Login screen Button click events
        self.begin.clicked.connect(lambda : self.beginLogin())
        self.one.clicked.connect(lambda : self.insertPass(str(1)))
        self.two.clicked.connect(lambda : self.insertPass(str(2)))
        self.three.clicked.connect(lambda : self.insertPass(str(3)))
        self.four.clicked.connect(lambda : self.insertPass(str(4)))
        self.five.clicked.connect(lambda : self.insertPass(str(5)))
        self.six.clicked.connect(lambda : self.insertPass(str(6)))
        self.seven.clicked.connect(lambda : self.insertPass(str(7)))
        self.eight.clicked.connect(lambda : self.insertPass(str(8)))
        self.nine.clicked.connect(lambda : self.insertPass(str(9)))
        self.zero.clicked.connect(lambda : self.insertPass(str(0)))

        #error page
        self.goback.clicked.connect(lambda : self.errorBack())

        # Login
        self.login.clicked.connect(lambda : self.logIn(root))

        self.clearpass.clicked.connect(lambda :  self.clearText())
        self.passEdit.setEnabled(False)
        self.passEdit.setEchoMode(2)
        self.passEdit.setMaxLength(4)
        self.passEdit.setText("")

        # main window ops
        self.lock_2.clicked.connect(lambda : self.lockBack())

        self.startSecs = 0
        self.startmins = 0
        self.timer = QtCore.QTimer(self)

        # this timer will control the lcd display, i stop it to start it when i need it
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.timer.stop()

        self.start.clicked.connect(lambda : self.startBiz())
        # self.worker = WorkerThread()
        
    def errorBack(self):
        self.stackedWidget.setCurrentIndex(2)

    def beginLogin(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def insertPass(self, index):
        current = self.passEdit.text()
        self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(180, 180, 180); border-width:2px; border-radius: 7px;")
        print str(len(current)) + index
        self.passEdit.setText(current + index)

    def logIn(self, root):
        self.lcdnum.display("00"+ ":"+ "00")
        current = self.passEdit.text()

        if not len(current) > 0:
            self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(255, 0, 0); border-width:2px; border-radius: 7px;")

        if len(current) == 4 and current == root[0][0].text:
            print "correct password"
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.passEdit.setText("")
            self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(255, 0, 0); border-width:2px; border-radius: 7px;")
        
        """if states[2] == "1":
            self.rone_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: outset; border-radius: 6px;")

        if states[3] == "1":
            self.rtwo_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: outset; border-radius: 6px;")

        if states[4] == "1":
            self.rthree_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: outset; border-radius: 6px;")"""

    def clearText(self):
        self.passEdit.clear()

    # main op functions
    def lockBack(self):
        self.passEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    def updateLCD(self):
        self.startSecs += 1
        self.updateDet()


    def updateDet(self):
        self.lcdnum.display("0"+"%s" % str(self.startmins) + ":" + "%s" % str(self.startSecs))

        if self.startSecs == 60:
            self.startSecs = 0
            self.startmins += 1
            self.lcdnum.display("0"+"%s" % str(self.startmins) + ":" + "%s" % str(self.startSecs))

        if self.startSecs <= 9:
            self.lcdnum.display("0"+"%s" % str(self.startmins) + ":0" + "%s" % str(self.startSecs))

        if self.startmins == 4:
            self.lcdnum.display("0"+"%s" % str(self.startmins) + ":0" + "%s" % str(self.startSecs))
            self.timer.stop()

        # manipulate the relays and update xml file

        # at three minutes, turn relay one on, turn relay 2 on
        if self.startmins == 3 and self.startSecs == 0:
            # relay one on
            self.rone_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")

            # relay two on
            self.rtwo_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")
        
        # at 3 mins and 35 seconds turn relay 2 off
        if self.startmins == 3 and self.startSecs == 5:
            # relay 2 off
            print self.states[3]
            self.rtwo_2.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")


        # at 3 mins and 30 seconds turn relay one off, relay 3 on 
        if self.startmins == 3 and self.startSecs == 30:
            # relay one off
            self.rone_2.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")

            # relay 3 on
            print self.states[3]
            self.rthree_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")


        # at 3 mins and 35 seconds turn relay 3 off
        if self.startmins == 3 and self.startSecs == 35:
            self.rthree_2.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")


    def startBiz(self):
        # code for playing music +
        try:
            mp3_files = [f for f in listdir('./MusicFiles/') if f[-4:] == '.mp3']
            
            numMps = 0

            parse = ET.parse('cript.xml')
            root = parse.getroot()


            # 0 is START 1 is STOP
            if root[1][0].text == "0":

                # Stop (Pause) the timer
                self.timer.stop()

                #kill all background music when stop button is pressed
                subprocess.Popen(['killall', 'mpg321'])
                

                self.start.setStyleSheet("background-color: rgb(161, 255, 167); border-style: solid; border-radius: 7px; border-width: 3px; border-color: rgb(180, 180, 180);")
                self.start.setText("START")
                root[1][0].text = str(1)
                root.set('Toggle', 'On/Off')

                # revert the timer back to zero and display it on the lcd
                #self.startSecs = 0
                #self.lcdnum.display("00"+":"+"00")
            
            elif root[1][0].text == "1":
                if len(mp3_files) == numMps:
                    self.stackedWidget.setCurrentIndex(3)
                    self.errorOccur.setText("An Error Occurred")
                    self.errorCode.setText("<b>Error Code</b>" + " :550")
                    self.realError.setText("Did not find any .mp3 files in the Musics Folder")
                else:
                    x = random.randint(0, len(mp3_files))
                    try:
                        subprocess.Popen(['mpg321', './MusicFiles/%s' % mp3_files[x]])
                        print "Playing mp3 file "
                        time.sleep(1)
                    except IndexError:
                        subprocess.Popen(['mpg321', './MusicFiles/%s' % mp3_files[x-1]])
                        print "Playing mp3 file "
                        time.sleep(1)

                self.start.setText("STOP")
                self.start.setStyleSheet("background-color: rgb(255, 87, 90); border-style: solid; border-radius: 7px; border-width: 3px; border-color: rgb(180, 180, 180);")
                root[1][0].text = str(0)
                root.set('Toggle', 'On/Off')

                # Start (Continue) with thhe timer
                self.timer.start()

            else:
                self.stackedWidget.setCurrentIndex(3)
                self.errorOccur.setText("An Error Occurred")
                self.errorCode.setText("<b>Error Code</b>" + " :450")
                self.realError.setText("Error Parsing the xml file : Could not parse On/Off button state")

            parse.write('cript.xml')
        except OSError:
            self.stackedWidget.setCurrentIndex(3)
            self.errorOccur.setText("An Error Occurred")
            self.errorCode.setText("<b>Error Code</b>" + " :550")
            self.realError.setText("Did not find any .mp3 files in the Musics Folder")
        else:
            print "There are %s .mp3 files in the MusicFiles Directory" % len(mp3_files)
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    control = controller()

    screen = QtGui.QDesktopWidget().screenGeometry()
    h = 800
    w = 480
    hs = (screen.width() - h)/2
    ws = (screen.height() - w)/2
    control.setGeometry(hs, ws, h, w)
    control.show()
    app.exec_()
if __name__ == '__main__':
    main()
