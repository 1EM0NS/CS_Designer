from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel

class OrderView(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("点餐视图")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

class CartView(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("购物车视图")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

class MyView(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("我的视图")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("点餐应用")

        # 创建三个按钮
        self.order_button = QPushButton("点餐")
        self.cart_button = QPushButton("购物车")
        self.my_button = QPushButton("我的")

        # 创建三个视图
        self.order_view = OrderView()
        self.cart_view = CartView()
        self.my_view = MyView()

        # 将三个按钮添加到一个水平布局中
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.order_button)
        button_layout.addWidget(self.cart_button)
        button_layout.addWidget(self.my_button)

        # 将三个视图添加到一个垂直布局中
        view_layout = QVBoxLayout()
        view_layout.addWidget(self.order_view)
        view_layout.addWidget(self.cart_view)
        view_layout.addWidget(self.my_view)

        # 将按钮布局和视图布局添加到主窗口中
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addLayout(view_layout)
        main_layout.addLayout(button_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # 为按钮添加事件处理程序
        self.order_button.clicked.connect(self.show_order_view)
        self.cart_button.clicked.connect(self.show_cart_view)
        self.my_button.clicked.connect(self.show_my_view)

    def show_order_view(self):
        self.order_view.show()
        self.cart_view.hide()
        self.my_view.hide()

    def show_cart_view(self):
        self.order_view.hide()
        self.cart_view.show()
        self.my_view.hide()

    def show_my_view(self):
        self.order_view.hide()
        self.cart_view.hide()
        self.my_view.show()

if __name__ == "__main__":
    app = QApplication([])
    main_view = MainView()
    main_view.show()
    app.exec_()
