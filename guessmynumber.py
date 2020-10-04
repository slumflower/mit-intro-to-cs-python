#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Ja 23:51:40 2019

@author: portiajohnson
"""

# Paste your code into this box

x = int(input('Please think of a number between 0 and 100!'))
epsilon = 0.01
num_guesses = 0

low = 0
high = 100
guess = (high +low)/2.0


while abs(guess - x) >= epsilon:
    if guess < x :
        low = guess
        print('Is your secret number ', guess, '?')
    else:
        high = guess
        print('Is your secret number ', guess, '?')
       
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if response == 'l' :
        low = guess
        guess = (low + high)//2
    elif response == 'h':
        high = guess
        guess = (low + high)//2
    elif response == 'c' :
        print('Game over. Your secret number was:', guess)
        break 
    else:
        print('Sorry, I did not understand your input.')
        
#new answer
print("Please think of a number between 0 and 100!")

high = 100
low = 0

answer = False

while answer != 'c': 
    guess = (hi + lo)//2
    print('Is your secret number ', guess, '?') 


    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if response == 'l' :
        low = guess
        guess = (low + high)//2
    elif response == 'h':
        high = guess
        guess = (low + high)//2
    elif response == 'c' :
        answer == True
    else:
        print("Sorry, I did not understand your input.")
        
print('Game over. Your secret number was:', guess)
        
        
#corrected answer
print("Please think of a number between 0 and 100!")

high = 100
low = 0
answer = False

while answer != True: 
    guess = (high + low)//2
    print('Is your secret number ', guess, '?') 
    
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if response == 'l' :
        low = guess
        guess = (low + high)//2
    elif response == 'h':
        high = guess
        guess = (low + high)//2
    elif response == 'c' :
        answer = True
    else:
        print("Sorry, I did not understand your input.")
        
print('Game over. Your secret number was:', guess)



