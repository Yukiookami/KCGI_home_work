'''
Author: M21W0292 鄒欣雨
Date: 2021-10-26 20:02:21
LastEditTime: 2021-10-26 22:57:03
FilePath: /python/4.1/M21W0292_GuessNumber.py
'''
from random import randint

target = randint(1, 100)

while True:
  guess = int(input('整数を入力してください'))
  
  if target - guess > 0:
    print('入力値より大きいです')
  elif guess - target > 0:
    print('入力値 より小さいです')
  else:
    print('当たり！')
    break