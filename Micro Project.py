import PyQt5
import psutil
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

for proc in psutil.process_iter():
         try:
             # Get process name & pid from process object.
             processName = proc.name()
             pid = proc.pid
             print(processName , ' ::: ', pid)
         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs '
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getInteger()

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer","PID:", 0, 0,99999 , 1)
        if okPressed:
            p = psutil.Process(i)
            p.kill()
            exit() 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
