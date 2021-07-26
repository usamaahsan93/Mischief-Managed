# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:00:21 2021

@author: Usama Ahsan
"""
#l=[]
with open('counterUpdate.py','r') as f:
    a=f.readlines()
#    l.append(a)
#print()

k=[] 
for i in a:
    jkl="f.write(\'"+i
    jkl=jkl.replace('\n',"\\n")
    jkl=jkl.replace('\t',"\\t")
    #jkl=jkl.replace('"',"\\\"")
    jkl=jkl+'\')\n'
    k.append(bytes(jkl,'utf-8'))
    
with open('mytst.py','wb') as f:
    f.writelines(k)
