from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from qfluentwidgets import InfoBarIcon, InfoBar, InfoBarPosition
import resources_rc
from register.register import RegisterDialog
from navigation.manage import Window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 676)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)

        self.frame_6.setStyleSheet \
            ("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgba(255, 255, 255,230), stop:1 rgba(50, 50, 200,245));\n"
             "border-radius:20px 20px 20px 20px;\n""blur: 10px;\n")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 36)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.frame_6)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # fram透明（上方）
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(381, 481))
        self.frame_4.setMaximumSize(QtCore.QSize(381, 481))
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")  # 中间窗口
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 381, 481))
        self.frame_2.setMinimumSize(QtCore.QSize(381, 481))
        self.frame_2.setMaximumSize(QtCore.QSize(381, 481))
        self.frame_2.setStyleSheet("QFrame{image: url(:/svg/未标题-1.png);\n"
                                   "\n"
                                   "background-color: rgba(255, 255, 255, 0);}")

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 20, 341, 441))
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "    image: none;\n"
                                   "background-color: rgba(255, 255, 255, 20%);\n"
                                   "border-radius:6px \n"
                                   "}\n"
                                   "QLabel{\n"
                                   "\n"
                                   "    background-color: rgba(255, 255, 255, 0);\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(24, 24, 24, 8)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 64))
        self.widget.setStyleSheet("image: url(:/svg/img/svg/闪电-实.png);")
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_10.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 24)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_10)
        self.label.setMaximumSize(QtCore.QSize(16777215, 26777))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_7.setStyleSheet("border-radius:16px ;\n"
                                   "background-color: rgba(255, 255, 255, 51);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_2 = QtWidgets.QWidget(self.frame_7)
        self.widget_2.setMaximumSize(QtCore.QSize(18, 18))
        self.widget_2.setStyleSheet("image: url(:/buttom_white/img/buttom_white/发送邮件_send-email.svg);\n"
                                    "background-color: rgba(255, 255, 255, 0);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6.addWidget(self.widget_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    background-color: rgba(255, 255, 255, 0);\n"
                                    "    selection-color: rgb(34, 34, 34);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 9)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_8.setStyleSheet("border-radius:16px ;\n"
                                   "background-color: rgba(255, 255, 255, 51);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_3 = QtWidgets.QWidget(self.frame_8)
        self.widget_3.setMaximumSize(QtCore.QSize(18, 18))
        self.widget_3.setStyleSheet("image: url(:/buttom_white/img/buttom_white/电子锁开_electronic-locks-open.svg);\n"
                                    "background-color: rgba(255, 255, 255, 0);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_7.addWidget(self.widget_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    background-color: rgba(255, 255, 255, 0);\n"
                                      "    selection-color: rgb(34, 34, 34);\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 9)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(84, 42, 155);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton.clicked.connect(self.tips)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 48))
        self.pushButton_2.clicked.connect(self.login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setStyleSheet("""
                    QPushButton {
                        background-color: black;
                        border: none;
                        color: white;
                        border-radius: 10px;
                        padding: 10px 20px;
                        opacity: 0.8;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255,150);
                        color: black;
                        border: 2px solid white;
                        opacity: 1;
                        blur: 2px;
                    }
                    QPushButton:pressed {
                        background-color: rgba(255, 255, 255,150);
                        blur: 2px;
                        border: 2px solid black;
                    }
                """)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(84, 42, 155);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.register)
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addWidget(self.frame_4)
        spacerItem7 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        # fram_5（下方）透明
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setMinimumSize(QtCore.QSize(48, 48))
        self.pushButton_4.setMaximumSize(QtCore.QSize(48, 48))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    border-radius:24px ;\n"
                                        "    background-color: rgba(251, 252, 255, 51);\n"
                                        "\n"
                                        "}")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttom_white/img/buttom_white/github _github.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setMinimumSize(QtCore.QSize(48, 48))
        self.pushButton_5.setMaximumSize(QtCore.QSize(48, 48))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    border-radius:24px ;\n"
                                        "    background-color: rgba(251, 252, 255, 51);\n"
                                        "\n"
                                        "}")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttom_white/img/buttom_white/gitlab_gitlab.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout.addWidget(self.frame_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "餐饮管理系统"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "密码"))

        self.checkBox.setText(_translate("MainWindow", "记住我"))
        self.pushButton.setText(_translate("MainWindow", "忘记密码？"))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_3.setText(_translate("MainWindow", "没有账户?"))
        self.pushButton_3.setText(_translate("MainWindow", "添加一个账户"))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_4.setText(_translate("MainWindow", "SIGN-IN PLATFORM"))

    def employee_login(self, employee):
        # 执行员工登录操作
        InfoBar.success(
            title='成功',
            content="登录成功，正在进入系统...",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )
        #todo: 进入系统
        c = Window()
        c.show()
        self.close()
        print("员工登录成功")
    def tips(self):
        InfoBar.warning(
            title='你好',
            content="忘记了也是没办法的事情呢",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )
    def customer_login(self, customer):
        # 执行客户登录操作
        InfoBar.success(
            title='成功',
            content="登录成功，正在进入系统...",
            orient=QtCore.Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )
        #todo: 进入系统
        print("客户登录成功")

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "" or password == "":
            InfoBar.error(
                title='警告',
                content="您的用户名或密码为空，请重新输入！",
                orient=QtCore.Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,  # won't disappear automatically
                parent=self,

            )
            return
        else:
            import pymysql
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1784',
                                 database='餐饮管理系统')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM employee WHERE username = %s", (username,))
            employee = cursor.fetchone()
            cursor.execute("SELECT * FROM customer WHERE username = %s", (username,))
            customer = cursor.fetchone()

            if employee is None and customer is None:
                InfoBar.error(
                    title='警告',
                    content="未注册的账户！",
                    orient=QtCore.Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=3000,  # won't disappear automatically
                    parent=self,

                )

                # 检查密码是否正确
            if employee is not None and employee[4] != password or customer is not None and customer[8] != password:
                InfoBar.error(
                    title='登录失败',
                    content="密码错误！",
                    orient=QtCore.Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=3000,  # won't disappear automatically
                    parent=self,

                )
                return

                # 根据用户类型执行不同的操作
            if employee is not None:
                self.employee_login(employee)
            elif customer is not None:
                self.customer_login(customer)

            db.close

    def register(self):
        # 执行注册操作
        register_dialog = RegisterDialog()
        register_dialog.show_animation()
        register_dialog.exec_()
