#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:20:50 2021

@author: Era
"""
#User input
annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
portion = (annual_salary / 12) * portion_saved

semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

#Given information
current_savings = 0.0
portion_down_payment = total_cost * 0.25
r = 0.04
annual_return = current_savings*(r/12)
month = 0

#for calculation
while current_savings <= portion_down_payment:
    current_savings += (current_savings *r/12)  + portion
    month += 1
    
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        portion = (annual_salary / 12) * portion_saved
        
print('Number of months:{}'.format(month))
