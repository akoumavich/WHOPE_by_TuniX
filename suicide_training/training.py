from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier


#splits the data into training data and testing data
def split_data(X:np.ndarray,Y: np.ndarray)->(np.ndarray,np.ndarray,np.ndarray,np.ndarray):
    """split the data into training data and testing data

    Args:
        X (ndarray): the vectorized tweets of the dataset that we're gonna split
        Y (ndarray): the target of the dataset that we're gonna split
    Returns:
        tuple:  tuple containing the training dataset and the testing dataset spltted into 80% of the dataset that we've split
    """    
    return  train_test_split(X, Y, test_size=0.2, random_state=0) #the training dataset is 80% of the dataset that we've split

#trains a model with training data
def trained_model(X_train: np.ndarray,y_train: np.ndarray, n_estimator, r_state):
    """trains a model with training data

    Args:
        X_train (np.ndarray): vector of training data
        y_train (np.ndarray): vcetor of target of the training dataset
        n_estimator (_type_): number of estimators
        r_state (_type_): random state

    Returns:
        RandomForestClassifier: the trained model
    """   
    classifier = RandomForestClassifier(n_estimators=n_estimator, random_state=r_state)
    #training the classifier
    classifier.fit(X_train, y_train) 
    return classifier

