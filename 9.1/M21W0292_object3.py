'''
Author: 鄒欣雨
Date: 2021-11-30 21:53:01
LastEditTime: 2021-11-30 22:02:04
FilePath: /python/9.1/M21W0292_object3.py
'''
class AnimalZoo:
  def __init__(self, name):
    self.__animaCount = 0
    self.__zooName = name
  def animal_up(self, newAnimal):
    self.__animaCount += newAnimal
  def zoo_info(self):
    print('今', self.__animaCount, '匹の動物が', self.__zooName, 'にいます')

my_zoo = AnimalZoo('KCGI動物園')

my_zoo.animal_up(3)

my_zoo.zoo_info()

my_zoo.animal_up(7)

my_zoo.zoo_info()