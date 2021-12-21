# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:31:20 2021

@author: KCG
"""


import random

import tkinter as tk

root = tk.Tk()

root.title('おみくじ')
root.geometry('300x200')

tk.Label(root, text="あなたの運勢を占います！")

buff = tk.StringVar()
lb = tk.Label(root, textvariable=buff).pack()

def fortne():
    words = ["大吉：運勢はとても良い",
         "吉：運勢はとても良い",
         "小吉：運勢はすこし良い",
         "凶：運勢は悪い",
         "大凶：運勢はとても悪い"]
    n = random.randint(0, len(words)-1)
    buff.set(f'あなたの運勢は「{words[n]}」です')

tk.Button(root, text="押すと占います", command=fortne).pack()

root.mainloop()