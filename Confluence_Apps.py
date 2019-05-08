import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
import os

#CSV to JSON Conversion
Apple_DataCSV = os.path.join("C:\\Users\kruna\OneDrive\Documents\HOMEWORK_Dara Science BootCamp\confluence-apps\output\Apple_data_ext_trf.csv") 
# Read in the CSV file
with open(Apple_DataCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.Apple_Data
    db.segment.drop()
    header= ['Serial_number','App_Name','App_Size','currency','App_Price','Type','Review_count','User_Rating','Content_Rating','Category']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)

#CSV to JSON Conversion
Google_DataCSV = os.path.join("C:\\Users\kruna\OneDrive\Documents\HOMEWORK_Dara Science BootCamp\confluence-apps\output\Google_data_ext_trf.csv") 
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

#CSV to JSON Conversion 
Appgoog_sumCSV = os.path.join("C:\\Users\kruna\OneDrive\Documents\HOMEWORK_Dara Science BootCamp\confluence-apps\output\Apple-Google_Summary.csv") 
# Read in the CSV file
with open(Appgoog_sumCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.Apple_Google_Summary
    db.segment.drop()
    header= ['App_Store','Category','Type','Content_Rating','Avg_App_Price','Avg_review_count','Avg_User_Rating']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)


