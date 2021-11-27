# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:59:39 2021

@author: kcg
"""

# 高さ５，半径10の円柱の体積
def cylinder_volume(height, radius):
    volume = (radius ** 2) * 3.14 * height
    return volume

#円柱の体積を求める公式
print(cylinder_volume(10, 5))