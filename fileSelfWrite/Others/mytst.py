f.write('import re, fileinput, time, subprocess,sys, os\n')
f.write('time.sleep(1)\n')
f.write('with open ("code2.py", "r+") as f:\n')
f.write('\tfor line in fileinput.input("code2.py"):\n')
f.write('\t\tif "#counter:" in line :\n')
f.write('\t\t\tt=int(re.search("[\d]+",line).group(0))\n')
f.write('\t\t\tif t>=5:\n')
f.write('\t\t\t\tprint("greater than 5")\n')
f.write('\t\t\t\twith open("./text.txt","w+") as f:\n')
f.write('\t\t\t\t\tf.write("This file has been opened "+str(t)+" times, amd will now remain static.")\t\n')
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
