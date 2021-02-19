#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:06:59 2021

@author: Era
"""
#User input
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))

#Given information
current_savings = 0
portion_down_payment = total_cost * 0.25
r = 0.04
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * 0.1
annual_return = current_savings*(r/12)
month = 0

#for calculation
while (current_savings < portion_down_payment):
    current_savings += (current_savings *r/12)  + portion_saved
    month += 1
print('Number of months:{}'.format(month))
