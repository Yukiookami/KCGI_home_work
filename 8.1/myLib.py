'''
Author: zxy
Date: 2021-11-23 18:45:36
LastEditTime: 2021-11-23 20:06:28
FilePath: /python/8.1/myLib.py
'''
from FolderFCP.bmi_app import bmi

print("あなたの肥満度を計算します")
weight = int(input("体重をkgで入力>>"))
height = int(input("身長をcmで入力>>"))
bmi(height, weight)

