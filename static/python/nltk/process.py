import nltk

raw_text = "Mr. Christie's comments came after weeks of steadfast denials by the governor that his administration was involved."

# tokenize = nltk.word_tokenize(raw_text)
# pos_tag = nltk.pos_tag(raw_text)
# help = nltk.help.upenn_tagset('CC')

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())

print 'text: ', text.similar('bought')

# print 'tokenize: ', tokenize
# print 'pos_tag: ', pos_tag
# print 'help: ', help