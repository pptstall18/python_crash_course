# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:46:48 2021

@author: lihen
"""


# The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0. 
# Can you fill in the gaps to make that happen?

def number_group(number):
  if number>0:
    return "Positive"
  elif number<0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative