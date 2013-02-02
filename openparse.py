#! /usr/bin/python  
# -*- coding: utf-8 -*  

import string, re, collections

#Song = {}
#se non mi trovo con la ordereddict creo una lista con l'associazione id>label
#LabelList = []

#valuta se partire cmq da labelid 0, così da esser coerente col numero battute

def TempoMapConv(tempomap):
  patregex=re.compile('[Xx.]*$')
  i=0; opList={}
  opList['bars']=tempomap[i];i+=1
  if tempomap[i].count('/'):
    #opList['meter']=tempomap[i];i+=1
    opList['meter']=tempomap[i].split('/');i+=1
  #opList['tempo']=tempomap[i];i+=1
  opList['tempo']=tempomap[i].split('-');i+=1
  if i<len(tempomap):
    if patregex.match(tempomap[i]):
      opList['pattern']=tempomap[i];i+=1
      if i<len(tempomap):
	opList['volume']=tempomap[i]
    else:
      opList['volume']=tempomap[i]
  return opList

def loadFile():
  Song=collections.OrderedDict()
  empty = "\n","#"
  LabelId = -1
  cfgfile = open("test.klick","r")
  for riga in cfgfile.readlines():
    ignora = 0
    if riga == "":
      print "fine del file"
      break
    else:
      for i in empty:
	if string.find(riga,i) == 0:
	  #print "* ignora riga ("+i.replace('\n','newline')+"): "+riga[:-1]
	  ignora = 1
	  continue #ignora la riga
	else:
	  continue
      if not ignora:
	RigaPulita = riga[:-1].split()
	if RigaPulita[0][-1] == ':':
	  LabelId = LabelId+1
	  Label=RigaPulita[0][:-1]
	  #for Valori in RigaPulita[1:]
	  #Song.append([Label,RigaPulita[1:]])
	  Song[Label]=[TempoMapConv(RigaPulita[1:])]
	  #Song[LabelId]=Song[Label]
	  #LabelList.append(Label)
	  
	else:
	  #pass
	  Song[Label].append(TempoMapConv(RigaPulita))
	  #Song[LabelId].append(RigaPulita)
  cfgfile.close()
  return Song


#for i in range(max(filter(lambda x: str(x).isdigit(), Song.keys())) + 1):
#for i in range(len(Song.keys())):
#  print Song.keys()[i]+' (pattern: '+str(len(Song.values()[i]))+'):'
#  print Song.values()[i]
#  print
  
      #Song.append(RigaPulita)


#break
#print Song