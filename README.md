# **GNRC Data Pipeline**

## *Table of Contents*  
+ Overview
+ APIs  
+ Data Downloads  
+ Exports and Data Storage
+ File Structure   

## Overview  

*Note:* While GNRC is a public organization and most information/data/process/sources can be made available upon request, not all information is pushed to this repository. If you are the recipient of data or analysis and have further questions about sourcing or methods please contact the Research Department.

This repository outlines the process for gathering frequently requested data through the most efficient methods and building a formatted database with rigorously documented sources and transformations. Data is integrated from public dataset APIs, staff-compiled data, and proprietary data sources, passed through a series of transformations, and stored in a SQLite database.

This process is an ETL Data Pipeline (extract, transform, and load) maintained by the GNRC research staff.

### **Extract**

## APIs or direct HTML Downloads
+ Census Bureau Decennial, Subject, TIGER, and American Community Survey  
+ Bureau of Economic Analysis various data series   
+ Bureau of Labor Statistics various data series  
+ Socrata Nashville API      

## Downloaded Data Sources  
+ Woods and Poole Projections (proprietary in raw format)  
+ Department of Housing and Urban Development Residential Permits  
+ TN State Data Center  
+ Historical Census Population  
+ Center for Neighborhood Technology Housing and Transportation Cost Burden  
+ JobsEQ Industry and Occupational Employment etc.  
+ University of Wisconsin County Health Rankings  
+ Tennessee Bureau of Investigation Incident Reports  
+ Zillow Housing Statistics  

### **Transform**

These data are aggregated to appropriate geographies, and formatted and standardized to be pulled into other projects and filtered appropriately. The primary method of transformation used at this time is simple structural adjustment made by aggregating raw data into relevant groups for analysis, as well as destructive as the decision was made not to store the raw data as it is easily re-extracted.

### **Load**  

Data are loaded into a SQLite database where the structure is maintained by research staff and transportable and available to be shared to other staff.   

## File Structure  

#### **Data Guides** (Not Pushed)  
Contains: Various lists of variables, column names, and descriptions that are imported and run through APIs to call the listed data   

#### **Notebooks**  
Contains: The following folders  

*API Pulls*: This folder contains notebooks for each respective data series and year. Variable changes between different data series are tracked and stored in the Data Guides folder, as a way to validate the points where a new data guide is needed for different years.

*Download Formatting & Transformations*: This folder contains notebooks for the data downloaded from the web or provided by GNRC staff. Internally, search for a file 'Data_Downloads_Guide.csv' with a guide to all data downloads, sources, last updates, notes, etc. in the Data Downloads folder. Sources include but are not limited to:    
+ Woods & Poole proprietary population, households, and industry employment projections    
+ Center for Neighborhood Technology Housing & Transportation Cost Burden  
+ Census Bureau historical population  
+ Zillow  
+ Internal vehicular crash tracking  
+ Tennessee Bureau of Investigation  
+ University of Wisconsin County Health Rankings  
+ JobsEQ various datasets  

*API Sourced Transformations*: This folder contains notebooks transforming the raw data into frequently requested metrics. Note that the subject tables, ACS 1YRs, and TIGER files are currently transformed in the "pull" documents because of their brevity. The download formatting documents bring the data to this point as well.  

Contains: The following files  

**geodicts.py**: custom module containing lists of FIPS codes to filter relevant geographies, as well as dictionaries to convert full Census geography names to commonly used names, and to tag either geography name with a full geographic ID.    

#### **Data** (Not Pushed)  
Contains: The data that is pulled and ready to be run through transformations stored as feather files to optimize space.     

#### **Database** (Not Pushed)  
Contains: SQLite database with common GEO_ID field for Comprehensive Plans, data requests, etc.

*The "data" and "outputs" folders can be empty if storage space is needed, and then duplicated with the notebook files at anytime.*
