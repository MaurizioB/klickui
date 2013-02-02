#! /usr/bin/python  
# -*- coding: utf-8 -*  

from ui_patternwidget import *
from ui_labelwidget import *

def bind(objectName, propertyName, type):

    def getter(self):
        return type(self.findChild(QtCore.QObject, objectName).property(propertyName).toPyObject())
    
    def setter(self, value):
        self.findChild(QtCore.QObject, objectName).setProperty(propertyName, QtCore.QVariant(value))
    
    return property(getter, setter)

class LabelWidget(LabelWidget):
  def __init__(self, parent=None):
    super(LabelWidget, self).__init__(parent)
    
    #al momento è così, poi implementa questo dal main
    #self.startBar=1
    self.addSubPattern()

  def __str__(self):
    return '\n'.join([str(p) for p in self.listPatterns()])
    #if self.label: label='%s:' % self.label
    

  def addSubPattern(self):
    self.NewPattern=PatternWidget(self)
    self.NewPattern.setObjectName('NewPattern')
    self.NewPattern.meter='4/4'
    self.patternLayout.addWidget(self.NewPattern)
    QtCore.QObject.connect(self.NewPattern.BarSpinBox, QtCore.SIGNAL("valueChanged(int)"), lambda x: self._set_bars())
    print self.NewPattern.BarSpinBox.text()


  def stampa(self,x):
    print self

  def listPatterns(self):
    return [p for p in self.PatternFrame.children() if isinstance(p, PatternWidget)]
  
  def _get_bars(self):
    return sum([b.bars for b in self.listPatterns()])

  def _set_bars(self):
    totbars=sum([b.bars for b in self.listPatterns()])
    self.TotBarCountLbl.setText(str(totbars))
    self.LastBarLbl.setText(str(self.startBar+totbars-1))
  
  bars = property(_get_bars, _set_bars)
  


class PatternWidget(PatternWidget):
  def __init__(self, parent=None):
    super(PatternWidget, self).__init__(parent)
    
    # definisci i valori di default:
    #self.beatss=4
    
    #per ora lasciamo così, più avanti trova un sistema migliore per coinvogliare la variabile con gli oggetti.
    #tipo un metodo accents che restituisca anche gli accenti "fantasma"
    self.accents=['X','x','x','x']
    self.label=None
    for b in ['X','x','x','x']:
      self.addBeat(b)
    QtCore.QObject.connect(self.MeterNumSpinBox, QtCore.SIGNAL("valueChanged(int)"), lambda: self.setBeatBtns())
    
    #self.FirstBarLbl.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    #self.connect(self, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.on_context_menu)
    
    self.popMenu = QtGui.QMenu(self)
    self.popMenu.addAction(QtGui.QAction('test0', self))
    self.popMenu.addAction(QtGui.QAction('test1', self))
    self.popMenu.addSeparator()
    self.popMenu.addAction(QtGui.QAction('test2', self))
    
    #self.accents=self.listAccents()
    self.newAccents=lambda: self.listAccents()
  
  def _get_meter(self):
    return (self.MeterNumSpinBox.value(), self.MeterDenSpinBox.value())
  
  def _set_meter(self, assign):
    if type(assign) is str:
      assign=map(int, assign.split('/'))
    self.beats=assign[0]
    self.denom=assign[1]

  #def label(self, assign=None):
    #if not assign:
      #return None
    #else:
      ##aggiungi definizione della label attuale
      ##self.label=assign
      #return assign
  

  bars = bind("BarSpinBox", "value", int)
  beats = bind("MeterNumSpinBox", "value", int)
  denom = bind("MeterDenSpinBox", "value", int)
  meter = property(_get_meter, _set_meter)
  tempo = bind("TempoMainSpinBox", "value", int)
  volume = bind("VolSpinBox", "value", int)
  


  
  def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.mapToGlobal(point))
        
  def __str__(self):
    #if self.label(): label='%s:' % self.label()
    #else: label=''
    if self.label: label='%s:' % self.label
    else: label=''
    if self.MeterNumSpinBox.isEnabled(): meter='%i/%i ' % (self.beats, self.denom)
    else: meter=''
    if self.BeatsFrame.isEnabled(): accents=''.join(self.accents)+' '
    else: accents=''
    if self.VolDefBtn.isChecked(): volume=self.volume()
    else: volume=''
    #[label:] bars [meter] tempo [pattern] [volume]
    return '%s\t%i %s%i %s%s' % (label, self.bars, meter, self.tempo, accents, volume)


  def setBeatBtns(self):
    if self.BeatsLayout.count() < self.beats:
      while self.BeatsLayout.count() != self.beats:
        self.addBeat('x')
        self.accents.append('x')
    elif self.BeatsLayout.count() > self.beats:
      for i in range(self.BeatsLayout.count(), self.beats, -1):
        self.BeatsLayout.itemAt(i-1).widget().deleteLater()
        del self.accents[-1]
  
  def addBeat(self, accent):
    self.beat=BeatBtn(self)
    self.beat.setObjectName('beat')
    self.beat.accent=accent
    self.beat.checkStateSet(accent)
    self.BeatsLayout.addWidget(self.beat)
    
  def listAccents(self):
    return [p.accent for p in self.BeatsFrame.children() if isinstance(p, BeatBtn)]
  

class BeatBtn(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(BeatBtn, self).__init__(parent)
        #palette=QtGui.QPalette()
        
        self.setMinimumHeight(72)
        self.setCheckable(True)
        self.accent='x'
        #self.checkStateSet(self.accent)
        self.setChecked(True)
        self.setToolTip("Left click to switch Accent/Beat, right for silence")
        

    # definisci meglio i checkstate (accent)
    def mouseReleaseEvent(self, event):
      if event.button() == QtCore.Qt.LeftButton:
        self.nextCheckState()
      elif event.button() == QtCore.Qt.RightButton:
        self.accent='.'
        self.checkStateSet(self.accent)
        
    def checkStateSet(self, accent='x'):
      palette=QtGui.QPalette()

      # riordina in modo più logico gli stati
      if accent=='.':
        brush = QtGui.QBrush(QtGui.QColor(210,210,210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
      elif accent=='X':
        brush = QtGui.QBrush(QtGui.QColor(10,10,10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60,185,60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
      else:
        brush = QtGui.QBrush(QtGui.QColor(150,150,150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150,200,150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)

      self.setPalette(palette)

    
    def nextCheckState(self):
      #palette=QtGui.QPalette()
      #print palette.currentColorGroup
      #print self
      #fai ordine e valuta se invertire l'ordine di questi next
      if self.accent=='x':
        # Accento forte!
        self.accent='X'
        self.checkStateSet('X')
      else:
        # Accento normale
        self.accent='x'
        self.checkStateSet('x')
      #self.accents=accent

    #forse puoi toglierla ora
    def emptyCheckState(self):
      self.accent='.'
      self.checkStateSet('.')
