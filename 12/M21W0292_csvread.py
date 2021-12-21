# -*- coding: utf-8 -*-
"""
Spyder Editor

鄒欣雨
M21W0292
"""

import csv
with open("./schools.csv","r", encoding="utf-8") as file_in:
    schools_data = csv.reader(file_in)
    for row in schools_data:
        print(row)