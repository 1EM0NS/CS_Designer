import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from login import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.anim=None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.lineEdit_2.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.resize(QDesktopWidget().screenGeometry().width(),
                    QDesktopWidget().screenGeometry().height())  # 主窗大小
        self.e = 1
        # 按ESC键开关
        
    def keyPressEvent(self, QKeyEvent):
        """快捷键"""
        if QKeyEvent.key() == Qt.Key_Escape:  # esc
            if self.e == 1:
                self.animation_exit()
            elif self.e == 0:
                self.animation_start()

    def animation_start(self):
        self.e = 1
        self.show()
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        posi = QRect(int(QDesktopWidget().screenGeometry().width() / 2-230 ),
                                      int(QDesktopWidget().screenGeometry().height() / 2 -300), 0, 0)
        self.anim.setStartValue(posi)
        self.anim.setEndValue(posi)
        self.anim.setDuration(800)
        self.anim.setEasingCurve(QEasingCurve.OutCurve)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(0)
        main_opacity.setEndValue(1)
        main_opacity.setDuration(1000)
        main_opacity.start()
        self.anim.start()

    def animation_exit(self):
        self.e = 0
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        posi = QRect(int(QDesktopWidget().screenGeometry().width() / 2 - 230),
                     int(QDesktopWidget().screenGeometry().height() / 2 - 300), 0, 0)
        self.anim.setStartValue(posi)
        self.anim.setEndValue(posi)
        self.anim.setDuration(800)
        self.anim.setEasingCurve(QEasingCurve.OutCurve)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(1)
        main_opacity.setEndValue(0)
        main_opacity.setDuration(1000)
        main_opacity.start()
        self.anim.start()

        self.anim.start()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()



    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass






if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.animation_start()
    sys.exit(app.exec_())
