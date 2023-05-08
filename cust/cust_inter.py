import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, \
    QSizePolicy, QHeaderView, QMessageBox
from qfluentwidgets import PushButton, LineEdit, TextEdit, ComboBox, InfoBar, InfoBarPosition, MessageBox

from cust.dish_widget import MenuWidget
from cust.my_info import My_info

class MainWindow(QWidget):
    def __init__(self,cust):
        super().__init__()
        self.cust = cust
        self.initUI()
    def initUI(self):
        # 创建窗口布局
        main_layout = QVBoxLayout()
        tab_layout = QHBoxLayout()


        # 创建选项卡
        tab_widget = QTabWidget()
        my_tab = QWidget()
        order_tab = QWidget()

        # 创建“我的”界面的部件
        my_label = QLabel("我的界面")
        my_layout = QVBoxLayout()
        my_layout.addWidget(my_label)
        my_info = My_info(self.cust)
        my_layout.addWidget(my_info)

        my_tab.setLayout(my_layout)


        # 创建“点餐”界面的部件
        order_label = QLabel("点餐界面")
        self.scroll_area = MenuWidget()

        order_layout = QVBoxLayout()
        order_layout.addWidget(order_label)
        order_layout.addWidget(self.scroll_area)
        order_tab.setLayout(order_layout)
        self.xia_dan = PushButton("下单")
        self.xia_dan.clicked.connect(self.place_order)
        order_layout.addWidget(self.xia_dan)

        # 将选项卡添加到选项卡部件中
        tab_widget.addTab(my_tab, "我的")
        tab_widget.setCurrentIndex(1)
        tab_widget.addTab(order_tab, "点餐")

        # 将选项卡部件添加到主布局中
        tab_layout.addWidget(tab_widget)
        main_layout.addLayout(tab_layout)

        # 设置主窗口布局
        self.setLayout(main_layout)
        self.setGeometry(600, 200, 650, 800)
        self.setWindowTitle('点点点点点餐吧')
        self.show()

    def place_order(self):
        # 执行下单逻辑
        #todo  下单逻辑的实现
        len = self.scroll_area.order(self.cust[0])
        if len > 0:
            InfoBar.success(
                title='成功',
                content=f"您的商品已下单成功！",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=1500,  # won't disappear automatically
                parent=self,

            )
            #一个付款二维码
            #todo 付款二维码的实现
            # 创建一个QMessageBox
            msg_box = QMessageBox()

            # 设置提示文本和图标
            msg_box.setText("请付款")
            msg_box.setStandardButtons(QMessageBox.Ok)

            # 添加QLabel作为自定义控件
            label = QLabel()
            label.setPixmap(QPixmap("../cust/img/qrcode.jpg").scaledToWidth(300))
            msg_box.layout().addWidget(label)
            # 显示QMessageBox
            msg_box.exec_()
        else:
            InfoBar.info(
                title='再看看',
                content=f"你什么都没选！",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=1500,  # won't disappear automatically
                parent=self,

            )
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
