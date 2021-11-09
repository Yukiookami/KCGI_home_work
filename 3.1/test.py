'''
Author: zxy
Date: 2021-10-19 18:54:06
LastEditTime: 2021-10-19 19:19:51
FilePath: /python/3.1/test.py
'''
a = 100
b = 200
c = 300

sum = a + b + c

print(a, b, c, sep="，", end="・・・・・合計は")
print(sum)

# weight = float(input("体重を入れて＞＞＞"))
# height = float(input("身長を入れて＞＞＞"))

# bim = weight / height ** 2

# print( round(bim, 2))

from math import factorial as fa

print(fa(1))
print(fa(3))
print(fa(4))
print(fa(6))
print(fa(10))
print(fa(50))