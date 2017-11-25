
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class main_window(QWidget):
	def __init__(self):
		super(main_window,self).__init__()
		self.init_ui()

	def init_ui(self):
		self.show()

def main():
	pyqt_app=QApplication(sys.argv)
	_=main_window()
	sys.exit(pyqt_app.exec_())

if __name__ == '__main__':
	main()