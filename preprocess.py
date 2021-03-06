from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

class PreProcess:
    def __init__(self):
        self.tokenizer = word_tokenize
        self.stemmer = PorterStemmer()
        self.punct = string.punctuation
        self.digits = string.digits
        self.stop = stopwords.words("english")

    def process_sent(self, snt):
        snt = self.tokenizer(snt)
        snt = [self.stemmer.stem_word(wrd.lower()) for wrd in snt if \
                    wrd not in self.stop and \
                    wrd not in self.digits and \
                    wrd not in self.punct ]
        return snt

    def process(self, snts):
        return [self.process_sent(snt) for snt in snts]

if __name__ == '__main__':
    pre_process = PreProcess()
    res = pre_process.process(['Hi my name is Mateus. How are you!?>', 'Hey, this is me!'])
    print(res)
