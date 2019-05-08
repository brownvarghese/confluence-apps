import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
import os
#C:\Users\kruna\OneDrive\Documents\HOMEWORK_Dara Science BootCamp\confluence-apps\Resources
#CSV to JSON Conversion
Google_DataCSV = os.path.join("C:\\Users\kruna\OneDrive\Documents\HOMEWORK_Dara Science BootCamp\confluence-apps\Final_files\Google_data_ext_trf.csv") 
# Read in the CSV file
with open(Google_DataCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.Android_Data
    db.segment.drop()
    header= ['Serial_number','App_Name','App_Size','currency','App_Price','Type','Review_count','User_Rating','Content_Rating','Category']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)
