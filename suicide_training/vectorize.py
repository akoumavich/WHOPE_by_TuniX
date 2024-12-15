from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import os , sys
sys.path.append(os.getcwd())
import numpy as np
import suicide_training.import_dataset as imd
import suicide_training.pre_processing as pp

def vectorize_data(tweets:list,goal:str,n_features=1500) -> np.ndarray:
    """use a TFIDF vectorizer to vectorize the tweets

    Args:
        tweets (list): the preprocessed tweets to vectorize
        goal (str): training or predicting
        n_features (int, optional): the number of features. Defaults to 1500.

    Returns:
        np.ndarray: _description_
    """    
    tfidfconverter = TfidfVectorizer(max_features=n_features, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    #vectorize the tweets
    if goal=='train':
        X = tfidfconverter.fit_transform(tweets).toarray()
    if goal=='predict':
        training_tweets,y=imd.import_dataset()
        #preprocess the data
        training_tweets=pp.text_preprocess(training_tweets)
        #vectorize
        X=tfidfconverter.fit_transform(training_tweets).toarray()
        X = tfidfconverter.transform(tweets)
    return X