# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:55:38 2021

@author: lihen
"""

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n= n+1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 