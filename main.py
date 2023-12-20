import random
import sys
import numpy as np
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QEvent, QObject, QPoint
from PyQt5.QtWidgets import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def answ_check(game_mode, user_answ):
    if bool(game_mode):
        answ_arr = np.array(range(9))
        answ_arr = answ_arr.reshape(3, 3)
        if answ_arr == user_answ:
            return True
        else:
            return False
    else:
        answ_arr = np.array(range(16))
        answ_arr = answ_arr.reshape(4, 4)
        if answ_arr == user_answ:
            return True
        else:
            return False


class StartPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("startPage.ui", self)
        self.startButton.clicked.connect(self.run_dialogue)
        self.timeModeButton.toggled.connect(self.time_mode)
        self.resultsButton.clicked.connect(self.show_results)

    def time_mode(self):
        if self.timeModeButton.isChecked():
            ...
        else:
            ...

    def show_results(self):
        ...

    def run_eight(self):
        self.window_eight = Eight()
        self.window_eight.show()
        helper = MouseHelper(self.window_eight.windowHandle())
        helper.pressed.connect(lambda point: self.window_eight.change_board(point.x(), point.y()))

    def run_fifteen(self):
        self.window_fifteen = Fifteen()
        self.window_fifteen.show()
        helper = MouseHelper(self.window_fifteen.windowHandle())
        helper.pressed.connect(lambda point: self.window_fifteen.change_board(point.x(), point.y()))

    def run_dialogue(self):
        game_mode, ok_pressed = QInputDialog.getItem(self, "Выберите режим", "Выбор режима",
                                                     ("16 клеток", "8 клеток"), 1, False)
        if ok_pressed:
            if game_mode == "8 клеток":
                self.run_eight()
            else:
                self.run_fifteen()


class MouseHelper(QObject):
    pressed = pyqtSignal(QPoint)
    released = pyqtSignal(QPoint)

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self.window.installEventFilter(self)

    @property
    def window(self):
        return self._window

    def eventFilter(self, obj, event):
        if self.window is obj:
            if event.type() == QEvent.MouseButtonPress:
                self.pressed.emit(event.pos())
            elif event.type() == QEvent.MouseButtonRelease:
                self.released.emit(event.pos())
        return super().eventFilter(obj, event)


class Eight(QWidget):
    def __init__(self):
        self.NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
        super().__init__()
        uic.loadUi("eight.ui", self)
        self.setup_board()

    def setup_board(self):
        nums = self.NUMS
        board = np.zeros(9, dtype=np.int32).reshape(3, 3)
        self.button00.setText(random.choice(nums))
        board[0, 0] = int(self.button00.text()) if self.button00.text() != "" else 0
        del nums[nums.index(str(self.button00.text()))]
        self.button01.setText(random.choice(nums))
        board[0, 1] = int(self.button01.text()) if self.button01.text() != "" else 0
        del nums[nums.index(str(self.button01.text()))]
        self.button02.setText(random.choice(nums))
        board[0, 2] = int(self.button02.text()) if self.button02.text() != "" else 0
        del nums[nums.index(str(self.button02.text()))]
        self.button10.setText(random.choice(nums))
        board[1, 0] = int(self.button10.text()) if self.button10.text() != "" else 0
        del nums[nums.index(str(self.button10.text()))]
        self.button11.setText(random.choice(nums))
        board[1, 1] = int(self.button11.text()) if self.button11.text() != "" else 0
        del nums[nums.index(str(self.button11.text()))]
        self.button12.setText(random.choice(nums))
        board[1, 2] = int(self.button12.text()) if self.button12.text() != "" else 0
        del nums[nums.index(str(self.button12.text()))]
        self.button20.setText(random.choice(nums))
        board[2, 0] = int(self.button20.text()) if self.button20.text() != "" else 0
        del nums[nums.index(str(self.button20.text()))]
        self.button21.setText(random.choice(nums))
        board[2, 1] = int(self.button21.text()) if self.button21.text() != "" else 0
        del nums[nums.index(str(self.button21.text()))]
        self.button22.setText(random.choice(nums))
        board[2, 2] = int(self.button22.text()) if self.button22.text() != "" else 0
        del nums[nums.index(str(self.button22.text()))]

    def change_board(self, x, y):
        print(x, y)


