#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:59:03 2021

@author: Era
"""

semi_annual_raise = .07
annual_return = 0.04
total_cost = 1000000
down_payment = 0.25 * total_cost

starting_annual_salary = float(input('Enter the starting salary: '))

epsilon = 100
high_savings = 10000
low_savings = 0
best_savings_integer = high_savings
steps = 0
pay_in_three_years = True
while True:
    steps += 1
    annual_salary = starting_annual_salary
    best_portion = best_savings_integer / 10000
    portion = (annual_salary / 12) * best_portion
    
    current_savings = 0.0
    month = 0
    
    while month <= 36:
        current_savings += portion + (current_savings * (annual_return/12))
        month += 1
        
        if month % 6 ==0:
            annual_salary += annual_salary * semi_annual_raise
            portion = (annual_salary / 12) * best_portion
            
    if abs(current_savings - down_payment) <= epsilon:
        break
    
    if current_savings > down_payment:
        high_savings = best_savings_integer
    else:
        low_savings = best_savings_integer
        
    if low_savings >= high_savings:
        pay_in_three_years = False
        break
    
    best_savings_integer = (high_savings + low_savings) //2
    
if pay_in_three_years:
    print('Best savings rate: {}'.format(best_portion))
    print('Steps in bisection search: {}'. format(steps))
else:
    print('It is not possible to pay the down payment in three yeers.')