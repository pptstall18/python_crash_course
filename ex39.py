# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:02:29 2021

@author: lihen
"""

# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    if number == 1:
    # If number is equal to 1, it's a power (base**0).
      return True
    else:
      return False

  # Recursive case: keep dividing number by base.
  return is_power_of(number // base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False