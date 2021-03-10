# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:51:51 2021

@author: lihen
"""


# Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.

# Specifically:

# If both the last_name and the first_name parameters are supplied, the function should return like s
def format_name(first_name, last_name):
	# code goes here
	if len(first_name)>0 and len(last_name)>0:
		string="Name: " + str(last_name) + ", " +str(first_name)
	elif len(first_name)==0 and len(last_name)==0:
		string=""
	else:
		string="Name: " + str(last_name)+str(first_name)
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string