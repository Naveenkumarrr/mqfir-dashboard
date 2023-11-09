import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import datetime

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

header = html.Header(className="header text-white", style={'background-color': 'black', 'padding': '10px'}, children=[
    html.Div(className="container", children=[
        html.H1(className="display-4", children="Tivoli Daily Report")
    ])
])

app.layout = html.Div([header, html.Div(className="row justify-content-center", children=[
    html.Div(className="col-md-4", style={'background-color': 'black', 'margin-top': '10px', 'padding': '20px', 'border-radius': '10%'}, children=[
        dbc.Label("Database Username", className="form-label", style={'color': 'red', 'margin-top': '15px'}),
        dcc.Input(id="username", type="text", placeholder="Username", className="form-control"),

        dbc.Label("Database Password", className="form-label", style={'color': 'red', 'margin-top': '15px'}),
        dcc.Input(id="password", type="password", placeholder="Password", className="form-control"),
        
        dbc.CardGroup([
            dbc.Label("Choose a Date", className="form-label", style={'color': 'red', 'margin-top': '15px'}),
            dbc.Input(id="date", type="date"),
        ]),

        html.Button(id="submit-button", className="btn btn-success btn-lg", children="Submit", type="submit",
                    style={'padding': '10px 40px', 'margin': '20px'})]),
    html.Hr(),
    html.Div(id="output-state")
])

])

@app.callback(Output("output-state", "children"),
              [Input("submit-button", "n_clicks")],  
              [State("username", "value"), 
               State("password", "value"),
               State("date", "value")])
def update_output(n_clicks, username, password, date):

    if n_clicks is None:
        n_clicks = 0

    if n_clicks > 0:
        error = False
        if not username:
            error = True
            return html.Div(["Username is required"])
        
        if not password:
            error = True
            return html.Div(["Password is required"])

        if not date:
            error = True
            return html.Div(["Date is required"])
        
        if not error:
            return [
                html.H4("Username: {}".format(username)),
                html.H4("Password: {}".format(password)),
                html.H4("Date: {}".format(date))
            ]

    return ""
if __name__ == "__main__":
    app.run_server(debug=True)