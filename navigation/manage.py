# coding:utf-8
import sys

import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QPalette
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel, QTableWidgetItem, QWidget
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import TableWidget, setTheme, Theme, TableView
from navigation.cust_search import Cust_search
from navigation.cust_edit import Cust_edit
from navigation.emp_search import Emp_search
from navigation.emp_edit import Emp_edit
from navigation.dish_search import Dish_search
from navigation.dish_edit import Dish_edit
class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)


        self.setObjectName(text.replace(' ', '-'))


class AvatarWidget(NavigationWidget):
    """ Avatar widget """

    def __init__(self, parent=None):
        super().__init__(isSelectable=False, parent=parent)
        self.avatar = QImage('resource/t.png').scaled(
            24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)

        if self.isPressed:
            painter.setOpacity(0.7)

        # draw background
        if self.isEnter:
            c = 255 if isDarkTheme() else 0
            painter.setBrush(QColor(c, c, c, 10))
            painter.drawRoundedRect(self.rect(), 5, 5)

        # draw avatar
        painter.setBrush(QBrush(self.avatar))
        painter.translate(8, 6)
        painter.drawEllipse(0, 0, 24, 24)
        painter.translate(-8, -6)

        if not self.isCompacted:
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)
            font = QFont('Segoe UI')
            font.setPixelSize(14)
            painter.setFont(font)
            painter.drawText(QRect(44, 0, 255, 50), Qt.AlignVCenter, '旧区的餐饮管理系统')


class Window(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))

        # use dark theme mode
        # setTheme(Theme.DARK)

        # change the theme color
        setThemeColor('#724CAF')

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True,showReturnButton=True)
        self.navigationInterface.setStyleSheet("QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgba(236, 123, 163,230),stop:0.4 rgba(179, 214, 54,230) ,stop:0.6 rgba(57, 233, 221,230),stop:1 rgba(57, 233, 221,200));border : 3px solid rgba(200, 200, 255,120);border-radius: 20px;}")

        self.stackWidget = QStackedWidget(self)

        # 这里是界面定义部分
        #客户查询部分#todo
        self.cust_searchInterface = Widget('客户查询', self)
        self.cust_searchInterface.hBoxLayout.addWidget(Cust_search())
        self.cust_searchInterface.hBoxLayout.removeWidget(self.cust_searchInterface.label)
        self.cust_searchInterface.label.deleteLater()
        #客户操作部分
        self.cust_editInterface = Widget('客户操作', self)
        self.cust_editInterface.hBoxLayout.addWidget(Cust_edit())
        self.cust_editInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.cust_editInterface.label.deleteLater()
        #员工查询部分
        self.emp_searchInterface = Widget('员工查询', self)
        self.emp_searchInterface.hBoxLayout.addWidget(Emp_search())
        self.emp_searchInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.emp_searchInterface.label.deleteLater()
        #员工操作部分
        self.emp_editInterface = Widget('员工操作', self)
        self.emp_editInterface.hBoxLayout.addWidget(Emp_edit())
        self.emp_editInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.emp_editInterface.label.deleteLater()
        #菜品查询部分
        self.dish_searchInterface = Widget('菜品查询', self)
        self.dish_searchInterface.hBoxLayout.addWidget(Dish_search())
        self.dish_searchInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.dish_searchInterface.label.deleteLater()
        #菜品操作部分
        self.dish_editInterface = Widget('菜品操作', self)
        self.dish_editInterface.hBoxLayout.addWidget(Dish_edit())
        self.dish_editInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.dish_editInterface.label.deleteLater()


        # self.musicInterface = Widget('Music Interface', self)
        # self.videoInterface = Widget('Video Interface', self)
        # self.folderInterface = Widget('Folder Interface', self)
        self.settingInterface = Widget('Setting Interface', self)

        # 添加自定义部件（MyWidget）
        # self.widget = MyWidget()

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):#todo
        self.addSubInterface(self.cust_searchInterface, FIF.SEARCH, '客户查询')
        self.addSubInterface(self.cust_editInterface, FIF.EDIT, '客户操作')
        # 来个分隔符号
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.emp_searchInterface, FIF.VIEW, '员工查询')
        self.addSubInterface(self.emp_editInterface, FIF.PENCIL_INK, '员工操作')
        self.navigationInterface.addSeparator()
        # 来个分隔符号
        self.addSubInterface(self.dish_searchInterface, FIF.SEARCH, '菜品查询')
        self.addSubInterface(self.dish_editInterface, FIF.EDIT, '菜品操作')


        # self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video library')

        self.navigationInterface.addSeparator()

        # add navigation items to scroll area
        # self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder library', NavigationItemPosition.SCROLL)
        # for i in range(1, 21):
        #     self.navigationInterface.addItem(
        #         f'folder{i}',
        #         FIF.FOLDER,
        #         f'Folder {i}',
        #         lambda: print('Folder clicked'),
        #         position=NavigationItemPosition.SCROLL
        #     )

        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=AvatarWidget(),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        #!IMPORTANT: don't forget to set the default route key if you enable the return button
        # self.navigationInterface.setDefaultRouteKey(self.musicInterface.objectName())

        # set the maximum width
        # self.navigationInterface.setExpandWidth(300)

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(0)

    def initWindow(self):
        self.resize(1200, 700)
        self.setWindowIcon(QIcon('resource/t.png'))
        self.setWindowTitle('餐饮系统后台管理')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text
        )

    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        with open(f'../navigation/resource/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

    def showMessageBox(self):
        w = MessageBox(
            'This is a help message',
            'You clicked a customized navigation widget. You can add more custom widgets by calling `NavigationInterface.addWidget()` 😉',
            self
        )
        w.exec()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
