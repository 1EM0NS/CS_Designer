import sys
import pymysql
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from qfluentwidgets import PushButton, LineEdit, TextEdit, ComboBox, InfoBar, InfoBarPosition, MessageBox
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']

# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

#报表类
class Bb_inter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fig = plt.figure()
        self.fig.set_alpha(0.0)
        layout = QVBoxLayout()
        self.sals()
        self.lirun()
        self.fig.set_facecolor('none')
        canvas = FigureCanvas(self.fig)
        refresh = PushButton('刷新')
        refresh.clicked.connect(self.refresh)
        layout.addWidget(refresh)
        layout.addWidget(canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def autolabel(self,rects,c):
        for i,rect in enumerate(rects):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2. -0.12, 0.8 * height, '%s' % int(c[i]), size=10,
                     family="Times new roman",label='revenue')

    def lirun(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        order_query = "SELECT `dish`.`name`, SUM(`dish`.`price` * `orderc`.`quantity`) AS `revenue`, SUM(`dish`.`cost` * `orderc`.`quantity`) AS `cost` FROM `orderc` JOIN `dish` ON `orderc`.`dish_id` = `dish`.`dish_id` GROUP BY `dish`.`name`ORDER BY revenue DESC;"
        cursor = db.cursor()
        cursor.execute(order_query)
        data = cursor.fetchall()
        dish_name = []
        cost = []
        revenue = []
        for i in range(len(data)):
            dish_name.append(data[i][0])
            revenue.append(data[i][1])
            cost.append(data[i][2])
        #利润数组
        profit  = [float(x) - float(y) for x, y in zip(revenue, cost)]
        ax = self.fig.add_subplot(212)
        ax.bar(dish_name, cost, width=0.5, color=['r'], alpha=0.1, label='cost')
        ax.bar(dish_name, revenue, width=0.5, color=['b'], alpha=0.5, label='revenue')
        ax.bar(dish_name, profit, width=0.5, color=['g'], alpha=0.5, label='profit')
        ax.plot(dish_name, profit, color='y',alpha=0.7, marker='o', linestyle='--', label='profit')
        # 添加标签和标题
        ax.set_ylabel("利润收入成本")
        ax.set_facecolor('none')

        ax.legend(loc='upper right')
    def sals(self):
        # 连接到MySQL数据库
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute('''SELECT d.name AS dish_name, SUM(o.quantity) AS sales, SUM(d.price * o.quantity) AS revenue
                    FROM dish d
                    JOIN `orderc` o ON d.dish_id = o.dish_id
                    GROUP BY d.dish_id
                    ORDER BY sales DESC;''')
        # 执行查询并获取结果
        data = cursor.fetchall()

        # 将结果添加到列表中
        dish_name = []
        sales = []
        revenue = []
        for i in range(len(data)):
            dish_name.append(data[i][0])
            sales.append(data[i][1])
            #销售额
            revenue.append(data[i][2])
        # 创建条形图

        ax = self.fig.add_subplot(211)
        ax.bar(dish_name, sales, width=0.5, color=['r','g','b','r','g','b'],alpha=0.3,label='sales')
        # 添加标签和标题
        ax.set_ylabel("销售额")
        ax.set_facecolor('none')
        ax.set_title("销售与利润报表")
        ax.legend(loc='upper right')
        self.autolabel(ax.patches,revenue)

    def refresh(self):
        self.fig.clear()
        self.sals()
        self.lirun()
        self.fig.set_facecolor('none')
        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()
        InfoBar.success(
            title='成功',
            content=f"刷新成功",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=1200,  # won't disappear automatically
            parent=self,
        )
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Bb_inter()
    window.show()
    sys.exit(app.exec_())
