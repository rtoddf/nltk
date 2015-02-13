import nltk

tagged_token = nltk.tag.str2tuple('fly/NN')
# print 'tagged_token: ', tagged_token

# print tagged_token[0]
# print tagged_token[1]

sent = '''The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT interest/NN of/IN both/ABX governments/NNS ''/'' ./.'''

tuples = [nltk.tag.str2tuple(t) for t in sent.split()]

print tuples