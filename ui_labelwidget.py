# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labelwidget.ui'
#
# Created: Fri Feb  1 18:00:43 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LabelWidget(object):
    def setupUi(self, LabelWidget):
        LabelWidget.setObjectName(_fromUtf8("LabelWidget"))
        LabelWidget.resize(678, 80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LabelWidget.sizePolicy().hasHeightForWidth())
        LabelWidget.setSizePolicy(sizePolicy)
        LabelWidget.setMinimumSize(QtCore.QSize(678, 0))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(LabelWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.LabelFrame = QtGui.QFrame(LabelWidget)
        self.LabelFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LabelFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.LabelFrame.setObjectName(_fromUtf8("LabelFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.LabelFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.LabelDataFrame = QtGui.QWidget(self.LabelFrame)
        self.LabelDataFrame.setMinimumSize(QtCore.QSize(120, 74))
        self.LabelDataFrame.setMaximumSize(QtCore.QSize(120, 16777215))
        self.LabelDataFrame.setObjectName(_fromUtf8("LabelDataFrame"))
        self.LabelName = QtGui.QLineEdit(self.LabelDataFrame)
        self.LabelName.setGeometry(QtCore.QRect(2, 0, 118, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LabelName.setFont(font)
        self.LabelName.setObjectName(_fromUtf8("LabelName"))
        self.TotBarCountLbl = QtGui.QLabel(self.LabelDataFrame)
        self.TotBarCountLbl.setGeometry(QtCore.QRect(80, 46, 32, 13))
        self.TotBarCountLbl.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.TotBarCountLbl.setFrameShape(QtGui.QFrame.Panel)
        self.TotBarCountLbl.setFrameShadow(QtGui.QFrame.Sunken)
        self.TotBarCountLbl.setObjectName(_fromUtf8("TotBarCountLbl"))
        self.TotBarLbl = QtGui.QLabel(self.LabelDataFrame)
        self.TotBarLbl.setGeometry(QtCore.QRect(10, 45, 61, 16))
        self.TotBarLbl.setObjectName(_fromUtf8("TotBarLbl"))
        self.FirstBarLbl = QtGui.QLabel(self.LabelDataFrame)
        self.FirstBarLbl.setEnabled(False)
        self.FirstBarLbl.setGeometry(QtCore.QRect(43, 60, 24, 13))
        self.FirstBarLbl.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.FirstBarLbl.setFrameShape(QtGui.QFrame.Panel)
        self.FirstBarLbl.setFrameShadow(QtGui.QFrame.Sunken)
        self.FirstBarLbl.setObjectName(_fromUtf8("FirstBarLbl"))
        self.LastBarLbl = QtGui.QLabel(self.LabelDataFrame)
        self.LastBarLbl.setEnabled(False)
        self.LastBarLbl.setGeometry(QtCore.QRect(88, 60, 24, 13))
        self.LastBarLbl.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.LastBarLbl.setFrameShape(QtGui.QFrame.Panel)
        self.LastBarLbl.setFrameShadow(QtGui.QFrame.Sunken)
        self.LastBarLbl.setObjectName(_fromUtf8("LastBarLbl"))
        self.FromLbl = QtGui.QLabel(self.LabelDataFrame)
        self.FromLbl.setEnabled(False)
        self.FromLbl.setGeometry(QtCore.QRect(10, 58, 31, 16))
        self.FromLbl.setObjectName(_fromUtf8("FromLbl"))
        self.TotLbl = QtGui.QLabel(self.LabelDataFrame)
        self.TotLbl.setEnabled(False)
        self.TotLbl.setGeometry(QtCore.QRect(70, 58, 17, 16))
        self.TotLbl.setObjectName(_fromUtf8("TotLbl"))
        self.LabelEnabledBtn = QtGui.QPushButton(self.LabelDataFrame)
        self.LabelEnabledBtn.setGeometry(QtCore.QRect(2, 28, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LabelEnabledBtn.setFont(font)
        self.LabelEnabledBtn.setCheckable(True)
        self.LabelEnabledBtn.setChecked(True)
        self.LabelEnabledBtn.setObjectName(_fromUtf8("LabelEnabledBtn"))
        self.LabelCmtBtn = QtGui.QPushButton(self.LabelDataFrame)
        self.LabelCmtBtn.setGeometry(QtCore.QRect(62, 28, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LabelCmtBtn.setFont(font)
        self.LabelCmtBtn.setObjectName(_fromUtf8("LabelCmtBtn"))
        self.horizontalLayout.addWidget(self.LabelDataFrame)
        self.PatternFrame = QtGui.QWidget(self.LabelFrame)
        self.PatternFrame.setMinimumSize(QtCore.QSize(550, 0))
        self.PatternFrame.setObjectName(_fromUtf8("PatternFrame"))
        self.patternLayout = QtGui.QVBoxLayout(self.PatternFrame)
        self.patternLayout.setSpacing(0)
        self.patternLayout.setMargin(0)
        self.patternLayout.setMargin(0)
        self.patternLayout.setObjectName(_fromUtf8("patternLayout"))
        self.horizontalLayout.addWidget(self.PatternFrame)
        self.horizontalLayout_2.addWidget(self.LabelFrame)

        self.retranslateUi(LabelWidget)
        QtCore.QMetaObject.connectSlotsByName(LabelWidget)

    def retranslateUi(self, LabelWidget):
        LabelWidget.setWindowTitle(QtGui.QApplication.translate("LabelWidget", "LabelWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.TotBarCountLbl.setText(QtGui.QApplication.translate("LabelWidget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.TotBarLbl.setText(QtGui.QApplication.translate("LabelWidget", "Total bars:", None, QtGui.QApplication.UnicodeUTF8))
        self.FirstBarLbl.setText(QtGui.QApplication.translate("LabelWidget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.LastBarLbl.setText(QtGui.QApplication.translate("LabelWidget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.FromLbl.setText(QtGui.QApplication.translate("LabelWidget", "From", None, QtGui.QApplication.UnicodeUTF8))
        self.TotLbl.setText(QtGui.QApplication.translate("LabelWidget", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelEnabledBtn.setText(QtGui.QApplication.translate("LabelWidget", "ENABLED", "0", QtGui.QApplication.UnicodeUTF8))
        self.LabelCmtBtn.setText(QtGui.QApplication.translate("LabelWidget", "COMMENT", "0", QtGui.QApplication.UnicodeUTF8))


class LabelWidget(QtGui.QWidget, Ui_LabelWidget):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

