import json
from Utilities.Logger import LoggerClass
from Utilities.UtilFunctions import *
from Utilities.ArticlesDownloaderThread import ArticlesDownloaderThreadClass

data_path = 'data/not_downloaded'

STANFORD_RESOURCES = {
        'english.all.3class.distsim.crf.ser.gz': 'Resources/stanford-ner/english.all.3class.distsim.crf.ser.gz',
        'stanford-ner.jar': 'Resources/stanford-ner/stanford-ner.jar'
    }
NUMBER_OF_THREADS = 50

logger = LoggerClass()


logger.Log('Info', 'run.py started')

data = getData2(data_path, logger)
print(len(data))
data= data[7700:]
print(len(data))

divided_lists = divideList(NUMBER_OF_THREADS, data, logger)

threads_list = []

for i in range(0, NUMBER_OF_THREADS):
    thread_name = 'THREAD_' + str(i)
    th = ArticlesDownloaderThreadClass(STANFORD_RESOURCES, i, thread_name, divided_lists[i])
    threads_list.append(th)

print(threads_list)

for thread in threads_list:
    thread.start()










