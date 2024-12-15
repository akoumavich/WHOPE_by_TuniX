import pandas as pd


def get_tag_numbers (df:pd.DataFrame) -> pd.DataFrame:
    """this function takes a dataframe as an argument and returns the same dataframe with a new column 
    called 'count_at' that contains the number of tags in each line 

    Args:
        df (pd.DataFrame): dataframe of tweets 

    Returns:
        pd.DataFrame: dataframe with a new column that contains the number of tags in each line
    """

    df['count_at'] = df['text'].apply(lambda x: str(x).count('@'))
    return df

def get_keyWord_number (df:pd.DataFrame,key_word:str) -> int:
    """this function takes a dataframe and a key word as an argument and returns the total sum of 
    occurrences of the key word in all tweets  

    Args:
        df (pd.DataFrame): dataframe of tweets 
        key_word (str): the key word

    Returns:
        int: the sum 
    """
    s = df['text'].apply(lambda x: str(x).count(key_word  ))

    res=s.sum()
    return res

def get_tweet_length(df:pd.DataFrame)-> pd.DataFrame:
    """this function takes a dataframe as an argument and returns the same dataframe with a new column that
    represents the length of the tweet in each year

    Args:
        df (pd.DataFrame): dataframe of tweets 

    Returns:
        pd.DataFrame: dataframe with the len_tweet column 
    """
    df['len_tweet']=df['text'].apply(lambda x : len(x))
    return df 