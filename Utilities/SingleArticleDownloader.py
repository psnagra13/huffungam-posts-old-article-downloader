from newspaper import Article
from datetime import datetime
from Utilities.NerTagger import NerTaggerClass
from Utilities.Logger import LoggerClass
class SingleArticleDownloaderClass:

    def __init__(self, logger_class_object, STANFORD_RESOURCES):

        self.logger_class_object = logger_class_object
        self.ner_tagger_object = NerTaggerClass(logger_class_object, STANFORD_RESOURCES)


    def downloadArticle(self, url_of_article):
        article = Article(url_of_article)
        article.download()
        article.parse()
        article.nlp()

        authors_from_newspaper_library = article.authors
        text = article.text
        top_image = article.top_image
        movies = article.movies
        generated_keywords_from_newspaper_library = article.keywords
        generated_summary_from_newspaper_library = article.summary

        organizations, persons, locations = self.ner_tagger_object.extractNamedEntities(text)

        article_object = {
            'newsArticleUrl' : url_of_article,
            'authorsFromNewspaperLibrary' : authors_from_newspaper_library if authors_from_newspaper_library != '' else ' ',
            'textFromNewspaperLibrary' : text,
            'imageFromNewspaperLibrary' : top_image if top_image != '' else ' ',
            'moviesFromNewspaperLibrary' : movies if movies != '' else ' ',
            'generated_keywordsFromNewspaperLibrary': generated_keywords_from_newspaper_library if generated_keywords_from_newspaper_library != '' else ' ',
            'generated_summaryFromNewspaperLibrary': generated_summary_from_newspaper_library if generated_summary_from_newspaper_library != '' else ' ',
            'persons_present': persons,
            'organizations_present': organizations,
            'locations_present': locations,
        }

        return article_object

if __name__ == '__main__':
    STANFORD_RESOURCES = {
        'english.all.3class.distsim.crf.ser.gz': '../Resources/stanford-ner/english.all.3class.distsim.crf.ser.gz',
        'stanford-ner.jar': '../Resources/stanford-ner/stanford-ner.jar'
    }
    logger = LoggerClass()
    single_article_downloader_class_object = SingleArticleDownloaderClass(logger, STANFORD_RESOURCES)
    url_of_article = 'https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020'
    print(datetime.now())
    result = single_article_downloader_class_object.downloadArticle(url_of_article)
    print(datetime.now())

    print(result)

