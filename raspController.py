import os
import random
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from os import listdir
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
from PyQt4.QtGui import QAction
import rasp_controlsFinal


class controller(QtGui.QMainWindow, rasp_controlsFinal.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+R"), self, self.restartTimer)

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+H"), self, self.hideMenu)

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+S"), self, self.stopTimer)

        #have the +
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        # parses the xml file
        parse = ET.parse('cript.xml')
        self.root = parse.getroot()
        stored = self.root[0][0].text

        self.states = []

        if len(self.root) == 5:
            for i in range(len(self.root)):
                self.states.append(self.root[i][0].text)
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
        self.login.clicked.connect(lambda : self.logIn(self.root))

        self.clearpass.clicked.connect(lambda :  self.clearText())
        self.passEdit.setEnabled(False)
        self.passEdit.setEchoMode(2)
        self.passEdit.setMaxLength(4)
        self.passEdit.setText("")

        # main window ops
        self.lock_2.clicked.connect(lambda : self.lockBack())

        self.startSecs = 60
        self.startmins = 3
        self.timer = QtCore.QTimer(self)
        self.counter = 0

        # this timer will control the lcd display, i stop it to start it when i need it
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.timer.stop()

        self.mp3_files = [self.f for self.f in listdir('./MusicFiles/') if self.f[-4:] == '.mp3']
        #print self.f[:3]
        
        self.start.clicked.connect(lambda : self.startBiz())
        # self.worker = WorkerThread()

    def hideMenu(self):
        self.passEdit.setText("")
        self.beginLogin()

    def stopTimer(self):
        # Stop (Pause) the timer
        self.timer.stop()

        #kill all background music when stop button is pressed
        subprocess.Popen(['killall', 'mpg321'])

        self.start.setStyleSheet("background-color: rgb(161, 255, 167); border-style: solid; border-radius: 7px; border-width: 3px; border-color: rgb(180, 180, 180);")
        self.start.setText("START")
        self.root[1][0].text = str(1)
        self.root.set('Toggle', 'On/Off')

    def restartTimer(self):
        # revert back all functionality
        self.counter = 0
        self.timer.stop()
        self.startSecs = 60
        self.startmins = 3
        self.lcdnum.display("0"+"%s" % str(4) + ":0" + "%s" % str(0))
        subprocess.Popen(['killall', 'mpg321'])

        self.start.setStyleSheet("background-color: rgb(161, 255, 167); border-style: solid; border-radius: 7px; border-width: 3px; border-color: rgb(180, 180, 180);")
        
        self.start.setText("START")
        self.root[1][0].text = str(1)
        self.root.set('Toggle', 'On/Off')


        
    # Error handling, go back to the login page
    def errorBack(self):
        self.stackedWidget.setCurrentIndex(2)

    # take you to the login page
    def beginLogin(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def insertPass(self, index):
        current = self.passEdit.text()
        self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(180, 180, 180); border-width:2px; border-radius: 7px;")
        #print str(len(current)) + index
        self.passEdit.setText(current + index)

    def logIn(self, root):
        self.lcdnum.display("00"+ ":"+ "00")
        current = self.passEdit.text()

        if not len(current) > 0:
            self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(255, 0, 0); border-width:2px; border-radius: 7px;")

        if len(current) == 4 and current == root[0][0].text:
            #print "correct password"
            self.stackedWidget.setCurrentIndex(2)
 
            if str(self.startSecs) == "60" and str(self.startmins) == "3":
                self.lcdnum.display("0"+"%s" % str(4) + ":0" + "%s" % str(0))
            else:
                self.lcdnum.display("0"+"%s" % str(self.startmins) + ":" + "%s" % str(self.startSecs))
            
                if self.startSecs <= 9:
                    self.lcdnum.display("0"+"%s" % str(self.startmins) + ":0" + "%s" % str(self.startSecs))
        else:
            self.passEdit.setText("")
            self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(255, 0, 0); border-width:2px; border-radius: 7px;")
        
    
    def clearText(self):
        self.passEdit.clear()

    # main op functions
    def lockBack(self):
        self.passEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    def updateLCD(self):

        if self.counter == 4:
            self.counter = 0
            self.timer.stop()
            self.startSecs = 60
            self.startmins = 3
            self.lcdnum.display("0"+"%s" % str(4) + ":0" + "%s" % str(0))
            subprocess.Popen(['killall', 'mpg321'])

            parse = ET.parse('cript.xml')
            root = parse.getroot()

            self.start.setStyleSheet("background-color: rgb(161, 255, 167); border-style: solid; border-radius: 7px; border-width: 3px; border-color: rgb(180, 180, 180);")
            self.start.setText("START")
            root[1][0].text = str(1)
            root.set('Toggle', 'On/Off')

            
        else:
            self.startSecs -= 1
            #print self.startSecs
            self.updateDet()


    def updateDet(self):
        self.lcdnum.display("0"+"%s" % str(self.startmins) + ":" + "%s" % str(self.startSecs))

        if self.startSecs == 0:
            self.counter += 1

            if self.startmins != 0:
                self.startmins -= 1
            
            self.startSecs = 60
            self.lcdnum.display("0"+"%s" % str(self.startmins) + ":" + "%s" % str(self.startSecs))
        
        if self.startSecs <= 9:
            self.lcdnum.display("0"+"%s" % str(self.startmins) + ":0" + "%s" % str(self.startSecs))



        # manipulate the relays and update xml file

        # at three minutes and 30 secs, turn relay one and relay 2 on
        if self.startmins == 3 and self.startSecs == 30:
            subprocess.call(['killall', 'mpg321'])

            try:
                subprocess.Popen(['mpg321', './MusicFiles/001.mp3'])
                print "Playing mp3 file 001.mp3"

            except IndexError:
                subprocess.Popen(['mpg321', './MusicFiles/%s' % self.mp3_files[x-1]])
                print "Playing mp3 file "

            # relay one on
            self.rone_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")

            # relay two on
            self.rtwo_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")
        
        # deactivate relay 2 after 5 seconds
        if self.startmins == 3 and self.startSecs == 25:
            self.rtwo_2.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")

        
        # after 3 mins turn relay 1 off
        if self.startmins == 0 and self.startSecs == 30:
            subprocess.call(['killall', 'mpg321'])

            try:
                subprocess.Popen(['mpg321', './MusicFiles/002.mp3'])
                print "Playing mp3 file 001.mp3"

            except IndexError:
                subprocess.Popen(['mpg321', './MusicFiles/%s' % self.mp3_files[x-1]])

            # deactivate relay 1
            self.rone_2.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")

            # activate relay 3
            self.rthree_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")


        # sfter 5 seconds turn relay 3 off
        if self.startmins == 0 and self.startSecs == 25:
            # relay three off
            self.rthree_2.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-radius: 4px; border-width: 2px; border-color: rgb(180, 180, 180);")


    def startBiz(self):
        # code for playing music +
        try:
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
                
                if len(self.mp3_files) == numMps:
                    self.stackedWidget.setCurrentIndex(3)
                    self.errorOccur.setText("An Error Occurred")
                    self.errorCode.setText("<b>Error Code</b>" + " :550")
                    self.realError.setText("Did not find any .mp3 files in the Musics Folder")
               
                else:
                    try:
                        self.t = True
                        self.songs = []

                        """for song_id in range(len(self.mp3_files)):
                            if song_id == 0 or song_id == 1 or song_id == 2:
                                pass
                            else:
                                self.songs.append(song_id)

                            song_id += 1

                        print len(self.songs)

                        x = random.randint(self.songs[0], len(self.songs))"""
                        while self.t:
                            x = random.randint(0, (len(self.mp3_files) -1) )

                            if self.mp3_files[x][:3] != "001" and self.mp3_files[x][:3] != '002' and self.mp3_files[x][:3] != '003':
                                self.t = False


                        subprocess.Popen(['mpg321', './MusicFiles/%s' % self.mp3_files[x]])
                        time.sleep(1)

                        self.start.setText("STOP")
                        self.start.setStyleSheet("background-color: rgb(255, 87, 90); border-style: solid; border-radius: 7px; border-width: 3px; border-color: rgb(180, 180, 180);")
                        root[1][0].text = str(0)
                        root.set('Toggle', 'On/Off')

                        # Start (Continue) with thhe timer
                        self.timer.start()


                    except IndexError:
                        subprocess.Popen(['mpg321', './MusicFiles/%s' % self.mp3_files[x-1]])
                        time.sleep(1)
                        print "Got and IndexError"

                
            else:
                self.stackedWidget.setCurrentIndex(3)
                self.errorOccur.setText("An Error Occurred")
                self.errorCode.setText("<b>Error Code</b>" + " :450")
                self.realError.setText("Error Parsing the xml file : Could not parse On/Off start state")

            parse.write('cript.xml')
        except OSError:
            self.stackedWidget.setCurrentIndex(3)
            self.errorOccur.setText("An Error Occurred")
            self.errorCode.setText("<b>Error Code</b>" + " :550")
            self.realError.setText("Did not find any .mp3 files in the Musics Folder")
        else:
            print "There are %s .mp3 files in the MusicFiles Directory" % len(self.mp3_files)
        
    
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
