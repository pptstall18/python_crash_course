# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:55:12 2021

@author: lihen
"""

def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)