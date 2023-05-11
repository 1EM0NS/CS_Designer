# coding:utf-8


import sys


from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget


from WindowsEffect import WindowEffect



class Demo(QWidget):


    def __init__(self, parent=None):

        super().__init__(parent)


        self.windowEffect = WindowEffect()

        self.resize(500, 500)

        self.setWindowFlags(Qt.FramelessWindowHint)

        # 必须用样式表使背景透明，别用 setAttribute(Qt.WA_TranslucentBackground)，不然界面会卡顿

        self.setStyleSheet("background:transparent")

        self.windowEffect.setAcrylicEffect(int(self.winId()))


    def mousePressEvent(self, QMouseEvent):

        """ 移动窗口 """

        self.windowEffect.moveWindow(self.winId())



if __name__ == "__main__":

    app = QApplication(sys.argv)

    demo = Demo()

    demo.show()

    sys.exit(app.exec_())
