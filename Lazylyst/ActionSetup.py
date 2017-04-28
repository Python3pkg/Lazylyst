# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActionSetup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_actionDialog(object):
    def setupUi(self, actionDialog):
        actionDialog.setObjectName(_fromUtf8("actionDialog"))
        actionDialog.resize(626, 626)
        self.verticalLayout = QtGui.QVBoxLayout(actionDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.actShortInputLayout = QtGui.QGridLayout()
        self.actShortInputLayout.setSpacing(1)
        self.actShortInputLayout.setObjectName(_fromUtf8("actShortInputLayout"))
        self.actOptionalsLabel = QtGui.QLabel(actionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actOptionalsLabel.sizePolicy().hasHeightForWidth())
        self.actOptionalsLabel.setSizePolicy(sizePolicy)
        self.actOptionalsLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actOptionalsLabel.setFont(font)
        self.actOptionalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actOptionalsLabel.setObjectName(_fromUtf8("actOptionalsLabel"))
        self.actShortInputLayout.addWidget(self.actOptionalsLabel, 6, 1, 1, 1)
        self.actTriggerLineEdit = KeyBindLineEdit(actionDialog)
        self.actTriggerLineEdit.setObjectName(_fromUtf8("actTriggerLineEdit"))
        self.actShortInputLayout.addWidget(self.actTriggerLineEdit, 2, 4, 1, 1)
        self.actTagLabel = QtGui.QLabel(actionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actTagLabel.sizePolicy().hasHeightForWidth())
        self.actTagLabel.setSizePolicy(sizePolicy)
        self.actTagLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actTagLabel.setFont(font)
        self.actTagLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actTagLabel.setObjectName(_fromUtf8("actTagLabel"))
        self.actShortInputLayout.addWidget(self.actTagLabel, 0, 1, 1, 1)
        self.actNameLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actNameLabel.setFont(font)
        self.actNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actNameLabel.setObjectName(_fromUtf8("actNameLabel"))
        self.actShortInputLayout.addWidget(self.actNameLabel, 2, 1, 1, 1)
        self.actPassiveRadio = QtGui.QRadioButton(actionDialog)
        self.actPassiveRadio.setChecked(True)
        self.actPassiveRadio.setObjectName(_fromUtf8("actPassiveRadio"))
        self.actShortInputLayout.addWidget(self.actPassiveRadio, 6, 3, 1, 1)
        self.actOptionalsLineEdit = QtGui.QLineEdit(actionDialog)
        self.actOptionalsLineEdit.setObjectName(_fromUtf8("actOptionalsLineEdit"))
        self.actShortInputLayout.addWidget(self.actOptionalsLineEdit, 6, 2, 1, 1)
        self.actIntervalLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actIntervalLabel.setFont(font)
        self.actIntervalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actIntervalLabel.setObjectName(_fromUtf8("actIntervalLabel"))
        self.actShortInputLayout.addWidget(self.actIntervalLabel, 4, 3, 1, 1)
        self.actActiveRadio = QtGui.QRadioButton(actionDialog)
        self.actActiveRadio.setObjectName(_fromUtf8("actActiveRadio"))
        self.actShortInputLayout.addWidget(self.actActiveRadio, 0, 3, 1, 1)
        self.actNameLineEdit = QtGui.QLineEdit(actionDialog)
        self.actNameLineEdit.setObjectName(_fromUtf8("actNameLineEdit"))
        self.actShortInputLayout.addWidget(self.actNameLineEdit, 2, 2, 1, 1)
        self.passiveBeforeCheck = QtGui.QCheckBox(actionDialog)
        self.passiveBeforeCheck.setObjectName(_fromUtf8("passiveBeforeCheck"))
        self.actShortInputLayout.addWidget(self.passiveBeforeCheck, 6, 4, 1, 1)
        self.actPathLabel = QtGui.QLabel(actionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actPathLabel.sizePolicy().hasHeightForWidth())
        self.actPathLabel.setSizePolicy(sizePolicy)
        self.actPathLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actPathLabel.setFont(font)
        self.actPathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actPathLabel.setObjectName(_fromUtf8("actPathLabel"))
        self.actShortInputLayout.addWidget(self.actPathLabel, 4, 1, 1, 1)
        self.actTagLineEdit = HoverLineEdit(actionDialog)
        self.actTagLineEdit.setObjectName(_fromUtf8("actTagLineEdit"))
        self.actShortInputLayout.addWidget(self.actTagLineEdit, 0, 2, 1, 1)
        self.actPathLineEdit = QtGui.QLineEdit(actionDialog)
        self.actPathLineEdit.setObjectName(_fromUtf8("actPathLineEdit"))
        self.actShortInputLayout.addWidget(self.actPathLineEdit, 4, 2, 1, 1)
        self.actTriggerLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actTriggerLabel.setFont(font)
        self.actTriggerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actTriggerLabel.setObjectName(_fromUtf8("actTriggerLabel"))
        self.actShortInputLayout.addWidget(self.actTriggerLabel, 2, 3, 1, 1)
        self.actIntervalLineEdit = QtGui.QLineEdit(actionDialog)
        self.actIntervalLineEdit.setObjectName(_fromUtf8("actIntervalLineEdit"))
        self.actShortInputLayout.addWidget(self.actIntervalLineEdit, 4, 4, 1, 1)
        self.actActiveCheckLayout = QtGui.QHBoxLayout()
        self.actActiveCheckLayout.setObjectName(_fromUtf8("actActiveCheckLayout"))
        self.activeTimerCheck = QtGui.QCheckBox(actionDialog)
        self.activeTimerCheck.setObjectName(_fromUtf8("activeTimerCheck"))
        self.actActiveCheckLayout.addWidget(self.activeTimerCheck)
        self.activeThreadedCheck = QtGui.QCheckBox(actionDialog)
        self.activeThreadedCheck.setObjectName(_fromUtf8("activeThreadedCheck"))
        self.actActiveCheckLayout.addWidget(self.activeThreadedCheck)
        self.actShortInputLayout.addLayout(self.actActiveCheckLayout, 0, 4, 1, 1)
        self.actShortInputLayout.setColumnStretch(1, 1)
        self.actShortInputLayout.setColumnStretch(2, 7)
        self.actShortInputLayout.setColumnStretch(3, 1)
        self.actShortInputLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.actShortInputLayout)
        self.actReturnLayout = QtGui.QGridLayout()
        self.actReturnLayout.setSpacing(1)
        self.actReturnLayout.setObjectName(_fromUtf8("actReturnLayout"))
        self.actSelectInputList = KeyListWidget(actionDialog)
        self.actSelectInputList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.actSelectInputList.setObjectName(_fromUtf8("actSelectInputList"))
        self.actReturnLayout.addWidget(self.actSelectInputList, 1, 2, 1, 1)
        self.actAvailReturnList = QtGui.QListWidget(actionDialog)
        self.actAvailReturnList.setObjectName(_fromUtf8("actAvailReturnList"))
        self.actReturnLayout.addWidget(self.actAvailReturnList, 2, 3, 1, 1)
        self.actAvailTriggerList = QtGui.QListWidget(actionDialog)
        self.actAvailTriggerList.setObjectName(_fromUtf8("actAvailTriggerList"))
        self.actReturnLayout.addWidget(self.actAvailTriggerList, 2, 1, 1, 1)
        self.actInputLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actInputLabel.setFont(font)
        self.actInputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actInputLabel.setObjectName(_fromUtf8("actInputLabel"))
        self.actReturnLayout.addWidget(self.actInputLabel, 0, 2, 1, 1)
        self.actReturnLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actReturnLabel.setFont(font)
        self.actReturnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actReturnLabel.setObjectName(_fromUtf8("actReturnLabel"))
        self.actReturnLayout.addWidget(self.actReturnLabel, 0, 3, 1, 1)
        self.actSelectReturnList = KeyListWidget(actionDialog)
        self.actSelectReturnList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.actSelectReturnList.setObjectName(_fromUtf8("actSelectReturnList"))
        self.actReturnLayout.addWidget(self.actSelectReturnList, 1, 3, 1, 1)
        self.actAvailInputList = QtGui.QListWidget(actionDialog)
        self.actAvailInputList.setViewMode(QtGui.QListView.ListMode)
        self.actAvailInputList.setObjectName(_fromUtf8("actAvailInputList"))
        self.actReturnLayout.addWidget(self.actAvailInputList, 2, 2, 1, 1)
        self.actSelectLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actSelectLabel.setFont(font)
        self.actSelectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actSelectLabel.setObjectName(_fromUtf8("actSelectLabel"))
        self.actReturnLayout.addWidget(self.actSelectLabel, 1, 0, 1, 1)
        self.actSelectTriggerList = KeyListWidget(actionDialog)
        self.actSelectTriggerList.setObjectName(_fromUtf8("actSelectTriggerList"))
        self.actReturnLayout.addWidget(self.actSelectTriggerList, 1, 1, 1, 1)
        self.actAvailLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actAvailLabel.setFont(font)
        self.actAvailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actAvailLabel.setObjectName(_fromUtf8("actAvailLabel"))
        self.actReturnLayout.addWidget(self.actAvailLabel, 2, 0, 1, 1)
        self.actPassiveTriggerLabel = QtGui.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actPassiveTriggerLabel.setFont(font)
        self.actPassiveTriggerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actPassiveTriggerLabel.setObjectName(_fromUtf8("actPassiveTriggerLabel"))
        self.actReturnLayout.addWidget(self.actPassiveTriggerLabel, 0, 1, 1, 1)
        self.actReturnLayout.setRowStretch(1, 1)
        self.actReturnLayout.setRowStretch(2, 2)
        self.verticalLayout.addLayout(self.actReturnLayout)
        self.actLowerLayout = QtGui.QHBoxLayout()
        self.actLowerLayout.setObjectName(_fromUtf8("actLowerLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.actLowerLayout.addItem(spacerItem)
        self.actButtonBox = QtGui.QDialogButtonBox(actionDialog)
        self.actButtonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.actButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.actButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.actButtonBox.setCenterButtons(True)
        self.actButtonBox.setObjectName(_fromUtf8("actButtonBox"))
        self.actLowerLayout.addWidget(self.actButtonBox)
        self.actLowerLayout.setStretch(0, 20)
        self.actLowerLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.actLowerLayout)

        self.retranslateUi(actionDialog)
        QtCore.QObject.connect(self.actButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), actionDialog.accept)
        QtCore.QObject.connect(self.actButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), actionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(actionDialog)
        actionDialog.setTabOrder(self.actTagLineEdit, self.actNameLineEdit)
        actionDialog.setTabOrder(self.actNameLineEdit, self.actPathLineEdit)
        actionDialog.setTabOrder(self.actPathLineEdit, self.actOptionalsLineEdit)
        actionDialog.setTabOrder(self.actOptionalsLineEdit, self.actActiveRadio)
        actionDialog.setTabOrder(self.actActiveRadio, self.actTriggerLineEdit)
        actionDialog.setTabOrder(self.actTriggerLineEdit, self.actIntervalLineEdit)
        actionDialog.setTabOrder(self.actIntervalLineEdit, self.actPassiveRadio)
        actionDialog.setTabOrder(self.actPassiveRadio, self.passiveBeforeCheck)
        actionDialog.setTabOrder(self.passiveBeforeCheck, self.actSelectTriggerList)
        actionDialog.setTabOrder(self.actSelectTriggerList, self.actAvailTriggerList)
        actionDialog.setTabOrder(self.actAvailTriggerList, self.actSelectInputList)
        actionDialog.setTabOrder(self.actSelectInputList, self.actAvailInputList)
        actionDialog.setTabOrder(self.actAvailInputList, self.actSelectReturnList)
        actionDialog.setTabOrder(self.actSelectReturnList, self.actAvailReturnList)
        actionDialog.setTabOrder(self.actAvailReturnList, self.actButtonBox)

    def retranslateUi(self, actionDialog):
        actionDialog.setWindowTitle(_translate("actionDialog", "Setup Action", None))
        self.actOptionalsLabel.setToolTip(_translate("actionDialog", "Optionals to send to function", None))
        self.actOptionalsLabel.setText(_translate("actionDialog", "Optionals", None))
        self.actTagLabel.setToolTip(_translate("actionDialog", "Human readable name of action", None))
        self.actTagLabel.setText(_translate("actionDialog", "Tag ", None))
        self.actNameLabel.setToolTip(_translate("actionDialog", "Function name of action", None))
        self.actNameLabel.setText(_translate("actionDialog", "Name", None))
        self.actPassiveRadio.setToolTip(_translate("actionDialog", "Action is triggered by an active action", None))
        self.actPassiveRadio.setText(_translate("actionDialog", "Passive", None))
        self.actIntervalLabel.setToolTip(_translate("actionDialog", "Time in seconds between calling action", None))
        self.actIntervalLabel.setText(_translate("actionDialog", "Interval (s)", None))
        self.actActiveRadio.setToolTip(_translate("actionDialog", "Action is called using a keybind or click", None))
        self.actActiveRadio.setText(_translate("actionDialog", "Active", None))
        self.passiveBeforeCheck.setToolTip(_translate("actionDialog", "Action is to applied prior its triggering active action", None))
        self.passiveBeforeCheck.setText(_translate("actionDialog", "Before Trigger", None))
        self.actPathLabel.setToolTip(_translate("actionDialog", "Path relative Lazylyst where function is held", None))
        self.actPathLabel.setText(_translate("actionDialog", "Path", None))
        self.actTriggerLabel.setToolTip(_translate("actionDialog", "Keybind to activate action", None))
        self.actTriggerLabel.setText(_translate("actionDialog", "Trigger", None))
        self.activeTimerCheck.setToolTip(_translate("actionDialog", "Repeat action every interval", None))
        self.activeTimerCheck.setText(_translate("actionDialog", "Timer", None))
        self.activeThreadedCheck.setToolTip(_translate("actionDialog", "Run action in background", None))
        self.activeThreadedCheck.setText(_translate("actionDialog", "Thread", None))
        self.actAvailReturnList.setSortingEnabled(True)
        self.actAvailTriggerList.setSortingEnabled(True)
        self.actInputLabel.setToolTip(_translate("actionDialog", "Variable(s) to send to function", None))
        self.actInputLabel.setText(_translate("actionDialog", "Inputs", None))
        self.actReturnLabel.setToolTip(_translate("actionDialog", "Variable(s) to be returned by function ", None))
        self.actReturnLabel.setText(_translate("actionDialog", "Returns", None))
        self.actAvailInputList.setSortingEnabled(True)
        self.actSelectLabel.setText(_translate("actionDialog", "Selected", None))
        self.actSelectTriggerList.setSortingEnabled(True)
        self.actAvailLabel.setText(_translate("actionDialog", "Available", None))
        self.actPassiveTriggerLabel.setToolTip(_translate("actionDialog", "Active actions which trigger a passive action", None))
        self.actPassiveTriggerLabel.setText(_translate("actionDialog", "Passive Triggers", None))

from CustomWidgets import HoverLineEdit, KeyBindLineEdit, KeyListWidget