# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:57:40 2021

@author: lihen
"""

# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.
def sum_divisors(n):
  sum = 0
  t=1
  while t < n:
    if n % t == 0:
      sum += t
    t += 1
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114