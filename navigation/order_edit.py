import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QMessageBox
import pymysql
from qfluentwidgets import InfoBar, InfoBarPosition, LineEdit, PushButton, TextEdit, SpinBox, ComboBox
import datetime
class Order_edit(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.emp_id_label = QLabel("订单编号")
        self.emp_id_edit = SpinBox()
        self.get_info_btn = PushButton("获取订单信息")
        self.get_info_btn.clicked.connect(self.get_employee_info)
        self.info_label = TextEdit()
        self.info_label.setReadOnly(True)
        self.info_label.setStyleSheet(
            'QTextEdit{background-color:rgba(255,255,100,0.1);border-radius:5px;padding:5px;font-size:20px;font-family:"Microsoft YaHei", sans-serif;}'
            'QTextEdit:hover{background-color:rgba(255,100,100,0.1);border-radius:5px;padding:5px;font-size:100px;}')
        self.action_combo = ComboBox()
        self.action_combo.addItem("新增订单")
        self.action_combo.addItem("修改订单")
        self.action_combo.addItem("删除订单")
        self.action_combo.setCurrentIndex(1)
        self.action_combo.currentIndexChanged.connect(self.on_action_combo_changed)

        self.username_label = QLabel("客户编号")
        self.username_edit = LineEdit()
        self.name_label = QLabel("菜品编号")
        #透明


        self.name_edit = LineEdit()
        self.gender_label = QLabel("订单日期")
        self.gender_edit = LineEdit()
        self.password_label = QLabel("数量")
        self.password_edit = LineEdit()
        self.submit_btn = PushButton("修改")
        self.submit_btn.clicked.connect(self.on_submit_btn_clicked)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.emp_id_label)
        hbox1.addWidget(self.emp_id_edit)
        hbox1.addWidget(self.get_info_btn)
        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.info_label)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.action_combo)
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox2)
        vbox2.addWidget(self.username_label)
        vbox2.addWidget(self.username_edit)
        vbox2.addWidget(self.name_label)
        vbox2.addWidget(self.name_edit)
        vbox2.addWidget(self.gender_label)
        vbox2.addWidget(self.gender_edit)
        vbox2.addWidget(self.password_label)
        vbox2.addWidget(self.password_edit)
        vbox2.addWidget(self.submit_btn)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)


        self.db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1784',
                                 database='餐饮管理系统')
        self.cursor = self.db.cursor()

    def closeEvent(self, event):
        self.db.close()

    def get_employee_info(self):
        emp_id = self.emp_id_edit.text()

        sql = "SELECT * FROM orderc WHERE order_id=%s"
        self.cursor.execute(sql, (emp_id,))
        result = self.cursor.fetchone()

        if result:
            self.username_edit.setText(str(result[1]))
            self.name_edit.setText(str(result[2]))
            self.gender_edit.setText(str(result[3]))
            self.password_edit.setText(str(result[4]))

        else:
            InfoBar.error(
                title='错误',
                content=f"没有找到订单编号为{emp_id}的订单",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_LEFT,
                duration=1200,  # won't disappear automatically
                parent=self,
            )

    def add_employee(self):
        username = self.username_edit.text()
        name = self.name_edit.text()
        gender = self.gender_edit.text()
        password = self.password_edit.text()

        sql = "INSERT INTO orderc (cust_id, dish_id, order_time, quantity) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (username, name, gender, password))
        self.db.commit()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_label.insertPlainText(time+"：新增订单成功🥰\n")

    def update_employee(self):
        emp_id = self.emp_id_edit.text()
        username = self.username_edit.text()
        name = self.name_edit.text()
        gender = self.gender_edit.text()
        password = self.password_edit.text()

        sql = "UPDATE orderc SET cust_id=%s, dish_id=%s, order_time=%s, quantity=%s WHERE order_id=%s"
        self.cursor.execute(sql, (username, name, gender, password, emp_id))
        self.db.commit()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_label.insertPlainText(time + "：更新订单成功🥰\n")

    def delete_employee(self):
        emp_id = self.emp_id_edit.text()

        sql = "DELETE FROM orderc WHERE order_id=%s"
        self.cursor.execute(sql, (emp_id,))
        self.db.commit()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_label.insertPlainText(time + "：删除订单成功🥰\n")

    def on_action_combo_changed(self, index):
        if index == 0:
            self.emp_id_edit.setEnabled(False)
            self.username_edit.setText("")
            self.name_edit.setText("")
            self.gender_edit.setText("")
            self.password_edit.setText("")
            self.submit_btn.setText("新增订单")
            self.submit_btn.clicked.disconnect()
            self.submit_btn.clicked.connect(self.add_employee)
        elif index == 1:
            self.emp_id_edit.setEnabled(True)
            self.username_edit.setEnabled(True)
            self.name_edit.setEnabled(True)
            self.gender_edit.setEnabled(True)
            self.submit_btn.setText("更新订单")
            self.submit_btn.clicked.disconnect()
            self.submit_btn.clicked.connect(self.update_employee)
        elif index == 2:
            self.emp_id_edit.setEnabled(True)
            self.username_edit.setEnabled(False)
            self.name_edit.setEnabled(False)
            self.gender_edit.setEnabled(False)
            self.password_edit.setEnabled(False)
            self.submit_btn.setText("删除订单")
            self.submit_btn.clicked.disconnect()
            self.submit_btn.clicked.connect(self.delete_employee)

    def on_submit_btn_clicked(self):
        if self.action_combo.currentIndex() == 0:
            self.add_employee()
        elif self.action_combo.currentIndex() == 1:
            self.update_employee()
        elif self.action_combo.currentIndex() == 2:
            self.delete_employee()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Order_edit()
    sys.exit(app.exec_())