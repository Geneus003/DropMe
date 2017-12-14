from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import (QPixmap, QFont, QMouseEvent)
from PyQt5.QtCore import (Qt, QEvent, pyqtSignal, QCoreApplication)
import sys

app = QApplication(sys.argv)
root = QWidget()
name_event = pyqtSignal()


class RegisterScreenVar:

    def __init__(self):

        self.drop_logo = QLabel(root)
        self.drop_png = QPixmap("images/DropMeLogo.png")
        self.login_but = QLabel(root)
        self.login_but_img = QPixmap("images/Login_but.png")
        self.login_lab = QLabel('Login', root)
        self.pas_lab = QLabel('Password', root)
        self.login_box = QLineEdit(root)
        self.reg_box = QLineEdit(root)
        self.new_account = QLabel("Don't have an account?", root)
        self.new_word = ""
        # self.presss()

    def presss(self):
        btn = QPushButton("Print", root)
        btn.clicked.connect(self.printtt)
        btn.resize(100, 100)
        btn.move(600, 600)

    def printtt(self):
        print("hello")


reg_screen_var = RegisterScreenVar()


def drop_me():

    def register_screen(reg_screen_var, root, app):
        # design of register screen

        root.resize(1280, 720)
        root.move(400, 200)
        root.setWindowTitle('Drop_Me')
        root.setStyleSheet('background-image: url(images/reg_back.png);')

        reg_screen_var.login_but.setPixmap(reg_screen_var.login_but_img)
        reg_screen_var.login_but.setAttribute(Qt.WA_TranslucentBackground, True)
        reg_screen_var.login_but.move(520, 500)

        reg_screen_var.drop_logo.setPixmap(reg_screen_var.drop_png)
        reg_screen_var.drop_logo.setAttribute(Qt.WA_TranslucentBackground, True)
        reg_screen_var.drop_logo.move(370, 0)

        reg_screen_var.login_lab.setFont(QFont("OpenSans-Regular", 20, QFont.Bold))
        reg_screen_var.login_lab.setStyleSheet('QLabel {color: #F6F6F6}')
        reg_screen_var.login_lab.setAttribute(Qt.WA_TranslucentBackground, True)
        reg_screen_var.login_lab.move(580, 230)

        reg_screen_var.pas_lab.setFont(QFont("OpenSans-Regular", 20, QFont.Bold))
        reg_screen_var.pas_lab.setStyleSheet('QLabel {color: #F6F6F6}')
        reg_screen_var.pas_lab.setAttribute(Qt.WA_TranslucentBackground, True)
        reg_screen_var.pas_lab.move(550, 350)

        reg_screen_var.login_box.setFont(QFont("OpenSans-Regular", 18, QFont.Bold))
        reg_screen_var.login_box.setStyleSheet('QLineEdit {color:black; width: 300px}')
        reg_screen_var.login_box.move(470, 290)

        reg_screen_var.reg_box.setFont(QFont("OpenSans-Regular", 18, QFont.Bold))
        reg_screen_var.reg_box.setStyleSheet('QLineEdit {color:black; width: 300px}')
        reg_screen_var.reg_box.move(470, 400)

        reg_screen_var.new_account.setAttribute(Qt.WA_TranslucentBackground, True)
        reg_screen_var.new_account.setStyleSheet("QLabel {color: #F6F6F6}")
        reg_screen_var.new_account.setFont(QFont("OpenSans-Regular", 10, QFont.Bold))
        reg_screen_var.new_account.move(540, 620)

        root.show()

        sys.exit(app.exec_())

    register_screen(reg_screen_var, root, app)

drop_me()
