#Programmer: Hannah Frederick
#Date:09/26/2025
#Program Description: Utilize a MongoDB shell to store the database and Dash to create a user-friendly dashboard that displays information from the database. The dashboard contains a dynamic geolocation map and pie chart that update based off the data shown in the table at the top of the page, which can be filtered using preset conditions at the top of the table. Additional filter options for each column using AgGrid are also available
#This file sets up program to use Dash Pages
import dash
from dash import Dash
from dash import html
from flask import Flask

server = Flask(__name__)
server.secret_key = 'secret'

app = dash.Dash(__name__, server=server, use_pages=True)

app.layout = html.Div(children=[
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)