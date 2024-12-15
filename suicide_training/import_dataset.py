import numpy as np
import sys
import os
sys.path.append(os.getcwd())
import tweet_collection.tweet_collection as tw


def import_dataset() -> (list, np.ndarray):
    """import the dataset to be used for training the model

    Returns:
         tuple (list, np.ndarray): the training set and the target
    """    
    #import the training set
    dataset=tw.get_training_dataframe()
    #split the data from the target
    x, y =list(dataset["text"]), np.array(dataset["target"])
    return (x,y)
