#FIX ME HOW TO CITE RESOURCE? dO IT IN CODE?
#Programmer: Hannah Frederick
#Date:10/03/2025
#Program Description: Utilize a MongoDB shell to store the database and Dash to create a user-friendly dashboard that displays information from the database. The dashboard contains a dynamic geolocation map and pie chart that update based off the data shown in the table at the top of the page, which can be filtered using preset conditions at the top of the table. Additional filter options for each column using AgGrid are also available
#This page utilizes K Means Clustering to uncover any hidden patterns or structures between an animal's age and outcome type

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import dash
from dash import html, dcc
import plotly.express as px
from flask import session

#register page with Dash pages
dash.register_page(__name__,path='/KMeansClustering', name='KMeansClustering')

#Import CRUD module
from animal_shelter import AnimalShelter

def layout():
    #Connect to session and MongoDB database
    username = session.get('username')
    password = session.get('password')
    
    if not username or not password:
        return html.Div("Unauthorized acces. Please log in.", style={'color':'red'})
    
    db = AnimalShelter(username, password, 'localhost', 27017, 'AAC', 'animals')
    
    data = pd.DataFrame.from_records(db.read({"age_upon_outcome_in_weeks": {"$ne": None}, "outcome_type": {"$ne": None}}))
    if '_id' in data.columns:
        data.drop(columns=['_id'],inplace=True)   

    
    #read and drop any empty relevant columns
    X = data[["age_upon_outcome_in_weeks", "outcome_type"]].dropna()
    
    #encode outcome_type as numeric
    X["outcome_type_encoded"] = X["outcome_type"].astype("category").cat.codes
    
    X_encoded = X[["age_upon_outcome_in_weeks", "outcome_type_encoded"]].copy()
    
    #number of clusters
    K = 3

    Centroids = X_encoded.sample(n=K).reset_index(drop=True)
    
    diff = 1
    j = 0
    
    #assigns all points to the closest cluster centroid and recomputes centroids of newly formed centroids
    while(diff != 0):
        XD = X_encoded.copy()
        i = 1
        for index1, row_c in Centroids.iterrows():
            ED = []
            for index2, row_d in XD.iterrows():
                d1 = (row_c["outcome_type_encoded"] - row_d["outcome_type_encoded"])**2
                d2 = (row_c["age_upon_outcome_in_weeks"] - row_d["age_upon_outcome_in_weeks"])**2
                d = np.sqrt(d1+d2)
                ED.append(d)
            X[i] = ED
            i = i + 1
    
        C=[]
        for index, row in X.iterrows():
            min_dist = row[1]
            pos = 1
            for i in range(K):
                if row[i + 1] < min_dist:
                    min_dist = row[i + 1]
                    pos = i + 1
            C.append(pos)
        X_encoded.loc[:, "Cluster"] = C
        Centroids_new = X_encoded.groupby(["Cluster"]).mean()[["age_upon_outcome_in_weeks", "outcome_type_encoded"]]
        if j == 0:
            diff = 1
            j = j+ 1
        else:
            diff = (Centroids_new['age_upon_outcome_in_weeks'] - Centroids['age_upon_outcome_in_weeks']).sum() + (Centroids_new['outcome_type_encoded'] - Centroids['outcome_type_encoded']).sum()
            print(diff.sum())
        Centroids = X_encoded.groupby(["Cluster"]).mean()[["age_upon_outcome_in_weeks", "outcome_type_encoded"]]

    X_encoded["outcome_type"] = X["outcome_type"]
    
    #Visualize the data and revert labels back to category names       
    fig = px.scatter (
        X_encoded,
        x = "outcome_type_encoded",
        y = "age_upon_outcome_in_weeks",
        color = X_encoded["Cluster"].astype(str),
        title = "Outcome Type - K Means Clustering",
        labels = {"age_upon_outcome_in_weeks": "Age Upon Outcome In Weeks", "outcome_type": "Outcome Type"},
        color_discrete_sequence = ["#1f77b4", "#2ca02c", "#9467bd"]
    )

    category_labels = dict(enumerate(X["outcome_type"].astype("category").cat.categories))

    fig.add_scatter(
        x = Centroids["outcome_type_encoded"],
        y = Centroids ["age_upon_outcome_in_weeks"],
        mode = 'markers',
        marker = dict(color='red', symbol = 'x'),
        name = 'Centroids'
    )

    fig.update_layout(
        xaxis_title = "Outcome Type",
        title_x = 0.5,
        xaxis = dict(
            tickmode = 'array',
            tickvals = list(range(len(category_labels))),
            ticktext = list(category_labels.values())
        )
    )

    return html.Div([
        dcc.Graph(figure=fig)
    ])