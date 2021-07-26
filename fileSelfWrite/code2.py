#counter:1
#-*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:37:44 2021

@author: Usama Ahsan
"""

# import os, stat
# from shutil import copyfile
#copyfile(__file__, __file__)
import subprocess
# print(__file__)

#os.chmod(__file__,777)
#print(os.unlink(__file__))

with open('.temp.py','w+') as f:
#    f.write(r'!#C:\Users\Usama Ahsan\Anaconda3\python.exe\n')
    f.write('import re, fileinput, time, subprocess,sys, os\n')
    f.write('time.sleep(1)\n')
    f.write('with open ("code2.py", "r+") as f:\n')
    f.write('\tfor line in fileinput.input("code2.py"):\n')
    f.write('\t\tif "#counter:" in line :\n')
    f.write('\t\t\tt=int(re.search("[\d]+",line).group(0))\n')
    f.write('\t\t\tif t>=3:\n')
    f.write('\t\t\t\tprint("greater than 5")\n')
    f.write('\t\t\t\twith open("./text.txt","w+") as f:\n')
    f.write('\t\t\t\t\tf.write("This file has been opened "+str(t)+" times, and will now remain static.")\t\n')
    f.write('\t\t\t\tbreak\n')
    f.write('\t\t\telse:\n')
    f.write('\t\t\t\tf.write(line.replace("#counter:"+str(t),"#counter:"+str(t+1)))\n')
    f.write('\t\t\t\twith open("./text.txt","w+") as f:\n')
    f.write('\t\t\t\t\tf.write("This file has been opened "+str(t)+" times.")\n')
    f.write('\t\t\t\tbreak\n')
    f.write('os.system("notepad.exe ./text.txt")\n')
    f.write('subprocess.Popen("powershell Start-Sleep -Seconds 0; Remove-Item ./text.txt")\n')
    f.write('subprocess.Popen("powershell Start-Sleep -Seconds 0.2; Remove-Item ./.temp.py")\n')
    f.write('sys.exit()\n')

subprocess.Popen('python .temp.py')
print('Code2.py exit')


    # f.write('import re, fileinput, time, subprocess,sys\n')
    # f.write('time.sleep(1)\n')
    # f.write('with open ("'+__file__+'", "r+") as f:\n')
    # f.write('\tfor line in fileinput.input("'+__file__+'"):\n')
    # f.write('\t\tif "#counter:" in line :\n')
    # f.write('\t\t\tt=int(re.search("[\d]+",line).group(0))\n')
    # f.write('\t\t\tif t>=3:\n')
    # f.write('\t\t\t\tprint("greater than 3")\n')
    # f.write('\t\t\t\tbreak\n')
    # f.write('\t\t\telse:\n')
    # f.write('\t\t\t\tf.write(line.replace("#counter:"+str(t),"#counter:"+str(t+1)))\n')
    # f.write('\t\t\tsys.exit()\n')
    
    #f.write("subprocess.Popen('powershell Start-Sleep -Seconds 1; Remove-Item ./test.py')\n")
    
    #f.write('time.sleep(3)\n')
    #f.write('time.sleep(3)\n')
    #f.write('time.sleep(3)\n')
    #f.write('time.sleep(3)\n')
    #f.write('from shutil import copyfile\n')
    #f.write('copyfile("./code.py", "./code1.py")\n')
    #f.write('os.remove("./code.py")\n')
    #f.write('print("Counter Updated")\n')
    #f.write('sys.exit()')
    

#subprocess.Popen('powershell Start-Sleep -Seconds 2; Remove-Item ./test.py\n')


#import testing
#testing.fn()
#os.chdir(r'C:\Users\Usama Ahsan\Anaconda3')
#subprocess.call('python test.py',shell=True)
#os.system('testing.py')execfile('testing.py')


# def run(self, cmd):
#     completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
#     return completed


    # f.write('import re, fileinput, time, subprocess,sys, os\n')
    # f.write('time.sleep(1)\n')
    # f.write('with open ("code2.py", "r+") as f:\n')
    # f.write('\tfor line in fileinput.input("code2.py"):\n')
    # f.write('\t\tif "#counter:" in line :\n')
    # f.write('\t\t\tprint(line)\n')
    # f.write('\t\t\tt=int(re.search("[\d]+",line).group(0))\n')
    # f.write('\t\t\tif t>=10:\n')
    # f.write('\t\t\t\tprint("greater than 5")\n')
    # f.write('\t\t\t\tbreak\n')
    # f.write('\t\t\telse:\n')
    # f.write('\t\t\t\tf.write(line.replace("#counter:"+str(t),"#counter:"+str(t+1)))\n')
    # f.write('\t\t\t\twith open("./text.txt","w+") as f:\n')
    # f.write('\t\t\t\t\tf.write("This file has been opened "+str(t)+" times.")\n')
    # f.write('\t\t\t\tbreak\n')
    # f.write('os.system("notepad.exe ./text.txt")\n')
    # f.write("subprocess.Popen('powershell Start-Sleep -Seconds 0; Remove-Item ./text.txt')\n")
    # f.write("subprocess.Popen('powershell Start-Sleep -Seconds 0.1; Remove-Item ./.temp.py')\n")
    
    # f.write('sys.exit()\n')

# print('test.py written')