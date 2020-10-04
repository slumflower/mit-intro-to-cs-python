# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file.
"""

from math import *

def polysum(n,s):

    '''
    n: number of sides
    s: length of each side
    '''
    area = (0.25*n*(s**2))/tan(pi/n)
    perimeter = n*s
    
    '''
    function should sum area and the square of perimeter
    '''
    
    sum = area + (perimeter**2)
    
    '''
    return the sum, rounded to 4 decimal places
    '''
    
    return round(sum,4)
    