# -*- coding: utf-8 -*-
"""Untitled53.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-rSLCOhLJyAtbvWP3cwQ9Y1MaRZYLSo6
"""

def kms():
    kiloMeters = float(input("Enter no of kilometers : "))
    print("{} km is Equal to {} miles".format(kiloMeters,kiloMeters*0.621))
kms()

def celToFarh():
    celsius = int(input("Enter temperature in celsius : "))
    Farenheit = (celsius*(9/5))+32
    print("{}° Celsius is Equal to {}° Farenheit".format(celsius,Farenheit))
    
celToFarh()

import calendar

def showCalender():
    year = int(input("Enter calender year: "))
    print(calendar.calendar(year))
    
showCalender()

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))


def swapNumbers(num_1,num_2):
        print('Before Swapping',num_1,num_2)
        num_1 = num_1+num_2
        num_2 = num_1-num_2
        num_1 = num_1-num_2
        print('before Swapping',num_1,num_2)

swapNumbers(num_1,num_2)

