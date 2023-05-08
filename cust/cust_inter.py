import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, \
    QSizePolicy, QHeaderView
from dish_widget import MenuWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
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
        my_tab.setLayout(my_layout)

        # 创建“点餐”界面的部件
        order_label = QLabel("点餐界面")
        scroll_area = MenuWidget()
        order_button = QPushButton("下单")
        order_button.clicked.connect(self.place_order)
        order_layout = QVBoxLayout()
        order_layout.addWidget(order_label)
        order_layout.addWidget(scroll_area)
        order_layout.addWidget(order_button)
        order_tab.setLayout(order_layout)

        # 将选项卡添加到选项卡部件中
        tab_widget.addTab(my_tab, "我的")
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

        print("下单成功！")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
