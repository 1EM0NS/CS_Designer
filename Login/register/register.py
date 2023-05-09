from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PyQt5.QtGui import QPalette, QLinearGradient, QColor, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, \
    QMainWindow, QFrame
from qfluentwidgets import InfoBar, InfoBarPosition,PushButton,LineEdit
import condition
import pymysql
class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        print("进入注册")
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置透明背景
        self.setStyleSheet('''
                    QDialog {
                        background: transparent;
                    }
                    
QFrame {
    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #724CAF, stop: 1 rgba(250, 128, 114, 0.9));
    border-radius: 10px;
}
                    QLabel, QLineEdit {
                        background: rgba(255, 255, 255, 0.6);
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton {
                        background: #FFA07A;
                        border-radius: 5px;
                        padding: 5px;
                        min-width: 50px;
                    }
                    QPushButton:hover {
                        background: #FF8C69;
                    }
                ''')

        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(50, 50, 300, 300))

        layout = QVBoxLayout(self.frame)
        self.username_label = QLabel('在下方输入你要注册的用户名：')
        self.username_edit = LineEdit()
        self.password_label = QLabel('在下方输入你要注册的密码：')
        self.password_edit = LineEdit()
        self.password_edit.setEchoMode(LineEdit.Password)
        self.password_confirm_label = QLabel('确认你的密码：')
        self.password_confirm_edit = LineEdit()
        self.password_confirm_edit.setEchoMode(LineEdit.Password)
        self.submit_button = PushButton('注册')
        self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button = PushButton('退出')
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_button.clicked.connect(self.register)
        self.cancel_button.clicked.connect(self.cancel)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.password_confirm_label)
        layout.addWidget(self.password_confirm_edit)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.cancel_button)

    def register(self):
        # 获取用户名和密码

        username = self.username_edit.text()
        password = self.password_edit.text()
        password_confirm = self.password_confirm_edit.text()

        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee WHERE username = %s", (username,))
        employee = cursor.fetchone()
        cursor.execute("SELECT * FROM customer WHERE username = %s", (username,))
        customer = cursor.fetchone()
        db.close()
        if not username or not password or not password_confirm:
            InfoBar.error(
                title='失败',
                content="用户名或密码不能为空！",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=800,
                parent=self
            )
            return

        if password != password_confirm:
            InfoBar.error(
                title='失败',
                content="两次密码不一致！",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=800,
                parent=self
            )
            return
        if employee or customer:
            InfoBar.error(
                title='失败',
                content="用户名已存在！",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=800,
                parent=self
            )
            return
        else:

            self.add_customer(username, password)
            InfoBar.success(
                title='成功',
                content="注册成功！",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=800,
                parent=self
            )
            self.username_edit.clear()
            self.password_edit.clear()
            self.password_confirm_edit.clear()
            return

    def cancel(self):
        #动画淡出对话框
        self.close()

    def add_customer(self, username, password):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='1784',
                             database='餐饮管理系统')
        cursor = db.cursor()
        cursor.execute("INSERT INTO customer(username, password,name,contact,gender,id_card,ethnicity,hometown) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (username, password,'1','1','Male','1','1','1'))
        db.commit()
        db.close()
    #出现动画
    def show_animation(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(0)
        main_opacity.setEndValue(1)
        main_opacity.setDuration(1000)
        main_opacity.start()
        self.animation.start()

if __name__ == '__main__':
    app = QApplication([])
    main_window = RegisterDialog()
    main_window.show()
    app.exec()