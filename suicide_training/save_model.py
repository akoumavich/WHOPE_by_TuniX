import pickle
import training as tr 
import import_dataset as imd
import pre_processing as pp
import vectorize as vect


#import data 
tweets,y=imd.import_dataset()

#preprocess the data
tweets=pp.text_preprocess(tweets)

#vectorize
tweets=vect.vectorize_data(tweets,'train',n_features=1500)

#split data into traingin and test data
X_train,X_test,y_train,y_test=tr.split_data(tweets,y)

#get the classifier that will do the job
def optimum_classifier(X_train,y_train,n_estimator=1500 , r_state=0):
    """gets the classifier that will do the job

    Args:
        X_train (ndarray): the vectorized training data
        y_train (ndarray): the target dataset
        n_estimator (int, optional): the number of estimators. Defaults to 1500.
        r_state (int, optional): the random state. Defaults to 0.

    Returns:
        RandomForestClassifier: a trained random forest classifier
    """    
    return tr.trained_model(X_train,y_train, n_estimator, r_state)

#save the classifier as a model
def save_as_model(classifier):
    """save the classifier as a model

    Args:
        classifier (RandomForestClassifier): the classifier to save
    """
    with open('suicide_classifier', 'wb') as picklefile:
        pickle.dump(classifier,picklefile)


if (__name__=='__main__'):
    save_as_model(optimum_classifier(X_train,y_train,n_estimator=1500))