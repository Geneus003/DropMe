from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QLabel)
from PyQt5.QtGui import (QImage, QPalette, QBrush, QPixmap)
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
root = QWidget()


class RegisterScreenVar:

    def __init__(self):

        self.reg_button = QPushButton('Register', root)
        self.drop_logo = QLabel(root)
        self.drop_png = QPixmap("images/DropmeLogo.png")
        self.login_lab = QLabel('Login',root)


reg_screen_var = RegisterScreenVar()


def drop_me(reg_screen_var, root, app):

    def register_screen():

        root.resize(1080, 720)
        root.move(400, 200)
        root.setWindowTitle('Drop_Me')
        root.setStyleSheet('background-color:#529AB9;')

        reg_screen_var.reg_button.setCheckable(True)
        reg_screen_var.reg_button.move(100, 100)
        reg_screen_var.reg_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;height:50px ; width:50px;}')

        reg_screen_var.drop_logo.setPixmap(reg_screen_var.drop_png)
        reg_screen_var.drop_logo.move(280, 0)

        reg_screen_var.login_lab.setStyleSheet('QLabel {background-color: red}')
        reg_screen_var.login_lab.move(300, 200)




        root.show()

        sys.exit(app.exec_())

    register_screen()

drop_me(reg_screen_var, root, app)
