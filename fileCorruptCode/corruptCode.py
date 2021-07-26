# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:32:03 2020

@author: Usama Ahsan
"""

with open('K17-1017.pdf','rb') as f:
    a=f.read()
    
import numpy as np

x=np.random.randint(len(a)-len(a)//5)

a=a[0:x]+a[x+np.random.randint(len(a)//6):-1]

with open('K17-1017-c.pdf','wb') as f:
    f.write(a)
