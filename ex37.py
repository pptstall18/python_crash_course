# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:01:18 2021

@author: lihen
"""
# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for i in range(1,11):
  print(i**3)
  
  
  
  

# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
for x in range(0,101):
    if x % 7 == 0:
        print(x)