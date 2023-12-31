import random
import sys
import numpy as np
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QEvent, QObject, QPoint
from PyQt5.QtWidgets import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Win(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("win.ui", self)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.hide()


class Lose(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("lose.ui", self)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.hide()


class StartPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("startPage.ui", self)
        self.startButton.clicked.connect(self.run_dialogue)

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
        self.board = np.zeros(9, dtype=np.int32).reshape(3, 3)
        super().__init__()
        uic.loadUi("eight.ui", self)
        self.setup_board()

    def setup_board(self):
        nums = self.NUMS
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
        self.check_button.clicked.connect(lambda: self.answ_check(self.board))

    def answ_check(self, user_answ):
        self.answ_arr = np.array(range(9))
        self.answ_arr = self.answ_arr.reshape(3, 3)
        if np.array_equal(self.answ_arr, user_answ):
            self.win_screen = Win()
            self.win_screen.show()
        else:
            self.lost_screen = Lose()
            self.lost_screen.show()

    def change_board(self, x, y):
        if x in range(20, 128) and y in range(20, 135):
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
        elif x in range(274, 382) and y in range(20, 135):
            move = self.move_button()
            if move == "Down":
                txt = self.button12.text()
                self.button12.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[1, 2] = self.board[1, 2], self.board[0, 2]
            elif move == "Left":
                txt = self.button01.text()
                self.button01.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[0, 1] = self.board[0, 1], self.board[0, 2]
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
        elif x in range(20, 128) and y in range(154, 268):
            move = self.move_button()
            if move == "Up":
                txt = self.button10.text()
                self.button10.setText(self.button00.text())
                self.button00.setText(txt)
                self.board[0, 0], self.board[1, 0] = self.board[1, 0], self.board[0, 0]
            elif move == "Down":
                txt = self.button10.text()
                self.button10.setText(self.button20.text())
                self.button10.setText(txt)
                self.board[2, 0], self.board[1, 0] = self.board[1, 0], self.board[2, 0]
            elif move == "Right":
                txt = self.button10.text()
                self.button10.setText(self.button11.text())
                self.button11.setText(txt)
                self.board[1, 1], self.board[1, 0] = self.board[1, 0], self.board[1, 1]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(147, 255) and y in range(154, 268):
            move = self.move_button()
            if move == "Up":
                txt = self.button11.text()
                self.button11.setText(self.button01.text())
                self.button01.setText(txt)
                self.board[0, 1], self.board[1, 1] = self.board[1, 1], self.board[0, 1]
            elif move == "Down":
                txt = self.button11.text()
                self.button11.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 1], self.board[1, 1] = self.board[1, 1], self.board[2, 1]
            elif move == "Right":
                txt = self.button11.text()
                self.button11.setText(self.button12.text())
                self.button12.setText(txt)
                self.board[1, 2], self.board[1, 1] = self.board[1, 1], self.board[1, 2]
            else:
                txt = self.button11.text()
                self.button11.setText(self.button10.text())
                self.button10.setText(txt)
                self.board[1, 0], self.board[1, 1] = self.board[1, 1], self.board[1, 0]
        elif x in range(274, 382) and y in range(154, 268):
            move = self.move_button()
            if move == "Up":
                txt = self.button12.text()
                self.button12.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[1, 2] = self.board[1, 2], self.board[0, 2]
            elif move == "Down":
                txt = self.button12.text()
                self.button12.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[1, 2] = self.board[1, 2], self.board[2, 2]
            elif move == "Left":
                txt = self.button12.text()
                self.button12.setText(self.button11.text())
                self.button11.setText(txt)
                self.board[1, 2], self.board[1, 1] = self.board[1, 1], self.board[1, 1]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(20, 128) and y in range(287, 401):
            move = self.move_button()
            if move == "Right":
                txt = self.button21.text()
                self.button21.setText(self.button20.text())
                self.button20.setText(txt)
                self.board[2, 1], self.board[2, 0] = self.board[2, 0], self.board[2, 1]
            elif move == "Up":
                txt = self.button21.text()
                self.button21.setText(self.button11.text())
                self.button11.setText(txt)
                self.board[2, 1], self.board[1, 1] = self.board[1, 1], self.board[2, 1]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(147, 255) and y in range(287, 401):
            move = self.move_button()
            if move == "Right":
                txt = self.button22.text()
                self.button22.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 2], self.board[2, 1] = self.board[2, 1], self.board[2, 2]
            elif move == "Left":
                txt = self.button20.text()
                self.button20.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 0], self.board[2, 1] = self.board[2, 1], self.board[2, 0]
            elif move == "Up":
                txt = self.button11.text()
                self.button11.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 2], self.board[1, 1] = self.board[1, 1], self.board[2, 2]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(274, 382) and y in range(287, 402):
            move = self.move_button()
            if move == "Up":
                txt = self.button12.text()
                self.button12.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[1, 2] = self.board[1, 2], self.board[2, 2]
            elif move == "Left":
                txt = self.button21.text()
                self.button21.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[2, 1] = self.board[2, 1], self.board[2, 2]
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
        self.check_button.clicked.connect(lambda: self.answ_check(self.board))

    def answ_check(self, user_answ):
        self.answ_arr = np.array(range(9))
        self.answ_arr = self.answ_arr.reshape(3, 3)
        if np.array_equal(self.answ_arr, user_answ):
            self.win_screen = Win()
            self.win_screen.show()
        else:
            self.lost_screen = Lose()
            self.lost_screen.show()

    def change_board(self, x, y):
        if x in range(20, 101) and y in range(20, 99):
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
        elif x in range(220, 301) and y in range(20, 99):
            move = self.move_button()
            if move == "Down":
                txt = self.button12.text()
                self.button12.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[1, 2] = self.board[1, 2], self.board[0, 2]
            elif move == "Right":
                txt = self.button03.text()
                self.button03.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[0, 3] = self.board[0, 3], self.board[0, 2]
            elif move == "Left":
                txt = self.button01.text()
                self.button01.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[0, 1] = self.board[0, 1], self.board[0, 2]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(120, 201) and y in range(20, 99):
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
        elif x in range(320, 401) and y in range(20, 99):
            move = self.move_button()
            if move == "Down":
                txt = self.button13.text()
                self.button13.setText(self.button03.text())
                self.button03.setText(txt)
                self.board[0, 3], self.board[1, 3] = self.board[1, 3], self.board[0, 3]
            elif move == "Left":
                txt = self.button02.text()
                self.button02.setText(self.button03.text())
                self.button03.setText(txt)
                self.board[0, 2], self.board[0, 3] = self.board[0, 3], self.board[0, 2]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(20, 101) and y in range(118, 196):
            move = self.move_button()
            if move == "Up":
                txt = self.button10.text()
                self.button10.setText(self.button00.text())
                self.button00.setText(txt)
                self.board[0, 0], self.board[1, 0] = self.board[1, 0], self.board[0, 0]
            elif move == "Down":
                txt = self.button10.text()
                self.button10.setText(self.button20.text())
                self.button10.setText(txt)
                self.board[2, 0], self.board[1, 0] = self.board[1, 0], self.board[2, 0]
            elif move == "Right":
                txt = self.button10.text()
                self.button10.setText(self.button11.text())
                self.button11.setText(txt)
                self.board[1, 1], self.board[1, 0] = self.board[1, 0], self.board[1, 1]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(120, 201) and y in range(118, 196):
            move = self.move_button()
            if move == "Up":
                txt = self.button11.text()
                self.button11.setText(self.button01.text())
                self.button01.setText(txt)
                self.board[0, 1], self.board[1, 1] = self.board[1, 1], self.board[0, 1]
            elif move == "Down":
                txt = self.button11.text()
                self.button11.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 1], self.board[1, 1] = self.board[1, 1], self.board[2, 1]
            elif move == "Right":
                txt = self.button11.text()
                self.button11.setText(self.button12.text())
                self.button12.setText(txt)
                self.board[1, 2], self.board[1, 1] = self.board[1, 1], self.board[1, 2]
            else:
                txt = self.button11.text()
                self.button11.setText(self.button10.text())
                self.button10.setText(txt)
                self.board[1, 0], self.board[1, 1] = self.board[1, 1], self.board[1, 0]
        elif x in range(220, 301) and y in range(118, 196):
            move = self.move_button()
            if move == "Up":
                txt = self.button12.text()
                self.button12.setText(self.button02.text())
                self.button02.setText(txt)
                self.board[0, 2], self.board[1, 2] = self.board[1, 2], self.board[0, 2]
            elif move == "Down":
                txt = self.button12.text()
                self.button12.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[1, 2] = self.board[1, 2], self.board[2, 2]
            elif move == "Right":
                txt = self.button12.text()
                self.button12.setText(self.button13.text())
                self.button13.setText(txt)
                self.board[1, 3], self.board[1, 2] = self.board[1, 2], self.board[1, 3]
            else:
                txt = self.button12.text()
                self.button12.setText(self.button11.text())
                self.button11.setText(txt)
                self.board[1, 2], self.board[1, 1] = self.board[1, 1], self.board[1, 1]
        elif x in range(320, 401) and y in range(118, 196):
            move = self.move_button()
            if move == "Up":
                txt = self.button13.text()
                self.button13.setText(self.button03.text())
                self.button03.setText(txt)
                self.board[0, 3], self.board[1, 3] = self.board[1, 3], self.board[0, 3]
            elif move == "Down":
                txt = self.button13.text()
                self.button13.setText(self.button23.text())
                self.button23.setText(txt)
                self.board[2, 3], self.board[1, 3] = self.board[1, 3], self.board[2, 3]
            elif move == "Left":
                txt = self.button13.text()
                self.button13.setText(self.button12.text())
                self.button12.setText(txt)
                self.board[1, 2], self.board[1, 3] = self.board[1, 3], self.board[1, 2]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(20, 101) and y in range(216, 294):
            move = self.move_button()
            if move == "Down":
                txt = self.button20.text()
                self.button20.setText(self.button30.text())
                self.button30.setText(txt)
                self.board[2, 0], self.board[3, 0] = self.board[3, 0], self.board[2, 0]
            elif move == "Right":
                txt = self.button21.text()
                self.button21.setText(self.button20.text())
                self.button20.setText(txt)
                self.board[2, 1], self.board[2, 0] = self.board[2, 0], self.board[2, 1]
            elif move == "Up":
                txt = self.button21.text()
                self.button21.setText(self.button11.text())
                self.button11.setText(txt)
                self.board[2, 1], self.board[1, 1] = self.board[1, 1], self.board[2, 1]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(220, 301) and y in range(216, 294):
            move = self.move_button()
            if move == "Down":
                txt = self.button22.text()
                self.button22.setText(self.button32.text())
                self.button32.setText(txt)
                self.board[2, 2], self.board[3, 2] = self.board[3, 2], self.board[2, 2]
            elif move == "Right":
                txt = self.button23.text()
                self.button23.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[2, 3] = self.board[2, 3], self.board[2, 2]
            elif move == "Left":
                txt = self.button21.text()
                self.button21.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[2, 1] = self.board[2, 1], self.board[2, 2]
            else:
                txt = self.button12.text()
                self.button12.setText(self.button22.text())
                self.button22.setText(txt)
                self.board[2, 2], self.board[1, 2] = self.board[1, 2], self.board[2, 2]

        elif x in range(120, 201) and y in range(216, 294):
            move = self.move_button()
            if move == "Down":
                txt = self.button31.text()
                self.button31.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 1], self.board[3, 1] = self.board[3, 1], self.board[2, 1]
            elif move == "Right":
                txt = self.button22.text()
                self.button22.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 2], self.board[2, 1] = self.board[2, 1], self.board[2, 2]
            elif move == "Left":
                txt = self.button20.text()
                self.button20.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 0], self.board[2, 1] = self.board[2, 1], self.board[2, 0]
            else:
                txt = self.button11.text()
                self.button11.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[1, 1], self.board[2, 1] = self.board[2, 1], self.board[1, 1]
        elif x in range(320, 401) and y in range(216, 294):
            move = self.move_button()
            if move == "Down":
                txt = self.button33.text()
                self.button33.setText(self.button23.text())
                self.button23.setText(txt)
                self.board[3, 3], self.board[2, 3] = self.board[2, 3], self.board[3, 3]
            elif move == "Left":
                txt = self.button22.text()
                self.button22.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 2], self.board[2, 1] = self.board[2, 1], self.board[2, 2]
            elif move == "Up":
                txt = self.button13.text()
                self.button13.setText(self.button23.text())
                self.button23.setText(txt)
                self.board[1, 3], self.board[2, 3] = self.board[2, 3], self.board[1, 3]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(20, 101) and y in range(312, 391):
            move = self.move_button()
            if move == "Up":
                txt = self.button20.text()
                self.button20.setText(self.button30.text())
                self.button30.setText(txt)
                self.board[3, 0], self.board[2, 0] = self.board[2, 0], self.board[3, 0]
            elif move == "Right":
                txt = self.button30.text()
                self.button30.setText(self.button31.text())
                self.button31.setText(txt)
                self.board[3, 1], self.board[3, 0] = self.board[3, 0], self.board[3, 1]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(120, 201) and y in range(312, 391):
            move = self.move_button()
            if move == "Up":
                txt = self.button31.text()
                self.button31.setText(self.button21.text())
                self.button21.setText(txt)
                self.board[2, 1], self.board[3, 1] = self.board[3, 1], self.board[2, 1]
            elif move == "Left":
                txt = self.button31.text()
                self.button31.setText(self.button30.text())
                self.button30.setText(txt)
                self.board[3, 0], self.board[3, 1] = self.board[3, 1], self.board[3, 0]
            elif move == "Right":
                txt = self.button31.text()
                self.button31.setText(self.button32.text())
                self.button32.setText(txt)
                self.board[3, 2], self.board[3, 1] = self.board[3, 1], self.board[3, 2]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(220, 301) and y in range(312, 391):
            move = self.move_button()
            if move == "Up":
                txt = self.button32.text()
                self.button32.setText(self.button22.text())
                self.button32.setText(txt)
                self.board[3, 2], self.board[2, 2] = self.board[2, 2], self.board[3, 2]
            elif move == "Left":
                txt = self.button32.text()
                self.button32.setText(self.button31.text())
                self.button31.setText(txt)
                self.board[3, 2], self.board[3, 1] = self.board[3, 1], self.board[3, 2]
            elif move == "Right":
                txt = self.button32.text()
                self.button32.setText(self.button33.text())
                self.button33.setText(txt)
                self.board[3, 3], self.board[3, 2] = self.board[3, 2], self.board[3, 3]
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Invalid move option!")
                msg.exec_()
        elif x in range(320, 401) and y in range(312, 391):
            move = self.move_button()
            if move == "Up":
                txt = self.button33.text()
                self.button33.setText(self.button23.text())
                self.button23.setText(txt)
                self.board[2, 3], self.board[3, 3] = self.board[2, 3], self.board[3, 3]
            elif move == "Left":
                txt = self.button33.text()
                self.button33.setText(self.button32.text())
                self.button32.setText(txt)
                self.board[3, 2], self.board[3, 3] = self.board[3, 3], self.board[3, 2]
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
