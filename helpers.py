from __future__ import division

# from nltk.corpus import inaugural

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 100 * count/total

def get_lexical_diversity(self):
    return lexical_diversity(text1)

def get_fileids(self):
    return self.fileids()

def get_categories(self):
    return self.categories()


def get_raw_text(self, address):
    return self.raw(address)

def get_text_count(self, address):
    return len(self.words(address))

def get_uniqs_count(self, address):
    return len(set([w.lower() for w in self.words(address)]))

def get_uniqs(self, address):
    return set([w.lower() for w in self.words(address)])
