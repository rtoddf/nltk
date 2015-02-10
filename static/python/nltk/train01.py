import nltk
from nltk.corpus import nps_chat

text = nltk.corpus.nps_chat.words()
cut = int(0.9 * len(text))
training_data, test_data = text[:cut], text[cut:]

# check to see if any of the original data is lost or overlaps
print text == training_data + test_data

# check to see if we are dividing the text correctly
print len(training_data)/len(test_data)

print test_data