import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app=QApplication(sys.argv)
time=QTime.currentTime()
message="HAAAAAAAAAAAAAAAA"
label=QLabel("DAAAAAAAAAAAAAAA")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000,app.quit)
app.exec_()
