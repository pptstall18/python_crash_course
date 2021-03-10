# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:54:49 2021

@author: lihen
"""


# Can you work out what this function does? Try passing different parameters to the attempts function to see what it does. 
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)