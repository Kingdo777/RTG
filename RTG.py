# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\RTG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 630))
        MainWindow.setMaximumSize(QtCore.QSize(850, 630))
        MainWindow.setSizeIncrement(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 641, 391))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 400, 831, 36))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.t_15 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t_15.setInputMask("")
        self.t_15.setAlignment(QtCore.Qt.AlignCenter)
        self.t_15.setPlaceholderText("")
        self.t_15.setObjectName("t_15")
        self.horizontalLayout.addWidget(self.t_15)
        self.t0 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t0.setAlignment(QtCore.Qt.AlignCenter)
        self.t0.setPlaceholderText("")
        self.t0.setObjectName("t0")
        self.horizontalLayout.addWidget(self.t0)
        self.t30 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t30.setAlignment(QtCore.Qt.AlignCenter)
        self.t30.setPlaceholderText("")
        self.t30.setObjectName("t30")
        self.horizontalLayout.addWidget(self.t30)
        self.t60 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t60.setAlignment(QtCore.Qt.AlignCenter)
        self.t60.setPlaceholderText("")
        self.t60.setObjectName("t60")
        self.horizontalLayout.addWidget(self.t60)
        self.t90 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t90.setAlignment(QtCore.Qt.AlignCenter)
        self.t90.setPlaceholderText("")
        self.t90.setObjectName("t90")
        self.horizontalLayout.addWidget(self.t90)
        self.t120 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t120.setAlignment(QtCore.Qt.AlignCenter)
        self.t120.setPlaceholderText("")
        self.t120.setObjectName("t120")
        self.horizontalLayout.addWidget(self.t120)
        self.t180 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t180.setAlignment(QtCore.Qt.AlignCenter)
        self.t180.setPlaceholderText("")
        self.t180.setObjectName("t180")
        self.horizontalLayout.addWidget(self.t180)
        self.t240 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.t240.setAlignment(QtCore.Qt.AlignCenter)
        self.t240.setPlaceholderText("")
        self.t240.setObjectName("t240")
        self.horizontalLayout.addWidget(self.t240)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 20, 181, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gfr = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gfr.setMinimumSize(QtCore.QSize(20, 40))
        self.gfr.setMaximumSize(QtCore.QSize(57, 16777215))
        self.gfr.setAlignment(QtCore.Qt.AlignCenter)
        self.gfr.setObjectName("gfr")
        self.horizontalLayout_3.addWidget(self.gfr)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.uge = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.uge.setMinimumSize(QtCore.QSize(0, 40))
        self.uge.setMaximumSize(QtCore.QSize(57, 16777215))
        self.uge.setAlignment(QtCore.Qt.AlignCenter)
        self.uge.setObjectName("uge")
        self.horizontalLayout_4.addWidget(self.uge)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.RTG_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.RTG_PushButton.setGeometry(QtCore.QRect(660, 310, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RTG_PushButton.setFont(font)
        self.RTG_PushButton.setObjectName("RTG_PushButton")
        self.RTG_label = QtWidgets.QLabel(self.centralwidget)
        self.RTG_label.setGeometry(QtCore.QRect(10, 490, 831, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.RTG_label.setFont(font)
        self.RTG_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RTG_label.setObjectName("RTG_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 440, 831, 36))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.bg_15 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg_15.setInputMask("")
        self.bg_15.setAlignment(QtCore.Qt.AlignCenter)
        self.bg_15.setObjectName("bg_15")
        self.horizontalLayout_2.addWidget(self.bg_15)
        self.bg0 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg0.setAlignment(QtCore.Qt.AlignCenter)
        self.bg0.setObjectName("bg0")
        self.horizontalLayout_2.addWidget(self.bg0)
        self.bg30 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg30.setAlignment(QtCore.Qt.AlignCenter)
        self.bg30.setObjectName("bg30")
        self.horizontalLayout_2.addWidget(self.bg30)
        self.bg60 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg60.setAlignment(QtCore.Qt.AlignCenter)
        self.bg60.setObjectName("bg60")
        self.horizontalLayout_2.addWidget(self.bg60)
        self.bg90 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg90.setAlignment(QtCore.Qt.AlignCenter)
        self.bg90.setObjectName("bg90")
        self.horizontalLayout_2.addWidget(self.bg90)
        self.bg120 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg120.setAlignment(QtCore.Qt.AlignCenter)
        self.bg120.setObjectName("bg120")
        self.horizontalLayout_2.addWidget(self.bg120)
        self.bg180 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg180.setAlignment(QtCore.Qt.AlignCenter)
        self.bg180.setObjectName("bg180")
        self.horizontalLayout_2.addWidget(self.bg180)
        self.bg240 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.bg240.setAlignment(QtCore.Qt.AlignCenter)
        self.bg240.setObjectName("bg240")
        self.horizontalLayout_2.addWidget(self.bg240)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.Reset_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_PushButton.setGeometry(QtCore.QRect(660, 140, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Reset_PushButton.setFont(font)
        self.Reset_PushButton.setObjectName("Reset_PushButton")
        self.Clean_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Clean_PushButton.setGeometry(QtCore.QRect(660, 220, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Clean_PushButton.setFont(font)
        self.Clean_PushButton.setObjectName("Clean_PushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_7.setText(_translate("MainWindow", " t???"))
        self.t_15.setText(_translate("MainWindow", "-15"))
        self.t0.setText(_translate("MainWindow", "0"))
        self.t30.setText(_translate("MainWindow", "30"))
        self.t60.setText(_translate("MainWindow", "60"))
        self.t90.setText(_translate("MainWindow", "90"))
        self.t120.setText(_translate("MainWindow", "120"))
        self.t180.setText(_translate("MainWindow", "180"))
        self.t240.setText(_translate("MainWindow", "240"))
        self.label_6.setText(_translate("MainWindow", "min  "))
        self.label.setText(_translate("MainWindow", "GFR???"))
        self.gfr.setText(_translate("MainWindow", "100"))
        self.gfr.setPlaceholderText(_translate("MainWindow", "ml/min"))
        self.label_2.setText(_translate("MainWindow", "ml/min"))
        self.label_3.setText(_translate("MainWindow", "UGE???"))
        self.uge.setText(_translate("MainWindow", "10"))
        self.uge.setPlaceholderText(_translate("MainWindow", "g"))
        self.label_4.setText(_translate("MainWindow", "g"))
        self.RTG_PushButton.setText(_translate("MainWindow", "?????????RTG"))
        self.RTG_label.setText(_translate("MainWindow", "RTG = ???(mg/dl)"))
        self.label_8.setText(_translate("MainWindow", "BG???"))
        self.bg_15.setText(_translate("MainWindow", "158"))
        self.bg_15.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg0.setText(_translate("MainWindow", "156"))
        self.bg0.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg30.setText(_translate("MainWindow", "195"))
        self.bg30.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg60.setText(_translate("MainWindow", "225"))
        self.bg60.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg90.setText(_translate("MainWindow", "235"))
        self.bg90.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg120.setText(_translate("MainWindow", "225"))
        self.bg120.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg180.setText(_translate("MainWindow", "200"))
        self.bg180.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.bg240.setText(_translate("MainWindow", "160"))
        self.bg240.setPlaceholderText(_translate("MainWindow", "mg/dl"))
        self.label_5.setText(_translate("MainWindow", "mg/dl"))
        self.Reset_PushButton.setText(_translate("MainWindow", "Reset"))
        self.Clean_PushButton.setText(_translate("MainWindow", "Clean"))
