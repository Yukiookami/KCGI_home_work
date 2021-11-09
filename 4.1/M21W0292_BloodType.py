'''
Author: M21W0292 鄒欣雨
Date: 2021-10-26 19:55:08
LastEditTime: 2021-10-26 22:40:39
FilePath: /python/4.1/M21W0292_BloodType.py
'''
ba = input('父親:')
mo = input('母親:')

def printMsg (msg):
  print(f'あなたの血液かたは{msg}です')

def printError ():
  print('AまたはBを入力してください')

if ba == 'A':
  if mo == 'A':
    printMsg("AまたはO")
  elif mo == 'B':
    printMsg("A、B、O、ABのいずれか")
  else:
    printError()
elif ba == 'B':
  if mo == 'A':
    printMsg("A、B、O、ABのいずれか")
  elif mo == 'B':
    printMsg("BまたはO")
  else:
    printError()
else:
  printError()