import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
import pymysql
from qfluentwidgets import InfoBar, InfoBarPosition,LineEdit,PushButton,TextEdit,SpinBox

class Cust_edit(QWidget):
    def __init__(self):
        super().__init__()

        # 创建界面上的各个控件
        self.lbl_id = TextEdit()
        self.lbl_id.setText('1.输入客户id获取客户信息\n2.直接修改信息后提交即可')
        self.lbl_id.setStyleSheet(
            'QTextEdit{background-color:rgba(255,255,100,0.1);border-radius:5px;padding:5px;font-size:20px;font-family:"Microsoft YaHei", sans-serif;}'
            'QTextEdit:hover{background-color:rgba(255,100,100,0.1);border-radius:5px;padding:5px;font-size:20px;}')
        self.lbl_id.setReadOnly(True)

        self.edit_id = SpinBox()
        self.btn_search = PushButton('客户信息获取')
        self.lbl_name = QLabel('姓名：')
        self.edit_name = LineEdit()
        self.lbl_contact = QLabel('联系方式：')
        self.edit_contact = LineEdit()
        self.lbl_gender = QLabel('性别：')
        self.edit_gender = LineEdit()
        self.lbl_id_card = QLabel('身份证号：')
        self.edit_id_card = LineEdit()
        self.lbl_ethnicity = QLabel('民族：')
        self.edit_ethnicity = LineEdit()
        self.lbl_hometown = QLabel('籍贯：')
        self.edit_hometown = LineEdit()
        self.lbl_username = QLabel('用户名：')
        self.edit_username = LineEdit()
        self.lbl_password = QLabel('密码：')
        self.edit_password = LineEdit()
        self.btn_submit = PushButton('提交')

        # 创建布局并将控件添加到布局中
        hbox_id = QHBoxLayout()
        hbox_id.addWidget(self.lbl_id)
        hbox_id.addWidget(self.edit_id)
        hbox_id.addWidget(self.btn_search)
        hbox_name = QHBoxLayout()
        hbox_name.addWidget(self.lbl_name)
        hbox_name.addWidget(self.edit_name)
        hbox_contact = QHBoxLayout()
        hbox_contact.addWidget(self.lbl_contact)
        hbox_contact.addWidget(self.edit_contact)
        hbox_gender = QHBoxLayout()
        hbox_gender.addWidget(self.lbl_gender)
        hbox_gender.addWidget(self.edit_gender)
        hbox_id_card = QHBoxLayout()
        hbox_id_card.addWidget(self.lbl_id_card)
        hbox_id_card.addWidget(self.edit_id_card)
        hbox_ethnicity = QHBoxLayout()
        hbox_ethnicity.addWidget(self.lbl_ethnicity)
        hbox_ethnicity.addWidget(self.edit_ethnicity)
        hbox_hometown = QHBoxLayout()
        hbox_hometown.addWidget(self.lbl_hometown)
        hbox_hometown.addWidget(self.edit_hometown)
        hbox_username = QHBoxLayout()
        hbox_username.addWidget(self.lbl_username)
        hbox_username.addWidget(self.edit_username)
        hbox_password = QHBoxLayout()
        hbox_password.addWidget(self.lbl_password)
        hbox_password.addWidget(self.edit_password)
        hbox_submit = QHBoxLayout()
        hbox_submit.addStretch(1)
        hbox_submit.addWidget(self.btn_submit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_id)
        vbox.addLayout(hbox_name)
        vbox.addLayout(hbox_contact)
        vbox.addLayout(hbox_gender)
        vbox.addLayout(hbox_id_card)
        vbox.addLayout(hbox_ethnicity)
        vbox.addLayout(hbox_hometown)
        vbox.addLayout(hbox_username)
        vbox.addLayout(hbox_password)
        vbox.addLayout(hbox_submit)

        self.setLayout(vbox)

        # 绑定按钮点击事件
        self.btn_search.clicked.connect(self.search_customer_info)
        self.btn_submit.clicked.connect(self.submit_customer_info)

        # 设置窗口属性
        self.setWindowTitle('客户信息')
        self.setGeometry(300, 300, 400, 300)
    def search_customer_info(self):
        # 获取客户编号
        cust_id = self.edit_id.text()

        # 查询客户信息并显示在界面上

        cnx = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1784',
                                 database='餐饮管理系统')
        cursor = cnx.cursor()
        query = ("SELECT * FROM customer WHERE cust_id = %s")
        cursor.execute(query, (cust_id,))
        customer_info = cursor.fetchone()

        if customer_info:
                self.edit_name.setText(customer_info[1])
                self.edit_contact.setText(customer_info[2])
                self.edit_gender.setText(customer_info[3])
                self.edit_id_card.setText(customer_info[4])
                self.edit_ethnicity.setText(customer_info[5])
                self.edit_hometown.setText(customer_info[6])
                self.edit_username.setText(customer_info[7])
                self.edit_password.setText(customer_info[8])
        else:
                self.edit_name.setText('')
                self.edit_contact.setText('')
                self.edit_gender.setText('')
                self.edit_id_card.setText('')
                self.edit_ethnicity.setText('')
                self.edit_hometown.setText('')
                self.edit_username.setText('')
                self.edit_password.setText('')
                QMessageBox.information(self, '提示', '客户编号不存在！')
        cursor.close()
        cnx.close()

    def submit_customer_info(self):
        # 获取客户编号和修改后的客户信息
        cust_id = self.edit_id.text()
        name = self.edit_name.text()
        contact = self.edit_contact.text()
        gender = self.edit_gender.text()
        id_card = self.edit_id_card.text()
        ethnicity = self.edit_ethnicity.text()
        hometown = self.edit_hometown.text()
        username = self.edit_username.text()
        password = self.edit_password.text()

        # 更新客户信息
        try:
            cnx = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1784',
                                  database='餐饮管理系统')
            cursor = cnx.cursor()
            update_query = ("UPDATE customer SET name=%s, contact=%s, gender=%s, id_card=%s, ethnicity=%s, hometown=%s, username=%s, password=%s WHERE cust_id=%s")
            data = (name, contact, gender, id_card, ethnicity, hometown, username, password, cust_id)
            cursor.execute(update_query, data)
            cnx.commit()
            print(f"客户信息更新成功，客户编号为：{cust_id}")
            InfoBar.success(
                title='成功',
                content=f"客户信息更新成功，客户编号为：{cust_id}",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,  # won't disappear automatically
                parent=self,

            )
        except Exception as e:
            print(e)
            InfoBar.warning(
                title='警告',
                content=f"客户信息更新失败，客户编号为：{cust_id}",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,  # won't disappear automatically
                parent=self,

            )
            cnx.rollback()
            QMessageBox.information(self, '提示', '客户信息更新失败！')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    customer_info = Cust_edit()
    customer_info.show()
    sys.exit(app.exec_())