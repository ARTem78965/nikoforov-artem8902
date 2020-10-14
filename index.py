import sys, orb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QLineEdit, QPushButton, QFormLayout


class dbConnect(orb.Table, QDialog):
    __db_columns__ = [
        orb.Column(orb.ColumnType.String, 'username'),
        orb.Column(orb.ColumnType.String, 'password'),
        orb.Column(orb.ColumnType.Boolean, 'active')
    ]
    db = orb.Database('registr')                        # db name
    db.setUsername('postgres')                          # db user name
    db.setPassword('A331166a')                          # password
    db.setHost('localhost')                             # host
    db.setPort(5432)                                    # port

    orb.Orb.instance().registerDatabase(db)
    db.sync(dryRun=False)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setMinimumWidth(480)
        self.setMinimumHeight(389)
        vbox = QVBoxLayout()
        label = QLabel("Ваши данные внесены в базу данных!")
        label.setFont(QtGui.QFont("Times News Romans", 20))
        vbox.addWidget(label)
        self.setLayout(vbox)


class login(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.fn = QLineEdit()
        self.fn.setObjectName("name")
        self.fn.setText("")

        self.ln = QLineEdit()
        self.ln.setObjectName("password")
        self.ln.setText("")

        self.submit = QPushButton()
        self.submit.setObjectName("button")
        self.submit.setText("Войти")

        layout = QFormLayout()
        layout.addWidget(self.fn)
        layout.addWidget(self.ln)
        layout.addWidget(self.submit)

        self.setLayout(layout)
        self.submit.clicked.connect(self.Button2Click)

    def Button2Click(self, MainWindow):
        self.m = dbConnect()
        self.m.show()
        self.close()


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(150, 310, 191, 51))
        self.Button.clicked.connect(self.Button1Click)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Button.setFont(font)
        self.Button.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 110, 211, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 160, 211, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 210, 211, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.Button.setText(_translate("MainWindow", "Registr"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Внесите свои данные"))

    def Button1Click(self, MainWindow):
        self.l = login()
        self.l.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
