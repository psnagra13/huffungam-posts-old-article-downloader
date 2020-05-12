import json
from Utilities.Logger import LoggerClass
from Utilities.UtilFunctions import *
from Utilities.ArticlesDownloaderThread import ArticlesDownloaderThreadClass
import pickle
data_path = 'data/news-category-dataset/News_Category_Dataset_v2.json'

STANFORD_RESOURCES = {
        'english.all.3class.distsim.crf.ser.gz': 'Resources/stanford-ner/english.all.3class.distsim.crf.ser.gz',
        'stanford-ner.jar': 'Resources/stanford-ner/stanford-ner.jar'
    }
NUMBER_OF_THREADS = 10

logger = LoggerClass()

logger.Log('Info', 'run.py started')

data = getData(data_path, logger)

downloaded = {}
with open('downloaded.pkl', 'rb') as f:
        downloaded=pickle.load(f)
print(len(downloaded))

not_downloaded = []

for row in data:
    link = row['link']
    if link not in downloaded:
        not_downloaded.append(str(row))

print(len(not_downloaded))

not_downloaded_str = '\n'.join(not_downloaded)

file = open('data/not_downloaded', 'w')
file.write(not_downloaded_str)
file.close()