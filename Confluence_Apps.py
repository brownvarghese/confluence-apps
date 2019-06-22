import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
import os

#CSV to JSON Conversion
Apple_DataCSV = os.path.join("Resources", "Apple_data_ext_trf.csv") 
# Read in the CSV file
with open(Apple_DataCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.Apple_Data
    db.segment.drop()
    header= ['','App_Name','App_Size','currency','App_Price','Type','Review_count','User_Rating','Content_Rating','Category']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)

#CSV to JSON Conversion
Google_DataCSV = os.path.join("Resources","Google_data_ext_trf.csv") 
# Read in the CSV file
with open(Google_DataCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.Android_Data
    db.segment.drop()
    header= ['','App_Name','App_Size','currency','App_Price','Type','Review_count','User_Rating','Content_Rating','Category']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)

#CSV to JSON Conversion 
App_sumCSV = os.path.join("Resources","asdata_sum.csv") 
# Read in the CSV file
with open(App_sumCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.App_sumCSV
    db.segment.drop()
    header= ['App_Store','Category','Type','Content_Rating','Avg_App_Price','Avg_Review_Count','Avg_User_Rating']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)

#CSV to JSON Conversion 
goog_sumCSV = os.path.join("Resources","gpsdata_sum.csv") 
# Read in the CSV file
with open(goog_sumCSV, 'r') as csvfile:
    reader = csv.DictReader( csvfile )
    mongo_client=MongoClient() 
    db= mongo_client.Confluence_Apps.goog_sumCSV
    db.segment.drop()
    header= ['App_Store','Category','Type','Content_Rating','Avg_App_Price','Avg_review_count','Avg_User_Rating']

    for each in reader:
        row={}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)
