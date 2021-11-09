#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:41:06 2021

@author: zouxinyu
"""
import turtle

t1 = turtle.Turtle()

n = int(input('辺数を入力してください'))

for i in range(n):
    t1.forward(100)
    t1.left(360 / n)
    
turtle.done()
turtle.bye()