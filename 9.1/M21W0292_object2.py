'''
Author: 鄒欣雨
Date: 2021-11-30 21:36:24
LastEditTime: 2021-11-30 21:52:33
FilePath: /python/9.1/M21W0292_object2.py
'''
class Animals:
  def say(self):
    print('私は動物です')

class Tigers(Animals):
  def say(self):
    print('私は虎です')
  def claim(self):
    print('私はライイオンよりも強い')

tiger = Tigers()

tiger.say()
tiger.claim()

animal = Animals()

animal.say()

try:
  animal.claim()
except:
  print('エラー')