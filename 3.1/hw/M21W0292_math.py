'''
Author: 鄒欣雨 M21W0292
Date: 2021-10-19 20:29:31
LastEditTime: 2021-10-25 14:26:56
FilePath: /python/3.1/hw/M21W0292_math.py
'''
import math

for val in range(2, 7):
  outS = f"{val}の平方根は{round(math.sqrt(val), 2)}です"
  print(outS)

for val in range(0, 5):
  outS = f"eの{val}乗は{round(math.exp(val), 2)}です"
  print(outS)

outS = f"半径１０cmの円の面積は{round(math.pi * (10 ** 2), 2)}です"
print(outS)
