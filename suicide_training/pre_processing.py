from nltk.stem import WordNetLemmatizer
import re 

#Pre-Process the data + Lemmatization 
def text_preprocess(X:list)->list:
    """preprocess the data + Lemmatization

    Args:
        X (list):  list of tweets to preprocess

    Returns:
        list: list of preprocessed tweets
    """    
    #initialize the lemmatizer
    stemmer = WordNetLemmatizer()

    tweets = []

    for i in range(0, len(X)):
        tweet =str(X[i])
        # Converting to Lowercase
        tweet = tweet.lower()
        
        # Lemmatization
        tweet = tweet.split()

        tweet = [stemmer.lemmatize(word) for word in tweet]
        #creating the new list of clean tweets
        tweet = ' '.join(tweet)
        # Remove all the special characters
        tweet = re.sub(r'[^a-zA-Z\d\s:]', ' ', tweet)
        
        # remove all single characters
        tweet =  re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', tweet)
        
        # Substituting multiple spaces with single space
        tweet = re.sub(r'\s+', ' ', tweet, flags=re.I)
        
        # Removing prefixed 'b'
        tweet = re.sub(r'^b\s+', '', tweet)
        
        tweets.append(tweet)
    return tweets
