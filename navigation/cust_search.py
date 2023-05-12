import pymysql
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QTableWidgetItem, QLineEdit, QVBoxLayout, QPushButton, QHeaderView
from qfluentwidgets import TableWidget, ComboBox, PushButton, LineEdit, InfoBar, InfoBarPosition
from qfluentwidgets import FluentIcon as FIF


def dec_sear(cls):
    new_search = cls.search

    def search(self):
        InfoBar.success(
            title='成功',
            content=f"信息查询成功",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=1200,  # won't disappear automatically
            parent=self,
        )
        return new_search(self)

    cls.search = search
    return cls

# todo 装饰器完善
@dec_sear
class Cust_search(QWidget):
    def __init__(self):
        self.flag = 0
        super().__init__()
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute("select * from customer ")
        data = cursor.fetchall()
        db.close()
        print(data)

        # setTheme(Theme.DARK)

        self.vBoxLayout = QVBoxLayout(self)
        # 查询文本框
        self.search_edit = LineEdit(self)
        self.search_edit.setPlaceholderText("请输入查询内容")
        self.comboBox = ComboBox(self)

        self.comboBox.addItems(['客户编号', '客户名称', '用户名'])
        self.comboBox.setCurrentIndex(0)

        self.comboBox.move(200, 200)

        self.setStyleSheet('Demo{background:white}')

        self.pushButton = PushButton('开始查询', self, FIF.SEARCH)
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton2 = PushButton('刷新', self, FIF.SYNC)
        self.tableView = TableWidget(self)

        self.tableView.setWordWrap(False)
        # data数量
        self.tableView.setRowCount(len(data))
        self.tableView.setColumnCount(9)
        info = data
        for i, songInfo in enumerate(info):
            for j in range(9):
                self.tableView.setItem(i, j, QTableWidgetItem(str(songInfo[j])))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(
            ['客户编号', '姓名', '联系方式', '性别', '身份证号', '民族', '籍贯', '用户名', '密码'])

        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.setSortingEnabled(True)

        self.tableView.setAlternatingRowColors(True)

        self.tableView.setStyleSheet('''
            QTableView { border: 0px solid #D9D9D9;
                         background-color: rgba(235, 238, 205,80);
                         selection-background-color: rgba(0, 200, 255,100);
                            selection-color: #fff;
                            alternate-background-color: rgba(255, 255, 255,120);
                            gridline-color: #ccc;
                            outline: 0;
                            font-size: 14px;
                            color: #000;


            }
            QTableView::item {
        padding-top: 20px; /* 设置上边距 */
        padding-bottom: 20px; /* 设置下边距 */
    }''')  # for demo purposes

        self.vBoxLayout.setContentsMargins(1, 1, 1, 1)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setContentsMargins(1, 1, 1, 1)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.search_edit)
        self.hBoxLayout.addWidget(self.comboBox)
        self.hBoxLayout.addWidget(self.pushButton2)
        self.hBoxLayout.addWidget(self.pushButton)

        self.vBoxLayout.addWidget(self.tableView)
        self.resize(625, 700)
        self.function()

    def function(self):
        self.pushButton.clicked.connect(self.search)
        self.comboBox.currentTextChanged.connect(self.select)
        self.pushButton2.clicked.connect(self.refresh)

    def search(self):
        # 在表格内搜索

        text = self.search_edit.text()
        for i in range(self.tableView.rowCount()):
            if self.tableView.item(i, self.flag) is not None:
                if self.tableView.item(i, self.flag).text() == text:
                    self.tableView.scrollToItem(self.tableView.item(i, self.flag))
                    for j in range(self.tableView.columnCount()):
                        self.tableView.item(i, j).setBackground(QBrush(QColor(0, 200, 255, 100)))

    def select(self):
        # 选择下拉框

        text = self.comboBox.text()
        if text == '客户编号':
            self.flag = 0
        elif text == '客户名称':
            self.flag = 1
        elif text == '用户名':
            self.flag = 7
        print(self.flag)

    def refresh(self):
        # 刷新
        self.tableView.clearContents()

        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute("select * from customer ")
        data = cursor.fetchall()
        self.tableView.setRowCount(len(data))
        print(data)
        info = data
        for i, songInfo in enumerate(info):
            for j in range(9):
                self.tableView.setItem(i, j, QTableWidgetItem(str(songInfo[j])))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(
            ['客户编号', '姓名', '联系方式', '性别', '身份证号', '民族', '籍贯', '用户名', '密码'])
