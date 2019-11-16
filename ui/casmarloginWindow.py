from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(270, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(270, 130))
        LoginWindow.setMaximumSize(QtCore.QSize(270, 130))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(20, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.verify_login)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(150, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("lblusuario")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("lblsenha")
        self.lineUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUsuario.setGeometry(QtCore.QRect(80, 10, 161, 20))
        self.lineUsuario.setObjectName("lineUsuario")
        self.linePass = QtWidgets.QLineEdit(self.centralwidget)
        self.linePass.setGeometry(QtCore.QRect(80, 40, 161, 20))
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.btnLogin.setStatusTip(_translate("LoginWindow", "Clique para confirmar o login."))
        self.btnLogin.setWhatsThis(_translate("LoginWindow", "Botão para confirmar o login."))
        self.btnLogin.setText(_translate("LoginWindow", "Login"))
        self.btnCancel.setStatusTip(_translate("LoginWindow", "Clique para cancelar login."))
        self.btnCancel.setWhatsThis(_translate("LoginWindow", "Botão para cancelar."))
        self.btnCancel.setText(_translate("LoginWindow", "Cancelar"))
        self.label.setText(_translate("LoginWindow", "Usuário"))
        self.label_2.setText(_translate("LoginWindow", "Senha"))
        self.lineUsuario.setStatusTip(_translate("LoginWindow", "Digite seu usuario para login."))
        self.lineUsuario.setWhatsThis(_translate("LoginWindow", "campo para digitar usuario para login."))
        self.linePass.setStatusTip(_translate("LoginWindow", "Digite sua senha para login."))
        self.linePass.setWhatsThis(_translate("LoginWindow", "Campo para digitar sua senha para login."))

    def verify_login(self):
        user = self.lineUsuario.text()
        password = self.linePass.text()
        user_secret = "nx23"
        password_secret = "12345seis"
        msg = QMessageBox()
        msg.setWindowTitle("Verificando Login")
        if user == user_secret and password == password_secret:
            msg.setText("Acertou mizeravi")
        else:
            msg.setText("Erro animal")
        msg_box = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
