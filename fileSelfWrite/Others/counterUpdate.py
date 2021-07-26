import re, fileinput, time, subprocess,sys, os
time.sleep(1)
with open ("code2.py", "r+") as f:
	for line in fileinput.input("code2.py"):
		if "#counter:" in line :
			t=int(re.search("[\d]+",line).group(0))
			if t>=5:
				print("greater than 5")
				with open("./text.txt","w+") as f:
					f.write("This file has been opened "+str(t)+" times, amd will now remain static.")	
				break
			else:
				f.write(line.replace("#counter:"+str(t),"#counter:"+str(t+1)))
				with open("./text.txt","w+") as f:
					f.write("This file has been opened "+str(t)+" times.")
				break
os.system("notepad.exe ./text.txt")
subprocess.Popen('powershell Start-Sleep -Seconds 0; Remove-Item ./text.txt')
subprocess.Popen('powershell Start-Sleep -Seconds 0.2; Remove-Item ./.temp.py')
sys.exit()
