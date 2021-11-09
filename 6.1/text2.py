#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:22:20 2021

@author: zouxinyu
"""

import turtle

t1 = turtle.Turtle()

t1.shape("turtle")
t1.color("red", "yellow")

t1.begin_fill()
for i in range(5):
    t1.forward(100)
    t1.left(360 / 5 * 2)

t1.end_fill()

t2 = turtle.Turtle()

t2.shape("turtle")
t2.color("blue", "yellow")

t2.right(180)
for i in range(5):
    t2.forward(100)
    t2.right(360 / 5 * 2)

turtle.done()
turtle.bye()