import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("media/pylogo.png"))
        self.setWindowTitle("Bem-vindo ao PyCasmar! - Favor Realizar Login")
        self.setGeometry(200, 200, 800, 600)
        self.login_attempts = 3
        self.ui()

    # Create the User Interface
    def ui(self):
        # Create and configure a label to display the Program Name
        self.lbl_program_name = QLabel("PyCasmar", self)
        self.lbl_program_name.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.lbl_program_name.move(320, 170)
        # Create and configure the user text box
        self.user_text_box = QLineEdit(self)
        self.user_text_box.setPlaceholderText("Digite o seu usuario")
        self.user_text_box.move(300, 220)
        # Create and configure the password text box
        self.password_text_box = QLineEdit(self)
        self.password_text_box.setPlaceholderText("Digite o seu usuario")
        # Set echo of the password to hide the information
        self.password_text_box.setEchoMode(QLineEdit.Password)
        self.password_text_box.move(300, 250)
        # Create and configure the Login Button
        btn_login = QPushButton("Login", self)
        btn_login.move(330, 300)
        # When the button is clicked, call check_values
        btn_login.clicked.connect(self.check_values)
        # Create and configure a label to display a message to the user asking for the login
        self.lbl_msg = QLabel("Aguardando autenticação", self)
        self.lbl_msg.move(310, 325)
        self.lbl_msg2 = QLabel(self)
        self.lbl_msg2.move(310, 325)

    def check_values(self):
        # Get user and password text
        user = self.user_text_box.text()
        password = self.password_text_box.text()
        ############################################################################
        # %!TEMP!% THIS SHOULD BE REMOVED FOR A REAL USER REGISTRATION INFORMATION
        # THIS FILE IS ONLY FOR TEST PURPOSE
        ############################################################################
        with open("user_registration/user_registration.csv") as csv_file:
            content = pd.read_csv(csv_file, delimiter=',')
            # Check if the user exist in the file
            if True in content['user'].isin([user]):
                # If it does then look for the corresponding password and compare to the password text box value
                if content[content['user'] == user]['pass'].to_string(index=False).strip() == password:
                    allow = True
                else:
                    allow = False
            else:
                allow = False
        # When allowed the tittle screen should change to the user tag
        if allow:
            self.setWindowTitle("Bem-vindo ao PyAtena! - {}".format(user))
            # In here we change to the real program window
            
        # If not allowed the lbl_msg then change to display a error message.
        else:
            self.login_attempts -= 1
            self.lbl_msg.setText("Usuario ou Senha Incorretos.")
            self.lbl_msg.adjustSize()
            self.lbl_msg.move(300, 325)
            self.lbl_msg2.setText("{} tentativas restantes.".format(self.login_attempts))
            self.lbl_msg2.adjustSize()
            self.lbl_msg2.move(300, 355)
        
        if self.login_attempts == 0:
            sys.exit()

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__" :
    main()
