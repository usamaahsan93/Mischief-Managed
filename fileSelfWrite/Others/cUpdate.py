import re, fileinput, time
time.sleep(3)
with open ('code1.py', 'r+') as f:
	for line in fileinput.input('code1.py'):
	    if '#counter:' in line :
	    	print(line,type(line))
	    	t=int(re.search('[\d]+',line).group(0))
	    	f.write(line.replace('#counter:'+str(t),'#counter:'+str(t+1)))
	    	print('Match Found')
	    	break