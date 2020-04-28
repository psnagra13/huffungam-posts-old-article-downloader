import os
from Utilities.UtilFunctions import *
from Utilities.Logger import LoggerClass
import pickle
data_path = 'data/processedData'
downloaded_files =[]

logger = LoggerClass()

for path, subdirs, files in os.walk(data_path):
    for name in files:
        downloaded_files.append(os.path.join(path, name))
downloaded = {}
dup=0
raw_data=''
for file in downloaded_files:
    print(file)
    f = open(file, "r")
    raw_data += f.read() + '\n'

file = open('data/all', 'w')
file.write(raw_data)
file.close()
