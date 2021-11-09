#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:49:45 2021

@author: zouxinyu
"""
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape("turtle")
t1.color("red")
t2.shape("turtle")
t2.color("blue")

t1.forward(50)
for i in range(3):
    t1.forward(150)
    t1.right(360 / 3)

t2.left(180)
t2.forward(50)

while True:
    t2.forward(150)
    t2.left(110)
    if abs(t2.pos()) < 50 and abs(t2.pos()) > 48:
        break
    
turtle.done()
turtle.bye()