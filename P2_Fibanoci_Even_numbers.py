# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:25:28 2022

@author: INDHRNA
"""
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


"""

from time import time
start = time()
import numpy as np
import pandas as pd
from numpy import arange, mod,sum
from pandas import Series
#%%%

if __name__ == '__main__':
    
    number = 4000000
    l = [1,2]
    even = [2]
    for num in (range(3,number)):
        plus = l[-1]+l[-2]
        if plus>=number:    break
        l.append(plus)
        if plus%2==0:
            even.append(plus)
       
    # even = l%2  
    total = sum(even)
