#! /usr/bin/env python

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
                html.H1(children='ChemEco'),

                html.Div(children='''
                            ChemEco: A web application framework for data mining and machine learning.
                                    '''),

                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'ChemML'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'ChemEco'},
                                ],
                        'layout': {
                            'title': 'ChemEco Workflow Visualization'
                                  }
                            }
                        )
            ]
                    )

if __name__ == '__main__':
    app.run_server(debug=True)