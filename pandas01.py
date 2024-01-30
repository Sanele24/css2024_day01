#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:13:04 2024

@author: sanelecebekhulu
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

import pandas

file = pandas.read_csv ("diab_data.csv")

print(file)

print(file.info())

print(file.describe())


file = pandas.read_csv("housing_data.csv")

print(file)

print(file.info())

print(file.describe())

file = pandas.read_csv ("iris.csv")

print(file)

print(file.info())

print(file.describe())

file = pandas.read_csv("insurance_data.csv", skiprows=5)

file = pandas.read_csv("insurance_data.csv", skiprows= 5)

