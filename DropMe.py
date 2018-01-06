from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtCore import (Qt, QSize)
import sys

app = QApplication(sys.argv)
root = QWidget()
wind = 1


def check_log(event):
    log_screen_var.__anext__()
    drop_me(2)


def new_acc_fun(event):
    log_screen_var.__anext__()
    drop_me(3)


class LoginScreenVar():

    def __init__(self):

        self.drop_logo = QLabel(root)
        self.drop_png = QPixmap("images/DropMeLogo.png")
        self.login_but = QLabel(root)
        self.login_but_img = QPixmap("images/Login_but.png")
        self.account_hint_img = QPixmap("images/account-hint.png")
        self.login_lab = QLabel('Login', root)
        self.pas_lab = QLabel('Password', root)
        self.login_box = QLineEdit(root)
        self.reg_box = QLineEdit(root)
        self.new_account = QLabel("Don't have an account?", root)

        self.initui()

    def initui(self):

        self.new_account.mousePressEvent = new_acc_fun
        self.login_but.mousePressEvent = check_log

    def __anext__(self):

        self.new_account.deleteLater()
        self.drop_logo.deleteLater()
        self.login_box.deleteLater()
        self.login_but.deleteLater()
        self.login_lab.deleteLater()
        self.pas_lab.deleteLater()
        self.reg_box.deleteLater()


class RegisterScreenVar():

    def __init__(self):

        self.register_lab = QLabel("Register")


log_screen_var = LoginScreenVar()
reg_screen_var = RegisterScreenVar()


def drop_me(wind):

    def check_acc_ser():
        print("loading")

    def register_screen(reg_screen_war, root):

        reg_screen_var.register_lab.move(100, 100)

    def login_screen(log_screen_var, root):
        # design of register screen

        root.resize(1280, 720)
        root.move(400, 200)
        root.setWindowTitle('Drop_Me')
        root.setStyleSheet('background-image: url(images/reg_back.png);')

        log_screen_var.login_but.setPixmap(log_screen_var.login_but_img)
        log_screen_var.login_but.setAttribute(Qt.WA_TranslucentBackground, True)
        log_screen_var.login_but.move(520, 500)

        log_screen_var.drop_logo.setPixmap(log_screen_var.drop_png)
        log_screen_var.drop_logo.setAttribute(Qt.WA_TranslucentBackground, True)
        log_screen_var.drop_logo.move(370, 0)

        log_screen_var.login_lab.setFont(QFont("OpenSans-Regular", 20, QFont.Bold))
        log_screen_var.login_lab.setStyleSheet('QLabel {color: #F6F6F6}')
        log_screen_var.login_lab.setAttribute(Qt.WA_TranslucentBackground, True)
        log_screen_var.login_lab.move(580, 230)

        log_screen_var.pas_lab.setFont(QFont("OpenSans-Regular", 20, QFont.Bold))
        log_screen_var.pas_lab.setStyleSheet('QLabel {color: #F6F6F6}')
        log_screen_var.pas_lab.setAttribute(Qt.WA_TranslucentBackground, True)
        log_screen_var.pas_lab.move(550, 350)

        log_screen_var.login_box.setFont(QFont("OpenSans-Regular", 18, QFont.Bold))
        log_screen_var.login_box.setStyleSheet('QLineEdit {color:black; width: 300px}')
        log_screen_var.login_box.move(470, 290)

        log_screen_var.reg_box.setFont(QFont("OpenSans-Regular", 18, QFont.Bold))
        log_screen_var.reg_box.setStyleSheet('QLineEdit {color:black; width: 300px}')
        log_screen_var.reg_box.move(470, 400)

        log_screen_var.new_account.move(540, 600)
        log_screen_var.new_account.setAttribute(Qt.WA_TranslucentBackground, True)
        log_screen_var.new_account.setPixmap(log_screen_var.account_hint_img)

    if wind == 1:
        login_screen(log_screen_var, root)

    elif wind == 2:
        register_screen(reg_screen_var, root)

    elif wind == 3:
        check_acc_ser()

    root.show()


drop_me(wind)

sys.exit(app.exec_())
