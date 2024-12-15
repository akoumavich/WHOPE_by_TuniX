
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


#import th datasets to analyze
df=collection.get_predicted_dataframe()
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


def get_prediction_analysis_tab()->html.Div:
     """
    Get the contents of the analysis tab for displaying in a Div.

    Returns:
        html.Div: Div containing the contents of the analysis tab.
    """
     return html.Div(children=[
        html.Div(children=[
        html.H2(" "),
        html.Div(id="Group_buttons",className="prediction graph buttons",children=[
            html.Button("suicidal vs Non-suicidal",id="button_perc_suic_vs_nsuic",style={'background-color': '#ffffff','border-top': 'thick double #0f93ff'}),
            html.Button("keyWord Repartition",id="button_keyword_Repartition",style={'backgroundColor':'#0A1828','color':'#f7f8fa'}),
            html.Button("heat map",id='heatmap_button',style={'backgroundColor':'#0A1828','color':'#f7f8fa'}),
            html.Button("sentiment repartition",id='sentiment_button',style={'backgroundColor':'#0A1828','color':'#f7f8fa'})
        ],style={'padding': '10px',
                    'width': 'auto', 
                    'display': 'flex','justify-content':'space-evenly'})
  ]),
        html.H2(" "),
        html.Div(id="graph_displayed",children=[
                dcc.Input(
                id="input_keyword",
                type="text",
                placeholder="Search a keyWord",
                style={'display':'None','margin':'auto','width':'600px'}
        ),
        html.Div(id="sentiment_dropdowns",children=[
            html.Div(id='type_dropdown_div',children=[
                html.H4('Choose your dataset',style={'fontFamily':'Segoe Print','fontSize':'20px','color':'#47a673'}),
                dcc.Dropdown(['suicidal','non_suicidal'],['suicidal','non_suicidal'],id='type_dropdown',multi=True)]
                ,style={'margin':'20px'}),
            html.Div(id='sentiment_dropdown_div',children=[ 
                html.H4('Choose the sentiment',style={'fontFamily':'Segoe Print','fontSize':'20px','color':'#47a673'}),
                dcc.Dropdown(['Positive','Negative','Neutral'],'Negative',id='sentiment_dropdown',multi=False)],style={'margin':'20px'}),
                dcc.Dropdown(['suicidal','non_suicidal'],['suicidal','non_suicidal'],id='type_dropdown_duplicate',multi=True)
        ],style={'display':'none'}),
        dcc.Graph(id="graph",figure=perc_suicidal_non_suicidal(0)[0])
        
        ])
    ])
@callback(
    Output('graph', 'figure',allow_duplicate=True),
    Output('input_keyword','style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic', 'style',allow_duplicate=True),
    Output('button_keyword_Repartition', 'style',allow_duplicate=True),
    Output('heatmap_button', 'style',allow_duplicate=True),
    Output('sentiment_button', 'style',allow_duplicate=True),
    
    Output('sentiment_dropdowns', 'style',allow_duplicate=True),

    Input('button_perc_suic_vs_nsuic', 'n_clicks'),

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

    return fig , {'display': 'none'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'display': 'none'}


@callback(
    Output('graph', 'figure',allow_duplicate=True),
    Output('input_keyword','style',allow_duplicate=True),
    Output('button_keyword_Repartition', 'style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic', 'style',allow_duplicate=True),
    
    Output('sentiment_button', 'style',allow_duplicate=True),
    Output('heatmap_button', 'style',allow_duplicate=True),
    Output('sentiment_dropdowns', 'style',allow_duplicate=True),
    Input('button_keyword_Repartition', 'n_clicks'),

    prevent_initial_call=True,
    
    suppress_callback_exceptions=True
)
def show_search_box(n_clicks):
    df_l=df.groupby('day')['count_at'].sum()

    #create the plot and show it
    fig = px.bar(df_l, barmode="group")
    return fig , {'display': 'block','width':'25%','margin':'auto'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'display': 'none'}



@callback(
    Output('graph', 'figure',allow_duplicate=True),
    Input('input_keyword', 'value'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def show_keyword_repartition(value):
    df['count_at'] = pd.Series(df['text'].apply(lambda x: str(x).count(str(value))))
    df_l=pd.DataFrame(df.groupby(['day','target'])['count_at'].sum()).reset_index()
    #create the plot and show it
    fig=px.bar(df_l,x='day',y='count_at',color='target')
    return fig 
    
@callback(
    Output('graph', 'figure',allow_duplicate=True),
    Output('input_keyword','style',allow_duplicate=True),
    Output('heatmap_button', 'style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic', 'style',allow_duplicate=True),
    Output('button_keyword_Repartition', 'style',allow_duplicate=True),
    Output('sentiment_button', 'style',allow_duplicate=True),
    Output('sentiment_dropdowns', 'style',allow_duplicate=True),
    Output('sentiment_dropdown_div', 'style',allow_duplicate=True),
    Output('type_dropdown_div', 'style',allow_duplicate=True),
    Output('type_dropdown_duplicate', 'style',allow_duplicate=True),
    
    Input('heatmap_button', 'n_clicks'),
    Input('type_dropdown_duplicate','value'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def show_heatmap(n_clicks,value) :
    df_chosen=df
    if len(value)==1:
        if value[0]=='suicidal':
            df_chosen = df_suicidal
        else:
            df_chosen=df_non_suicidal
    data_to_plot=df_chosen.groupby('day')['hour'].value_counts().unstack().fillna(0)
    
    fig = px.imshow(data_to_plot,
                labels=dict(y="day", x="hour", color="nbr tweets"),
                y=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
                x=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
               )
    fig.update_xaxes(side="top")

    return fig ,{'display': 'none'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'display': 'block'},{'display': 'none'},{'display': 'none'},{'display': 'block'}





@callback(
    Output('graph', 'figure',allow_duplicate=True),
    Output('input_keyword','style',allow_duplicate=True),
    Output('heatmap_button', 'style',allow_duplicate=True),
    Output('button_perc_suic_vs_nsuic', 'style',allow_duplicate=True),
    Output('button_keyword_Repartition', 'style',allow_duplicate=True),
    Output('sentiment_button', 'style',allow_duplicate=True),
    Output('sentiment_dropdowns', 'style',allow_duplicate=True),
    Output('sentiment_dropdown_div', 'style',allow_duplicate=True),
    Output('type_dropdown_div', 'style',allow_duplicate=True),
    Output('type_dropdown_duplicate', 'style',allow_duplicate=True),
    Input('sentiment_button', 'n_clicks'),
    Input('sentiment_dropdown','value'),
    Input('type_dropdown','value'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def show_sentiment(n_clicks,sent_value,type_value) :
    df_chosen=df
    color='#87b8ea'
    if len(type_value)==1:
        if type_value[0]=='suicidal':
            df_chosen = df_suicidal
            color='#ae0e52'
        else:
            df_chosen=df_non_suicidal
            color='#038c93'

    df_l=sentiment_dataframe(df_chosen)
    df_l=df_l.loc[df_l['TextBlob_Analysis']==str(sent_value)].groupby('day').count().reset_index()

    #create the plot and show it

    fig = go.Figure(px.bar(df_l, x='day',y='TextBlob_Analysis'))
    fig.update_traces(marker_color=color)
    return fig ,{'display': 'none'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'background-color': '#ffffff','border-top': 'thick double#0f93ff'},{'display': 'flex','flex-direction': 'column'},{'display':'block'},{'display':'block'},{'display':'none'}


