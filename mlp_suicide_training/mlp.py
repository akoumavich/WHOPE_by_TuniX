from sklearn.neural_network import MLPClassifier
import os , sys
sys.path.append(os.getcwd())
import suicide_training.training as tr 
import suicide_training.import_dataset as imd
import suicide_training.vectorize as vect
import suicide_training.pre_processing as pp
from sklearn.metrics import accuracy_score


def MLP_trained_model(X_train,y_train, hidden_layer_sizes=(5,2)):
    """training the model with the given hidden layer sizes

    Args:
        X_train (np.ndarray):   the training data
        y_train ( np.ndarray):   the training labels
        hidden_layer_sizes (tuple, optional): hidden layer sizes.   Defaults to (5,2).

    Returns:
        MLPClassifier: the trained model
    """    

    classifier = MLPClassifier(hidden_layer_sizes,
                        max_iter = 500,activation = 'relu',
                        solver = 'adam',learning_rate_init=0.05)
    classifier.fit(X_train, y_train) 
    return classifier


def predict_data(X_train,X_test,y_train,hidden_layer_sizes):
    """predicts the given test data with the given hidden layer sizes

    Args:
        X_train (ndarray): vectorized training data
        X_test (ndarray): Vectorized testing data
        y_train (ndarray): corresponding training data  vector
        hidden_layer_sizes (tuple):  the hidden layer sizes

    Returns:
        ndarray: the predicted labels
    """    
    #make classifier
    classifier=MLP_trained_model(X_train,y_train,hidden_layer_sizes)
    y_pred=classifier.predict(X_test)

    return y_pred

def evaluate_model(X_train, X_test, y_train, y_test,hidden_layer_sizes):
    """
   predicts the given test data with the given hidden layer sizes and returns the accuracy score

    Args:
        X_train (ndarray): vectorized training data
        X_test (ndarray): Vectorized testing data
        y_train (ndarray): corresponding training data  vector
        hidden_layer_sizes (tuple):  the hidden layer sizes

    Returns:
        np.float64: the accuracy score
    """ 
      
    y_pred=predict_data(X_train,X_test,y_train,hidden_layer_sizes)
    return accuracy_score(y_test, y_pred)

if __name__ == '__main__':
    #import data 
    tweets,y=imd.import_dataset()
    #preprocess the data
    tweets=pp.text_preprocess(tweets)
    #vectorize
    tweets=vect.vectorize_data(tweets,'train')
    #split data into training and test data
    X_train,X_test,y_train,y_test=tr.split_data(tweets,y)

print('Accuracy: {:.2f}'.format(evaluate_model(X_train, X_test, y_train, y_test,(1024,16,4))))