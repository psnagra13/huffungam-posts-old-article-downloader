import threading
from Utilities.Logger import LoggerClass
from Utilities.SingleArticleDownloader import SingleArticleDownloaderClass

class ArticlesDownloaderThreadClass(threading.Thread):
    def __init__(self, STANFORD_RESOURCES, threadId, name, data):
        threading.Thread.__init__(self)

        self.threadId = threadId
        self.name = name
        self.data = data
        self.logger = LoggerClass(self.name)
        self.singleArticleDownloaderClass = SingleArticleDownloaderClass(self.logger, STANFORD_RESOURCES)
        self.logger.Log('Info' , 'Initialized Thread with name ' + self.name + ' and id '+ str(self.threadId))

    def run(self):
        self.logger.Log('Info' , 'Starting Thread with name ' + self.name + ' and id '+ str(self.threadId))

        file_name = "logs/" + self.name + "_downloaded.txt"

        for row in self.data:
            try:
                self.logger.Log('Info', 'Downloading for ' + row['link'])

                d = self.singleArticleDownloaderClass.downloadArticle(row['link'])
                d['category'] = row['category']
                d['headline'] = row['headline']
                d['authors_orig'] = row['authors']
                d['short_description'] = row['short_description']
                d['date'] = row['date']

                f = open(file_name, "a")
                f.write(str(d) + '\n')
                f.close()
            except Exception as e:
                self.logger.Log('Error', 'in downloading for ' + row['link'])
                self.logger.Log('Error', str(e))

        self.logger.Log('Info' , 'Thread work finished for  name ' + self.name + ' and id '+ str(self.threadId))

        return


