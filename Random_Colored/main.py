#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:54:10 2021

@author: sdn1
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
import numpy as np
import os

i=0
while(i<1):
    1/0
    print(bcolors.OKGREEN + chr(np.random.randint(250,400)) + bcolors.ENDC, end='')
    os.system('python $(pwd)/main.py')
    i=i+1
    print(i)
