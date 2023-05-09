import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QTableWidgetItem, QLineEdit, QVBoxLayout, QPushButton, QHeaderView
from qfluentwidgets import TableWidget, ComboBox, PushButton, LineEdit
from qfluentwidgets import FluentIcon as FIF


class Emp_search(QWidget):
    def __init__(self):
        self.flag = 0
        super().__init__()
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute("select * from employee")
        data = cursor.fetchall()
        db.close()
        print(data)

        # setTheme(Theme.DARK)

        self.vBoxLayout = QVBoxLayout(self)
        # 查询文本框
        self.search_edit = LineEdit(self)
        self.search_edit.setPlaceholderText("请输入查询内容")
        self.comboBox = ComboBox(self)

        self.comboBox.addItems(['员工编号', '员工名称', '用户名'])
        self.comboBox.setCurrentIndex(0)

        self.comboBox.move(200, 200)

        self.resize(500, 500)
        self.setStyleSheet('Demo{background:white}')

        self.pushButton = PushButton('开始查询', self, FIF.SEARCH)
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton2 = PushButton('刷新', self, FIF.SYNC)
        self.tableView = TableWidget(self)

        self.tableView.setWordWrap(False)
        self.tableView.setRowCount(35)
        self.tableView.setColumnCount(7)
        info = data
        for i, songInfo in enumerate(info):
            for j in range(7):
                self.tableView.setItem(i, j, QTableWidgetItem(str(songInfo[j])))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(
            ['员工编号', '用户名', '姓名', '性别', '密码', '联系方式', '籍贯'])

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
    }''')
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
                        self.tableView.item(i, j).setBackground(QBrush(QColor(0, 200, 255,100)))

    def select(self):
        # 选择下拉框

        text = self.comboBox.text()
        if text == '员工编号':
            self.flag = 0
        elif text == '员工名称':
            self.flag = 2
        elif text == '用户名':
            self.flag = 1
        print(self.flag)

    def refresh(self):
        # 刷新
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute("select * from employee")
        data = cursor.fetchall()
        self.tableView.setRowCount(len(data))
        print(data)
        info = data
        #清空table
        self.tableView.clearContents()
        for i, songInfo in enumerate(info):
            for j in range(7):
                self.tableView.setItem(i, j, QTableWidgetItem(str(songInfo[j])))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(
            ['员工编号', '用户名', '姓名', '性别', '密码', '联系方式', '籍贯'])