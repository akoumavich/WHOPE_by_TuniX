
from dash import Dash, html, Input, Output, ctx, callback

import os
import sys

sys.path.append(os.getcwd())

import div_button_production.predict_csv as pc
import div_button_production.predict_tweet as ptw


def get_prediction_tab():
 return html.Div([
    html.H3('choose a button to click',style={'fontFamily':'Segoe Print','fontSize':'20px',"text-align": "center"}),
    html.Div( style={"text-align": "center",'display': 'flex','justify-content':'space-evenly'},children=[
    html.Button('import csv', id='btn_csv', n_clicks=0,style={'backgroundColor':'#0A1828','color':'#f7f8fa'}),
    html.Button('predict Tweet', id='btn_tweet', n_clicks=0,style={'backgroundColor':'#0A1828','color':'#f7f8fa'}),
 ])
 ,html.Div(id='container_prediction')
    
],style={'color':'#47a673'})



@callback(
    Output('container_prediction', 'children'),
    Output('btn_csv', 'style',allow_duplicate=True),
    Output('btn_tweet', 'style',allow_duplicate=True),
    Input('btn_csv', 'n_clicks'),
    Input('btn_tweet', 'n_clicks'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def displayClick(btn1, btn2):
    """displays the button that was clicked

    Args:
        btn1 (button): button1
        btn2 (button): buton2

    Returns:
        Html.Div: div containing the button
        """    
    if "btn_csv" == ctx.triggered_id:
        return pc.predict_csv(),{'background-color': '#ffffff','border-top': 'thick double #0f93ff'},{'backgroundColor':'#0A1828','color':'#f7f8fa'}
    elif "btn_tweet" == ctx.triggered_id:
        return ptw.predict_tweet(),{'backgroundColor':'#0A1828','color':'#f7f8fa'},{'background-color': '#ffffff','border-top': 'thick double #0f93ff'}
