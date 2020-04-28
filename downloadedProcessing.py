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
for file in downloaded_files:
    print(file)
    data = getData2(file, logger)

    for row in data:
        newsArticleUrl= row['newsArticleUrl']
        if newsArticleUrl not in downloaded:
            downloaded[newsArticleUrl]=1
        else:
            dup+=1

print(len(downloaded))
print(dup)
with open('downloaded.pkl', 'wb') as f:
    pickle.dump(downloaded, f, pickle.HIGHEST_PROTOCOL)

dd={}
with open('downloaded.pkl', 'rb') as f:
        dd=pickle.load(f)
print(len(dd))



# i=0
# for file in downloaded_files:
#     print(file)
#     f = open(file, "r")
#     raw_data = f.read().split('\n')
#     raw_data = raw_data[:-1]
#     raw_data = '\n'.join(raw_data)
#     file = open('data/processedData/'+str(i), 'w')
#     file.write(raw_data)
#     file.close()
#     i+=1

