import sys
import os
sys.path.append(os.getcwd())
import seaborn as sns
import matplotlib.pyplot as plt 
from suicide_analysis.temporal_analysis import *
from suicide_analysis.tweet_text_analysis import *
from suicide_analysis.vocabulary_analysis import *
from tweet_collection.tweet_collection import *
import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from tweet_collection.tweet_collection import *
import numpy as np

def show_perc_suicidal_non_suicidal(df: pd.DataFrame) :
    """give the percentage of suicidal and non suicidal persons

    Args:
        df (pd.DataFrame): dataframe of tweets 
    """
    #get the suicidal dataframe 
    df_suicidal=get_suicidal_dataframe(df)
    
    #get the suicidal dataframe
    df_non_suicidal=get_non_suicidal_dataframe(df)
    
    #get the length of suicidal tweets and non suicidal tweets
    nb_tweet_suicidal= df_suicidal.shape[0]
    nb_tweet_non_suicidal=df_non_suicidal.shape[0]
    
    #define the values and labels that would be used to create the pie chart
    values=[nb_tweet_non_suicidal,nb_tweet_suicidal]
    labels=['percentage of non suicidal tweets','percentage of suicidal tweets']
    
    # creating the pie chart
        #choosing the colors palette
    colors=sns.color_palette('pastel')
        #choosing the colors to use
    labels_colors=sns.color_palette(['black','black'])
        #choosing the text font
    sns.set(font='Georgia')
        #plotting the pie
    plt.pie(values, colors = colors,explode= [0,0.02] ,autopct='%.0f%%')
        #setting the title 
    plt.title('percentage of suicidal and non suicidal tweets',fontsize=18, color='blue', ha='center')
        #setting the legend
    plt.legend(labels, loc="upper right", prop={'size': 8}, edgecolor='blue', labels=labels, labelcolor=labels_colors)


def show_tag_repartition():
    """compare the number of tags between suicidal and non suicidal tweets.
    
    """

    df=get_predicted_dataframe()
    #get the suicidal and non suicidal dataframes
    df1=get_suicidal_dataframe(df)
    df2=get_non_suicidal_dataframe(df)

    #get the number of tags in the suicidal and non suicidal dataframes 
    suicidal_data= get_tag_numbers(df1)
    non_suicidal_data=get_tag_numbers(df2)

    #create the plot and show it
    frames = [suicidal_data, non_suicidal_data]
    df3 = pd.concat(frames)
    sns.barplot(data=df3,x='target', y='count_at', color='blue')
    plt.xlabel('Type of tweets')
    plt.ylabel('Number of tags')
    plt.title('Comparison of the number of tags between suicidal and non suicidal tweets')
    plt.show()



SUICIDAL=1
NONSUICIDAL=0
def show_wordcloud (df:pd.DataFrame,mask_path:str,cat:int=None)-> None:
    """plots a wordcloud of the most recurrent words in tweets of a certain category

    Args:
        df (pd.Dataframe): dataframe of tweets
        mask_path (str): the path of the mask. to get the path use image.HAPPY for the happy mask for example
        cat (int, optional):    categeory of the dataframe to show. Defaults to None.

    """   


    #using the appropriate dataframe
    if cat!=None:
        df1=df.copy()
        if cat==SUICIDAL:
            df1=get_suicidal_dataframe(df)
        elif cat==NONSUICIDAL:
            df1=get_non_suicidal_dataframe(df)
    else: 
        df1=df
    
    #exctracting vocabulary of the data frame
    dict_features=extract_features(df1,100,len_exp=3)
    list_of_features =dict_features.keys()

    #joining all the vocab into a single string
    text_to_wordcloud =" ".join((list_of_features))

    #impoting the mask 
    mask = np.array(Image.open(mask_path))

    #editing mask arrays
    n,p,k=mask.shape
    for i in range(n):
        for j in range(p):
            for t in range(k):
                if mask [i,j,t]==0:
                    mask[i,j,t]=255



    #creating the wordcloud
    word_cloud = WordCloud(
               mask = mask, background_color = "white"  
                ).generate(text_to_wordcloud)
    plt.imshow(word_cloud, interpolation="None")

    plt.axis("off")


def show_tweet_per_day(df:pd.DataFrame()):
    """show tweets' number in every day 

    Args:
        df (pd.DataFrame): Dataframe of tweets
    """
    sns.set_theme(style="whitegrid")
    plt.title('number of tweets in every day  ',fontsize=18, color='blue', ha='center')
    sns.histplot(data=df,x="day",discrete=True)



def show_tweet_per_month (df):
    """show tweets' number in each month

    Args:
        df (_type_): Dataframe of tweets 
    """
    sns.set_theme(style="whitegrid")
    plt.title('number of tweets in each month ',fontsize=18, color='blue', ha='center')
    sns.histplot(data=df,x="month",discrete=True)


def show_tweet_per_year (df:pd.DataFrame()):
    """show tweets'number in each year

    Args:
        df (pd.DataFrame): Dataframe of tweets
    """
    sns.set_theme(style="whitegrid")
    plt.title('number of tweets in each year  ',fontsize=18, color='blue', ha='center')
    sns.histplot(data=df,x="year",discrete=True)


def show_tweet_per_hour (df:pd.DataFrame()):
    """show tweets' number in every hour 

    Args:
        df (pd.DataFrame): Dataframe of tweets 
    """
    sns.set_theme(style="whitegrid")
    plt.title('number of tweets in every hour',fontsize=18, color='blue', ha='center')
    sns.histplot(data=df,x="hour",discrete=True) 



