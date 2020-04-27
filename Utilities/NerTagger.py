from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

class NerTaggerClass:

    def __init__(self,  logger_class_object, STANFORD_RESOURCES):
        self.logger_class_object = logger_class_object
        self.tagger = StanfordNERTagger(STANFORD_RESOURCES['english.all.3class.distsim.crf.ser.gz'],
					   STANFORD_RESOURCES['stanford-ner.jar'],
					   encoding='utf-8')

    def extractNamedEntities(self, text):

        tokenized_text = self.__tokenizeText(text)
        tagged_text = self.__nerTagText(tokenized_text)
        organizations, persons, locations = self.__extractNamedEntities(tagged_text)
        return organizations, persons, locations

    def __extractNamedEntities(self, tagged_text_list):

        persons = {}
        locations = {}
        organizations = {}

        i =0
        while i <len(tagged_text_list):

            curr_word, curr_category = tagged_text_list[i][0], tagged_text_list[i][1]

            if curr_category == 'O':
                i+=1
                continue

            else:
                word = curr_word
                category = curr_category

                i+=1
                while i <len(tagged_text_list) :
                    curr_word, curr_category = tagged_text_list[i][0], tagged_text_list[i][1]
                    if curr_category != category:
                        break
                    else:
                        word = word + '_' + curr_word
                        i+=1
                if category == 'ORGANIZATION':
                    if word in organizations:
                        organizations[word]+=1
                    else:
                        organizations[word]=1
                if category == 'LOCATION':
                    if word in locations:
                        locations[word]+=1
                    else:
                        locations[word]=1
                if category == 'PERSON':
                    if word in persons:
                        persons[word]+=1
                    else:
                        persons[word]=1

        return organizations, persons, locations

    def __tokenizeText(self, text):
        tokenized_text = word_tokenize(text)
        return tokenized_text

    def __nerTagText(self, text):
        tagged = self.tagger.tag(text)
        return tagged




if __name__ == '__main__':


    STANFORD_RESOURCES = {
       'english.all.3class.distsim.crf.ser.gz' : '../Resources/stanford-ner/english.all.3class.distsim.crf.ser.gz',
        'stanford-ner.jar' : '../Resources/stanford-ner/stanford-ner.jar'
    }
    object = NerTaggerClass( None, STANFORD_RESOURCES)

    text = 'The forum directed Grewal Eye Institute, Sector 9, to pay over Rs 1 lakh to the complainant. The Grewal Institute, however, filed an appeal against the forum order. (Representational Image) The forum directed Grewal Eye Institute, Sector 9, to pay over Rs 1 lakh to the complainant. The Grewal Institute, however, filed an appeal against the forum order. (Representational Image)\n\nThe State Consumer Disputes Redressal Commission has directed Grewal Eye Institute and an Insurance Company to pay Rs two lakh to a woman.\n\nThe Apollo Munich Health Insurance Company has been directed to pay Rs 51,000 as the claim amount and Rs 50,000 as compensation, while Grewal Eye Institute has been asked to refund Rs 50,000 excessively charged and Rs 50,000 as compensation.\n\nThe complainant, Shabnam Khunger of Sector 38, Chandigarh said that on December 26, 2011, she opted for health insurance policy from the Insurance Company, which was valid till December 25, 2012, and was renewed to January 19, 2018.\n\nOn October 2, 2017, Shabnam Khunger visited the Grewal Hospital for an eye checkup ad was advised a cataract surgery, and told two kinds of surgeries which is Phaco/Robolazr cataract surgery, which would cost her Rs 1.49 lakh.\n\nShabnam then contacted the Insurance firm for a cashless treatment.\n\nHowever, she was given only Rs 48,000 as cashless treatment under policy, and her claim of Rs 1.01 lakh was rejected. She thus filed a formal case against the insurance firm at the Forum.\n\nThe Insurance firm in reply submitted that there was no need for performing a robotic surgery upon Shabnam Khunger; and that claim for the remaining amount was rightly repudiated by the insurance company.\n\nThe Grewal Eye Institute submitted that the patient opted to go ahead with Robolazr with Symphony IOL implantation worth Rs 1.49 lakh. The Robolazr with Symphony IOL surgery was performed and final bill and discharge certificate after surgery as a protocol to get final approval was sent. We have received the final approval for Rs 48,000 and rest of the amount was paid by patient.\n\nThe forum thus directed Grewal Eye Institute, Sector 9, to pay over Rs 1 lakh to the complainant. The Grewal Institute, however, filed an appeal against the forum order.\n\nThe Commission after hearing the appeal filed by the institute, held that the Grewal Eye Hospital advised Robolazr Cataract Surgery with IOL implant left eye and the doctor concerned, specifically requested Shabnam Khunger to discuss the details with her surgeon to decide which procedure will be suited for her eyes.\n\nHowever, she chose the Robolazr Cataract Surgery.\n\nThe commission in the judgment said, “Dr S P S Grewal stated that the agreed rate of cataract surgery was Rs 48,000. But in the present case, the patient had decided to go for the advised Robolazr Cataract Surgery, it cannot be inferred that the liability of the insurance company restricted to the extent of Rs 48,000, because Dr S P S Grewal stated that this amount was meant for basic cataract surgery. Thus, we are of the considered view that the insurance company is liable to make payment of the entire amount, which is reasonable in terms of the policy. In this view of the matter, the observations of the District Forum that Grewal Hospital had conducted the Robolazr Cataract Surgery, which was neither necessary nor was advised nor was opted by the patient are against the facts and evidence, and thus, not sustainable in the eyes of law.”\n\n“Furthermore, if the machine is costly and out of the reach of a particular hospital or a doctor, then they are not obliged to purchase and install it at the cost of the patients. If they have already installed it, then they cannot charge extra amount for installation of the said machine from the patients. To this extent, we are treating it as an unfair trade practice on part of the Grewal Hospital”, held the commission in its order.\n\n📣 The Indian Express is now on Telegram. Click here to join our channel (@indianexpress) and stay updated with the latest headlines\n\nFor all the latest Chandigarh News, download Indian Express App.'

    organizations, persons, locations = object.tagArticle(text)

    print(organizations)
    print(persons)
    print(locations)


