from dash import Dash, dcc, html, Input, Output, callback

import os
import sys

sys.path.append(os.getcwd())
import dash_bootstrap_components as dbc
import prediction_tab as pt
import analysis_tab as at
import training_tab as tt
import authentifictaion as auth

import dash_auth

if __name__ == '__main__':
    #users dictionary
    USERNAME_PASSWORD_PAIRS = auth.import_dico()

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    #creating Dashboard
    app = Dash(__name__, external_stylesheets=external_stylesheets)

    #initializing authentification
    auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)

    #setting up tabs
    app.layout = html.Div([
        html.Img(src=('assets/logo.png'),style={'height':'10%', 'width':'10%'}),
        dcc.Tabs(id="tabs", value='tab_views', children=[
            dcc.Tab(label='Training Dataset Analysis', value='training_tab',style={'backgroundColor':'#0A1828','fontFamily':'Courier New','fontWeight' : 'bold'}),
            dcc.Tab(label='Want to predict ? ...', value='prediction_tab',style={'backgroundColor':'#0A1828','fontFamily':'Courier New','fontWeight' : 'bold'},)
            ,dcc.Tab(label='Predicted Dataset Analysis', value='analysis_tab',style={'backgroundColor':'#0A1828','fontFamily':'Courier New','fontWeight' : 'bold'})
        ],style={'fontSize':'20px','color':'#f7f8fa'}),
        html.Div(id='tabs-content')
        
    ])


    @callback(Output('tabs-content', 'children'),Input('tabs', 'value'))
    def render_content(tab:str)->html.Div:   
        """changes the tab on click

            Args:
                tab (str): value of the tab

            Returns:
                dcc.Div:div containing the tab
            """    
        if tab == 'training_tab':
            return tt.get_training_tab()
        elif tab == 'prediction_tab':
            return  pt.get_prediction_tab()
        elif tab=="analysis_tab":
            return at.get_prediction_analysis_tab()

    if __name__ == '__main__':
        app.run(debug=False)