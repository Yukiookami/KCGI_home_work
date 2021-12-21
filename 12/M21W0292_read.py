#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:32:43 2021

@author: zouxinyu
"""
with open('schools.csv', 'rt', encoding='utf_8') as read_obj2 :
    for line in read_obj2:
        print(line.rstrip().split(","))
