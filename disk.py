import os
import time


command_result = os.popen("smartctl -a disk0").read()
lines = command_result.splitlines()

print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
for line in lines:
    if line.find("Data Units Read") != -1:
        print(line)
    if line.find("Data Units Written") != -1:
        print(line)