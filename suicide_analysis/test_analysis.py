import os
import sys

from temporal_analysis import *
from tweet_text_analysis import *
from vocabulary_analysis import *

sys.path.append(os.getcwd())
import pandas as pd
from colorama import Fore

from tweet_collection.tweet_collection import *


#test get_tag_numbers function
def test_get_tag_numbers(df:pd.DataFrame)-> None:
    """ test get_tag_numbers function 

    Args:
        df (pd.DataFrame): df to be tested
    """    
    try:

        #dataframe to test
        tup=df.shape
        df_test=get_tag_numbers(df)

        #asserting function output type, number of columns and type of data
        assert type(df_test)==type(pd.DataFrame())
        assert df_test.shape[1]==tup[1]+1
        assert df_test.count_at.dtype==int or df_test.count_at.dtype=="int64"
        print(Fore.GREEN+"get_tag_numbers is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_tag_numbers test failed")
        print(Fore.RED+ str(e))

#test get_tweet_length function
def test_get_tweet_length(df:pd.DataFrame)-> None:
    """test get_tweet_length function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    try:

        #dataframe to test
        tup=df.shape
        df_test=get_tweet_length(df)
    

        #asserting function output type, number of columns and type of data
        assert type(df_test)==type(pd.DataFrame())
        assert df_test.shape[1]== tup[1]+1
        assert df_test.len_tweet.dtype==int or df_test.len_tweet.dtype=="int64"
        print(Fore.GREEN+"get_tweet_length is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_tweet_length test failed")
        print(Fore.RED+ str(e))

#test get_polarity_dataframe function
def test_get_polarity_dataframe(df:pd.DataFrame)-> None:
    """test get_polarity_dataframe function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    try:

        #dataframe to test
        tup=df.shape
        df_test=get_polarity_dataframe(df)

        #asserting function output type, number of columns
        assert type(df_test)==type(pd.DataFrame())
        assert df_test.shape[1]== tup[1]+1
        print(Fore.GREEN+"get_polarity_dataframe is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_polarity_dataframe test failed")
        print(Fore.RED+ str(e))

#test get_abreged_text function
def test_get_abreged_text(df:pd.DataFrame)-> None:
    """test get_abreged_text function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    try:

        #dataframe to test
        tup=df.shape
        df_test=get_abreged_text(df)
    
        #asserting function output type, number of columns and type of data
        assert type(df_test)==type(pd.DataFrame())
        assert df_test.shape[1]== tup[1]+1
        assert df_test.abreged_text.dtype==int or df_test.abreged_text.dtype=="int64"
        print(Fore.GREEN+"get_abreged_text is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_abreged_text test failed")
        print(Fore.RED+ str(e))

#test get_tweet_per_hour function
def test_get_tweet_per_hour(df:pd.DataFrame)-> None:
    """test get_tweet_per_hour function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    try:

    #dataframe to test
        df_test=get_tweet_per_hour(df)

        #asserting function output type, number of columns
        assert type(df_test)==type(pd.Series(dtype='int64'))
        assert len(df_test.shape)== 1
        assert (df_test.shape[0])== 24
        print(Fore.GREEN+"get_tweet_per_hour is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_tweet_per_hour test failed")
        print(Fore.RED+ str(e))

#test get_tweet_per_month function
def test_get_tweet_per_month(df:pd.DataFrame)-> None:
    """test get_tweet_per_month function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    try:

    #dataframe to test
        tup=df.shape
        df_test=get_tweet_per_month(df)

        #asserting function output type, number of columns
        assert type(df_test)==type(pd.Series(dtype='int64'))
        assert len(df_test.shape)== 1
        print(Fore.GREEN+"get_tweet_per_month is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_tweet_per_month test failed")
        print(Fore.RED+ str(e))

#test get_tweet_per_year function
def test_get_tweet_per_year(df:pd.DataFrame)-> None:
    """test get_tweet_per_year function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    
    try:

    #dataframe to test
        df_test=get_tweet_per_year(df)

        #asserting function output type, number of columns
        assert type(df_test)==type(pd.Series(dtype='int64'))
        assert len(df_test.shape)== 1
        print(Fore.GREEN+"get_tweet_per_year is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_tweet_per_year test failed")
        print(Fore.RED+ str(e))

#test get_tweet_per_day function
def test_get_tweet_per_day(df:pd.DataFrame)-> None:
    """test get_tweet_per_day function

    Args:
        df (pd.DataFrame): dataframe to be tested
    """    
    try:

    #dataframe to test
        tup=df.shape
        df_test=get_tweet_per_day(df)

        #asserting function output type, number of columns
        assert type(df_test)==type(pd.Series(dtype='int64'))
        assert len(df_test.shape)== 1
        print(Fore.GREEN+"get_tweet_per_day is tested successfully")

    except Exception as e:

        print(Fore.RED+"get_tweet_per_day test failed")
        print(Fore.RED+ str(e))

#test extract_features function
def test_extract_features(df,length,number_of_features)->None :
    """test extract_features function

    Args:
        df (_type_): dataframe to be tested
        length (_type_): the length of the extracted features
        number_of_features (_type_): the number of features
    """    
    try:

        #dataframe to test
        dict_features=extract_features(df,len_exp=length,nb_exp=number_of_features)


        #asserting function output type, number of columns
        assert type(dict_features)==(dict)
        assert len(list(dict_features.keys()))==number_of_features
        assert len(list(dict_features.keys())[0].split(" "))==length
        print(Fore.GREEN+"test_extract_features is tested successfully")

    except Exception as e:

        print(Fore.RED+"test_extract_features test failed")
        print(Fore.RED+str(e))

if __name__=="__main__" :

    df=get_training_dataframe()
    df1=get_suicidal_dataframe(df)
    test_get_abreged_text(df)
    test_get_polarity_dataframe(df)
    test_get_tag_numbers(df)
    test_get_tweet_length(df)

    df=get_general_dataframe()
    test_get_tweet_per_hour(df)
    test_get_tweet_per_month(df)
    test_get_tweet_per_day(df)
    test_get_tweet_per_hour(df)

    test_extract_features(df.iloc[0:100],length=3,number_of_features=10)