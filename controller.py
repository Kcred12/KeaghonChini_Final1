from PyQt5 .QtWidgets import *
from view import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.menu_button.clicked.connect(lambda: self.open_menu())
        self.receipt_button.clicked.connect(lambda: self.show_receipt())


    def open_menu(self):
        self.main_menu_label.hide()
        self.menu_button.hide()
        self.receipt_button.hide()
        self.quit_button.hide()

    def show_receipt(self):
        self.menu_button.show()