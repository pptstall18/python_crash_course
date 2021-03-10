# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:17:50 2021

@author: lihen
"""

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a+amount_b
print(result)