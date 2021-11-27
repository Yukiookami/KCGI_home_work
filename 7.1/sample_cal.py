# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:52:21 2021

@author: kcg
"""

def calc(num, size="M"):
    unit_price = {"S": 50, "M":98, "L": 120}
    print("単価は", unit_price[size], end=";")
    return int(num) * unit_price[size]

while True :
    input_num = input("個数を入れてください。（qで終了）>>")
    if input_num == "q" :
        break    
    result = calc(input_num, size="S")
    print('単価98なので価格は', result)
print('処理終了')