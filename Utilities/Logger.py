from datetime import datetime

class LoggerClass:

    def __init__(self, name='MAIN'):
        self.name = name
        None

    def Log(self, type, message ):

        log_string = self.name + ' : '
        log_string += str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        log_string += ' '
        log_string +=  type
        log_string += ': '
        log_string += message
        log_string += '\n'

        if type == 'Info_ArticleDownloaded':
            file_path = 'logs/' + datetime.now().strftime("%Y%m%d") + "_articleDownloaded.txt"
            f = open(file_path, "a+")
            f.write(log_string)
            f.close
        else:
            file_path = 'logs/'+datetime.now().strftime("%Y%m%d") + ".txt"
            f = open(file_path, "a+")
            f.write(log_string)
            f.close