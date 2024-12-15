import sys
import os
sys.path.append(os.getcwd())
import suicide_training.pre_processing as pp
import suicide_training.vectorize as vect
import pandas as pd
import pickle


# loading the model
with open('suicide_classifier', 'rb') as training_model:
    model = pickle.load(training_model)
    
#predict the targets of a dataset    
def predicted_dataframe(data: pd.DataFrame | pd.Series) -> pd.Series | pd.DataFrame:
    """predict the targets of a dataset

    Args:
        data (pd.DataFrame | pd.Series): dataset that we're gonna do the prediction on

    Returns:
        pd.Series | pd.DataFrame: the dataset with a predicted target column and a predicted probability column
    """    

    X=list(data['text'])
    #preprocess the tweets
    X=pp.text_preprocess(X)
    #vectorize the tweets
    X=vect.vectorize_data(X,'predict')
    #predict the targets using the loaded model
    y_pred=model.predict(X)
    #prediction probabilities
    probabilities = model.predict_proba(X)
    #put the result in a column
    target_column=pd.Series(y_pred)
    target_probability_column=pd.Series(probabilities[:,1])

    
    #put the column in the dataset
    data['target']=target_column 
    data['probability']=target_probability_column
    if data.columns[0] not in ['id','date','text','day','hour','nlikes','nreplies','nretweets','year','month','target','probability']:
        data=data.iloc[:,1:]
    return data

#saving the predicted dataset in csv format
def save_predicted_dataframe(predicted_data : pd.DataFrame | pd.Series):
    """saving the predicted dataset in csv format

    Args:
        predicted_data (pd.DataFrame | pd.Series): the predicted dataset
    """    
   
    predicted_data.to_csv('datasets/predicted_dataset.csv')
