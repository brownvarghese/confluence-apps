# Confluence Apps

## A Rutgers 2019 Data Engineering and Visualization ETL Project

### Brown Varghese, Krunal Panchal, Radha Mahalingam

## Quick Summary

The ever-changing mobile landscape is a challenging space to navigate.  The percentage of mobile over desktop is only increasing. Android holds about 53.2% of the smartphone market, while iOS is 43%. To get more people to download various app, we need to make sure the consumers can easily find the apps that they need. We offer an ETL pipeline that assists young Adults and Parents to make an informed choice to buy/download free/paid mobile/tablet apps from Apple store or Google Play Store. The source data obtained are from two different data sources in Kaggle. At the end of the ETL process, we provide our data in a NoSQL database (Mongo DB) which exposes, for different categories/genres, type (free/paid) and content ratings, the KPIs to determine which app store for various categories will deliver the most value to the Mobile apps consumers. This current version is focused towards data from Google and Apple App stores but can be extended to include other app stores in future. This ETL pipeline will be the backbone to build a mobile app analytics platform in future – an intuitive and user-friendly front end to help consumers as well as producers.

### Steps to run the Pipeline

    1.	Make sure the downloaded files - googleplaystore.csv and appleStore.csv are stored in ‘Resources’ folder in the pwd (current working directory).
    2.	From pwd, run Jupyter Notebook.
    3.	Select Apps_Data_Extract.ipynb and run the script.
    4.	Select Apps_Data_transformation.ipynb and run the script
    5.	To load the CSV generated from programs above we will need to run following python script. This will require following steps
        a.	Make sure MongoDB Compass is installed
        b.	Launch mongod on Gitbash.
        c.	Launch Terminal or command line to run the python file mentioned below:
        i.	Confluence_Apps.py
        d.	Once script has run to success launch MongoDB Compass
        e.	Now you should  be able to see following DB and collections:
                    
            •	Database:
            Confluence_Apps

            •	Collections: 
            Android_Data.segment
            Apple_Data.segment
            Apple_Google_Summary.segment

## Narrative / Motivation

We are providing a Database for the Mobile apps consumers – especially young adults and parents to make informed decisions about what apps to buy / download for various categories of apps from Google Play Store and Apple store, based on apps price, user rating and number of users (installs).
Final Schema / Data Model / How to use the data
The process of data extraction and data transformation resulted in the following final data model, which was loaded on NoSQL database – Mongo DB. This data could have been loaded in a relational database like MySQL, as well.  But we choose to go with Mongo DB, because of the following reasons:

        1.	We wanted to learn more Mongo DB as we did not have prior experience.
        2.	We believe that in future, there will be document types (rows), which will hold unstructured data fields representing the mobile apps.  NoSQL database will come handy in those situations.

The details are provided as follows.

Google Play Store App Details(Android_Data.segment):  This collection in Mongo DB represents the Google Play Store App Details, after data cleaning and data wrangling.

Apple Store App Details(Apple_Data.segment):  This collection in Mongo DB represents the Apple Store App Details, after data cleaning and data wrangling.

Data Table Structure for Android and Apple Data Collection:

![](/images/image1.png)

Apps Summary Details(Apple_Google_Summary.segment): This collection in Mongo DB represents the aggregated summary level details of apps, grouped at the level of App Store/Category / Type / Content Rating.  This provides valuable analytics like average user ratings, average price and Average users at an aggregate level.

Data Table Structure for Android and Google Summary Data collection:

![](/images/image2.png)

### How to use the data?

The users are expected to query the Apps Summary Details(Apple_Google_Summary.segment) collection in Mongo DB by providing Category / Type / Content rating.  They will be presented with potentially two documents (rows) representing Apple store and Google Play Store. Based on the details provided like Average App Price, Average review count and Average review count, the users can elect to explore apps details either from Apple store (Apple Store App Details (Apple_Data.segment) or Google Play Store (Google Play Store App Details (Android_Data.segment).  In our view, this is supposed to provide a one-stop shop for comparing apps between Apple Store and Google Play Store based on apps popularity and cost effectiveness, which should aid the users to make determination to buy/download appropriate apps.

## Data Sources

We considered two datasets in .csv form from Kaggle on mobile apps from Google Play Store and Apple Store, each of which captured top 7000 to 9000 mobile apps, covering various categories. In the Kaggle site, these data datasets are infrequently updated, the latest update happened in March 2019.   These data sets allowed us to build KPIs around average user ratings and average number of users (KPIs representing popularity of apps) and average price (KPI representing cost effective apps) aggregated at various categories/content rating level.  

The structure of the input source datasets are as follows:

![](/images/image3.png)

## Transformation Step

In order to build our final collections/database, we had to perform the following data cleaning and data transformation activities:

### Data Cleaning steps performed [Apps_Data_Extract.ipynb]:

1.	Visual inspection of data 
2.	Verified the file contents with the head () method. 
3.	Dealt with missing data 
    a.	Dropped columns that have a high incidence of missing data
    b.	Added in default value for the missing columns
    c.	Invoked Lambda function to replace any values other than Alphanumeric and special characters with SPACES. Application_Name field contained nonstandard characters as some of the apps were intended for non-English speaking audience. This step allowed further processing of file in Transform and Load processes.  
4.	Removed incomplete rows
    a.	Deleted any rows that have a missing value. This will avoid errors in the Transformation and Load process.
    b.	Based on the utility of the final database, the structures of Apple app dataset and Google app dataset are aligned by bringing only selective columns into the dataframe.
5.	Normalized data types
    a.	Formatting columns to appropriate data type for father processing in Transformation and Load process. 
    b.	Type ()
6.	Renamed columns
    a.	Rename columns to more user-friendly names. DataFrame.rename(columns = {})
7.	Saved results
    a.	After data clean-up, exported data back into CSV format for further processing in another program


###Data transformation steps performed [Apps_Data_transformation.ipynb]:

1.	The Apps categorization between Apple Store and Google Play Store was different. Realigned Google Play Store ‘Category’ column based on Apple Store Category by executing  .replace command. See an example as follows:

    gps_data['Category'].replace('BEAUTY', 'LIFESTYLE',inplace=True)

2.	The Apps ‘Content Rating’ between Apple Store and Google Play Store was different. Realigned Google Play Store ‘Content Rating’ column based on Apple Store Content Rating by executing  .replace command. See an example as follows:

    gps_data['Content_Rating'].replace('Adults only 18+', '17+', inplace=True)

3.	In order to align with Google Play Store data, using a Lambda function, updated the ‘Type’ column in the Apple Store Apps data  as ‘Free or Paid’, based on the App Price = 0 or not respectively.

4.	Executed an aggregation function using NumPy on both Apple Store and Google Play Store Apps data to arrive at summary level detail for Average Price, Average User Rating and Average Rating Count.  This aggregation was done at Category / Type / Content Rating.  Here is the example:

    gps_data2=pd.pivot_table(gps_data1, index=['App_Store','Category','Type', 'Content_Rating'],values=['App_Price','User_Rating','Review_count'],aggfunc = np.average)

5.	After these transformations, exported the transformed Apps Detail files as well as Apps Summary files (for both Apple Store and Google Play Store) back into a .csv file format.  These files were processed as input part of the ‘Load’ process.


## Project Plan

![](/images/image4.png)
