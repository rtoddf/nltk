import nltk

def extract_property(prop, text):
    return [prop(word) for word in text]

def last_letter(word):
    return word[-1]

einstein = 'Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning.'
einstein_tokens = nltk.word_tokenize(einstein)
einstein_tokens.sort()
einstein_tokens.reverse()
print 'einstein: ', einstein_tokens

print 'length of words: ', extract_property(len, einstein_tokens)

# def monty():
# 	return 'Monty Python'

# print monty()

sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']



# len_words = extract_property(len, sent)
# print len_words
# # print extract_property(last_letter)
# last_letter = extract_property(lambda w: w[-1])
# print last_letter

# print sorted(sent, cmp)
# print sorted(sent, lambda x, y: cmp(len(y), len(x)))
