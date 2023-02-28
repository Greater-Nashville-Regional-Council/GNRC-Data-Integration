# **Parent-Data-Gathering**

## *Table of Contents*  
+ Overview
+ APIs  
+ Data Downloads  
+ Exports and Data Storage
+ File Structure   

## Overview  

*Note:* While GNRC is a public organization and most information/data/process/sources can be made available upon request, not all information is pushed to this repository. If you are the recipient of data or analysis and have further questions about sourcing or methods please contact the Research Department.

This repository outlines the process for gathering frequently requested data through the most efficient methods and building a formatted database with rigorously documented sources and transformations.

 In addition to data retrieved through public APIs by passing variable lists (stored elsewhere) consistent with changing variables YoY, data that must be downloaded from the internet or shared by staff is formatted uniformly here and transformations are tracked from the format in which these downloads arrive.  

## APIs or HTML Downloads
+ Census Bureau Decennial, Subject, and American Community Survey  
+ Census TIGER Files
+ Bureau of Economic Analysis GDP and Industry Employment    
+ Bureau of Labor Statistics LAUS    

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

## Formatting, Calculations, Exports and Data Storage  
As this process is developed as an outline for all data pulls and formatting, exports from API calls and download formatting are standardized and stored to be pulled into other projects and filtered appropriately. Frequently used formatting/calculations from raw data are performed for all geographies in the GNRC region and many adjacent geographies simultaneously. The raw data is catalogued, but can dropped at this point in a storage pinch. For every data source and year, requested data points are accumulated here over time. All files are available to be catalogued, or deleted and reproduced using the same process when needed for other projects for storage efficiency.

## File Structure  

#### **Data Guides** (Not Pushed)  
Contains: Various lists of variables, column names, and descriptions that are imported and run through APIs to call the listed data   

#### **Notebooks**  
Contains: The following folders  

*API Pulls*: This folder contains notebooks for each respective data series and year. Accepting the ACS 1YR estimates, each has its own data guide. The 1YRs are not large amounts of data and currently the variables are all the same year over year, if more data is added from these estimates they will be split as well.  
+ ACS 2010 5YR  
+ ACS 2020 5YR  
+ ACS 2021 5YR
+ ACS 2017 1YR  
+ ACS 2018 1YR  
+ ACS 2019 1YR  
+ ACS 2021 1YR  
+ Decennial 2020 PL  
+ Decennial 2000 SF1  
+ Decennial 2010 SF1  
+ Decennial 2000 SF3  
+ Subject Tables 2010, 2020 5YR  
+ TIGER Files 2000, 2010, 2020  

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

#### **Outputs** (Not Pushed)  
Contains: Formatted data that is ready to be pulled into other projects/repositories & central database for filtering and analysis also as feather files to optimize space.

*The "data" and "outputs" folders can be empty if storage space is needed, and then duplicated with the notebook files at anytime.*
