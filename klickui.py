#! /usr/bin/python  
# -*- coding: utf-8 -*  

import sys
from PyQt4 import QtCore, QtGui
#from PyQt4.QtCore import pyqt
from ui_mainwindow import *
from ui_classes import *
from openparse import *
import random

bars=0
#QtCore.QObject.connect(MainWindow.AddBtn, QtCore.SIGNAL("pressed()"), lambda: self.AddPattern(vbox))

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        global bars
        #bars=0
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)
        
        QtCore.QObject.connect(self.addBtn, QtCore.SIGNAL("pressed()"), lambda: self.addPattern())
        QtCore.QObject.connect(self.addBtn2, QtCore.SIGNAL("pressed()"), lambda: self.addLabel())
        QtCore.QObject.connect(self.addBtn3, QtCore.SIGNAL("pressed()"), lambda: self.NewLabel.addSubPattern())
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL("pressed()"), lambda: self.loadTempoMap())
        #QtCore.QObject.connect(self.addBeatBtn, QtCore.SIGNAL("pressed()"), lambda: self.addBeat(vars(self)['NewPattern%s' % bars]))
    
    def addPattern(self):
      #sistema 'sto global che mi sa che non serve
      global bars
      print bars
      bars+=1
      actual=str(bars)
      #forse puoi buttar via 'sta naming che fa schifo.
      self.NewPattern=PatternWidget(self)
      #togli beats qui di seguito, dovrebbe pensarci da solo il widget!
      #vars(self)['NewPattern%s' % bars].beats=4
      self.NewPattern.setObjectName('NewPattern')
      #fai ordine CAZZO!
      self.NewPattern.FirstBarLbl.setText(str(bars))
      #self.NewPattern.meter='4/4'
      #vars(self)['NewPattern%s' % bars].meter=meter()

      self.ContainerLayout.insertWidget(self.ContainerLayout.count()-1, self.NewPattern)

    
    def addLabel(self, name=''):
      
      def _get_startBar(self):
        return sum([b.bars for b in self.listLabels()[:-1]])+1
      
      def _set_startBar(self):
        print self
      
      self.NewLabel=LabelWidget(self)
      self.NewLabel.setObjectName('NewLabel')
      
      self.ContainerLayout.insertWidget(self.ContainerLayout.count()-1, self.NewLabel)
      self.NewLabel.LabelName.setText(name)
      
      #self.NewLabel.startBar=property(_get_startBar, _set_startBar)


      
    def addSubPattern(self):
      self.NewPattern=PatternWidget(self)
      self.NewPattern.setObjectName('NewPattern')
      self.NewPattern.meter='4/4'

      #self.NewLabel.patternLayout.insertWidget(self.NewLabel.patternLayout.count()-1, self.NewPattern)
      self.NewLabel.patternLayout.addWidget(self.NewPattern)
    

    #aggiungi label!
    # klickui.lbl.setSizePolicy(1,2)

    def listLabels(self):
        return [ch for ch in self.ContainerWidget.children() if isinstance(ch, LabelWidget)]


    def listPatterns(self):
        return [ch for ch in self.ContainerWidget.children() if isinstance(ch, PatternWidget)]
    
    #inutile?
    def listSubPatterns(self, label):
      return [ch for ch in label.PatternFrame.children() if isinstance(ch, PatternWidget)]
    #label.listPatterns()
    
    def loadTempoMap(self):
      Song=loadFile()
      for label in Song.keys():
        #print label+':\n'
        self.NewLabel=LabelWidget(self)
        self.NewLabel.setObjectName('NewLabel')
        self.ContainerLayout.insertWidget(self.ContainerLayout.count()-1, self.NewLabel)
        self.NewLabel.LabelName.setText(label)
        
        for bar in Song[label]:
          print bar['bars']
          if bar is Song[label][0]:
            self.NewLabel.NewPattern.label=label
          else:
            self.NewLabel.NewPattern=PatternWidget(self)
            self.NewLabel.NewPattern.setObjectName('self.NewLabel.NewPattern')
            self.NewLabel.patternLayout.insertWidget(self.NewLabel.patternLayout.count()-1, self.NewLabel.NewPattern)
          #AllPatt.append(self.NewPattern)
          
          
          print 'Song[label][0]: %s\nbar: %s' % (Song[label][0], bar)
          
          #self.NewPattern.BarSpinBox.setProperty("value", bar['bars'])
          self.NewLabel.NewPattern.bars=bar['bars']
          
          #verifica presenza del metro
          try:
            #controlla meglio ed applica l'enabled in modo coerente
            self.NewLabel.NewPattern.MeterNumSpinBox.setProperty("value", bar['meter'][0])
            self.NewLabel.NewPattern.MeterNumSpinBox.setEnabled(True)
            self.NewLabel.NewPattern.MeterDenSpinBox.setProperty("value", bar['meter'][1])
            self.NewLabel.NewPattern.MeterDenSpinBox.setEnabled(True)
            #self.NewPattern.MeterCustomBtn.setChecked(True)
          except:
            pass
          self.NewLabel.NewPattern.TempoMainSpinBox.setProperty("value", bar['tempo'][0])
          #verifica cambio tempo
          try:
            self.NewLabel.NewPattern.TempoScaleSpinBox.setProperty("value", bar['tempo'][1])
            self.NewLabel.NewPattern.TempoChangeCombo.setCurrentIndex(1)
          except:
            pass
          
          if bar.get('pattern'): 
            self.NewLabel.NewPattern.accents=[b for b in bar.get('pattern')]
            self.NewLabel.NewPattern.AccentsDefBtn.setChecked(True)
            print self.NewLabel.NewPattern.accents
            beats=[b for b in self.NewLabel.NewPattern.BeatsFrame.children() if isinstance(b, BeatBtn)]
            for b in beats:
              b.checkStateSet(self.NewLabel.NewPattern.accents[beats.index(b)])
          
          
          #volume?


if __name__ == "__main__":
  app=QtGui.QApplication(sys.argv)
  klickui=MainWindow()
  klickui.show()
  sys.exit(app.exec_())
