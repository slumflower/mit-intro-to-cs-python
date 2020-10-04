#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:51:59 2019

@author: portiajohnson
"""

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal
 

def remain(balance, annualInterestRate, monthlyPaymentRate, months):  
   if months == 1:
       return (balance - monthlyPaymentRate*balance) + (annualInterestRate/12)*(balance - monthlyPaymentRate*balance)
   else:
       return remain((balance - monthlyPaymentRate*balance) + (annualInterestRate/12)*(balance - monthlyPaymentRate*balance), annualInterestRate, monthlyPaymentRate, months-1)
    
    
print(remain(42, 0.2, 0.04, 12))

def remain(balance, annualInterestRate, monthlyPaymentRate, months):  
   if months == 1:
       return (round((balance - monthlyPaymentRate*balance) + (annualInterestRate/12)*(balance - monthlyPaymentRate*balance),2))
   else:
       return remain((balance - monthlyPaymentRate*balance) + (annualInterestRate/12)*(balance - monthlyPaymentRate*balance), annualInterestRate, monthlyPaymentRate, months-1)

print(remain(42, 0.2, 0.04, 12))





monthlyInterest = annualInterestRate/12

for i in range (12):
    minimum_payment = monthlyPaymentRate * balance
    unpaid_balance = balance - minimum_payment
    new_balance = unpaid_balance + monthlyInterest * unpaid_balance
    balance = new_balance
    

print(round(balance, 2))



monthlyInterest = annualInterestRate/12
fixedPayment = 10
months = 0


while months <= 12:

    unpaid_balance = balance - fixedPayment
    new_balance = unpaid_balance + monthlyInterest * unpaid_balance
    balance = new_balance

    if balance <= 0:
        print(round(balance, 2))

    else:
        fixedPayment += 10

