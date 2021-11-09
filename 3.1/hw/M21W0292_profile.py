'''
Author: 鄒欣雨 M21W0292
Date: 2021-10-19 21:22:53
LastEditTime: 2021-10-19 23:10:14
FilePath: /python/3.1/hw/M21W0292_profile.py
'''
name = "鄒欣雨"
year = "2021"
number = "M21W0292"
nationality = "中国"

my_profile = "氏名: {},  入学年度: {}, 番号: {}, 国籍: {}"

profile_text = my_profile.format(name, year, number, nationality)

print(my_profile, ' ', profile_text)

print(len(my_profile), len(profile_text))

print(profile_text.split(","))

profile_text2 = f"氏名: {name},  入学年度: {year}, 番号: {number}, 国籍: {nationality}"

print(profile_text2)

