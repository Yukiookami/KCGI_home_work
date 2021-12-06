'''
Author: 鄒欣雨
Date: 2021-11-30 20:04:03
LastEditTime: 2021-11-30 21:34:52
FilePath: /python/9.1/M21W0292_object1.py
'''
class Point:
  def __init__(self, x, y):
    self.__x = x
    self.__y = y
  def distance(self):
    return  (self.__x ** 2 + self.__y ** 2) ** 0.5

p0 = Point(0, 0)
p1 = Point(0, 5)
p2 = Point(5, 5)
p3 = Point(5, 0)

print("p0 から原点の距離 =>", p0.distance())
print("p1 から原点の距離 =>", p1.distance())
print("p2 から原点の距離 =>", p2.distance())
print("p3 から原点の距離 =>", p3.distance())
