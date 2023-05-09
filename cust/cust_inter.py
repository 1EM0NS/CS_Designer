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
        #设置选项卡圆角
        tab_widget.setStyleSheet("QTabBar::tab{width:100px;height:50px;font-size:20px;font-family:'Microsoft YaHei', sans-serif;padding:5px;background-color:rgba(255,255,255,0.1);border-radius: 5px;}"
                                 "QTabBar::tab:hover{background-color:rgba(255,255,255,0.4);padding:5px;font-size:20px;font-family:'Microsoft YaHei', sans-serif;border-radius: 5px;}"
                                    "QTabBar::tab:selected{background-color:rgba(255,255,255,0.6);padding:5px;font-size:20px;font-family:'Microsoft YaHei', sans-serif;blur:10px;border-radius: 5px;}"
                                    "QTabWidget::pane{border:0px solid white;background-color:transparent;}"
                                    "QTabWidget::tab-bar{alignment:center;}"
                                    "QTabWidget::tab-bar{background-color:transparent;}"
                                    "QTabWidget::tab-bar{border:0px solid white;}"
                                    "QTabWidget::tab-bar{margin-left:100px;margin-right:100px;}"
                                    "QTabWidget::tab-bar{margin-top:20px;}"
                                    "QTabWidget::tab-bar{margin-bottom:20px;}"
                                 )
        my_tab = QWidget()
        my_tab.setStyleSheet("background-color: qlineargradient(x1:0, y1:1, x2:1, y2:0,stop:0 rgba(172, 16, 105,240),stop:0.5 rgba(35, 90, 192,240), stop:1 rgba(0, 211, 196,240));\n")
        order_tab = QWidget()

        # 创建“我的”界面的部件

        my_layout = QVBoxLayout()
        my_info = My_info(self.cust)
        #背景透明
        my_info.setStyleSheet("background-color:transparent")
        my_layout.addWidget(my_info)

        my_tab.setLayout(my_layout)


        # 创建“点餐”界面的部件
        self.scroll_area = MenuWidget()

        order_layout = QVBoxLayout()
        order_layout.addWidget(self.scroll_area)
        #圆角
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
        self.setStyleSheet \
            ("background-color: qlineargradient(x1:0, y1:1, x2:1, y2:0,stop:0 rgba(172, 16, 105,240),stop:0.5 rgba(35, 90, 192,240), stop:1 rgba(0, 211, 196,240));\n"
             "blur: 10px;\n")
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
            #弹出窗口
            w = MessageBox("提示","什么都没选呢！",self)
            w.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
