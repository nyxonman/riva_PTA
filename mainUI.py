# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nishakya\OneDrive - Itron\Desktop\SHAKYA\ITRON_PROJECTS\DEMO\Test1\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainObj(object):
    def setupUi(self, MainObj):
        MainObj.setObjectName("MainObj")
        MainObj.setWindowModality(QtCore.Qt.ApplicationModal)
        MainObj.resize(900, 675)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainObj.sizePolicy().hasHeightForWidth())
        MainObj.setSizePolicy(sizePolicy)
        MainObj.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainObj.setAutoFillBackground(True)
        MainObj.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainObj.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainObj)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pktSizeLab = QtWidgets.QLabel(self.mainTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pktSizeLab.setFont(font)
        self.pktSizeLab.setAlignment(QtCore.Qt.AlignCenter)
        self.pktSizeLab.setWordWrap(True)
        self.pktSizeLab.setObjectName("pktSizeLab")
        self.gridLayout_4.addWidget(self.pktSizeLab, 1, 0, 1, 1)
        self.pktSizeDial = QtWidgets.QDial(self.mainTab)
        self.pktSizeDial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pktSizeDial.setStatusTip("")
        self.pktSizeDial.setWhatsThis("")
        self.pktSizeDial.setMinimum(3)
        self.pktSizeDial.setMaximum(10)
        self.pktSizeDial.setPageStep(2)
        self.pktSizeDial.setProperty("value", 6)
        self.pktSizeDial.setNotchesVisible(True)
        self.pktSizeDial.setObjectName("pktSizeDial")
        self.gridLayout_4.addWidget(self.pktSizeDial, 2, 0, 1, 1)
        self.pktIntDial = QtWidgets.QDial(self.mainTab)
        self.pktIntDial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pktIntDial.setMinimum(1)
        self.pktIntDial.setMaximum(50)
        self.pktIntDial.setPageStep(5)
        self.pktIntDial.setProperty("value", 15)
        self.pktIntDial.setNotchesVisible(True)
        self.pktIntDial.setObjectName("pktIntDial")
        self.gridLayout_4.addWidget(self.pktIntDial, 2, 2, 1, 1)
        self.pktCntDial = QtWidgets.QDial(self.mainTab)
        self.pktCntDial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pktCntDial.setMinimum(1)
        self.pktCntDial.setMaximum(25)
        self.pktCntDial.setPageStep(5)
        self.pktCntDial.setProperty("value", 1)
        self.pktCntDial.setNotchesVisible(True)
        self.pktCntDial.setObjectName("pktCntDial")
        self.gridLayout_4.addWidget(self.pktCntDial, 2, 1, 1, 1)
        self.pktResDial = QtWidgets.QDial(self.mainTab)
        self.pktResDial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pktResDial.setMinimum(1)
        self.pktResDial.setMaximum(50)
        self.pktResDial.setPageStep(5)
        self.pktResDial.setProperty("value", 15)
        self.pktResDial.setNotchesVisible(True)
        self.pktResDial.setObjectName("pktResDial")
        self.gridLayout_4.addWidget(self.pktResDial, 2, 3, 1, 1)
        self.pktIntLab = QtWidgets.QLabel(self.mainTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pktIntLab.setFont(font)
        self.pktIntLab.setAlignment(QtCore.Qt.AlignCenter)
        self.pktIntLab.setWordWrap(True)
        self.pktIntLab.setObjectName("pktIntLab")
        self.gridLayout_4.addWidget(self.pktIntLab, 1, 2, 1, 1)
        self.pktSizeVal = QtWidgets.QLineEdit(self.mainTab)
        self.pktSizeVal.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pktSizeVal.setFont(font)
        self.pktSizeVal.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pktSizeVal.setAutoFillBackground(True)
        self.pktSizeVal.setFrame(False)
        self.pktSizeVal.setAlignment(QtCore.Qt.AlignCenter)
        self.pktSizeVal.setObjectName("pktSizeVal")
        self.gridLayout_4.addWidget(self.pktSizeVal, 3, 0, 1, 1)
        self.pktCntVal = QtWidgets.QLineEdit(self.mainTab)
        self.pktCntVal.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pktCntVal.setFont(font)
        self.pktCntVal.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pktCntVal.setFrame(False)
        self.pktCntVal.setAlignment(QtCore.Qt.AlignCenter)
        self.pktCntVal.setObjectName("pktCntVal")
        self.gridLayout_4.addWidget(self.pktCntVal, 3, 1, 1, 1)
        self.pktIntVal = QtWidgets.QLineEdit(self.mainTab)
        self.pktIntVal.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pktIntVal.setFont(font)
        self.pktIntVal.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pktIntVal.setFrame(False)
        self.pktIntVal.setAlignment(QtCore.Qt.AlignCenter)
        self.pktIntVal.setObjectName("pktIntVal")
        self.gridLayout_4.addWidget(self.pktIntVal, 3, 2, 1, 1)
        self.pktResVal = QtWidgets.QLineEdit(self.mainTab)
        self.pktResVal.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pktResVal.setFont(font)
        self.pktResVal.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pktResVal.setFrame(False)
        self.pktResVal.setAlignment(QtCore.Qt.AlignCenter)
        self.pktResVal.setObjectName("pktResVal")
        self.gridLayout_4.addWidget(self.pktResVal, 3, 3, 1, 1)
        self.pktCntLab = QtWidgets.QLabel(self.mainTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pktCntLab.setFont(font)
        self.pktCntLab.setAlignment(QtCore.Qt.AlignCenter)
        self.pktCntLab.setWordWrap(True)
        self.pktCntLab.setObjectName("pktCntLab")
        self.gridLayout_4.addWidget(self.pktCntLab, 1, 1, 1, 1)
        self.pktResLab = QtWidgets.QLabel(self.mainTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pktResLab.setFont(font)
        self.pktResLab.setAlignment(QtCore.Qt.AlignCenter)
        self.pktResLab.setWordWrap(True)
        self.pktResLab.setObjectName("pktResLab")
        self.gridLayout_4.addWidget(self.pktResLab, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 1, 2, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.removeRowBtn = QtWidgets.QPushButton(self.mainTab)
        self.removeRowBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.removeRowBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeRowBtn.setObjectName("removeRowBtn")
        self.gridLayout.addWidget(self.removeRowBtn, 11, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.iterLab = QtWidgets.QLabel(self.mainTab)
        self.iterLab.setObjectName("iterLab")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iterLab)
        self.IterVal = QtWidgets.QLineEdit(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IterVal.sizePolicy().hasHeightForWidth())
        self.IterVal.setSizePolicy(sizePolicy)
        self.IterVal.setObjectName("IterVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.IterVal)
        self.rootCntLab = QtWidgets.QLabel(self.mainTab)
        self.rootCntLab.setObjectName("rootCntLab")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rootCntLab)
        self.rootCntVal = QtWidgets.QLineEdit(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rootCntVal.sizePolicy().hasHeightForWidth())
        self.rootCntVal.setSizePolicy(sizePolicy)
        self.rootCntVal.setObjectName("rootCntVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rootCntVal)
        self.label_2 = QtWidgets.QLabel(self.mainTab)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.outputToFile = QtWidgets.QCheckBox(self.mainTab)
        self.outputToFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outputToFile.setChecked(False)
        self.outputToFile.setObjectName("outputToFile")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.outputToFile)
        self.outputFilenameVal = QtWidgets.QLineEdit(self.mainTab)
        self.outputFilenameVal.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFilenameVal.sizePolicy().hasHeightForWidth())
        self.outputFilenameVal.setSizePolicy(sizePolicy)
        self.outputFilenameVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputFilenameVal.setObjectName("outputFilenameVal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.outputFilenameVal)
        self.showMap = QtWidgets.QCheckBox(self.mainTab)
        self.showMap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showMap.setObjectName("showMap")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.showMap)
        self.label_3 = QtWidgets.QLabel(self.mainTab)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.scrollToLastCmdHistory = QtWidgets.QCheckBox(self.mainTab)
        self.scrollToLastCmdHistory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollToLastCmdHistory.setChecked(True)
        self.scrollToLastCmdHistory.setObjectName("scrollToLastCmdHistory")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.scrollToLastCmdHistory)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 11, 1)
        self.saveEntryBtn = QtWidgets.QPushButton(self.mainTab)
        self.saveEntryBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.saveEntryBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveEntryBtn.setObjectName("saveEntryBtn")
        self.gridLayout.addWidget(self.saveEntryBtn, 12, 2, 1, 1)
        self.addRowBtn = QtWidgets.QPushButton(self.mainTab)
        self.addRowBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.addRowBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addRowBtn.setObjectName("addRowBtn")
        self.gridLayout.addWidget(self.addRowBtn, 11, 1, 1, 1)
        self.loadEntryBtn = QtWidgets.QPushButton(self.mainTab)
        self.loadEntryBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.loadEntryBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadEntryBtn.setObjectName("loadEntryBtn")
        self.gridLayout.addWidget(self.loadEntryBtn, 12, 1, 1, 1)
        self.cmdHistory = QtWidgets.QTextEdit(self.mainTab)
        self.cmdHistory.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdHistory.sizePolicy().hasHeightForWidth())
        self.cmdHistory.setSizePolicy(sizePolicy)
        self.cmdHistory.setReadOnly(True)
        self.cmdHistory.setObjectName("cmdHistory")
        self.gridLayout.addWidget(self.cmdHistory, 11, 0, 7, 1)
        self.resetEntryBtn = QtWidgets.QPushButton(self.mainTab)
        self.resetEntryBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.resetEntryBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetEntryBtn.setObjectName("resetEntryBtn")
        self.gridLayout.addWidget(self.resetEntryBtn, 13, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(135, 135, 135, 0))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 11, 5)
        self.resetBtn = QtWidgets.QPushButton(self.mainTab)
        self.resetBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.resetBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetBtn.setObjectName("resetBtn")
        self.gridLayout.addWidget(self.resetBtn, 17, 1, 1, 2)
        self.startTestBtn = QtWidgets.QPushButton(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTestBtn.sizePolicy().hasHeightForWidth())
        self.startTestBtn.setSizePolicy(sizePolicy)
        self.startTestBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.startTestBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startTestBtn.setObjectName("startTestBtn")
        self.gridLayout.addWidget(self.startTestBtn, 16, 3, 1, 3)
        self.liveViewBtn = QtWidgets.QPushButton(self.mainTab)
        self.liveViewBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liveViewBtn.sizePolicy().hasHeightForWidth())
        self.liveViewBtn.setSizePolicy(sizePolicy)
        self.liveViewBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.liveViewBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.liveViewBtn.setObjectName("liveViewBtn")
        self.gridLayout.addWidget(self.liveViewBtn, 16, 1, 1, 2)
        self.quitBtn = QtWidgets.QPushButton(self.mainTab)
        self.quitBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.quitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quitBtn.setObjectName("quitBtn")
        self.gridLayout.addWidget(self.quitBtn, 17, 3, 1, 3)
        self.clearLogBtn = QtWidgets.QPushButton(self.mainTab)
        self.clearLogBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.clearLogBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearLogBtn.setObjectName("clearLogBtn")
        self.gridLayout.addWidget(self.clearLogBtn, 13, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 14, 1, 1, 1)
        self.outputCmd = QtWidgets.QTextEdit(self.mainTab)
        self.outputCmd.setEnabled(True)
        self.outputCmd.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.outputCmd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.outputCmd.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.outputCmd.setReadOnly(True)
        self.outputCmd.setObjectName("outputCmd")
        self.gridLayout.addWidget(self.outputCmd, 11, 3, 5, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.mainTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 1, 1, 1)
        self.tabWidget.addTab(self.mainTab, "")
        self.consoleTab = QtWidgets.QWidget()
        self.consoleTab.setObjectName("consoleTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.consoleTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lowerText = QtWidgets.QTextEdit(self.consoleTab)
        self.lowerText.setReadOnly(True)
        self.lowerText.setObjectName("lowerText")
        self.gridLayout_3.addWidget(self.lowerText, 4, 0, 6, 4)
        self.exportDataMapFinal = QtWidgets.QCheckBox(self.consoleTab)
        self.exportDataMapFinal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exportDataMapFinal.setObjectName("exportDataMapFinal")
        self.gridLayout_3.addWidget(self.exportDataMapFinal, 0, 3, 1, 1)
        self.exportDataBtn = QtWidgets.QPushButton(self.consoleTab)
        self.exportDataBtn.setEnabled(False)
        self.exportDataBtn.setObjectName("exportDataBtn")
        self.gridLayout_3.addWidget(self.exportDataBtn, 1, 3, 1, 1)
        self.upperText = QtWidgets.QTextEdit(self.consoleTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperText.sizePolicy().hasHeightForWidth())
        self.upperText.setSizePolicy(sizePolicy)
        self.upperText.setReadOnly(True)
        self.upperText.setObjectName("upperText")
        self.gridLayout_3.addWidget(self.upperText, 0, 0, 4, 3)
        self.scrollToLastOutput = QtWidgets.QCheckBox(self.consoleTab)
        self.scrollToLastOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollToLastOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollToLastOutput.setChecked(True)
        self.scrollToLastOutput.setObjectName("scrollToLastOutput")
        self.gridLayout_3.addWidget(self.scrollToLastOutput, 3, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.consoleTab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 3, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setRowStretch(4, 1)
        self.gridLayout_3.setRowStretch(5, 1)
        self.gridLayout_3.setRowStretch(6, 1)
        self.gridLayout_3.setRowStretch(7, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.consoleTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainObj.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainObj)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        MainObj.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainObj)
        self.statusbar.setObjectName("statusbar")
        MainObj.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainObj)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainObj.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbout = QtWidgets.QAction(MainObj)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDebug_Mode = QtWidgets.QAction(MainObj)
        self.actionDebug_Mode.setCheckable(True)
        self.actionDebug_Mode.setObjectName("actionDebug_Mode")
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionDebug_Mode)
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainObj)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainObj)

    def retranslateUi(self, MainObj):
        _translate = QtCore.QCoreApplication.translate
        MainObj.setWindowTitle(_translate("MainObj", "Main Window"))
        self.pktSizeLab.setText(_translate("MainObj", "pktSize in Bytes"))
        self.pktSizeDial.setToolTip(_translate("MainObj", "Rotate the Dial to change the ping packet size in Bytes"))
        self.pktIntDial.setToolTip(_translate("MainObj", "Rotate the Dial to change the ping interval in seconds. This has meaning only when packet count is greater than 1"))
        self.pktCntDial.setToolTip(_translate("MainObj", "Rotate the Dial to change the ping packet count per Node"))
        self.pktResDial.setToolTip(_translate("MainObj", "Rotate the Dial to change the waiting time for the ping response in seconds."))
        self.pktIntLab.setText(_translate("MainObj", "pkt Interval in seconds"))
        self.pktSizeVal.setText(_translate("MainObj", "64"))
        self.pktCntVal.setText(_translate("MainObj", "1"))
        self.pktIntVal.setText(_translate("MainObj", "180"))
        self.pktResVal.setText(_translate("MainObj", "180"))
        self.pktCntLab.setText(_translate("MainObj", "pkt Count"))
        self.pktResLab.setText(_translate("MainObj", "pkt response time in seconds"))
        self.removeRowBtn.setToolTip(_translate("MainObj", "Remove the last row from the above table"))
        self.removeRowBtn.setText(_translate("MainObj", "Remove Row"))
        self.iterLab.setToolTip(_translate("MainObj", "Number of times the test is repeated for each node"))
        self.iterLab.setText(_translate("MainObj", "Iteration(s)"))
        self.IterVal.setToolTip(_translate("MainObj", "Number of times the test is repeated for each node"))
        self.rootCntLab.setToolTip(_translate("MainObj", "Number of ROOTs for test. This reflects to number of columns in the right side table"))
        self.rootCntLab.setText(_translate("MainObj", "Number of ROOT(s)"))
        self.rootCntVal.setToolTip(_translate("MainObj", "Number of ROOTs for test. This reflects to number of columns in the right side table"))
        self.outputToFile.setToolTip(_translate("MainObj", "To save the output of the result to a csv file. If unchecked, by default, it will save to last_testlog.csv"))
        self.outputToFile.setText(_translate("MainObj", "Output results to file"))
        self.outputFilenameVal.setToolTip(_translate("MainObj", "To save the output of the result to a csv file. If unchecked, by default, it will save to last_testlog.csv"))
        self.showMap.setToolTip(_translate("MainObj", "Show the mapping for the nodes in the table against short addr and pan id"))
        self.showMap.setText(_translate("MainObj", "Show Mapping"))
        self.scrollToLastCmdHistory.setToolTip(_translate("MainObj", "Check to scroll the result to the end always"))
        self.scrollToLastCmdHistory.setText(_translate("MainObj", "Scroll to Last"))
        self.saveEntryBtn.setToolTip(_translate("MainObj", "Save the entries from the above table to a csv file"))
        self.saveEntryBtn.setText(_translate("MainObj", "Save Entries"))
        self.addRowBtn.setToolTip(_translate("MainObj", "Add a row to the end of the above table"))
        self.addRowBtn.setText(_translate("MainObj", "Add Row"))
        self.loadEntryBtn.setToolTip(_translate("MainObj", "Click to load the entries from a saved file from a PC to the above table"))
        self.loadEntryBtn.setText(_translate("MainObj", "Load Entries"))
        self.cmdHistory.setToolTip(_translate("MainObj", "List of history of commands run"))
        self.resetEntryBtn.setToolTip(_translate("MainObj", "Reset the entries to the default values from the above table"))
        self.resetEntryBtn.setText(_translate("MainObj", "Reset Entries"))
        self.tableWidget.setToolTip(_translate("MainObj", "Modifyable Table to show the list of entries for the test. The order of the test would be row first and then column."))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainObj", "ROOT Addr"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainObj", "Entry 1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainObj", "Entry 2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainObj", "ROOT_1"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainObj", "eeee::1"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainObj", "0007814700bc0192"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainObj", "0007814700bc0194"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.resetBtn.setText(_translate("MainObj", "Reset"))
        self.startTestBtn.setToolTip(_translate("MainObj", "Start the test with the command shown in the above window"))
        self.startTestBtn.setText(_translate("MainObj", "Start Test"))
        self.liveViewBtn.setText(_translate("MainObj", "Live View in Web"))
        self.quitBtn.setToolTip(_translate("MainObj", "Quit the application"))
        self.quitBtn.setText(_translate("MainObj", "QUIT"))
        self.clearLogBtn.setToolTip(_translate("MainObj", "CLear the logs from the left window"))
        self.clearLogBtn.setText(_translate("MainObj", "Clear Logs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("MainObj", "Control"))
        self.lowerText.setToolTip(_translate("MainObj", "Output of the test results"))
        self.exportDataMapFinal.setToolTip(_translate("MainObj", "Include the map list and the final statistics in the exported data"))
        self.exportDataMapFinal.setText(_translate("MainObj", "Include Map list and final statistics"))
        self.exportDataBtn.setToolTip(_translate("MainObj", "Export the last result to a csv file"))
        self.exportDataBtn.setText(_translate("MainObj", "Export CSV Data"))
        self.scrollToLastOutput.setToolTip(_translate("MainObj", "Scroll the cursor always to the last for the window below"))
        self.scrollToLastOutput.setText(_translate("MainObj", "Scroll to last"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.consoleTab), _translate("MainObj", "Output"))
        self.progressBar.setToolTip(_translate("MainObj", "Progress Bar"))
        self.menuAbout.setTitle(_translate("MainObj", "About"))
        self.menuConfig.setTitle(_translate("MainObj", "Config"))
        self.toolBar.setWindowTitle(_translate("MainObj", "toolBar"))
        self.actionAbout.setText(_translate("MainObj", "About"))
        self.actionAbout.setToolTip(_translate("MainObj", "Details of the app"))
        self.actionDebug_Mode.setText(_translate("MainObj", "Debug Mode"))
        self.actionDebug_Mode.setToolTip(_translate("MainObj", "Click to enable debug mode for detailed logs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainObj = QtWidgets.QMainWindow()
    ui = Ui_MainObj()
    ui.setupUi(MainObj)
    MainObj.show()
    sys.exit(app.exec_())

