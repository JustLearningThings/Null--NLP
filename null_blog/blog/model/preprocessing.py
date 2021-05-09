from sklearn.base import BaseEstimator, TransformerMixin

import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, sent_tokenize

import re

class TextTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, stopwords, stemmer):
        super().__init__()
        self.stopwords = stopwords
        self.stemmer = stemmer
        self.hapaxes = []
        self.named_entities = []

    # by default a transformer's fit method just returns self
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # for every text in the X list transform its data
        for i, sample in enumerate(X):
            X[i] = self.__normalize(sample)
            X[i] = self.__eliminate_stopwords(X[i])
            X[i] = self.__get_hapaxes(X[i])
            X[i] = self.__stem(X[i])
            self.__named_entity_extraction(X[i])

        # return the transformed text list
        return X

    def __normalize(self, text):
        # select only the words, make them lowercase and eliminate \r and \n
        return ' '.join(re.findall('[a-zA-Z]+', text.lower().replace(r'\r', ' ').replace(r'\n', ' ')))

    def __eliminate_stopwords(self, text):
        if self.stopwords is not None:
            return ''.join([word for word in text if word not in self.stopwords])

    def __get_hapaxes(self, text, eliminate=True):
        # getting the hapaxes
        fd = FreqDist(word_tokenize(text))
        self.hapaxes.append(fd.hapaxes())

        # eliminating the hapaxes if needed (by default: needed)
        if eliminate:
            text = ''.join([word for word in text if word not in self.hapaxes])

        return text

    def __stem(self, text):
        return ' '.join([self.stemmer.stem(word) for word in word_tokenize(text)])

    def __named_entity_extraction(self, text):
        # tokenize text's sentences
        for sent in sent_tokenize(text):
            # get the part-of-speech tags of every token of the current sentence
            for chunk in nltk.ne_chunk(nltk.pos_tag(word_tokenize(sent))):
                # store named entities
                if hasattr(chunk, 'label'):
                    self.named_entities.append(chunk)
