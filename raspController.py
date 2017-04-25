import sys
import time
from PyQt4 import QtGui, QtCore
import rasp_controlsFinal
import xml.etree.ElementTree as ET


class passWord():
    def __init__(self, index):
        self.index = index

class controller(QtGui.QMainWindow, rasp_controlsFinal.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(2)

        #while True != False:
        #    print time.strftime("%H"+":"+"%M"+":"+"%S")
        self.lcdnum.display(time.strftime("%H"+":"+"%M"+":"+"%S"))

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        # parses the xml file
        parse = ET.parse('cript.xml')
        root = parse.getroot()
        stored = root[0][0].text

        states = []

        if len(root) == 4:
            for i in range(len(root)):
                states.append(root[i][0].text)
                i += 1
            print states
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

        # Login
        self.login.clicked.connect(lambda : self.logIn(root, states))

        self.clearpass.clicked.connect(lambda :  self.clearText())
        self.passEdit.setEnabled(False)
        self.passEdit.setEchoMode(2)
        self.passEdit.setMaxLength(4)
        self.passEdit.setText("")

        # main window ops
        self.lockback.clicked.connect(lambda : self.lockBack())

        self.start.clicked.connect(lambda : self.updateLCD())
        
        

    def beginLogin(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def insertPass(self, index):
        current = self.passEdit.text()
        self.passEdit.setStyleSheet("border-style: solid;	border-color: rgb(180, 180, 180); border-width:2px; border-radius: 7px;")
        print str(len(current)) + index
        self.passEdit.setText(current + index)

    def logIn(self, root, states):
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
        
        if states[1] == "1":
            self.rone_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: outset; border-radius: 6px;")

        if states[2] == "1":
            self.rtwo_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: outset; border-radius: 6px;")

        if states[3] == "1":
            self.rthree_2.setStyleSheet("background-color: rgb(85, 255, 127); border-style: outset; border-radius: 6px;")

    def clearText(self):
        self.passEdit.clear()

    # main op functions
    def lockBack(self):
        self.passEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    def updateLCD(self):
        mins = str(0)
        
        while True != False:
            self.lcdnum.display(time.strftime(":"+"%S"))
            time.sleep(0.2)
        
    
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
