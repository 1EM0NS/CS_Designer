import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QMessageBox
import pymysql
from qfluentwidgets import InfoBar, InfoBarPosition, LineEdit, PushButton, TextEdit, SpinBox, ComboBox
import datetime
class Emp_edit(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.emp_id_label = QLabel("员工编号")
        self.emp_id_edit = SpinBox()
        self.get_info_btn = PushButton("获取员工信息")
        self.get_info_btn.clicked.connect(self.get_employee_info)
        self.info_label = TextEdit()
        self.info_label.setReadOnly(True)
        self.info_label.setStyleSheet(
            'QTextEdit{background-color:rgba(255,255,100,0.1);border-radius:5px;padding:5px;font-size:20px;font-family:"Microsoft YaHei", sans-serif;}'
            'QTextEdit:hover{background-color:rgba(255,100,100,0.1);border-radius:5px;padding:5px;font-size:100px;}')
        self.action_combo = ComboBox()
        self.action_combo.addItem("新增员工")
        self.action_combo.addItem("修改员工")
        self.action_combo.addItem("删除员工")
        self.action_combo.setCurrentIndex(1)
        self.action_combo.currentIndexChanged.connect(self.on_action_combo_changed)

        self.username_label = QLabel("用户名")
        self.username_edit = LineEdit()
        self.name_label = QLabel("姓名")
        #透明


        self.name_edit = LineEdit()
        self.gender_label = QLabel("性别")
        self.gender_edit = LineEdit()
        self.password_label = QLabel("密码")
        self.password_edit = LineEdit()
        self.contact_label = QLabel("联系方式")
        self.contact_edit = LineEdit()
        self.hometown_label = QLabel("籍贯")
        self.hometown_edit = LineEdit()
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
        vbox2.addWidget(self.contact_label)
        vbox2.addWidget(self.contact_edit)
        vbox2.addWidget(self.hometown_label)
        vbox2.addWidget(self.hometown_edit)
        vbox2.addWidget(self.submit_btn)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

        self.setWindowTitle('员工管理系统')
        self.setGeometry(300, 300, 500, 200)
        self.show()

        self.db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1784',
                                 database='餐饮管理系统')
        self.cursor = self.db.cursor()

    def closeEvent(self, event):
        self.db.close()

    def get_employee_info(self):
        emp_id = self.emp_id_edit.text()

        sql = "SELECT * FROM employee WHERE emp_id=%s"
        self.cursor.execute(sql, (emp_id,))
        result = self.cursor.fetchone()

        if result:
            self.username_edit.setText(result[1])
            self.name_edit.setText(result[2])
            self.gender_edit.setText(result[3])
            self.password_edit.setText(result[4])
            self.contact_edit.setText(result[5])
            self.hometown_edit.setText(result[6])
        else:
            InfoBar.error(
                title='错误',
                content=f"没有找到员工编号为{emp_id}的员工",
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
        contact = self.contact_edit.text()
        hometown = self.hometown_edit.text()

        sql = "INSERT INTO employee (username, name, gender, password, contact, hometown) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (username, name, gender, password, contact, hometown))
        self.db.commit()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_label.insertPlainText(time+"：新增员工成功🥰\n")

    def update_employee(self):
        emp_id = self.emp_id_edit.text()
        username = self.username_edit.text()
        name = self.name_edit.text()
        gender = self.gender_edit.text()
        password = self.password_edit.text()
        contact = self.contact_edit.text()
        hometown = self.hometown_edit.text()

        sql = "UPDATE employee SET username=%s, name=%s, gender=%s, password=%s, contact=%s, hometown=%s WHERE emp_id=%s"
        self.cursor.execute(sql, (username, name, gender, password, contact, hometown, emp_id))
        self.db.commit()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_label.insertPlainText(time + "：更新员工成功🥰\n")

    def delete_employee(self):
        emp_id = self.emp_id_edit.text()

        sql = "DELETE FROM employee WHERE emp_id=%s"
        self.cursor.execute(sql, (emp_id,))
        self.db.commit()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_label.insertPlainText(time + "：删除员工成功🥰\n")

    def on_action_combo_changed(self, index):
        if index == 0:
            self.emp_id_edit.setEnabled(False)
            self.username_edit.setText("")
            self.name_edit.setText("")
            self.gender_edit.setText("")
            self.password_edit.setText("")
            self.contact_edit.setText("")
            self.hometown_edit.setText("")
            self.submit_btn.setText("新增员工")
            self.submit_btn.clicked.disconnect()
            self.submit_btn.clicked.connect(self.add_employee)
        elif index == 1:
            self.emp_id_edit.setEnabled(True)
            self.username_edit.setEnabled(True)
            self.name_edit.setEnabled(True)
            self.gender_edit.setEnabled(True)
            self.password_edit.setEnabled(True)
            self.contact_edit.setEnabled(True)
            self.hometown_edit.setEnabled(True)
            self.submit_btn.setText("更新员工")
            self.submit_btn.clicked.disconnect()
            self.submit_btn.clicked.connect(self.update_employee)
        elif index == 2:
            self.emp_id_edit.setEnabled(True)
            self.username_edit.setEnabled(False)
            self.name_edit.setEnabled(False)
            self.gender_edit.setEnabled(False)
            self.password_edit.setEnabled(False)
            self.contact_edit.setEnabled(False)
            self.hometown_edit.setEnabled(False)
            self.submit_btn.setText("删除员工")
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
    ex = Emp_edit()
    sys.exit(app.exec_())