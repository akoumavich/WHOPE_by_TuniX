
import sys
import os
sys.path.append(os.getcwd())

#importing dash libraries
from dash import  html,dcc, callback
from dash.dependencies import Input , Output 
import plotly.express as px
import plotly.graph_objects as go
#importing textblob
from textblob import TextBlob
# importing the application modules needed
import tweet_collection.tweet_collection as collection

import pandas as pd
# Import the necessary libraries
from PIL import Image
from numpy import asarray
 
 


#import th datasets to analyze
df=collection.get_training_dataframe()
df['count_at'] = pd.Series(df['text'].apply(lambda x: str(x).count('want')))

#get the suicidal dataframe 
df_suicidal=collection.get_suicidal_dataframe(df)
    
#get the suicidal dataframe
df_non_suicidal=collection.get_non_suicidal_dataframe(df)
def sentiment_dataframe(df):
    """
    Perform sentiment analysis on the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame to perform sentiment analysis on.

    Returns:
        pandas.DataFrame: DataFrame with sentiment analysis results appended.
    """
    df_l=df
    
    df_l ['TextBlob_Analysis'] = df['text'].apply(lambda x: getAnalysis(str(x)) )
    return df_l
def getPolarity(text):
    """
    Get the polarity of a given text.

    Args:
        text (str): Input text.

    Returns:
        float: Polarity score of the text.
    """
    
    return TextBlob(text).sentiment.polarity
def getAnalysis(text):

    """
    Perform sentiment analysis on a given text.

    Args:
        text (str): Input text.

    Returns:
        str: Sentiment label (Positive, Negative, or Neutral).
    """
    score=TextBlob(text).sentiment.polarity
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


def get_training_tab()->html.Div:
     """
    Get the contents of the analysis tab for displaying in a Div.

    Returns:
        html.Div: Div containing the contents of the analysis tab.
    """
     return html.Div(children=[
        html.Div(children=[
        html.H2(" "),
        html.Div(id="Group_buttons_training",className="prediction graph_training buttons",children=[
            html.Button("suicidal vs Non-suicidal",id="button_perc_suic_vs_nsuic_training",style={'background-color': '#ffffff','border-top': 'thick double #0f93ff'}),
            html.Button("keyWord Repartition",id="button_keyword_Repartition_training",style={'backgroundColor':'#0A1828','color':'#f7f8fa'}),
            html.Button("world Clouds",id='heatmap_button_training',style={'backgroundColor':'#0A1828','color':'#f7f8fa'})
        ],style={'padding': '10px',
                    'width': 'auto', 
                    'display': 'flex','justify-content':'space-evenly'})
  ]),
        html.H2(" "),
        html.Div(id="graph_training_displayed_training",children=[
                dcc.Input(
                id="input_keyword_training",
                type="text",
                placeholder="Search a keyWord",
                style={'display':'None','margin':'auto','width':'600px'}
        ),
        dcc.Graph(id="graph_training",figure=perc_suicidal_non_suicidal(0)[0]),
        html.Div(id='wordcloud_div',style={'display':'none'},children=[
        html.Img(src="assets/wordcloud_non_suicidal_hope.png",style={'margin':'auto','width':'60%'}), 
        html.Img(src="assets/wordcloud_suicidal_sad.png",style={'margin':'auto','width':'60%'})])
        
        ])
    ])
@callback(
    Output('graph_training', 'figure',allow_duplicate=True),
    Output('input_keyword_training','style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic_training', 'style',allow_duplicate=True),
    Output('button_keyword_Repartition_training', 'style',allow_duplicate=True),
    Output('heatmap_button_training', 'style',allow_duplicate=True),
    Output('wordcloud_div', 'style',allow_duplicate=True),
    Output('graph_training', 'style',allow_duplicate=True),
    Input('button_perc_suic_vs_nsuic_training', 'n_clicks'),

    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def perc_suicidal_non_suicidal(n_clicks) :
    
    #get the length of suicidal tweets and non suicidal tweets
    nb_tweet_suicidal= df_suicidal.shape[0]
    nb_tweet_non_suicidal=df_non_suicidal.shape[0]
    
    #define the values and labels that would be used to create the pie chart
    values=[nb_tweet_non_suicidal,nb_tweet_suicidal]
    labels=['percentage of non suicidal tweets','percentage of suicidal tweets']
    fig = px.pie(df, values=values, names=labels, hole=.3)

    return fig , {'display': 'none'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'display': 'none'},{'display': 'block'}


@callback(
    Output('graph_training', 'figure',allow_duplicate=True),
    Output('input_keyword_training','style',allow_duplicate=True),
    Output('button_keyword_Repartition_training', 'style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic_training', 'style',allow_duplicate=True),
    
    Output('heatmap_button_training', 'style',allow_duplicate=True),
    Output('wordcloud_div', 'style',allow_duplicate=True),
    
    Output('graph_training', 'style',allow_duplicate=True),
    Input('button_keyword_Repartition_training', 'n_clicks'),

    prevent_initial_call=True,
    
    suppress_callback_exceptions=True
)


def show_search_box(n_clicks):
    df_l=df.groupby('target')['count_at'].sum().reset_index()
    df_l.iloc[0,1]=(df_l.iloc[0,1]*df_non_suicidal.size)/df.size
    df_l.iloc[1,1]=(df_l.iloc[1,1]*df_suicidal.size)/df.size
    #create the plot and show it
    fig = px.bar(df_l, x='target',y='count_at',labels=['suicidal','non-suicidal'])
    return fig , {'display': 'block','width':'25%','margin':'auto'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'display':'none'},{'display':'block'}



@callback(
    Output('graph_training', 'figure',allow_duplicate=True),
    Input('input_keyword_training', 'value'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def show_keyword_repartition(value):
    df['count_at'] = pd.Series(df['text'].apply(lambda x: str(x).count(str(value))))
    df_l=pd.DataFrame(df.groupby('target')['count_at'].sum()).reset_index()
    df_l.iloc[0,1]=(df_l.iloc[0,1]/df_non_suicidal.size)*df.size
    df_l.iloc[1,1]=(df_l.iloc[1,1]/df_suicidal.size)*df.size
    #create the plot and show it
    fig=px.bar(df_l,x='target',y='count_at',labels=['suicidal','non-suicidal'])
    return fig 
    
@callback(
    Output('graph_training', 'style',allow_duplicate=True),
    Output('input_keyword_training','style',allow_duplicate=True),
    Output('heatmap_button_training', 'style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic_training', 'style',allow_duplicate=True),
    Output('button_keyword_Repartition_training', 'style',allow_duplicate=True),
    Output('wordcloud_div', 'style',allow_duplicate=True),

    Input('heatmap_button_training', 'n_clicks'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def show_heatmap(n_clicks) :


    return {'display': 'none'},{'display': 'none'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'display':'flex','flex-direction':'column'}




