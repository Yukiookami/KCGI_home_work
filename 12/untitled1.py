#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:26:40 2021

@author: zouxinyu
"""

import tkinter as tk

root = tk.Tk()
root.title("wo 22 ne")

root.geometry("300x400")

tk.Label(root, text="口口口22").pack()

tk.Button(root, text="小逼崽子", command=root.destroy).pack()

tk.Entry(root, width=20).pack()
tk.Text(root, width=20, height=5).pack()

lb = tk.Listbox(root)
lb.insert(0, "黑楼", "黑旗", "口口口")
lb.pack()

root.mainloop()