#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#A1695618-Converted
import sys, os
from PyQt4 import QtCore, QtGui
import threading
import time


class PbWidget(QtGui.QProgressBar):
	def __init__(self, parent=None, total=20):
		super(PbWidget, self).__init__()
		self.setMinimum(1)
		self.setMaximum(total)        
		self._active = False  

	def update_bar(self, to_add_number):
		while True:
			time.sleep(0.01)
			value = self.value() + to_add_number            
			self.setValue(value)
			QtGui.qApp.processEvents()
			if (not self._active or value >= self.maximum()):                
				break
		self._active = False

	def closeEvent(self, event):
		self._active = False

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.myList = ['One','Two','Three','Four','Five','Six','Seven']

		self.main_layout = QtGui.QVBoxLayout()
		self.pBars={}

		for each in self.myList:
			pb=PbWidget(total=101)
			self.main_layout.addWidget(pb)
			self.pBars[each]={'pb':pb, 'name':each, 'value': 0} 

		ok_button = QtGui.QPushButton("Distribute")
		ok_button.clicked.connect(self.OK)      
		self.main_layout.addWidget(ok_button)       

		central_widget = QtGui.QWidget()
		central_widget.setLayout(self.main_layout)
		self.setCentralWidget(central_widget)


	def internalFunc(self, myEvent, each):

		pb = self.pBars[each]['pb']

		state=True
		while state:
			if self.pBars[each]['value']>=100: state=False
			for i in range(12):
				self.pBars[each]['value']+=10
				print('\n\t ...Working on', each, self.pBars[each]['value'], '\n')
				# pb.update_bar( self.pBars[each]['value'])
				time.sleep(0.5)

		print("\n\t ProgressBar", each, 'has reached 100%. Its value =', self.pBars[each]['value'], '\n')


	def OK(self):
		for each in self.pBars:
			self.myEvent=threading.Event()
			self.c_thread=threading.Thread(target=self.internalFunc, args=(self.myEvent, each,))
			self.c_thread.start() 


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.resize(480, 320)
	window.show()
	sys.exit(app.exec_())


pb.update_bar( self.pBars[each]['value'])