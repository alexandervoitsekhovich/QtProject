from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication
from PyQt5.QtWidgets import QInputDialog
import sys
import random


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class StartPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("startPage.ui", self)
        self.startButton.clicked.connect(self.run_dialogue)
        self.window_eight = Eight()
        self.window_fifteen = Fifteen()

    def run_dialogue(self):
        game_mode, ok_pressed = QInputDialog.getItem(self, "Выберите режим", "Выбор режима",
                                                     ("16 клеток", "8 клеток"), 1, False)
        if ok_pressed:
            if game_mode == "8 клеток":
                self.window_eight.show()
            else:
                self.window_fifteen.show()


class Eight(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("eight.ui", self)


class Fifteen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("fifteen.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
