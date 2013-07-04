import sys
import serial
from PyQt4.QtCore import *
from PyQt4.QtGui import *
ser = serial.Serial("/dev/ttyUSB5", 9600, timeout=1)

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.browser=QTextBrowser()
		#self.lineedit=QLineEdit("Type an expression and press Enter")
		#self.lineedit.selectAll()
		layout=QVBoxLayout()
		layout.addWidget(self.browser)
		#layout.addWidget(self.lineedit)
		self.setLayout(layout)
		#self.lineedit.setFocus()
		#self.connect(self.lineedit,SIGNAL("returnPressed()"),self.updateUi)
		self.updateUi()
		self.browser.append("%s=<b>%s</b>"%(text,eval(text)))
		self.setWindowTitle("Calculate")

		
	def updateUi(self):
		try:
			ser.flushInput()
			text=ser.readline()
			self.browser.append("%s=<b>%s</b>"%(text,eval(text)))
		except:
			self.browser.append("<font color=red>%s is invalid!</font>"%text)

app=QApplication(sys.argv)
form=Form()
form.show()
app.exec_()

