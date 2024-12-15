
from dash import  html, Input, Output, callback, dcc,State

import os
import sys
import pandas as pd

sys.path.append(os.getcwd())


from suicide_training.prediction import *

#initialization of the data frame containing  the tweets
df=pd.DataFrame()

def predict_tweet()->html.Div:
    """this function returns the div of the tab of tweet prediction

    Returns:
        html.Div: Div containing tab elements
    """    
    
    return html.Div([
    html.H6('Enter the tweet : ',style={'fontFamily':'Segoe Print'}),
    dcc.Textarea(
            id="input_tweet"
            , style={'width': '100%','height': '100px','box_sizing':'content_box','border':'2px solid #0f93ff'}
        )
    ,
    html.Button('Predict', id='predict_tweet_btn', n_clicks=0,style={'backgroundColor':'#c7e6ff','color':'#0A1828'}),
    dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading_tweet_predict")
        ),
    html.Div(id="tweet_prediction_result")

])

@callback(
    Output("loading_tweet_predict", "children"),
    State('input_tweet', 'value'),
    Input('predict_tweet_btn', 'n_clicks'))
def predict_tweet_entered(value:str,clicks:int)->html.H6:
    """predicts the tweet

    Args:
        value (str): tweet text
        clicks (int): number of clicks on the button

    Returns:
        html.H6: html containing the result of the prediction
    """    
    
    if(clicks>0):
        df=pd.DataFrame()
        df["text"]=pd.Series([value])

        df=predicted_dataframe(df)

        prediction=df["target"].iloc[0]
        proba=round(df["probability"].iloc[0]*100,2)

        result=""
        img=""
        if int(prediction)==0:
            result="non suicidal"
            proba=100-proba
            if proba>60:
                img="happy"
            else:
                img="neutral"
        else :
            result="suicidal"
            if proba>60:
                img="sad"
            else:
                img="neutral"

        


        

    res_div =html.Div(id="tweet_prediction_result",children=[html.H6(f"the writer of this tweet is likely to be {result} at {proba}% ",style={'fontFamily':'Segoe Print'}) ,
                                                             html.Div(style={"text-align": "center"},
                                                                      children=[html.Img(src=(f'assets/{img}_smiley.png'),
                                                                                         style={'height':'5%', 'width':'5%'})])]
    ) 
    return res_div






