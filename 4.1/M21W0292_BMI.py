'''
Author: M21W0292 鄒欣雨
Date: 2021-10-26 19:51:10
LastEditTime: 2021-10-26 22:40:45
FilePath: /python/4.1/M21W0292_BMI.py
'''
cm = int(input('身長を入力してください'))
kg = int(input('体重を入力してください'))

bmi = kg / (cm / 100) ** 2
print(bmi)

if bmi < 18.5:
  print("痩身")
elif bmi > 25:
  print("肥満")
else:
  print("標準体重")