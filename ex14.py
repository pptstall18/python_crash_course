# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:44:59 2021

@author: lihen
"""



# Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. 
# Fill in the blanks to complete the code to make it work.
def lucky_number(name):
  number = len(name) * 9
  statement = "Hello " + name + ". Your lucky number is " + str(number)
  return(statement)
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))