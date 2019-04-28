# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:52:12 2019

@author: Callum
"""

'''
TOWER OF POWERS - by Callum Alexander

WARNING - This program is very easy to crash as the powers increase really really really quickly. I am
not responsible if your computer legit explodes because you were stupid enough to enter a crazy value for the limit
of the power tower.

Allows the user to enter the base, the power tower limit and will calculate the value.

'''

import time

limit = int(input('Enter the limit   '))
base = int(input('Enter the base     '))

i = 1
while i < limit:
    
    base = base ** i
    print(str(base))
    time.sleep(0.5)
    i += 1
    
print(str(base))