# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/orpl/gui/uis/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(999, 726)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabFileIO = QtWidgets.QWidget()
        self.tabFileIO.setObjectName("tabFileIO")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tabFileIO)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tabFileIO)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.textEditDataDir = QtWidgets.QLineEdit(self.tabFileIO)
        self.textEditDataDir.setReadOnly(True)
        self.textEditDataDir.setObjectName("textEditDataDir")
        self.horizontalLayout_3.addWidget(self.textEditDataDir)
        self.buttonSelectDirectory = QtWidgets.QPushButton(self.tabFileIO)
        self.buttonSelectDirectory.setObjectName("buttonSelectDirectory")
        self.horizontalLayout_3.addWidget(self.buttonSelectDirectory)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.treeViewFiles = QtWidgets.QTreeView(self.tabFileIO)
        self.treeViewFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeViewFiles.setSortingEnabled(True)
        self.treeViewFiles.setObjectName("treeViewFiles")
        self.treeViewFiles.header().setCascadingSectionResizes(False)
        self.horizontalLayout_7.addWidget(self.treeViewFiles)
        self.plainTextMetadata = QtWidgets.QPlainTextEdit(self.tabFileIO)
        self.plainTextMetadata.setReadOnly(True)
        self.plainTextMetadata.setObjectName("plainTextMetadata")
        self.horizontalLayout_7.addWidget(self.plainTextMetadata)
        self.boxDataSelection = QtWidgets.QGroupBox(self.tabFileIO)
        self.boxDataSelection.setObjectName("boxDataSelection")
        self.horizontalLayout_7.addWidget(self.boxDataSelection)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.boxDataPlot = QtWidgets.QGroupBox(self.tabFileIO)
        self.boxDataPlot.setObjectName("boxDataPlot")
        self.horizontalLayout_4.addWidget(self.boxDataPlot)
        self.boxXrefPlot = QtWidgets.QGroupBox(self.tabFileIO)
        self.boxXrefPlot.setObjectName("boxXrefPlot")
        self.horizontalLayout_4.addWidget(self.boxXrefPlot)
        self.boxYrefPlot = QtWidgets.QGroupBox(self.tabFileIO)
        self.boxYrefPlot.setObjectName("boxYrefPlot")
        self.horizontalLayout_4.addWidget(self.boxYrefPlot)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 6)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.tabFileIO)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.buttonSelectSpectra = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectSpectra.sizePolicy().hasHeightForWidth())
        self.buttonSelectSpectra.setSizePolicy(sizePolicy)
        self.buttonSelectSpectra.setObjectName("buttonSelectSpectra")
        self.horizontalLayout_14.addWidget(self.buttonSelectSpectra)
        self.buttonDropSpectra = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDropSpectra.sizePolicy().hasHeightForWidth())
        self.buttonDropSpectra.setSizePolicy(sizePolicy)
        self.buttonDropSpectra.setText("")
        self.buttonDropSpectra.setObjectName("buttonDropSpectra")
        self.horizontalLayout_14.addWidget(self.buttonDropSpectra)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.buttonSelectXref = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectXref.sizePolicy().hasHeightForWidth())
        self.buttonSelectXref.setSizePolicy(sizePolicy)
        self.buttonSelectXref.setObjectName("buttonSelectXref")
        self.horizontalLayout_10.addWidget(self.buttonSelectXref)
        self.buttonDropXref = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonDropXref.setText("")
        self.buttonDropXref.setObjectName("buttonDropXref")
        self.horizontalLayout_10.addWidget(self.buttonDropXref)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.radioButtonTylenol = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonTylenol.setChecked(True)
        self.radioButtonTylenol.setObjectName("radioButtonTylenol")
        self.verticalLayout_3.addWidget(self.radioButtonTylenol)
        self.radioButtonNylon = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonNylon.setChecked(False)
        self.radioButtonNylon.setObjectName("radioButtonNylon")
        self.verticalLayout_3.addWidget(self.radioButtonNylon)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.buttonSelectYref = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectYref.sizePolicy().hasHeightForWidth())
        self.buttonSelectYref.setSizePolicy(sizePolicy)
        self.buttonSelectYref.setObjectName("buttonSelectYref")
        self.horizontalLayout_9.addWidget(self.buttonSelectYref)
        self.buttonDropYref = QtWidgets.QPushButton(self.groupBox_3)
        self.buttonDropYref.setText("")
        self.buttonDropYref.setObjectName("buttonDropYref")
        self.horizontalLayout_9.addWidget(self.buttonDropYref)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.radioButtonNIST = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonNIST.setEnabled(False)
        self.radioButtonNIST.setCheckable(True)
        self.radioButtonNIST.setChecked(True)
        self.radioButtonNIST.setObjectName("radioButtonNIST")
        self.verticalLayout_4.addWidget(self.radioButtonNIST)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tabFileIO, "")
        self.tabProcessing = QtWidgets.QWidget()
        self.tabProcessing.setObjectName("tabProcessing")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabProcessing)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.processingToolBox = QtWidgets.QToolBox(self.tabProcessing)
        self.processingToolBox.setObjectName("processingToolBox")
        self.pageCRR = QtWidgets.QWidget()
        self.pageCRR.setGeometry(QtCore.QRect(0, 0, 133, 430))
        self.pageCRR.setObjectName("pageCRR")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pageCRR)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.pageCRR)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.spinBoxLeftCrop = QtWidgets.QSpinBox(self.pageCRR)
        self.spinBoxLeftCrop.setObjectName("spinBoxLeftCrop")
        self.verticalLayout_6.addWidget(self.spinBoxLeftCrop)
        self.label_5 = QtWidgets.QLabel(self.pageCRR)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.spinBoxRightCrop = QtWidgets.QSpinBox(self.pageCRR)
        self.spinBoxRightCrop.setObjectName("spinBoxRightCrop")
        self.verticalLayout_6.addWidget(self.spinBoxRightCrop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.processingToolBox.addItem(self.pageCRR, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 194, 327))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBoxMultiCRR = QtWidgets.QCheckBox(self.page_3)
        self.checkBoxMultiCRR.setObjectName("checkBoxMultiCRR")
        self.verticalLayout_10.addWidget(self.checkBoxMultiCRR)
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.spinBoxMCRRWidth = QtWidgets.QSpinBox(self.page_3)
        self.spinBoxMCRRWidth.setObjectName("spinBoxMCRRWidth")
        self.verticalLayout_10.addWidget(self.spinBoxMCRRWidth)
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.spinBoxMCRRthreshold = QtWidgets.QDoubleSpinBox(self.page_3)
        self.spinBoxMCRRthreshold.setSingleStep(0.01)
        self.spinBoxMCRRthreshold.setObjectName("spinBoxMCRRthreshold")
        self.verticalLayout_10.addWidget(self.spinBoxMCRRthreshold)
        self.line = QtWidgets.QFrame(self.page_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_10.addWidget(self.line)
        self.checkBoxSingleCRR = QtWidgets.QCheckBox(self.page_3)
        self.checkBoxSingleCRR.setObjectName("checkBoxSingleCRR")
        self.verticalLayout_10.addWidget(self.checkBoxSingleCRR)
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.spinBoxSCRRWidth = QtWidgets.QSpinBox(self.page_3)
        self.spinBoxSCRRWidth.setObjectName("spinBoxSCRRWidth")
        self.verticalLayout_10.addWidget(self.spinBoxSCRRWidth)
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.spinBoxSCRRstd = QtWidgets.QDoubleSpinBox(self.page_3)
        self.spinBoxSCRRstd.setSingleStep(0.01)
        self.spinBoxSCRRstd.setObjectName("spinBoxSCRRstd")
        self.verticalLayout_10.addWidget(self.spinBoxSCRRstd)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.processingToolBox.addItem(self.page_3, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 155, 423))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBoxBRAlgorithm = QtWidgets.QComboBox(self.page_2)
        self.comboBoxBRAlgorithm.setObjectName("comboBoxBRAlgorithm")
        self.comboBoxBRAlgorithm.addItem("")
        self.comboBoxBRAlgorithm.addItem("")
        self.comboBoxBRAlgorithm.addItem("")
        self.comboBoxBRAlgorithm.addItem("")
        self.verticalLayout_7.addWidget(self.comboBoxBRAlgorithm)
        self.line_4 = QtWidgets.QFrame(self.page_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.spinBoxPolyOrder = QtWidgets.QSpinBox(self.page_2)
        self.spinBoxPolyOrder.setMaximum(15)
        self.spinBoxPolyOrder.setObjectName("spinBoxPolyOrder")
        self.verticalLayout_7.addWidget(self.spinBoxPolyOrder)
        self.line_3 = QtWidgets.QFrame(self.page_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.spinBoxHWS = QtWidgets.QSpinBox(self.page_2)
        self.spinBoxHWS.setMinimum(1)
        self.spinBoxHWS.setObjectName("spinBoxHWS")
        self.verticalLayout_7.addWidget(self.spinBoxHWS)
        self.line_2 = QtWidgets.QFrame(self.page_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.spinBoxBubbleWidth = QtWidgets.QSpinBox(self.page_2)
        self.spinBoxBubbleWidth.setMinimum(1)
        self.spinBoxBubbleWidth.setObjectName("spinBoxBubbleWidth")
        self.verticalLayout_7.addWidget(self.spinBoxBubbleWidth)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.processingToolBox.addItem(self.page_2, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 133, 430))
        self.page.setObjectName("page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButtonNoNorm = QtWidgets.QRadioButton(self.page)
        self.radioButtonNoNorm.setChecked(True)
        self.radioButtonNoNorm.setObjectName("radioButtonNoNorm")
        self.verticalLayout_8.addWidget(self.radioButtonNoNorm)
        self.radioButtonMinMax = QtWidgets.QRadioButton(self.page)
        self.radioButtonMinMax.setObjectName("radioButtonMinMax")
        self.verticalLayout_8.addWidget(self.radioButtonMinMax)
        self.radioButtonAUC = QtWidgets.QRadioButton(self.page)
        self.radioButtonAUC.setObjectName("radioButtonAUC")
        self.verticalLayout_8.addWidget(self.radioButtonAUC)
        self.radioButtonSNV = QtWidgets.QRadioButton(self.page)
        self.radioButtonSNV.setChecked(False)
        self.radioButtonSNV.setObjectName("radioButtonSNV")
        self.verticalLayout_8.addWidget(self.radioButtonSNV)
        self.radioButtonMaxBand = QtWidgets.QRadioButton(self.page)
        self.radioButtonMaxBand.setObjectName("radioButtonMaxBand")
        self.verticalLayout_8.addWidget(self.radioButtonMaxBand)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.spinBoxNormBand = QtWidgets.QDoubleSpinBox(self.page)
        self.spinBoxNormBand.setObjectName("spinBoxNormBand")
        self.verticalLayout_8.addWidget(self.spinBoxNormBand)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.processingToolBox.addItem(self.page, "")
        self.verticalLayout_5.addWidget(self.processingToolBox)
        self.checkBoxAutoUpdate = QtWidgets.QCheckBox(self.tabProcessing)
        self.checkBoxAutoUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxAutoUpdate.setObjectName("checkBoxAutoUpdate")
        self.verticalLayout_5.addWidget(self.checkBoxAutoUpdate)
        self.buttonUpdate = QtWidgets.QPushButton(self.tabProcessing)
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.verticalLayout_5.addWidget(self.buttonUpdate)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.layoutPlots = QtWidgets.QVBoxLayout()
        self.layoutPlots.setObjectName("layoutPlots")
        self.boxRawSignal = QtWidgets.QGroupBox(self.tabProcessing)
        self.boxRawSignal.setObjectName("boxRawSignal")
        self.layoutPlots.addWidget(self.boxRawSignal)
        self.boxProcessedSignal = QtWidgets.QGroupBox(self.tabProcessing)
        self.boxProcessedSignal.setObjectName("boxProcessedSignal")
        self.layoutPlots.addWidget(self.boxProcessedSignal)
        self.layoutPlots.setStretch(0, 4)
        self.layoutPlots.setStretch(1, 4)
        self.horizontalLayout_2.addLayout(self.layoutPlots)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        self.tabWidget.addTab(self.tabProcessing, "")
        self.tabProfiles = QtWidgets.QWidget()
        self.tabProfiles.setObjectName("tabProfiles")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabProfiles)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tabProfiles)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.tabWidget.addTab(self.tabProfiles, "")
        self.tabBatchProcessing = QtWidgets.QWidget()
        self.tabBatchProcessing.setObjectName("tabBatchProcessing")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tabBatchProcessing)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tabBatchProcessing)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.tabWidget.addTab(self.tabBatchProcessing, "")
        self.tabLog = QtWidgets.QWidget()
        self.tabLog.setObjectName("tabLog")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tabLog)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelLogPath = QtWidgets.QLabel(self.tabLog)
        self.labelLogPath.setObjectName("labelLogPath")
        self.horizontalLayout_13.addWidget(self.labelLogPath)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.plainTextLog = QtWidgets.QPlainTextEdit(self.tabLog)
        self.plainTextLog.setEnabled(True)
        self.plainTextLog.setReadOnly(True)
        self.plainTextLog.setObjectName("plainTextLog")
        self.verticalLayout_9.addWidget(self.plainTextLog)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.buttonCopyLog = QtWidgets.QPushButton(self.tabLog)
        self.buttonCopyLog.setObjectName("buttonCopyLog")
        self.horizontalLayout_12.addWidget(self.buttonCopyLog)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.tabWidget.addTab(self.tabLog, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.processingToolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "ORPL - GUI"))
        self.label.setText(_translate("mainWindow", "Data Directory:"))
        self.buttonSelectDirectory.setText(_translate("mainWindow", "Select Directory"))
        self.boxDataSelection.setTitle(_translate("mainWindow", "Selected Spectrum"))
        self.boxDataPlot.setTitle(_translate("mainWindow", "Loaded Data"))
        self.boxXrefPlot.setTitle(_translate("mainWindow", "X Reference"))
        self.boxYrefPlot.setTitle(_translate("mainWindow", "Y Reference"))
        self.groupBox.setTitle(_translate("mainWindow", "File selection"))
        self.groupBox_4.setTitle(_translate("mainWindow", "Spectra"))
        self.buttonSelectSpectra.setText(_translate("mainWindow", "Select Spectra"))
        self.groupBox_2.setTitle(_translate("mainWindow", "X-axis Calibration"))
        self.buttonSelectXref.setText(_translate("mainWindow", "Select X-reference"))
        self.radioButtonTylenol.setText(_translate("mainWindow", "Tylenol"))
        self.radioButtonNylon.setText(_translate("mainWindow", "Nylon"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Y-axis Calibration"))
        self.buttonSelectYref.setText(_translate("mainWindow", "Select Y-reference"))
        self.radioButtonNIST.setText(_translate("mainWindow", "NIST SRM-2241"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFileIO), _translate("mainWindow", "File IO"))
        self.label_4.setText(_translate("mainWindow", "Crop from left"))
        self.label_5.setText(_translate("mainWindow", "Crop from right"))
        self.processingToolBox.setItemText(self.processingToolBox.indexOf(self.pageCRR), _translate("mainWindow", "Xaxis range"))
        self.checkBoxMultiCRR.setText(_translate("mainWindow", "Multi-accumulation Filter"))
        self.label_10.setText(_translate("mainWindow", "Width"))
        self.label_11.setText(_translate("mainWindow", "Disparity Threshold"))
        self.checkBoxSingleCRR.setText(_translate("mainWindow", "Single-accumulation filter"))
        self.label_12.setText(_translate("mainWindow", "Width"))
        self.label_13.setText(_translate("mainWindow", "STD factor"))
        self.processingToolBox.setItemText(self.processingToolBox.indexOf(self.page_3), _translate("mainWindow", "CRR"))
        self.comboBoxBRAlgorithm.setItemText(0, _translate("mainWindow", "None"))
        self.comboBoxBRAlgorithm.setItemText(1, _translate("mainWindow", "BubbleFill"))
        self.comboBoxBRAlgorithm.setItemText(2, _translate("mainWindow", "IModPoly"))
        self.comboBoxBRAlgorithm.setItemText(3, _translate("mainWindow", "MorphBR"))
        self.label_8.setText(_translate("mainWindow", "Polynomial Order"))
        self.label_7.setText(_translate("mainWindow", "half width window size"))
        self.label_6.setText(_translate("mainWindow", "Minimum Bubble Width"))
        self.processingToolBox.setItemText(self.processingToolBox.indexOf(self.page_2), _translate("mainWindow", "Baseline Removal"))
        self.radioButtonNoNorm.setText(_translate("mainWindow", "None"))
        self.radioButtonMinMax.setText(_translate("mainWindow", "MinMax"))
        self.radioButtonAUC.setText(_translate("mainWindow", "AUC"))
        self.radioButtonSNV.setText(_translate("mainWindow", "SNV"))
        self.radioButtonMaxBand.setText(_translate("mainWindow", "Max band"))
        self.label_9.setText(_translate("mainWindow", "Band selection"))
        self.processingToolBox.setItemText(self.processingToolBox.indexOf(self.page), _translate("mainWindow", "Normalization"))
        self.checkBoxAutoUpdate.setText(_translate("mainWindow", "Auto-update"))
        self.buttonUpdate.setText(_translate("mainWindow", "Update"))
        self.boxRawSignal.setTitle(_translate("mainWindow", "Raw Spectra"))
        self.boxProcessedSignal.setTitle(_translate("mainWindow", "Processed Spectra"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProcessing), _translate("mainWindow", "Processing"))
        self.label_2.setText(_translate("mainWindow", "Feature to come..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProfiles), _translate("mainWindow", "Profiles"))
        self.label_3.setText(_translate("mainWindow", "Feature to come..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBatchProcessing), _translate("mainWindow", "Batch Processing"))
        self.labelLogPath.setText(_translate("mainWindow", "TextLabel"))
        self.buttonCopyLog.setText(_translate("mainWindow", "Copy Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLog), _translate("mainWindow", "Log"))
