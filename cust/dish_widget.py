import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QScrollArea, QGridLayout, \
    QHBoxLayout, QSizePolicy, QSpinBox
from PyQt5.QtGui import QFont, QPixmap
import pymysql
from qfluentwidgets import PushButton,SpinBox,SmoothScrollArea

class DishWidget(QWidget):
    def __init__(self, dish_id, name, price, quantity, spiciness, is_recommend, created_time):
        super().__init__()
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.spiciness = spiciness
        self.is_recommend = is_recommend
        self.created_time = created_time
        # self.cost = cost
        # self.emp_id = emp_id
        self.initUI()

    def initUI(self):
        #qlabel透明样式
        transparent = 'background-color:rgba(255,255,255,0.5);border-radius:5px;padding:5px;font-family:"Microsoft YaHei", sans-serif;'

        img_label = QLabel()

        #若没有图片
        if not os.path.exists('../cust/img/{}.jpg'.format(self.dish_id)):
            img_label.setPixmap(QPixmap('../cust/img/1.jpg').scaled(150, 100))
        #找到图片
        else:
            img_label.setPixmap(QPixmap('../cust/img/{}.jpg'.format(self.dish_id)).scaled(130, 100))

        nameLabel = QLabel(self.name)

        nameLabel.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        nameLabel.setFont(QFont('Arial', 18))
        priceLabel = QLabel(f'价格: {self.price}元')
        priceLabel.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        quantityLabel = QLabel(f'剩余数量: {self.quantity}份')
        quantityLabel.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        spicinessLabel = QLabel(f'辣度: {self.spiciness}')
        label_q = QLabel('数量:')
        odd_q  = SpinBox()
        odd_q.setRange(0, self.quantity)
        # costLabel = QLabel(f'成本: {self.cost}元')
        # emp_idLabel = QLabel(f'操作员ID: {self.emp_id}')
        isRecommendLabel = QLabel()
        if self.is_recommend:
            isRecommendLabel.setText('推荐')
            isRecommendLabel.setStyleSheet('color: red')
        else:
            isRecommendLabel.setText(' ')

        img_label.setStyleSheet(transparent)
        nameLabel.setStyleSheet(transparent)
        priceLabel.setStyleSheet(transparent)
        quantityLabel.setStyleSheet(transparent)
        spicinessLabel.setStyleSheet(transparent)
        label_q.setStyleSheet(transparent)
        isRecommendLabel.setStyleSheet(transparent)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(img_label)
        hbox1.addWidget(nameLabel)
        hbox1.addWidget(isRecommendLabel)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(priceLabel)
        hbox2.addWidget(quantityLabel)
        hbox2.addWidget(spicinessLabel)
        hbox2.addWidget(label_q)
        hbox2.addWidget(odd_q)
        # hbox2.addWidget(costLabel)
        # hbox2.addWidget(emp_idLabel)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        self.setStyleSheet('border: 1px solid gray; padding: 10px;background-color: white')

class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('菜单')
        self.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgba(236, 123, 163,230),stop:0.4 rgba(179, 214, 54,230) ,stop:0.6 rgba(57, 233, 221,230),stop:1 rgba(57, 233, 221,200));')

        self.vboxlayout = QVBoxLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.vboxlayout)

        scrollArea = SmoothScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(self.scrollWidget)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scrollArea)

        self.loadDishes()

    def loadDishes(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')

        cursor = db.cursor()
        cursor.execute('SELECT * FROM dish')
        #添加项目
        for dish in cursor.fetchall():
            dish = dish[:-2]
            dishWidget = DishWidget(*dish)
            self.vboxlayout.addWidget(dishWidget)

        cursor.close()
        db.close()

    def order(self,cust_id):
        dishes = []  # 存储已点菜品
        for i in range(self.vboxlayout.count()):
            widget = self.vboxlayout.itemAt(i).widget()
            if isinstance(widget, DishWidget):
                dish_id = widget.dish_id
                quantity = widget.findChild(QSpinBox).value()
                if quantity > 0:
                    dishes.append((dish_id, quantity))
        if len(dishes) > 0:
            # 这里可以将已点菜品信息上传到服务器或者进行其他处理
            try:
                # 连接到数据库
                conn = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')

                # 获取一个游标对象
                cursor = conn.cursor()

                # 循环处理每个菜品编号和数量
                for dish_id, quantity in dishes:
                    # 插入一条订单记录到订单表中
                    insert_query = "INSERT INTO `orderc` (`cust_id`, `dish_id`, `order_time`, `quantity`) VALUES (%s, %s, NOW(), %s)"
                    cursor.execute(insert_query, (cust_id, dish_id, quantity))

                # 提交事务并关闭游标和连接
                conn.commit()
                cursor.close()
                conn.close()

            except Exception as error:
                print(f"Failed to place order: {error}")
            print(dishes)
        return len(dishes)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWidget = MenuWidget()
    menuWidget.show()
    sys.exit(app.exec_())
