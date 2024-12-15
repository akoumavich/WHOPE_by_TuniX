import sys
import os
sys.path.append(os.getcwd())
from dash import callback
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import base64
import io
import suicide_training.prediction as pred

def predict_csv()->html.Div:
    """
    Returns:
        html.Div: a Div containing the uploaded file contents
    """    
    return    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files'), ". The column containing the textual content of the tweets has to be named 'text'"
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            multiple=False  # Allow only a single file upload
        ),

        html.Button('Save File', id='save-button', n_clicks=0,style={'backgroundColor':'#c7e6ff','color':'#0A1828'}),
        dcc.Loading(
            id='loading-save-file',
            type='default',
            children=html.Div(id="loading_save_file")),

        html.Div(id='output-data-upload')
        ])

def parse_contents(contents, filename:str)->html.Div:
    """parses the contents of the Div containing the uploaded file

    Args:
        contents 
        filename (str): name of the uploaded file

    Returns:
        html.Div: _description_
    """    
    
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename.lower():
            # Assume the uploaded file is a CSV
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8'))
            )
        elif 'xls' in filename.lower():
            # Assume the uploaded file is an Excel file
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return html.Div('The file uploaded is not a CSV or Excel file.')
    except Exception as e:
        return html.Div(f'There was an error processing this file: {str(e)}')

    return df
  
@callback(
    Output('loading_save_file', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    Input('save-button', 'n_clicks')
)
def update_output(contents, filename:str, n_clicks:int)->html.Div:
    """updates the content of the div containing the uploaded file

    Args:
        contents : content of the div containing the file
        filename (str):  the name of the uploaded file
        n_clicks (int): the number of times the button has been clicked

    Returns:
        html.Div: content of the div containing the uploaded file 
    """    
    if contents is not None:
        children = parse_contents(contents, filename)
        children = pred.predicted_dataframe(children)
        if n_clicks > 0 and isinstance(children, pd.DataFrame):
            children.to_csv('datasets/predicted_dataset.csv')
            n_clicks=0
            return html.Div(f'File "{filename}" saved as predicted_dataset.csv')
        if isinstance(children, pd.DataFrame):
            return html.Div([
                html.H5(f'Uploaded File: {filename}'),
                html.H6('Preview:'),
                html.Div(
                    [
                        html.Table(
                            [html.Tr([html.Th(col) for col in children.columns])] +
                            [html.Tr([html.Td(children.iloc[i][col]) for col in children.columns]) for i in range((len(children)))]
                        )
                    ],
                    style={'overflowX': 'scroll'}
                )
            ])
        return children