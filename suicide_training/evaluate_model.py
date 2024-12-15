import os , sys
sys.path.append(os.getcwd())
import numpy as np
from sklearn.metrics import accuracy_score


def predict_data(X_test: np.ndarray,model) -> np.ndarray :
    """predicts data from a trained model

    Args:
        X_test (np.ndarray): vectorized testing dataset
        model : trained model

    Returns:
        np.ndarray: the vectorized predictions of the testing dataset
    """  

    y_pred= y_pred=model.predict(X_test)  #prediction of the testing dataset
    
    return y_pred 

def evaluate_model(y_test,y_pred)->np.float64:
    """evaluate the model

    Args:
        y_test (np.ndarray): the vectorized testing dataset
        y_pred (np.ndarray): the vectorized predictions of the testing dataset

    Returns:
        np.float64: the accuracy of the model
    """    
    return accuracy_score(y_test, y_pred)


