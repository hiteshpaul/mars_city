# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'habitat.ui'
#
# Created: Mon Jul  6 08:44:31 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(797, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 161, 561))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.mainGraphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.mainGraphicsView.setGeometry(QtCore.QRect(160, 0, 641, 551))
        self.mainGraphicsView.setObjectName(_fromUtf8("mainGraphicsView"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(179, 60, 281, 281))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.devicesListView = QtGui.QListView(self.verticalLayoutWidget_2)
        self.devicesListView.setObjectName(_fromUtf8("devicesListView"))
        self.verticalLayout_2.addWidget(self.devicesListView)
        self.addBranchDevices = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.addBranchDevices.setObjectName(_fromUtf8("addBranchDevices"))
        self.verticalLayout_2.addWidget(self.addBranchDevices)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 50, 191, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 183, 196))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.minButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.minButton.setChecked(True)
        self.minButton.setObjectName(_fromUtf8("minButton"))
        self.verticalLayout_3.addWidget(self.minButton)
        self.maxButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.maxButton.setObjectName(_fromUtf8("maxButton"))
        self.verticalLayout_3.addWidget(self.maxButton)
        self.avgButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.avgButton.setObjectName(_fromUtf8("avgButton"))
        self.verticalLayout_3.addWidget(self.avgButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.timeLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout.addWidget(self.timeLabel)
        self.timeLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.timeLineEdit.setObjectName(_fromUtf8("timeLineEdit"))
        self.horizontalLayout.addWidget(self.timeLineEdit)
        self.minutesLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.minutesLabel.setObjectName(_fromUtf8("minutesLabel"))
        self.horizontalLayout.addWidget(self.minutesLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.functionButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.functionButton.setObjectName(_fromUtf8("functionButton"))
        self.verticalLayout_3.addWidget(self.functionButton)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, 0, 621, 431))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.dataTab = QtGui.QWidget()
        self.dataTab.setObjectName(_fromUtf8("dataTab"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.dataTab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(29, 20, 191, 271))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.attributeName = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.attributeName.setObjectName(_fromUtf8("attributeName"))
        self.horizontalLayout_4.addWidget(self.attributeName)
        self.attributeValue = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.attributeValue.setText(_fromUtf8(""))
        self.attributeValue.setObjectName(_fromUtf8("attributeValue"))
        self.horizontalLayout_4.addWidget(self.attributeValue)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.listWidget = QtGui.QListWidget(self.dataTab)
        self.listWidget.setGeometry(QtCore.QRect(30, 10, 201, 291))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.dataTab)
        self.listWidget_2.setGeometry(QtCore.QRect(235, 11, 211, 291))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.tabWidget.addTab(self.dataTab, _fromUtf8(""))
        self.summaryTab = QtGui.QWidget()
        self.summaryTab.setObjectName(_fromUtf8("summaryTab"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.summaryTab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 40, 481, 151))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.summaryLabel = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.summaryLabel.setObjectName(_fromUtf8("summaryLabel"))
        self.horizontalLayout_5.addWidget(self.summaryLabel)
        self.summaryValue = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.summaryValue.setObjectName(_fromUtf8("summaryValue"))
        self.horizontalLayout_5.addWidget(self.summaryValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.summaryTab, _fromUtf8(""))
        self.graphButton = QtGui.QPushButton(self.centralwidget)
        self.graphButton.setGeometry(QtCore.QRect(420, 460, 131, 31))
        self.graphButton.setObjectName(_fromUtf8("graphButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAddDevice = QtGui.QAction(MainWindow)
        self.actionAddDevice.setObjectName(_fromUtf8("actionAddDevice"))
        self.actionCreate_Branch = QtGui.QAction(MainWindow)
        self.actionCreate_Branch.setObjectName(_fromUtf8("actionCreate_Branch"))
        self.actionModify_Summary = QtGui.QAction(MainWindow)
        self.actionModify_Summary.setObjectName(_fromUtf8("actionModify_Summary"))
        self.actionDelete_Node = QtGui.QAction(MainWindow)
        self.actionDelete_Node.setObjectName(_fromUtf8("actionDelete_Node"))
        self.menuFile.addAction(self.actionAddDevice)
        self.menuFile.addAction(self.actionCreate_Branch)
        self.menuEdit.addAction(self.actionModify_Summary)
        self.menuEdit.addAction(self.actionDelete_Node)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Habitat Monitor", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Data Source", None))
        self.addBranchDevices.setText(_translate("MainWindow", "Add Devices", None))
        self.groupBox.setTitle(_translate("MainWindow", "Select a summary function", None))
        self.minButton.setText(_translate("MainWindow", "Minimum", None))
        self.maxButton.setText(_translate("MainWindow", "Maximum", None))
        self.avgButton.setText(_translate("MainWindow", "Average", None))
        self.timeLabel.setText(_translate("MainWindow", "Time: ", None))
        self.minutesLabel.setText(_translate("MainWindow", "(format -- hh:mm:ss)", None))
        self.functionButton.setText(_translate("MainWindow", "Add Summary", None))
        self.attributeName.setText(_translate("MainWindow", "Attribute: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), _translate("MainWindow", "Raw Data", None))
        self.summaryLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.summaryValue.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summaryTab), _translate("MainWindow", "Summary", None))
        self.graphButton.setText(_translate("MainWindow", "Show Graph", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionAddDevice.setText(_translate("MainWindow", "Add Device", None))
        self.actionCreate_Branch.setText(_translate("MainWindow", "Create Branch", None))
        self.actionModify_Summary.setText(_translate("MainWindow", "Modify Summary", None))
        self.actionDelete_Node.setText(_translate("MainWindow", "Delete Node", None))

