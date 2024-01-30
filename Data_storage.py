#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:46 2024

@author: sanelecebekhulu
"""

"""
storing data in python
1. Listd
2. Disctionaries
3. Data frames- specific to pandas
""" 
import pandas 
file = pandas.read_csv ("country_data.csv")

print(file)

print(file.info())


age = 30
age = 25
age = 29

age = [30, 25, 29, 46, 22]

print(age)

print(age[0])

print(age[1])

print (min(age))

print (max(age))

print (len(age))

# print(avg(age))

avg = sum (age)/len(age)

print(avg(age))

"""
Dictionaries - key:value pairs

cat: "a cute animal"

"""

mammals = {"cat": "a cute animal", "lion": "king of the jungle", "elephant": "a gigantic herbivore"}







































































