from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
root = QWidget()


class RegisterScreenVar:

    def __init__(self):

        self.reg_button = QPushButton('Register', root)

reg_screen_var = RegisterScreenVar()


def drop_me(reg_screen_var, root, app):

    def register_screen():

        root.resize(1080, 720)
        root.move(400, 200)
        root.setWindowTitle('Drop_Me')

        reg_screen_var.reg_button.setCheckable(True)
        reg_screen_var.reg_button.move(100, 100)
        reg_screen_var.reg_button.setStyleSheet(root, {background-color = "red"})

        root.show()

        sys.exit(app.exec_())

    register_screen()

drop_me(reg_screen_var, root, app)
