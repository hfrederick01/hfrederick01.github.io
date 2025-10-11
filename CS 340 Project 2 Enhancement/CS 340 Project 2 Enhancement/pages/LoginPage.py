#Programmer: Hannah Frederick
#Date:09/26/2025
#Program Description: Utilize a MongoDB shell to store the database and Dash to create a user-friendly dashboard that displays information from the database. The dashboard contains a dynamic geolocation map and pie chart that update based off the data shown in the table at the top of the page, which can be filtered using preset conditions at the top of the table. Additional filter options for each column using AgGrid are also available
#This file sets up and controls the login page

# Configure the necessary Python module imports for dashboard components
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import callback, State
import dash
from flask import session
import bcrypt
from pymongo import MongoClient

# URL Lib to make sure that our input is 'sane'
import urllib.parse

#register page with Dash pages
dash.register_page(__name__, path='/', title="Login")

#Import CRUD module
from animal_shelter import AnimalShelter

client = MongoClient("mongodb://localhost:27017/")
HOST = 'localhost'
PORT = 27017
DB = 'AAC'
db=client["AAC"]
COL = 'users'

# Build App layout
layout = html.Div(children=[
    html.H1("Grazioso Salvare Login Page"),
    #Creates input fields for username and password
    dcc.Input(
            id="input_user",
            type="text",
            placeholder="Username",
            value=""
    ),
    dcc.Input(
            id="input_passwd",
            type="password",
            placeholder="Password",
            value=""
    ), 
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='login-message', style={'color':'red', 'marginTop': '10px'}),
    html.Hr(),
    html.Div(id="query-out", style={'whiteSpace': 'pre-line'}),
    html.Div("SNHU CS 499 - Hannah Frederick",
        style={
            'position':'fixed',
            'bottom': '0'
        }),
    dcc.Location(id='url',refresh=True) 
    
])

#callback and method for authentication of user's username and password
@callback(
    Output('login-message', 'children'),
    Output('url', 'pathname'),
    Input('submit-val', 'n_clicks'),
    State('input_user', 'value'),
    State('input_passwd', 'value'),
    prevent_initial_call=True
)
def login_user(n_clicks,inputUser,inputPass):
    if not inputUser or not inputPass:
        return "Please enter both username and password", dash.no_update
    
    user = db['admin'].find_one({"user": inputUser})
    
    if user and bcrypt.checkpw(inputPass.encode('utf-8'), user['pwd']):
        session['logged_in'] = True
        session['username'] = inputUser
        session['password'] = inputPass
        return '', '/ProjectTwoDashboard'
    else:
        return "Invalid username or password", dash.no_update
