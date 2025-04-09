import nltk
sentence = "InterExchange can't confirm your job offer until the following steps are complete."
tokens = nltk.word_tokenize(sentence)
print(tokens)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
for token in tokens:
    print(stemmer.stem(token))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for token in tokens:
    print(lemmatizer.lemmatize(token))