def show_boxplot_length (df: pd.DataFrame):
    """compare the length of suicidal tweets with non suicidal tweets

    Args:
        df (pd.DataFrame): dataframe of tweets
    """
    df_with_len_tweets=get_tweet_length(df)
    df_with_len_tweets_suicidal = get_suicidal_dataframe(df_with_len_tweets)
    df_with_len_tweets_non_suicidal = get_non_suicidal_dataframe(df_with_len_tweets)
    
    #determine the average length of suicidal and non suicidal tweets 
    average_suicidal=df_with_len_tweets_suicidal['len_tweet'].mean()
    average_non_suicidal =df_with_len_tweets_non_suicidal['len_tweet'].mean()
    
    #determine the max between the third quartiles of the datasets
    quartile3_suicidal= df_with_len_tweets_suicidal['len_tweet'].quantile(0.75)
    quartile3_non_suicidal=df_with_len_tweets_non_suicidal['len_tweet'].quantile(0.75)
    if quartile3_non_suicidal > quartile3_suicidal:
        quartile1_non_suicidal= df_with_len_tweets_non_suicidal['len_tweet'].quantile(0.25)
        inter_quartile= quartile3_non_suicidal - quartile1_non_suicidal
    else:
        quartile1_suicidal= df_with_len_tweets_suicidal['len_tweet'].quantile(0.25)
        inter_quartile= quartile3_suicidal - quartile1_suicidal
    
    #execute the boxplot 
        #choosing the text font 
    sns.set(font='Georgia')
        #setting the boxplot
    sns.boxplot(x=df_with_len_tweets['target'],y=df_with_len_tweets['len_tweet'],data=df_with_len_tweets)
        #setting axis labels
    plt.xlabel('Target')
    plt.ylabel('Length of the tweets')
        #setting the title
    plt.title('tweets'' length',fontsize=18, color='blue', ha='center')
        #choosing the limit of y axis to represent the graph 
    plt.ylim(-50, max(quartile3_suicidal , quartile3_non_suicidal) + 2* inter_quartile )
        #drawing a line to represent the non suicidal average tweet length 
    plt.hlines(y=average_non_suicidal, xmin=-0.5, xmax=0.5, colors='r', label='averege non suicidal tweet length',linewidth=2)
        #writing the non suicidal average value 
    plt.text(-0.7, average_non_suicidal, f'{round(average_non_suicidal,2)}', color='r', fontsize=10, ha='left', va='center')
        #drawing a line to represent the suicidal average tweet length 
    plt.hlines(y=average_suicidal, xmin=0.5, xmax=1.5, colors='green', label='averege suicidal tweet length',linewidth=2)
        #writing the suicidal average value 
    plt.text(1.7, average_suicidal, f'{round(average_suicidal,2)}', color='green', fontsize=10, ha='right', va='center')
    
    plt.legend()



def show_length_evolution (df: pd.DataFrame):
    """plot graphs for tweet length evolution during months in each year
    
    Args:
        df (pd.DataFrame): dataframe of tweets
    """
    sns.set(font='Georgia')
    sns.relplot(data=get_tweet_length(df), x="month", y="len_tweet", hue="target", kind="line",col="year",palette=['red','blue'])


def heatmap_day_hour(df:pd.DataFrame):
    """plot a heatmap representing the number of tweets in every hour of each day 

    Args:
        df (pd.DataFrame): dataframe of tweets
    """
    data_to_plot=df.groupby('day')['hour'].value_counts().unstack().fillna(0)
    sns.heatmap(data_to_plot,cmap='Reds') 
    plt.title('number of tweets',fontsize=18, color='red', ha='center')
    
heatmap_day_hour(get_suicidal_dataframe(get_predicted_dataframe()))
def likes_retweets_replies_evolution(df:pd.DataFrame):
    """shows the number of likes, retweets and replies evolution during years 

    Args:
        df (pd.DataFrame): dataframe of tweets
    """
    sns.set_theme(style='whitegrid')
    sns.color_palette('pastel')
    #creating seperate figures 
    fig, axes =plt.subplots(1,3,figsize=(18,6))
    #creating the figure that containes the number of likes evolution during years
    sns.lineplot(df,x='year',y='nlikes',hue='target',errorbar=None,ax=axes[0])
    axes[0].set_title('number of likes evolution during years',color='Blue')
    axes[0].legend(['suicidal','non suicidal'])
    #creating the figure that containes the number of likes evolution during years
    sns.lineplot(df,x='year',y='nretweets',hue='target',errorbar=None,ax=axes[1])
    axes[1].set_title('number of retweets evolution during years',color='Blue')
    axes[1].legend(['suicidal','non suicidal'])
    #creating the figure that containes the number of likes evolution during years
    sns.lineplot(df,x='year',y='nreplies',hue='target',errorbar=None,ax=axes[2])
    axes[2].set_title('number of replies evolution during years',color='Blue')
    axes[2].legend(['suicidal','non suicidal'])
     
    

def save_plot(name_of_the_plot :str)-> None :
    """this function is used to save the plots in the directory plots at gitlab

    Args:
        name_of_the_plot (str): the name of the function to plot
    """
    plt.savefig(f"plots/{name_of_the_plot}.png")
    print(f"plot saved on plots/{name_of_the_plot}.png")
    plt.figure()


