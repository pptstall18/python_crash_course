# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:02:58 2021

@author: lihen
"""


# Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
def sum_positive_numbers(n):
  if n < 1:
    return 0
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15