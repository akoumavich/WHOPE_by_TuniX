import pandas as pd
from nltk.corpus import stopwords



def get_tweet_per_day(df:pd.DataFrame) -> pd.DataFrame:
    """this function takes a dataframe as an argument and returns a new dataframe that contains the number of tweets per day

    Args:
        df (pd.DataFrame): dataframe of tweets

    Returns:
        pd.DataFrame: dataframe that contains the number of tweets in each day 
    """
    df2 = df.groupby(["day"])["day"].count()
    return df2


def get_tweet_per_month (df:pd.DataFrame) -> pd.DataFrame:
    """this function takes a dataframe as an argument and returs a new dataframe that contains the number of tweets in each month 

    Args:
        df (pd.DataFrame): dataframe of tweets 

    Returns:
        pd.DataFrame: dataframe that contains the number of tweets in each month 
    """
    df2 = df.groupby(["month"])["month"].count()
    return df2 



def get_tweet_per_year (df:pd.DataFrame) -> pd.DataFrame:
    """this function takes a dataframe as an argument and returns a dataframe that contains the number of tweets in each year

    Args:
        df (pd.DataFrame): dataframe of tweets

    Returns:
        pd.DataFrame: dataframe that contains the number of tweets in each year 
    """
    df2 = df.groupby(["year"])["year"].count()
    return df2     


def get_tweet_per_hour (df:pd.DataFrame) -> pd.DataFrame:
    """ this function takes a dataframe as an argument and returns a dataframe that contains the number of tweets in each hour


    Args:
        df (pd.DataFrame): dataframe of tweets 

    Returns:
        pd.DataFrame: dataframe that contains the number of tweets in each hour  
    """
    df2 = df.groupby(["hour"])["hour"].count()
    return df2  





