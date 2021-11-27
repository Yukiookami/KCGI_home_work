# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:46:13 2021

@author: kcg
"""

print("あなたの肥満度を計算します")
weight = int(input("体重をkgで入力>>"))
height = int(input("身長をcmで入力>>"))

bmi = weight / height**2 * 10000
bmi = round(bmi, 1)
if bmi < 18.5:
    message = "痩身"
elif 25.0 <= bmi:
    message = "肥満"
else:
    message = "標準体重"
print("あなたの肥満度は",bmi,"で",message,"です")


