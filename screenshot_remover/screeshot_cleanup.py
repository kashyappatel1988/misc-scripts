#!/usr/local/bin/python3

import sys
import os
import subprocess
import re
import datetime


current_DT = datetime.datetime.now()
user = (os.getlogin())
os.chdir(f'/Users/{user}/Desktop')
# print (sys.path)
# print (os.path.dirname(__file__))
# print (os.getcwd())
# reg =
cmd = ("find Screen* | grep '2019-11'")
try:
    proc1 = subprocess.check_output(cmd,shell=True)
except:
    print (f'No files found on {current_DT.date()}')
    sys.exit()

new_string =  str(proc1)
op = re.findall("Screen\sShot.\d+-\d+-\d+\s.*?png",new_string)
([os.system(f'rm -rf "{element}"') for element in op])
try:
    os.system(cmd)
except:
    print ("Error")
