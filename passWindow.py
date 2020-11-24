# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView, QInputDialog, QLineEdit
import solution,randomStr,loginPass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # 窗口login
        icon_windows = QtGui.QIcon()
        icon_windows.addPixmap(QtGui.QPixmap("img/closeWall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # 统一弹窗对象,设置图标好像不起作用，后面再来看看
        self.messageBox = QMessageBox()
        self.messageBox.setWindowIcon(icon_windows)
        # self.messageBox.
        # self.messageBox.setIconPixmap(icon_windows)

        # 设置登录密码，就不多弄一个界面了，直接弹窗输入密码确认
        self.loginFun()

        self.so = solution.manageThePass()
        self.rds = randomStr.createRandomStr()
        # 路径先写在这里
        frontPath = './passfile'
        # 存放列表文件名
        self.fileList = os.listdir(frontPath)
        # 存放列表文件的完整路径
        self.totalFileList = []
        for f in self.fileList:
            self.totalFileList.append(frontPath + '/' + f)
        print(self.totalFileList)
        self.path = self.totalFileList[0] if len(self.totalFileList) > 0 else ''
        # self.path = '' if len(fileList) < 1 else frontPath + '/' + fileList[0]
        # print(self.path)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 540)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(9)
        MainWindow.setFont(font)
        # 禁止调整窗口大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 8, 91, 41))

        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(2)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        font_10 = QtGui.QFont()
        font_10.setFamily("Adobe 宋体 Std L")
        font_10.setPointSize(10)
        font_12 = QtGui.QFont()
        font_12.setFamily("Adobe 宋体 Std L")
        font_12.setPointSize(12)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.pushButton_9.setFont(font_10)
        self.pushButton_9.setObjectName("pushButton_10")
        self.pushButton_9.clicked.connect(self.newEmptyFileFun)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setFont(font_12)
        self.comboBox.setGeometry(QtCore.QRect(70, 55, 151, 21))
        self.comboBox.addItems(self.fileList)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged[int].connect(self.sullDownFun)

        # self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_8.setFont(font_12)
        # self.lineEdit_8.setGeometry(QtCore.QRect(70, 55, 151, 21))
        # self.lineEdit_8.setObjectName("lineEdit_8")
        # self.lineEdit_8.setText(self.path)
        # self.lineEdit_8.setReadOnly(True)
        # self.lineEdit_8.setEnabled(False)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 55, 41, 21))
        self.label_9.setFont(font_12)
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 55, 51, 21))
        self.pushButton_7.setFont(font_10)
        self.pushButton_7.clicked.connect(self.loadFileFun)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 55, 51, 21))
        self.pushButton_8.setFont(font_10)
        self.pushButton_8.clicked.connect(self.transformFun)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setFont(font_12)
        self.lineEdit.setGeometry(QtCore.QRect(70, 90, 191, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 41, 21))
        self.label_2.setFont(font_12)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 90, 61, 21))
        self.pushButton.setFont(font_10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchFun)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 125, 321, 151))
        self.listView.setFont(font_12)
        # 禁止拖拽
        self.listView.setDragEnabled(False)
        # 禁止双击可编辑
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 41, 21))
        self.label_3.setFont(font_12)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 41, 21))
        self.label_4.setFont(font_12)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setFont(font_12)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 300, 201, 21))
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setFont(font_12)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 330, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 300, 51, 21))
        self.pushButton_2.setFont(font_10)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.updateFun)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 330, 51, 21))
        self.pushButton_3.setFont(font_10)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.deleteFun)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 41, 21))
        self.label_5.setFont(font_12)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setFont(font_12)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 380, 201, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 41, 21))
        self.label_6.setFont(font_12)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setFont(font_12)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 410, 201, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 380, 51, 51))
        self.pushButton_5.setFont(font_10)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.insertFun)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 450, 141, 21))
        self.label_7.setFont(font_12)
        self.label_7.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setFont(font_12)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 450, 30, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setValidator(QIntValidator(0, 99))
        self.check_1 = QtWidgets.QCheckBox(self.centralwidget)
        # self.check_1.stateChanged.connect(self.chooseFun)
        self.check_1.setGeometry(QtCore.QRect(196, 450, 45, 21))
        self.check_1.setObjectName("check_1")
        self.check_2 = QtWidgets.QCheckBox( self.centralwidget)
        # self.check_2.stateChanged.connect(self.chooseFun)
        self.check_2.setGeometry(QtCore.QRect(246, 450, 45, 21))
        self.check_2.setObjectName("check_2")
        self.check_3 = QtWidgets.QCheckBox(self.centralwidget)
        # self.check_3.stateChanged.connect(self.chooseFun)
        self.check_3.setGeometry(QtCore.QRect(296, 450, 45, 21))
        self.check_3.setObjectName("check_3")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 480, 61, 21))
        self.label_8.setFont(font_12)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setFont(font_12)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 480, 191, 21))
        self.lineEdit_7.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 480, 51, 21))
        self.pushButton_6.setFont(font_10)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.getRandomFun)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(icon_windows)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "密码管理"))
        self.label.setText(_translate("MainWindow", "密码提取"))
        self.label_2.setText(_translate("MainWindow", "名称："))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.label_3.setText(_translate("MainWindow", "名称："))
        self.label_4.setText(_translate("MainWindow", "密码："))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.label_6.setText(_translate("MainWindow", "名称："))
        self.pushButton_5.setText(_translate("MainWindow", "添加"))
        self.label_7.setText(_translate("MainWindow", "输入长度和类型："))
        self.check_1.setText(_translate("MainWindow", "数字"))
        self.check_2.setText(_translate("MainWindow", "字母"))
        self.check_3.setText(_translate("MainWindow", "符号"))
        self.label_8.setText(_translate("MainWindow", "随机数："))
        self.pushButton_6.setText(_translate("MainWindow", "生成"))
        self.label_9.setText(_translate("MainWindow", "路径："))
        self.pushButton_7.setText(_translate("MainWindow", "导入"))
        self.pushButton_8.setText(_translate("MainWindow", "转化"))
        self.pushButton_9.setText(_translate("MainWindow", "新增文本"))

    # 方法区
    def searchFun(self):
        text = self.lineEdit.text()
        if text.strip() == '' or text == None:
            self.clearFun()
            # self.messageBox.about(QMainWindow(), "警告", "输入内容不能为空")
            return - 1
        text = text.strip()
        if(text == 'all'):
            text = ''
        self.dict = self.so.decryptByLine(self.path,text)
        if self.dict == -1:
            self.messageBox.about(QMainWindow(), "警告", "检索文件必须为密文，请检查你的路径文件！")
            return -1
        if len(self.dict) < 1:
            self.messageBox.about(QMainWindow(), "提示", "搜索内容为空！")
        items = [key for key in self.dict]
        listModel = QStringListModel()
        listModel.setStringList(items)
        self.listView.setModel(listModel)
        self.listView.clicked.connect(self.listFun)

    def updateFun(self):
        text_2 = self.lineEdit_2.text()
        text_3 = self.lineEdit_3.text()
        if text_2.strip() == '' or text_2.strip() == None or text_3.strip() == '' or text_3.strip() == None:
            self.messageBox.about(QMainWindow(), "警告", "输入内容不能为空！")
            return -1
        rec_code = self.messageBox.warning(QMainWindow(),"警告框","修改名称为：'" + text_2 + "'的密码为：'" + text_3 + "'",self.messageBox.Yes | self.messageBox.No)
        if rec_code == self.messageBox.Yes:
            result = self.so.loadAndTransAndUpdate(2, text_3, text_2, self.path)
            if result == 1:
                # 判断搜索框中是否有内容，如果有调用搜索方法
                text = self.lineEdit.text()
                if text.strip() == '' or text == None:
                    pass
                else:
                    self.searchFun()
            else:
                self.messageBox.about(QMainWindow(), "警告", "更新失败！")

    def deleteFun(self):
        text_2 = self.lineEdit_2.text()
        text_3 = self.lineEdit_3.text()
        if text_2.strip() == '' or text_2.strip() == None or text_3.strip() == '' or text_3.strip() == None:
            self.messageBox.about(QMainWindow(), "警告", "输入内容不能为空！")
            return -1
        rec_code = self.messageBox.warning(QMainWindow(), "警告框", "删除名称为：'" + text_2 + "'",self.messageBox.Yes | self.messageBox.No)
        if rec_code == self.messageBox.Yes:
            result = self.so.loadAndTransAndUpdate(-1, text_3, text_2, self.path)
            if result == 1:
                # 判断搜索框中是否有内容，如果有调用搜索方法
                text = self.lineEdit.text()
                if text.strip() == '' or text == None:
                    pass
                else:
                    self.searchFun()
            else:
                self.messageBox.about(QMainWindow(), "警告", "删除失败！")

    def insertFun(self):
        text_4 = self.lineEdit_4.text()
        text_5 = self.lineEdit_5.text()
        if text_4.strip() == '' or text_4.strip() == None or text_5.strip() == '' or text_5.strip() == None:
            self.messageBox.about(QMainWindow(), "警告", "输入内容不能为空！")
            return -1
        rec_code = self.messageBox.information(QMainWindow(), "提示框", "增加名称为：'" + text_4 + "'，密码为：'" + text_5 + "'", self.messageBox.Yes | self.messageBox.No)
        if rec_code == self.messageBox.Yes:
            result = self.so.loadAndTransAndUpdate(1, text_5, text_4, self.path)
            if result == 1:
                # 判断搜索框中是否有内容，如果有调用搜索方法
                text = self.lineEdit.text()
                if text.strip() == '' or text == None:
                    pass
                else:
                    self.searchFun()
            elif result == -2:
                self.messageBox.about(QMainWindow(), "警告", "已存在该名称！")
            else:
                self.messageBox.about(QMainWindow(), "警告", "添加失败！")

    def listFun(self, index):
        name = index.data()
        password = self.dict[name]
        self.lineEdit_2.setText(name)
        self.lineEdit_3.setText(password)

    # def chooseFun(self):
    #     choice_1 = 1 if self.check_1.isChecked() else 0
    #     choice_2 = 1 if self.check_2.isChecked() else 0
    #     choice_3 = 1 if self.check_3.isChecked() else 0
    #     print(self.choice_1+self.choice_2+self.choice_3)

    def getRandomFun(self):
        num = self.lineEdit_6.text()
        if num.isdigit() == False:
            self.messageBox.about(QMainWindow(), "警告", "输入内容需为数字！")
            return -1
        choice_1 = 1 if self.check_1.isChecked() else 0
        choice_2 = 1 if self.check_2.isChecked() else 0
        choice_3 = 1 if self.check_3.isChecked() else 0
        s = self.rds.getRandomStr(int(num),choice_1,choice_2,choice_3)
        if s == -1:
            self.messageBox.about(QMainWindow(), "警告", "输入内容有误，生成失败！")
        else:
            self.lineEdit_7.setText(s)

    # 导入文本
    def loadFileFun(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(QMainWindow(), "选择文件", os.getcwd(),"All Files(*);;Text Files(*.txt)")
        # self.lineEdit_8.setText(fileName)
        tailFileName = fileName.split('/')[-1]
        self.comboBox.addItem(tailFileName)
        self.totalFileList.append(fileName)
        self.comboBox.setCurrentIndex(len(self.totalFileList) - 1)
        self.path = fileName
        # print(self.path)
        # 清空
        self.clearFun()

    # 转化文本
    def transformFun(self):
        # textPath = self.lineEdit_8.text()
        textIndex = self.comboBox.currentIndex()
        textPath = self.totalFileList[textIndex]
        pathEn = self.so.loadFileAndencrypt(textPath)
        if pathEn == -1:
            self.messageBox.about(QMainWindow(), "警告", "文本转化失败！")
        else:
            self.totalFileList.append(pathEn)
            tailFileName = pathEn.split('/')[-1]
            self.comboBox.addItem(tailFileName)
            self.comboBox.setCurrentIndex(len(self.totalFileList) - 1)
            self.path = pathEn
            # self.lineEdit_8.setText(pathEn)

    # 清空文本框
    def clearFun(self):
        # 清空列表
        items = []
        listModel = QStringListModel()
        listModel.setStringList(items)
        self.listView.setModel(listModel)
        # 清空文本框
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

    # 登录弹窗
    def loginFun(self):
        LOGIN, ok = QInputDialog.getText(MainWindow, '登录', '请输入密码：', QLineEdit.Password)
        if ok:
            if str(LOGIN) == str(loginPass.LOGINPASS):
                self.messageBox.about(QMainWindow(), "提示", "欢迎使用密码管理程序")
            else:
                self.messageBox.about(QMainWindow(), "提示", "密码错误请重新尝试")
                self.loginFun()
        else:
            sys.exit(484666)

    # 下拉事件
    def sullDownFun(self,i):
        # print("i : " , i, "data: ", self.totalFileList[i])
        self.path = self.totalFileList[i]

    # 新建空文本
    def newEmptyFileFun(self):
        FILENAME, ok = QInputDialog.getText(MainWindow, '新建文本', '请输入文本名称：')
        if ok:
            if(FILENAME.strip() != '' or FILENAME is not None):
                f = ''
                try:
                    tailFileName = FILENAME.strip() + '.txt'
                    fileName = './passfile/' + tailFileName
                    f = open(fileName, 'w')
                    self.totalFileList.append(tailFileName)
                    self.comboBox.addItem(tailFileName)
                    self.comboBox.setCurrentIndex(len(self.totalFileList) - 1)
                    self.path = fileName
                    self.messageBox.about(QMainWindow(), "提示", "文本创建成功")
                except Exception as e:
                    print(e)
                    self.messageBox.about(QMainWindow(), "警告", "文本创建失败")
                finally:
                    if f:
                        f.close()
            else:
                self.messageBox.about(QMainWindow(), "警告", "创建文本名称不规范")

    # 命名重复循环添加i
    def sameNameAddI(self, name):
        flag = 0
        while flag < 10:
            if name in self.fileList:
                if '(' in name:
                    pattern = re.compile(r'\(\d+\)')
                    nums = pattern.findall(name)
                    if nums > 0:
                        numAndBracket =nums[-1]
                        print(numAndBracket)
                        # 去掉前后括号
                        num = int(numAndBracket[1:-1])
                        name = name.replace(numAndBracket, "(" + str(num+1) + ")")
                else:
                    # 反转替换再反转
                    name = name[::-1].replace('.', '.(1)', 1)[::-1]
            else:
                return name
            flag += 1
        return -1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
