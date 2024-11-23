##########################################################################
#######BATCH WINDOW SCREENSHOT UTILITY TOOL MADE WITH PYTHON AND BASH#####
##########################################################################
##########################################################################

import subprocess
import os

exe = ".window.sh"
win_file= ".windows.temp"

status1,wmctrl_check = subprocess.getstatusoutput("wmctrl")
status2,magick_check = subprocess.getstatusoutput("import")

if status1 != 1:
    print("Please Install wmctrl on you're machine !!")
    exit(1)
if status2 !=1:
    print("Please Install ImageMagick on you're machine !!")

if not os.path.isfile(exe):
	f = open(exe,'w')
	f.write(f"#$/bin/bash\nmkdir out\nwmctrl -l |grep '0' |sed 's/ .*//' >> {win_file}")
	f.close()
	subprocess.call(["chmod","+x",exe])
	
	
os.system(f"./{exe}")
a=open(win_file,'r')
b=a.read()
arr=b.split()
a.close()
for i in range(len(arr)):
    subprocess.call(["import","-window",str(arr[i]),f"out/{i}.png"])
os.remove(win_file)
os.remove(exe)

##REQUIRMENTS##
#Need Imagemagick
#Need wmctrl
#Only supported on Linux based machines
