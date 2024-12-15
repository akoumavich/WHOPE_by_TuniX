#this file is a test file for tweet_collection.py

import pandas as pd
import tweet_collection as tw
from colorama import Fore

#testing the function get_training_dataframe
def test_training_dataframe() -> pd.DataFrame():
    """test the function get_training_dataframe

    Returns:
        pd.DataFrame :  the tested dataframe
    """    
    try:    
        data=tw.get_training_dataframe()
        assert (type(data)==type(pd.DataFrame())) or (type(data)==type(pd.Series())) #test that the output is a dataframe or a series
        assert len(data.columns)==2  #test that it has 2 columns
        assert list(data.columns) == ['text','target'] #test that its columns are text and target
        assert data.shape[0] !=0 #test that it is not an empty dataset
        print(Fore.GREEN+'test training_dataframe is a success')
        return data
    except Exception as e:
        print(Fore.RED+'test training_dataframe failed') #failure message
        print(Fore.RED+ str(e))

#testing the function get_general_dataframe       
def test_general_dataframe()-> pd.DataFrame():
    """test get_general_dataframe

    Returns:
        pd.DataFrame: the tested dataframe
    """    
    data=tw.get_general_dataframe()
    try:
        assert (type(data)==type(pd.DataFrame())) or (type(data)==type(pd.Series())) #test that the output is a dataframe or a series
        assert len(data.columns)== 10  #test that it has 10 columns
        assert list(data.columns) == ['id','date','text','day','hour','nlikes','nreplies','nretweets','year','month'] #test that its columns are id, date, text, day, hours, nlikes, nreplies and nretweets
        assert data.shape[0] !=0 #test that it is not an empty dataset
        print(Fore.GREEN+'test general_dataframe is a success')
        return data
    except Exception as e:
        print(Fore.RED+'test general_dataframe failed') #failure message
        print(Fore.RED+ str(e))
        
#testing the function get_suicidal_dataframe
def test_get_suicidal_dataframe(df:pd.DataFrame())-> pd.DataFrame():
    """tests the function get_suicidal_dataframe

    Args:
        df (pd.DataFrame): dataframe to test

    Returns:
        pd.DataFrame():tested dataframe
    """       
    data=tw.get_suicidal_dataframe(df)
    try:
        assert (type(data)==type(pd.DataFrame())) or (type(data)==type(pd.Series()))  #test that the output is a dataframe or a series
        assert len(data.columns)>=2 #test that it has at least 2 columns (tratining dataset or general dataset)
        assert 'target' in data.columns #test that it has the column target
        test = True  #initialise test
        for i in data['target']:
            if i!=1:         #the non_suicidal
                test= False   #if there's a non_suicidal tweet in the dataset fail the test
        assert test
        print(Fore.GREEN+'get_suicidal_dataframe is a success')
        return data
    except:
        print(Fore.RED+'test get_suicidal_dataframe failed') #failure message
        
#testing the function get_non_suicidal_dataframe
def test_get_non_suicidal_dataframe(df: pd.DataFrame)-> pd.DataFrame():
    """tests the function get_non_suicidal_dataframe

    Args:
        df (pd.DataFrame): dataframe to test

    Returns:
        pd.DataFrame: dataframe tested
    """    
    data=tw.get_non_suicidal_dataframe(df)  
    try:
        assert (type(data)==type(pd.DataFrame())) or (type(data)==type(pd.Series()))  #test that the output is a dataframe or a series
        assert len(data.columns)>=2  #test that it has at least 2 columns (training dataset or general dataset)
        assert 'target' in data.columns #test that it has the column target
        test = True #initialise test
        for i in data['target']:
            if i!=0:          #the suicidal
                test= False   #if there's a non_suicidal tweet in the dataset fail the test
        assert test
        print(Fore.GREEN+'get_non_suicidal_dataframe is a success')
        return data
    except:
        print(Fore.RED+'test get_non_suicidal_dataframe failed')     #failure message
if __name__=='__main__':
    df=test_training_dataframe()
    test_general_dataframe()
    test_get_suicidal_dataframe(df)
    test_get_non_suicidal_dataframe(df)

    