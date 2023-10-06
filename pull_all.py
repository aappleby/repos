#!/usr/bin/python3

#import glob
#for x in glob.iglob('*'):
#    print(x)

import os

root_dir = os.getcwd();

for root, dirs, files in os.walk('.'):
	for dir in dirs:
		if dir.startswith("."):
			continue
		if not os.path.exists(dir + "/.git"):
			continue
		dir = root_dir + "/" + dir
		#print("\n\n########################################")
		print(dir)
		os.chdir(dir)
		os.system("git pull")
	break
