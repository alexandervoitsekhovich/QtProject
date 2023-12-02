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
        self.NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
        super().__init__()
        uic.loadUi("eight.ui", self)
        self.setup_board()

    def setup_board(self):
        nums = self.NUMS
        self.button00.setText(random.choice(nums))
        del nums[nums.index(str(self.button00.text()))]
        self.button01.setText(random.choice(nums))
        del nums[nums.index(str(self.button01.text()))]
        self.button02.setText(random.choice(nums))
        del nums[nums.index(str(self.button02.text()))]
        self.button10.setText(random.choice(nums))
        del nums[nums.index(str(self.button10.text()))]
        self.button11.setText(random.choice(nums))
        del nums[nums.index(str(self.button11.text()))]
        self.button12.setText(random.choice(nums))
        del nums[nums.index(str(self.button12.text()))]
        self.button20.setText(random.choice(nums))
        del nums[nums.index(str(self.button20.text()))]
        self.button21.setText(random.choice(nums))
        del nums[nums.index(str(self.button21.text()))]
        self.button22.setText(random.choice(nums))
        del nums[nums.index(str(self.button22.text()))]


class Fifteen(QWidget):

    def __init__(self):
        self.NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", ""]
        super().__init__()
        uic.loadUi("fifteen.ui", self)
        self.setup_board()

    def setup_board(self):
        nums = self.NUMS
        self.button00.setText(random.choice(nums))
        del nums[nums.index(str(self.button00.text()))]
        self.button01.setText(random.choice(nums))
        del nums[nums.index(str(self.button01.text()))]
        self.button02.setText(random.choice(nums))
        del nums[nums.index(str(self.button02.text()))]
        self.button10.setText(random.choice(nums))
        del nums[nums.index(str(self.button10.text()))]
        self.button11.setText(random.choice(nums))
        del nums[nums.index(str(self.button11.text()))]
        self.button12.setText(random.choice(nums))
        del nums[nums.index(str(self.button12.text()))]
        self.button20.setText(random.choice(nums))
        del nums[nums.index(str(self.button20.text()))]
        self.button21.setText(random.choice(nums))
        del nums[nums.index(str(self.button21.text()))]
        self.button22.setText(random.choice(nums))
        del nums[nums.index(str(self.button22.text()))]
        self.button30.setText(random.choice(nums))
        del nums[nums.index(str(self.button30.text()))]
        self.button31.setText(random.choice(nums))
        del nums[nums.index(str(self.button31.text()))]
        self.button32.setText(random.choice(nums))
        del nums[nums.index(str(self.button32.text()))]
        self.button33.setText(random.choice(nums))
        del nums[nums.index(str(self.button33.text()))]
        self.button23.setText(random.choice(nums))
        del nums[nums.index(str(self.button23.text()))]
        self.button13.setText(random.choice(nums))
        del nums[nums.index(str(self.button13.text()))]
        self.button03.setText(random.choice(nums))
        del nums[nums.index(str(self.button03.text()))]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
