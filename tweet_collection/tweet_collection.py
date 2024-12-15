import pandas as pd
import numpy as np


#this function imports the dataset from csv file to be predicted
def get_dataframe_to_predict() -> pd.DataFrame:
    """this function imports the dataset from csv file to be predicted

    Returns:
        pd.DataFrame: dataset to be predicted
    """
    path="datasets/general_dataset.csv" 
    #reading the training dataset (suicidal data) 
    try :
        print("importing dataset ")
        df=pd.read_csv(path)
        print("dataset is successfully imported!")

    except Exception as e:
        print("reading train dataset Failed!")
        print(e)
        
    return df #retourne la dataframe d'entrainement

#this function imports the dataset from csv file for the training
def get_training_dataframe() -> pd.DataFrame:
    """this function imports the dataset from csv file for the training

    Returns:
        pd.DataFrame: train dataset 
    """
    path="datasets/twitter-suicidal_data.csv" 
    #reading the training dataset (suicidal data) 
    try :
        print("importing train dataset ")
        df=pd.read_csv(path)
        print("train dataset is successfully imported!")

    except Exception as e:
        print("reading train dataset Failed!")
        print(e)
        
    #reading the dataset 

    df.columns=['text', 'target']# naming columns
    df.dropna(inplace=True)
    return df #retourne la dataframe d'entrainement


#this function imports the dataset from csv file for the training
GENERAL_SOURCE_D = "datasets/dep_tweets.csv"
GENERAL_SOURCE_nonD = "datasets/non_dep_tweets.csv"

def get_general_dataframe ()->pd.DataFrame:
    """this function imports the dataset from csv file for the training
    
    Returns:
        pd.DataFrame:  dataset to be predicted
        """
    #reading the depressed dataset
    try :
        df=pd.read_csv(GENERAL_SOURCE_D)
    except Exception as e:
        print("reading depressed dataset Failed!")
    #reading the non-depressed dataset
    try :
        df_nonD=pd.read_csv(GENERAL_SOURCE_nonD)
        print("reading dataset completed Successfully!")
    except:
        print("reading non-depressed dataset Failed!")

    #merging the 2 datasets
    frames = [df, df_nonD]
    df = pd.concat(frames)
    #Cleaning the dataset
    # df.dropna(inplace=True)
    df=df.iloc[:,[0,3,6,14,15,22,23,24]]
    df.columns=['id','date','text','day','hour','nlikes','nreplies','nretweets']
    #Adding year column
    years=df["date"].str[0:4]
    df["year"]=years
    #Adding month column
    months=df["date"].str[5:7]
    df["month"]=months
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    df = df.dropna()
    #saving the dataframe in a csv file
    df.to_csv('datasets/general_dataset.csv')
    
    return df 

#this function extracts the suicidal tweets from the dataframe
def get_suicidal_dataframe(df: pd.DataFrame) ->pd.Series:
    """this function extracts the suicidal tweets from the dataframe

    Args:
        df (pd.DataFrame): dataframe to extract

    Returns:
        pd.Series: extracted suicidal tweets dataframe
    """    
    return df.loc[(df["target"])==1]

#this function extracts the non suicidal tweets from the dataframe
def get_non_suicidal_dataframe(df: pd.DataFrame)->pd.Series :
    """this function extracts the non suicidal tweets from the dataframe

    Args:
        df (pd.DataFrame): dataframe to extract

    Returns:
        pd.Series: extracted non suicidal tweets dataframe
    """    
    return df.loc[(df["target"])==0]

#returns a dataframe containing the predicted dataset
def get_predicted_dataframe() ->pd.DataFrame:
    """returns a dataframe containing the predicted dataset

    Returns:
        pd.DataFrame: predicted dataframe
    """     
    path="datasets/predicted_dataset.csv"

    #reading the dataframe
    try:
        df=pd.read_csv(path)
        print("reading predicted dataset completed Successfully!")
    except Exception as e:
        print("reading predicted dataset Failed!")
        print(e)
    
    # #cleaning the dataframe
    # df=df.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
    # df.columns=['id','date','text','day','hour','nlikes','nreplies','nretweets','year','month','target','probability']  
    return df #retourne la dataframe prédite