class Fifteen(QWidget):

    def __init__(self):
        self.NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", ""]
        super().__init__()
        uic.loadUi("fifteen.ui", self)
        self.setup_board()

    def setup_board(self):
        nums = self.NUMS
        self.board = np.zeros(16, dtype=np.int32).reshape(4, 4)
        self.button00.setText(random.choice(nums))
        self.board[0, 0] = int(self.button00.text()) if self.button00.text() != "" else 0
        del nums[nums.index(str(self.button00.text()))]
        self.button01.setText(random.choice(nums))
        self.board[0, 1] = int(self.button01.text()) if self.button01.text() != "" else 0
        del nums[nums.index(str(self.button01.text()))]
        self.button02.setText(random.choice(nums))
        self.board[0, 2] = int(self.button02.text()) if self.button02.text() != "" else 0
        del nums[nums.index(str(self.button02.text()))]
        self.button10.setText(random.choice(nums))
        self.board[1, 0] = int(self.button10.text()) if self.button10.text() != "" else 0
        del nums[nums.index(str(self.button10.text()))]
        self.button11.setText(random.choice(nums))
        self.board[1, 1] = int(self.button11.text()) if self.button11.text() != "" else 0
        del nums[nums.index(str(self.button11.text()))]
        self.button12.setText(random.choice(nums))
        self.board[1, 2] = int(self.button12.text()) if self.button12.text() != "" else 0
        del nums[nums.index(str(self.button12.text()))]
        self.button20.setText(random.choice(nums))
        self.board[2, 0] = int(self.button20.text()) if self.button20.text() != "" else 0
        del nums[nums.index(str(self.button20.text()))]
        self.button21.setText(random.choice(nums))
        self.board[2, 1] = int(self.button21.text()) if self.button21.text() != "" else 0
        del nums[nums.index(str(self.button21.text()))]
        self.button22.setText(random.choice(nums))
        self.board[2, 2] = int(self.button22.text()) if self.button22.text() != "" else 0
        del nums[nums.index(str(self.button22.text()))]
        self.button30.setText(random.choice(nums))
        self.board[3, 0] = int(self.button30.text()) if self.button30.text() != "" else 0
        del nums[nums.index(str(self.button30.text()))]
        self.button31.setText(random.choice(nums))
        self.board[3, 1] = int(self.button31.text()) if self.button31.text() != "" else 0
        del nums[nums.index(str(self.button31.text()))]
        self.button32.setText(random.choice(nums))
        self.board[3, 2] = int(self.button32.text()) if self.button32.text() != "" else 0
        del nums[nums.index(str(self.button32.text()))]
        self.button33.setText(random.choice(nums))
        self.board[3, 3] = int(self.button33.text()) if self.button33.text() != "" else 0
        del nums[nums.index(str(self.button33.text()))]
        self.button23.setText(random.choice(nums))
        self.board[2, 3] = int(self.button23.text()) if self.button23.text() != "" else 0
        del nums[nums.index(str(self.button23.text()))]
        self.button13.setText(random.choice(nums))
        self.board[1, 3] = int(self.button13.text()) if self.button13.text() != "" else 0
        del nums[nums.index(str(self.button13.text()))]
        self.button03.setText(random.choice(nums))
        self.board[0, 3] = int(self.button03.text()) if self.button03.text() != "" else 0
        del nums[nums.index(str(self.button03.text()))]

    def change_board(self, x, y):
        if x in range(20, 101) and y in range(20, 135):
            move = self.move_button()
            if move == "Down":
                txt = self.button10.text()
                self.button10.setText(self.button00.text())
                self.button00.setText(txt)
                self.board[0, 0], self.board[1, 0] = self.board[1, 0], self.board[0, 0]
            elif move == "Right":
                txt = self.button01.text()
                self.button01.setText(self.button00.text())
                self.button00.setText(txt)
                self.board[0, 0], self.board[0, 1] = self.board[0, 1], self.board[0, 0]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(147, 255) and y in range(20, 135):
            move = self.move_button()
            if move == "Down":
                txt = self.button11.text()
                self.button11.setText(self.button01.text())
                self.button01.setText(txt)
                self.board[0, 1], self.board[1, 1] = self.board[1, 1], self.board[0, 1]
            elif move == "Right":
                txt = self.button02.text()
                self.button02.setText(self.button01.text())
                self.button01.setText(txt)
                self.board[0, 2], self.board[0, 1] = self.board[0, 1], self.board[0, 2]
            elif move == "Left":
                txt = self.button00.text()
                self.button00.setText(self.button01.text())
                self.button01.setText(txt)
                self.board[0, 0], self.board[0, 1] = self.board[0, 1], self.board[0, 0]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()

    def move_button(self):
        move, ok_pressed = QInputDialog.getItem(
            self, "Выберите действие", "Ваше действие?",
            ("Up", "Down", "Left", "Right"), 1, False)
        if ok_pressed:
            return move


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
