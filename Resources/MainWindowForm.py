# Form implementation generated from reading ui file 'MainController.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setFixedSize(377, 138)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pButtonPath = QtWidgets.QPushButton(self.centralwidget)
        self.pButtonPath.setGeometry(QtCore.QRect(230, 10, 141, 31))
        self.pButtonPath.setObjectName("pButtonPath")
        self.pButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pButtonStart.setGeometry(QtCore.QRect(230, 55, 141, 31))
        self.pButtonStart.setObjectName("pButtonStart")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 6, 211, 80))
        self.groupBox.setObjectName("groupBox")
        self.labelPath = QtWidgets.QLabel(self.groupBox)
        self.labelPath.setGeometry(QtCore.QRect(10, 20, 191, 51))
        self.labelPath.setText("")
        self.labelPath.setScaledContents(False)
        self.labelPath.setWordWrap(True)
        self.labelPath.setObjectName("labelPath")
        self.labelFound = QtWidgets.QLabel(self.centralwidget)
        self.labelFound.setGeometry(QtCore.QRect(10, 90, 361, 16))
        self.labelFound.setText("")
        self.labelFound.setObjectName("labelFound")
        self.checkBoxRec = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxRec.setGeometry(QtCore.QRect(230, 90, 141, 18))
        self.checkBoxRec.setObjectName("checkBoxRec")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_install = QtGui.QAction(MainWindow)
        self.menu_install.setObjectName("menu_install")
        self.menu_about = QtGui.QAction(MainWindow)
        self.menu_about.setObjectName("menu_about")
        self.menu_version = QtGui.QAction(MainWindow)
        self.menu_version.setObjectName("menu_version")
        self.menu_action_start = QtGui.QAction(MainWindow)
        self.menu_action_start.setObjectName("menu_action_start")
        self.menu_action_path = QtGui.QAction(MainWindow)
        self.menu_action_path.setObjectName("menu_action_path")
        self.menu_action_pdf = QtGui.QAction(MainWindow)
        self.menu_action_pdf.setObjectName("menu_action_pdf")
        self.menu_action_tiff = QtGui.QAction(MainWindow)
        self.menu_action_tiff.setObjectName("menu_action_tiff")
        self.menu_2.addAction(self.menu_action_pdf)
        self.menu_2.addAction(self.menu_action_tiff)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_action_path)
        self.menu.addAction(self.menu_action_start)
        self.menuHelp.addAction(self.menu_about)
        self.menuHelp.addAction(self.menu_version)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проект Конвертор"))
        self.pButtonPath.setText(_translate("MainWindow", "Указать путь к pdf"))
        self.pButtonStart.setText(_translate("MainWindow", "Конвертировать"))
        self.groupBox.setTitle(_translate("MainWindow", "Путь до папки с файлами pdf"))
        self.checkBoxRec.setText(_translate("MainWindow", "Рекурсивный обход"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Открыть папку"))
        self.menuHelp.setTitle(_translate("MainWindow", "Помощь"))
        self.action.setText(_translate("MainWindow", "Открыть папку tiff"))
        self.menu_install.setText(_translate("MainWindow", "Установка"))
        self.menu_about.setText(_translate("MainWindow", "О программе"))
        self.menu_version.setText(_translate("MainWindow", "Версия"))
        self.menu_action_start.setText(_translate("MainWindow", "Конвертировать"))
        self.menu_action_path.setText(_translate("MainWindow", "Указать путь к pdf"))
        self.menu_action_pdf.setText(_translate("MainWindow", "с файлами pdf"))
        self.menu_action_tiff.setText(_translate("MainWindow", "c файлами tiff"))