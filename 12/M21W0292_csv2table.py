#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:35:39 2021

@author: zouxinyu
"""
import csv
data = []

with open("./schools.csv","r", encoding="utf-8") as file_in:
    schools_data = csv.reader(file_in)
    data.append(['<table>'])
    for row in schools_data:
        for ele in range(len(row)) :
            str = row[ele].replace(' ', '')
            row[ele] = '<td>' + str + '</td>'     
        row.insert(0, '<tr>')
        row.append('</tr>')
        data.append(row)
    data.append(['</table>'])
    print(data)

with open("./schools.html","w", encoding="utf-8", newline="") as file_out:
    csv_out = csv.writer(file_out, quotechar='\"', delimiter=' ')
    csv_out.writerows(data)