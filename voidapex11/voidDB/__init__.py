# voidDb/__init__.py

import json

class connect:

  def formatFile(self):
    '''
    formats a file useing json dump with indent=2
    '''
    json.dump(json.load(open(self.fileName, "r")), open(self.fileName, "w"), indent=2)
  
  def addTable(self, name: str, columns: list, data: list):
    '''
    adds a new voidDB table to the opened file
    '''
    try:
      og = json.load(open(self.fileName, "r"))
    except Exception as e:
      if e == "FileNotFoundError":
        open(self.fileName, "x")
      og = {}
    og[name] = {
      "feilds":columns, 
      "data":data,
    }
    json.dump(og, open(self.fileName, "w"), indent=2)

  def printTable(self, tableName: str, fileName=None):
    '''
    prints a voidDB table
    '''
    #if the filename is non spesified, use the default
    if fileName == None:
      fileName = self.fileName

    #opening the file
    file = json.load(open(fileName, "r"))

    #getting the table
    table = file[tableName]['data']

    #printing tableName
    print(tableName)

    #printing colom names
    for a in file[tableName]['feilds']:
      print(a, end='  ')
    print('')

    #printing data
    for i in table:
      print('|', end=' ')
      for a in i:
        print(i[a], end='')
        print('|', end=' ')
      print('')

  def getTable(self, tableName: str):
    '''
    returns a voidDB table for modificataion/tailored vewing
    '''
    ret1 = json.load(open(self.fileName, "r"))
    return ret1[tableName]

  def __init__(self, db_name):
    '''
    voidDB is a 
    '''
    self.fileName = db_name
    pass