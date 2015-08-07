import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier #wrapper to include sk algos within nltk classifier

import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words) # will be true or false
    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

training_set = featuresets[:1900] # first 1900
testing_set = featuresets[1900:] # everything after first 1900

#posterior = (prior occurences x liklihood) / evidence
#classifier = nltk.NaiveBayesClassifier.train(training_set)
classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()


print("original NB algo accuracy percent: ", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent: ", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

##GaussianNB_classifier = SklearnClassifier(GaussianNB())
##GaussianNB_classifier.train(training_set)
##print("GaussianNB_classifier accuracy percent: ", (nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent: ", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)



# GaussianNB, BernoulliNB

##GaussianNB_classifier = SklearnClassifier(GaussianNB())
##GaussianNB_classifier.train(training_set)
##print("GaussianNB_classifier accuracy percent: ", (nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)
##
##BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
##BernoulliNB_classifier.train(training_set)
##print("BernoulliNB_classifier accuracy percent: ", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

##save_classifier = open("naivebayes.pickle","wb") #wb = write as bytes
##pickle.dump(classifier, save_classifier)
##save_classifier.close()
