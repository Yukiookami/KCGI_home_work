'''
Author: zxy
Date: 2021-11-23 20:00:52
LastEditTime: 2021-11-23 20:04:21
FilePath: /python/8.1/FolderFCP/bmi_app.py
'''
def bmi (height, weight):
  '''BMIを計算・表示する関数
  入力は身長と体重'''
  bmi = weight / height ** 2 * 10000
  bmi = round(bmi, 1)
  if bmi < 18.5:
    msg = "瘦身"
  elif 25 < bmi:
    msg = "肥満"
  else:
    msg = "標準体重"
  print("あなたの肥満度は",bmi,"で",msg,"です")