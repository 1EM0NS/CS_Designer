# coding:utf-8
import sys

import pymysql
from PIL import Image
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QPalette
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel, QTableWidgetItem, QWidget
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, InfoBar, InfoBarPosition)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import TableWidget, setTheme, Theme, TableView
from navigation.cust_search import Cust_search
from navigation.cust_edit import Cust_edit
from navigation.emp_search import Emp_search
from navigation.emp_edit import Emp_edit
from navigation.dish_search import Dish_search
from navigation.dish_edit import Dish_edit
from navigation.order_search import Order_search
from navigation.order_edit import Order_edit
from navigation.stock_search import Stock_search
from navigation.stock_edit import Stock_edit
from navigation.bb_inter import Bb_inter
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
        self.avatar = QImage('C:/Users/User\Desktop\计算机软件综合实验\计算机软件综合实验/navigation/resource/t.png').scaled(
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
        st =  StandardTitleBar(self)
        #圆角
        self.setTitleBar(st)
        #窗口上半部分背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # use dark theme mode
        # setTheme(Theme.DARK)

        # change the theme color
        setThemeColor('#724CAF')

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True,showReturnButton=True)
        #设置背景图片
        self.navigationInterface.setStyleSheet("background-image:url(C:/Users/User/Desktop/计算机软件综合实验/计算机软件综合实验/navigation/resource/bg.png);border-bottom-left-radius:20px;")

        self.stackWidget = QStackedWidget(self)
        # 这里是界面定义部分
        #客户查询部分
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
        #订单查询部分
        self.order_searchInterface = Widget('订单查询', self)
        self.order_searchInterface.hBoxLayout.addWidget(Order_search())
        self.order_searchInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.order_searchInterface.label.deleteLater()
        #订单操作部分
        self.order_editInterface = Widget('订单操作', self)
        self.order_editInterface.hBoxLayout.addWidget(Order_edit())
        self.order_editInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.order_editInterface.label.deleteLater()
        #库存查询部分
        self.stock_searchInterface = Widget('库存查询', self)
        self.stock_searchInterface.hBoxLayout.addWidget(Stock_search())
        self.stock_searchInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.stock_searchInterface.label.deleteLater()
        #库存操作部分
        self.stock_editInterface = Widget('库存操作', self)
        self.stock_editInterface.hBoxLayout.addWidget(Stock_edit())
        self.stock_editInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        self.stock_editInterface.label.deleteLater()

        # self.stock_searchInterface.hBoxLayout.addWidget(Stock_search())
        # self.stock_searchInterface.hBoxLayout.removeWidget(self.cust_editInterface.label)
        # self.musicInterface = Widget('Music Interface', self)
        # self.videoInterface = Widget('Video Interface', self)
        # self.folderInterface = Widget('Folder Interface', self)
        self.settingInterface = Widget('报表查看', self)
        self.settingInterface.hBoxLayout.addWidget(Bb_inter())
        self.settingInterface.hBoxLayout.removeWidget(self.settingInterface.label)
        self.settingInterface.label.deleteLater()

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

    def initNavigation(self):
        self.addSubInterface(self.cust_searchInterface, FIF.SEARCH, '客户查询')
        self.addSubInterface(self.cust_editInterface, FIF.EDIT, '客户操作')
        # 来个分隔符号
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.emp_searchInterface, FIF.VIEW, '员工查询')
        self.addSubInterface(self.emp_editInterface, FIF.PENCIL_INK, '员工操作')
        self.navigationInterface.addSeparator()
        # 来个分隔符号
        self.addSubInterface(self.dish_searchInterface, FIF.MORE, '菜品查询')
        self.addSubInterface(self.dish_editInterface, FIF.SEND, '菜品操作')
        #来个分隔符号
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.order_searchInterface, FIF.ZOOM_IN, '订单查询')
        self.addSubInterface(self.order_editInterface, FIF.DOCUMENT, '订单操作')
        #来个分隔符号
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.stock_searchInterface, FIF.BOOK_SHELF, '原材料查询')
        self.addSubInterface(self.stock_editInterface, FIF.HIGHTLIGHT, '原材料操作')
        #来个分隔符号

        # self.addSubInterface(self.order_editInterface, FIF.PENCIL_INK, '订单操作')

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

        self.addSubInterface(self.settingInterface, FIF.COPY, '报表查看', NavigationItemPosition.BOTTOM)

        #!IMPORTANT: don't forget to set the default route key if you enable the return button
        # self.navigationInterface.setDefaultRouteKey(self.musicInterface.objectName())

        # set the maximum width
        # self.navigationInterface.setExpandWidth(300)

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(0)

    def initWindow(self):
        self.resize(1200, 700)
        self.setWindowIcon(QIcon('C:/Users/User\Desktop\计算机软件综合实验\计算机软件综合实验/navigation/resource/t.png'))
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
        # w = MessageBox('路漫漫其修远兮，吾将上下而求索',self)
        InfoBar.info(
            title='',
            content=f"悲剧并非终结，而是希望的起始",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=1200,  # won't disappear automatically
            parent=self,
        )
        InfoBar.info(
            title='',
            content=f"悲剧并非终结，而是希望的起始",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=1200,  # won't disappear automatically
            parent=self,
        )
        InfoBar.info(
            title='',
            content=f"悲剧并非终结，而是希望的起始",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_LEFT,
            duration=1200,  # won't disappear automatically
            parent=self,
        )
        InfoBar.info(
            title='',
            content=f"悲剧并非终结，而是希望的起始",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=1200,  # won't disappear automatically
            parent=self,
        )
        # w.exec()



if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
