from nltk.corpus import wordnet

syns = wordnet.synsets("program")
#synset
print syns

#just the word
print syns[0].lemmas()[0].name()

#definition
print syns[0].definition()

#examples
print syns[0].examples()

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        print 'l:',l
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print (w1.wup_similarity(w2))
