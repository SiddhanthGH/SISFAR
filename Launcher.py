from PyQt5 import QtCore, QtGui, QtWidgets
import math
import sys
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SISFAR")
        MainWindow.resize(386, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(144, 390, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.simulate)
        self.M = QtWidgets.QTextEdit(self.centralwidget)
        self.M.setGeometry(QtCore.QRect(180, 90, 104, 21))
        self.M.setObjectName("M")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(99, 90, 81, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.C = QtWidgets.QTextEdit(self.centralwidget)
        self.C.setGeometry(QtCore.QRect(180, 120, 104, 21))
        self.C.setObjectName("C")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(89, 120, 91, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(99, 180, 81, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.A = QtWidgets.QTextEdit(self.centralwidget)
        self.A.setGeometry(QtCore.QRect(180, 150, 104, 21))
        self.A.setObjectName("A")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(99, 150, 81, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.L = QtWidgets.QTextEdit(self.centralwidget)
        self.L.setGeometry(QtCore.QRect(180, 180, 104, 21))
        self.L.setObjectName("L")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(99, 240, 81, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.h = QtWidgets.QTextEdit(self.centralwidget)
        self.h.setGeometry(QtCore.QRect(180, 210, 104, 21))
        self.h.setObjectName("h")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(99, 210, 81, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gam = QtWidgets.QTextEdit(self.centralwidget)
        self.gam.setGeometry(QtCore.QRect(180, 270, 104, 21))
        self.gam.setObjectName("gam")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(99, 270, 81, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.v = QtWidgets.QTextEdit(self.centralwidget)
        self.v.setGeometry(QtCore.QRect(180, 240, 104, 21))
        self.v.setObjectName("v")
        self.At = QtWidgets.QCheckBox(self.centralwidget)
        self.At.setGeometry(QtCore.QRect(20, 320, 121, 21))
        self.At.setObjectName("At")
        self.Act = QtWidgets.QCheckBox(self.centralwidget)
        self.Act.setGeometry(QtCore.QRect(20, 340, 121, 21))
        self.Act.setObjectName("Act")
        self.Vt = QtWidgets.QCheckBox(self.centralwidget)
        self.Vt.setGeometry(QtCore.QRect(140, 320, 101, 21))
        self.Vt.setObjectName("Vt")
        self.ht = QtWidgets.QCheckBox(self.centralwidget)
        self.ht.setGeometry(QtCore.QRect(140, 340, 101, 21))
        self.ht.setObjectName("ht")
        self.rant = QtWidgets.QCheckBox(self.centralwidget)
        self.rant.setGeometry(QtCore.QRect(240, 320, 121, 21))
        self.rant.setObjectName("rant")
        self.rana = QtWidgets.QCheckBox(self.centralwidget)
        self.rana.setGeometry(QtCore.QRect(240, 340, 131, 21))
        self.rana.setObjectName("rana")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(137, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 21))
        self.menubar.setObjectName("menubar")
        self.menuEarth = QtWidgets.QMenu(self.menubar)
        self.menuEarth.setObjectName("menuEarth")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEarth.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SISFAR", "SISFAR"))
        self.pushButton.setText(_translate("MainWindow", "Simulate"))
        self.lineEdit.setText(_translate("MainWindow", "Mass of craft:"))
        self.lineEdit_2.setText(_translate("MainWindow", "Drag Coefficient:"))
        self.lineEdit_3.setText(_translate("MainWindow", "Lift Coefficient:"))
        self.lineEdit_4.setText(_translate("MainWindow", "Surface Area:"))
        self.lineEdit_5.setText(_translate("MainWindow", "Initial Velocity:"))
        self.lineEdit_6.setText(_translate("MainWindow", "Initial Altitude:"))
        self.lineEdit_8.setText(_translate("MainWindow", "Initial Angle:"))
        self.At.setText(_translate("MainWindow", "All v Time"))
        self.Act.setText(_translate("MainWindow", "Acceleration v Time"))
        self.Vt.setText(_translate("MainWindow", "Velocity v Time"))
        self.ht.setText(_translate("MainWindow", "Altitude v Time"))
        self.rant.setText(_translate("MainWindow", "Downrange v Time"))
        self.rana.setText(_translate("MainWindow", "Downrange v Altitude"))
        self.label.setText(_translate("MainWindow", "SISFAR"))
        self.menuEarth.setTitle(_translate("MainWindow", "Earth"))
#Once Button Pressed
    def simulate(self):
        import SIScript as sis 
        sis.Simulation(self)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())