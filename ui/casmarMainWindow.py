#!/usr/env/bin python
from PyQt5 import QtCore, QtGui, QtWidgets
from casmarloginWindow import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon.fromTheme("CasmarOdontologia")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLogoCasmar = QtWidgets.QLabel(self.centralwidget)
        self.lblLogoCasmar.setGeometry(QtCore.QRect(-10, 0, 811, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogoCasmar.sizePolicy().hasHeightForWidth())
        self.lblLogoCasmar.setSizePolicy(sizePolicy)
        self.lblLogoCasmar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblLogoCasmar.setText("")
        self.lblLogoCasmar.setPixmap(QtGui.QPixmap("Casmar_Login.png"))
        self.lblLogoCasmar.setScaledContents(True)
        self.lblLogoCasmar.setWordWrap(False)
        self.lblLogoCasmar.setOpenExternalLinks(False)
        self.lblLogoCasmar.setObjectName("lblLogoCasmar")
        self.n23Signature = QtWidgets.QLabel(self.centralwidget)
        self.n23Signature.setGeometry(QtCore.QRect(590, 550, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.n23Signature.setFont(font)
        self.n23Signature.setObjectName("n23Signature")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuStart = QtWidgets.QMenu(self.menubar)
        self.menuStart.setObjectName("menuStart")
        MainWindow.setMenuBar(self.menubar)

        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuStart.addAction(self.actionLogin)
        self.actionLogin.triggered.connect(self.call_login)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.system_exit)
        self.menuStart.addAction(self.actionExit)

        self.menubar.addAction(self.menuStart.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.n23Signature.setText(_translate("MainWindow", "Nx23 - Solucoes em Python"))
        self.menuStart.setTitle(_translate("MainWindow", "Inicio"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionLogin.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def call_login(self):
        self.new_window = QtWidgets.QMainWindow()
        self.login_window = Ui_LoginWindow()
        self.login_window.setupUi(self.new_window)
        self.new_window.show()
        MainWindow.hide()

    def system_exit(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
