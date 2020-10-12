# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 07:11:21 2020

@author: The Ayushie Sharma
"""

import pandas as pd


#!pip install Dash
import dash
import dash_html_components as html
#from   dash.dependencies import Input, Output
#import dash_core_components as dcc
#import plotly.graph_objects as go
#import plotly.express as px

import webbrowser


#this is the place for creating global variables for dash
app = dash.Dash()  #here app is by deafault a global variable and Dash is a class in a dash library

#defining of your function load_data
def load_data():
    
    dataset_name = "global_terror1.csv"
    #df is a local variable
    global df    
    df = pd.read_csv(dataset_name)
    
def create_app_ui():
    main_layout = html.Div()
    return main_layout

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    """
    global month_list
    month = {
             "January":1,
             "February":2,
             "March":3,
             "April":4,
             "May":5,
             "June":6,
             "July":7,
             "August":8,
             "September":9,
             "October":10,
             "November":11,
             "December":12
        
             }
    
   
    month_list = [{"label":key,"value":values} for key, values in month.items()]
    
    global date_list
    date_list = [x for x in range (1, 32)]
    
    global region_list
    
    region_list = [{'label':str(i), 'value':str(i)} for i in sorted(df['region_txt'].unique().tolist())]
     
    
    global attack_type_list
    
    attack_type_list = [{'label':str(i), 'value':str(i)} for i in sorted(df['attacktype1_txt'].unique().tolist()) ]           
   
    global year_list
    year_list = sorted (df['iyear'].unique().tolist())   
    
    global year_dict
    year_dict = { str(year):str(year)  for year in year_list }
    
    """
    
    
    



 #Main function   
def main(): 

    print("Starting the main function")
 
    #calling_functions
    
    load_data()

    open_browser()
   
    
#layout controls the UI and Callback controls the Action

    global app
    app.layout = create_app_ui()
    app.title = "Terrorism Analysis with Insights"
    app.run_server()
#don't write any statement after run_server function because it will cause no effect to the program
    df = None
    app = None
    print("Ending the main function")

   
   
if __name__ == '__main__':
    print("Starting the Project")
    main()
    print("Ending the Project")    