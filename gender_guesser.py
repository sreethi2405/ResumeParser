# EDA packages
import pandas as pd
import numpy as np
# ===ML Packages===
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
#from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def genderguesser(name):
    #print(name)
    # Load our data
    df = pd.read_csv('names_dataset.csv') # to compare with names dataset with possible male and female names and to predict gender
    df_names = df
    df_names.sex.replace({'F': 0, 'M': 1}, inplace=True)
    Xfeatures =df_names['name']
    # Feature Extraction

    cv = CountVectorizer() # instantiate
    X = cv.fit_transform(Xfeatures)
    cv.get_feature_names()
    y = df_names.sex
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = MultinomialNB() # Naive Bayes classifier for multinomial models suitable for classification with discrete features
    clf.fit(X_train, y_train) #	Fit Naive Bayes classifier according to X, y
    clf.score(X_test, y_test) #Returns the mean accuracy on the given test data and labels.
    sample_name = [name]
    vect = cv.transform(sample_name).toarray()
    return clf.predict(vect)  #Perform classification on an array of test vectors X.