#Programmer: Hannah Frederick
#Date:09/26/2025
#Program Description: Utilize a MongoDB shell to store the database and Dash to create a user-friendly dashboard that displays information from the database. The dashboard contains a dynamic geolocation map and pie chart that update based off the data shown in the table at the top of the page, which can be filtered using preset conditions at the top of the table. Additional filter options for each column using AgGrid are also available
#This file sets up and controls the Dashboard

# Configure the necessary Python module imports for dashboard components
import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output, State
import base64
from dash_ag_grid import AgGrid
import dash
from dash import callback
from flask import session
from pymongo import MongoClient
import os
from dash import Dash

# Configure the plotting routines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#register page with Dash pages
dash.register_page(__name__,path='/ProjectTwoDashboard', name='Dashboard')

#Import CRUD module
from animal_shelter import AnimalShelter


###########################
# Data Manipulation / Model
###########################

#method for connection Variables
def get_db():
    username = session.get('username')
    password = session.get('password')
    
    if not username or not password:
        return html.Div("Unauthorized acces. Please log in.", style={'color':'red'})
    return AnimalShelter(username, password, 'localhost', 27017, 'AAC', 'animals')


#########################
# Dashboard Layout / View
#########################

#Add in Grazioso Salvare’s logo
image_filename = "Grazioso Salvare Logo.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    
#Define the layout of the dashboard
def layout():
    db = get_db()
    # sending the read method an empty document requests all documents be returned. Drop the _'id' column if documents are returned
    df = pd.DataFrame.from_records(db.read({}))
    if '_id' in df.columns:
        df.drop(columns=['_id'],inplace=True)
    
    
    #Add custom filtering options for the data table
    custom_filter_columns = {
            "age_upon_outcome",
            "breed",
            "sex_upon_outcome",
            "color",
            "animal_type",
            "name",
            "date_of_birth",
            "datetime",
            "Monthyear",
            "outcome_subtype",
            "outcome_type",
            "location_lat",
            "location_long"
        }
    
    columnDefs = []
    for column in df.columns:
        if column in custom_filter_columns:
            columnDefs.append({
                "field": column,
               "filter": "agTextColumnFilter",
                "filterParams": {
                    "filterOptions": ["contains", "notContains"],
                    "maxNumConditions": 3,
                    "buttons": ["apply", "reset"]
                }
            })
        else:
            columnDefs.append({
                "field": column
            })

    
    return html.Div([
    html.Div(id='hidden-div', style={'display':'none'}),
    html.Center(html.B(html.H1('CS-340 Dashboard'))),
    html.Center(html.A(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), 
                style={
                    'width': '150px',
                    'height': 'auto',
                    'objectFit': 'contain'
                      }),
                    href='http://www.snhu.edu',
                   )),
    html.Hr(),
    html.A([
        html.Button('KMeans Clustering Page', id='kmeans_button'),
    ], href="/KMeansClustering"),
    html.Div("SNHU CS 499 - Hannah Frederick",
            style={
                'position':'fixed',
                'bottom': '0'
            }),
    #Adds the interactive filtering options for the data table
    dcc.RadioItems(
        id = 'filter-type',
        options = [
            {'label': 'Water Rescue', 'value' : 'water'},
            {'label': 'Mountain/Wilderness Rescue', 'value' : 'mountain_wilderness'},
            {'label': 'Disaster Rescue/Individual Tracking', 'value' : 'disaster_individual'},
            {'label': 'Reset', 'value' : 'reset'}
        ],
        value = 'reset',
    ),

    html.Hr(),

    #Defines the data table
    AgGrid(
        id='datatable-id',
        rowData=df.to_dict('records'),

        columnDefs=columnDefs,
        columnSize="autoSize",
        dashGridOptions={
            "rowSelection": "single"
        },
    ),

    #Adds the interactive filtering options for the charts
    html.Div([
        dcc.Dropdown(
        id = 'filter-chart',
        options = [
            {'label': 'Pie Chart', 'value' : 'pie'},
            {'label': 'Vertical Bar Chart', 'value' : 'vertical_bar'},
            {'label': 'Horizontal Bar Chart', 'value' : 'horizontal_bar'},
        ],
        value = 'pie',
        style={'width': '50%'}),
    ]),
        
    html.Br(),
    html.Hr(),
    
    #This sets up the dashboard so that the chart and geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            ),
        ])
])

#############################################
# Interaction Between Components / Controller
#############################################

#callback and method automaticcaly select the first row of the data table
@callback(
    Output('datatable-id','selectedRows'),
    [Input('datatable-id', 'rowData')])
def auto_select_first_row(row_data):
    if row_data:
        return [row_data[0]]
    return []

#callback and method update the dashboard so that the preset filters at the top of the data table make the data table interactive through use of MongoDB queries
@callback(
    Output('datatable-id','rowData'),
    [Input('filter-type', 'value')]
)
def update_dashboard(filter_type):
        db = get_db()
    
        if filter_type == 'water':
            query = {"animal_type": "Dog", "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]}, 
            "sex_upon_outcome": "Intact Female", "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}}
        elif filter_type == 'mountain_wilderness':
             query = {"animal_type": "Dog", "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
                     "sex_upon_outcome": "Intact Male", "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}}
        elif filter_type == 'disaster_individual':
            query = {"animal_type": "Dog", "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]},
                    "sex_upon_outcome": "Intact Male", "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}}
        else:
            query = {}
        
        data = pd.DataFrame.from_records(db.read(query))
        data.drop(columns=['_id'], inplace=True)

        if data.empty:
            return[]

        return data.to_dict('records')   

#callback and method display the breeds of animal based on quantity represented in the data table. Also updates the type of graph dispayed based on user selection
@callback(
    Output('graph-id', "children"),
    Input('datatable-id', "virtualRowData"),
    Input('filter-chart', 'value'))
    
def update_graphs(virtualRowData, chart_type):
    db = get_db()
    
    dff = pd.DataFrame.from_dict(virtualRowData)
    
    if chart_type == 'pie': 
            fig = px.pie(dff, names='breed', title='Preferred Animals By Breed Pie Chart')
    elif chart_type == 'vertical_bar':          
            fig = px.bar(dff, x='breed', title='Preferred Animals By Breed Vertical Bar Chart')
    elif chart_type == 'horizontal_bar':          
            fig = px.bar(dff, y='breed', title='Preferred Animals By Breed')
    else:
        return[]

    return [dcc.Graph(figure=fig)]

#callback and method update the geo-location chart for the selected data entry
@callback(
    Output('map-id', "children"),
    Input('datatable-id', "selectedRows"))
def update_map(selected_rows):  
    db = get_db()
        
    if not selected_rows:
        return html.P("No rows selected")

    selected = selected_rows[0]

    lat = selected['location_lat']
    long = selected['location_long']
    breed = selected['breed']
    name = selected['name']
    
    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[30.75,-97.48], zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            # Marker with tool tip and popup
            dl.Marker(position=[lat,long], children=[
                dl.Tooltip(breed),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(name)
                ])
            ])
        ])
    ]

print("Find program at: http://127.0.0.1:8050/")