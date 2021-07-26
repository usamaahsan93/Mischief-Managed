# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:37:44 2021

@author: Usama Ahsan
"""

import os, stat
from shutil import copyfile
#copyfile(__file__, __file__)
import subprocess
print(__file__)

#os.chmod(__file__,777)
#print(os.unlink(__file__))

with open('testdef.py','w+') as f:
#    f.write(r'!#C:\Users\Usama Ahsan\Anaconda3\python.exe\n')
    f.write('def fn():\n')
    f.write('\timport time\n')
    f.write('\ttime.sleep(3)\n')
    f.write('\tprint("Hello")\n')

with open('test.py','w+') as f:
#    f.write(r'!#C:\Users\Usama Ahsan\Anaconda3\python.exe\n')
    f.write('import time\n')
    f.write('import os,sys\n')
    f.write('time.sleep(3)\n')
    f.write('print("Hello\n")\n')
    f.write('os.remove("./code.py")')
    f.write('print("Code file removed")\n')
    f.write('sys.exit()')
    


print('waiting')
#import testing
#testing.fn()
#os.chdir(r'C:\Users\Usama Ahsan\Anaconda3')
#subprocess.call('python test.py',shell=True)
subprocess.Popen('python test.py')
#os.system('testing.py')execfile('testing.py')
print('baseCode End')
