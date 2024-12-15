import pandas as pd
from textblob import TextBlob 
from tqdm import tqdm
import nltk 
from nltk.corpus import stopwords
from collections import Counter


def get_abreged_text(df:pd.DataFrame) -> pd.DataFrame:
    """this function takes a dataframe as an arguent and returns the same dataframe with a new column that represents the number of 
    abridged words in every tweet

    Args:
        df (pd.DataFrame): dataframe of tweets 

    Returns:
        pd.DataFrame: dataframe with a new column 
    """

    #list that contains abridged words 
    l=['lol', 'ah', 'haha', 'xD', 'XOXOXO', 'TBH', 'tbh', 'ROFL', 'omg', 'OMFG', 'OMG', 'lmfao', 'LMFAO']

    #new column initialisation 
    new_column=[]

    #calculate the number of abridged words un each line 
    df1=df["text"]
    for i in tqdm(range(len(df))):
        tweet= df1.iloc[i][0]

        #number of abridged words in each tweet initialisation 
        slang_nbr=0
        for word in l:  
            if ((word).lower() in str(tweet).lower()) : 
                slang_nbr+=1
        new_column+=[slang_nbr]

    #adding the new column
    df['abreged_text']=new_column 

    return df 

def get_polarity_dataframe(df:pd.DataFrame)->pd.DataFrame:
    """this function takes a dataframe as an argument and returns the same dataframe with a new column added 
    that contains the polarity of each tweet

    Args:
        df (pd.DataFrame): dataframe of tweets 

    Returns:
        pd.DataFrame: dataframe with the new column 
    """
    df['polarity_tweet']=df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df



def extract_features(df : pd.DataFrame, nb_exp:int =1, len_exp:int=1)->dict:
    """this function takes a dataframe, the number and the length of the wanted expressions (nb_exp, len_exp) as an argument
    and returns a dict that contains the first nb_exp most frequently used expressions with a length equal to len_exp each

    Args:
        df (pd.DataFrame): dataframe of tweets 
        nb_exp (int, optional): number of expressions. Defaults to 1.
        len_exp (int, optional): length of each expression . Defaults to 1.

    Returns:
        dict: contains first the nb_exp most frequently used as keys and the number of occurrences of each one as values 
    """
    #import the column that contains the tweets  
    column_text=df['text']
    
    
    #downloading the stopwords
    nltk.download('stopwords')
    list_stop_words = set(stopwords.words('english'))
    
    
    #deleting stopwords in each tweet  
    str_col_text=' '.join(column_text)
    str_col_text_textblob=TextBlob(str_col_text)
    tweet_textblob_no_stop_words=TextBlob('')

    for word in tqdm(str_col_text_textblob.words):
        if word not in list_stop_words:
            
            tweet_textblob_no_stop_words= tweet_textblob_no_stop_words+ ' '+ word
    
    
    #extract the expressions of length len_exp
    kgram=tweet_textblob_no_stop_words.ngrams(n=len_exp)
    

    #number of occurrences of the expressions 
    kgram_tuples = [tuple(tri) for tri in kgram]
    compteur= Counter(kgram_tuples)
    
    #extract the first nb_exp most frequently used expressions (list containing tuples)
    most_used_exp= compteur.most_common(nb_exp)
    
    #extract the first nb_exp most frequently used expressions (list containing strings)
    dict_most_used_exp={}
    for i in tqdm(range(nb_exp)):
        tuple_exp=most_used_exp[i][0]
        #transform the tuple to an expression with a string type
        exp=''
        for j in tqdm(range(len_exp)):
            exp = exp + ' '+ tuple_exp[j]
        dict_most_used_exp [exp.strip()]=most_used_exp[i][1]
        
    return dict_most_used_exp