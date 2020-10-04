#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:33:04 2019

@author: portiajohnson
"""

balance = 3329
annualInterestRate = 0.2

epsilon = 0.01
low = balance / 12
high = (balance * (1 + annualInterestRate / 12) ** 12 ) / 12
ans = (low + high) / 2 
originalBalance = balance



while abs(balance) >= epsilon:
    
    balance = originalBalance
    
    for i in range(12):
        balance = (balance - ans) * (1 + annualInterestRate / 12)
        
    if balance > 0:
        low = ans
        
    else:
        high = ans
            
    ans = (low + high)/2
            
print ("Lowest Payment:", round(ans, 2))