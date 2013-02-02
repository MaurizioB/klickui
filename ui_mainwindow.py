# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Feb  1 18:00:41 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 786, 482))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ContainerWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.ContainerWidget.setObjectName(_fromUtf8("ContainerWidget"))
        self.ContainerLayout = QtGui.QVBoxLayout(self.ContainerWidget)
        self.ContainerLayout.setSpacing(0)
        self.ContainerLayout.setMargin(0)
        self.ContainerLayout.setMargin(0)
        self.ContainerLayout.setObjectName(_fromUtf8("ContainerLayout"))
        spacerItem = QtGui.QSpacerItem(20, 471, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.ContainerLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.ContainerWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(57, 64))
        self.dockWidget.setMaximumSize(QtCore.QSize(524287, 64))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(0, 47))
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.addBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.addBtn.setGeometry(QtCore.QRect(10, 0, 81, 41))
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.loadButton = QtGui.QPushButton(self.dockWidgetContents)
        self.loadButton.setGeometry(QtCore.QRect(540, 0, 81, 41))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.addBeatBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.addBeatBtn.setGeometry(QtCore.QRect(290, 0, 81, 41))
        self.addBeatBtn.setObjectName(_fromUtf8("addBeatBtn"))
        self.addBtn2 = QtGui.QPushButton(self.dockWidgetContents)
        self.addBtn2.setGeometry(QtCore.QRect(100, 0, 81, 41))
        self.addBtn2.setObjectName(_fromUtf8("addBtn2"))
        self.addBtn3 = QtGui.QPushButton(self.dockWidgetContents)
        self.addBtn3.setGeometry(QtCore.QRect(190, 0, 81, 41))
        self.addBtn3.setObjectName(_fromUtf8("addBtn3"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Main Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Aggiungi pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn.setText(QtGui.QApplication.translate("MainWindow", "&AddPat", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("MainWindow", "&Carica", None, QtGui.QApplication.UnicodeUTF8))
        self.addBeatBtn.setText(QtGui.QApplication.translate("MainWindow", "Add&Beat", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn2.setText(QtGui.QApplication.translate("MainWindow", "A&ddLbl", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn3.setText(QtGui.QApplication.translate("MainWindow", "Add&SubP", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save &as...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

