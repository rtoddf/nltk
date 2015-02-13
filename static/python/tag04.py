import nltk
from nltk.corpus import brown

# brown_learned_text = brown.words(categories='learned')
# brown_sorted = sorted(set(b for (a, b) in nltk.ibigrams(brown_learned_text) if a == 'often'))

brown_learned_text_tagged = brown.tagged_words(categories='learned', simplify_tags=True)
## b[0] is the word after a
## b[1] is part of speech of the word after a
## a[0] is, in this case, 'often'
## a[1] is, in this case, the part of speech of 'often'
tags = [b[1] for (a, b) in nltk.ibigrams(brown_learned_text_tagged) if a[0] == 'often']

freq_dist = nltk.FreqDist(tags)
freq_dist_tab = freq_dist.tabulate()

print freq_dist_tab