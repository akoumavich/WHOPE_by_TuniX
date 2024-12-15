import numpy as np
import import_dataset as imd
import pre_processing as pp
import vectorize as vect 
import training as tr
import evaluate_model as eval
import re 
import pickle
from colorama import Fore


#testing the function import_dataset
def test_import_dataset() -> (list, np.ndarray):
    """test import_dataset
    Returns:
        tuple:  tuple containing a list and a ndarray
    """    
    try:
        #executing import_dataset
        x, y= imd.import_dataset()
        #assert that it returns a tuple containing a list and a ndarray
        assert type(x)==list
        assert type(y)==np.ndarray
        #assert that the targets are 0 or 1
        assert y.any() in [0,1]
        #inform if it succeeds
        print(Fore.GREEN+'test import_dataset is a success')
        return (x, y)
    except Exception as e:
        #inform if it fails and print the error
        print(Fore.RED+'test import_dataset failed')
        print(Fore.RED+ str(e))

#testing the preprcoessing       
def test_text_preprocess(X:list)->list:
    """test preprocessing

    Args:
        X (list): the list to preprocess

    Returns:
        list: preprocessed tweets   
    """    
    try:
        #executing the preprocessing function
        processed_X=pp.text_preprocess(X)
        #assert that it returns a list
        assert type(processed_X) == list

        for i in range(0, len(processed_X)):
            tweet =str(processed_X[i])
            
             # assert all the special characters are removed
            assert not((re.compile(r'[^a-zA-Z\d\s:]')).search(tweet))
           
            # assert all single characters are removed
            assert not((re.compile(r'\s+[a-zA-Z]\s+')).search(tweet))
            
            #  assert the substitution of multiple spaces with single space
            assert not((re.compile(r'\s{2,}')).search(tweet))

            # Removing prefixed 'b'
            assert not((re.compile(r'^b\s+').search(tweet)))
            
            # testing the conversion to Lowercase
            assert tweet== tweet.lower()
        
        #inform if it succeeds
        print(Fore.GREEN+'preprocessing test is a success')
        return processed_X
    except Exception as e:
        #inform if it fails and print the error
        print(Fore.RED+ str(e))
        print(Fore.RED+'preprocessing test failed')


#verify the vectorization process

def vectoring_test(tweets: list, n_features: int) -> np.ndarray:
    """verify the vectorization process

    Args:
        tweets (list): list of tweets to be vectorized
        n_features (int): the number of features

    Returns:
        np.ndarray: the vectorization
    """    
    try:
        #execute the vectorization function
        vectorized_tweets = vect.vectorize_data(tweets,'train',n_features=n_features)

        #check the type of the vector
        assert type(vectorized_tweets)==np.ndarray
        
        #checkt the dimesnions
        assert vectorized_tweets.shape[0] ==len(tweets)
        assert vectorized_tweets.shape[1] <=n_features
        #inform if it succeeds
        print(Fore.GREEN+"vectorization succeded")
        return vectorized_tweets
    except Exception as e :
        #inform if it fails and print the error
        print(Fore.RED+"vectorization failed")
        print(Fore.RED+ str(e))
          

#testing split_data
def test_split_data(X: np.ndarray,y:np.ndarray):
    """test split_data function

    Args:
        X (np.ndarray): the vectorized dataset
        y (np.ndarray): the vectorized dataset target

    Returns:
        tuple:  a tuple of the training dataset and the testing dataset
    """    
    try:
        #execute the function tha we're testing
        X_train, X_test, y_train, y_test = tr.split_data(X,y)
        #assert that it returns a tuple of 4 ndarray
        assert type(X_train)==np.ndarray
        assert type(X_test)==np.ndarray
        assert type(y_train)==np.ndarray
        assert type(y_test)==np.ndarray
        #assert that the training dataset represent 80% of the dataset that we used and the rest is a testing dataset
        assert X_train.shape[0]==int(0.8*X.shape[0])
        assert y_train.shape[0]==int(0.8*y.shape[0])
        assert X_train.shape[0]+X_test.shape[0]==X.shape[0]
        assert y_train.shape[0]+y_test.shape[0]==y.shape[0]
        #inform if it succeeds
        print(Fore.GREEN+'test split_data is a success')
        return (X_train, X_test, y_train, y_test)
    except Exception as e:
        #inform if it fails and print the error
        print(Fore.RED+'test split_data failed')
        print(Fore.RED+ str(e))

#testing the function predict_data
def test_predict_data(X_test, model):
    """test predict_data

    Args:
        X_test (ndarray): the test data
        model (RandomForestClassifier): the classifier

    Returns:
        ndarray:  the predicted targets
    """    
    try: 
        #execute the function that we're testing
        y_pred =eval.predict_data(X_test,model)
        #assert that it returns a ndarray
        assert type(y_pred)==np.ndarray
        #assert that the predicted targets are 0 or 1
        assert y_pred.any() in [0,1]
        #inform if it succeds
        print(Fore.GREEN+'test predict_data is a success')
        return y_pred
    except Exception as e:
        #inform if it fails
        print(Fore.RED+'test predict_data failed')
        print(Fore.RED+ str(e))
        
def test_evaluate_model(y_test,y_pred):
    """evaluate the model

    Args:
        y_test (ndarray): the vector y_test
        y_pred (ndarray): the predicted targets' vector 


    Returns:
        np.float64:  the accuracy score
    """    
    try:
        #execute the function that we're testing
        accuracy=eval.evaluate_model(y_test,y_pred)
        #assert the type of accuracy
        assert type(accuracy)==np.float64
        #assert that the accuracy is between 0 and 1
        assert 0<=accuracy and accuracy<=1
        print(Fore.GREEN+f'The accuracy score for the model is {accuracy}')
        #success message
        print(Fore.GREEN+'test evaluate_model is a success')
        return accuracy
    except Exception as e:
        #failure message
        print(Fore.RED+'test evaluate_model failed')
        print(Fore.RED+ str(e))
if __name__=='__main__':
    X, y=test_import_dataset()
    X = test_text_preprocess(X)
    X = vectoring_test(X, n_features=1500)
    X_train, X_test, y_train, y_test=test_split_data(X,y)
    with open('suicide_classifier', 'rb') as training_model:
        model = pickle.load(training_model)
    y_pred=test_predict_data(X_test, model)
    accuracy = test_evaluate_model(y_test,y_pred)