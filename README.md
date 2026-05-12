# DSBDA - Problem Statements

This repository contains all problem statements for the **Distributed Systems and Big Data Analytics (DSBDA)** course. The problems are organized by technology and domain.

---

## Table of Contents
1. [MapReduce & Hadoop Applications (PS 1-5)](#mapreduce--hadoop-applications-ps-1-5)
2. [HBase & HiveQL Applications (PS 6-8)](#hbase--hiveql-applications-ps-6-8)
3. [Python Data Manipulation (PS 9-12)](#python-data-manipulation-ps-9-12)
4. [Python Data Cleaning & Machine Learning (PS 13-16)](#python-data-cleaning--machine-learning-ps-13-16)
5. [Python Data Visualization (PS 17-18, 21-22)](#python-data-visualization-ps-17-18-21-22)
6. [Tableau Data Visualization (PS 19-20, 23)](#tableau-data-visualization-ps-19-20-23)
7. [Python Advanced Data Operations (PS 24-26)](#python-advanced-data-operations-ps-24-26)
8. [Web Scraping Applications (PS 27-30)](#web-scraping-applications-ps-27-30)

---

## MapReduce & Hadoop Applications (PS 1-5)

### PS 1: Log File Analysis
**Objective:** Design a distributed application using MapReduce which processes a log file of a system.
- List out the users who have logged for the maximum period on the system
- Use simple log file from the Internet
- Process using pseudo distribution mode on Hadoop platform

### PS 2: Word Frequency Count
**Objective:** Design and develop a distributed application to find frequency of words from sample text data.
- Use sample text data
- Process using MapReduce
- Count occurrences of each word

### PS 3: Music Dataset - Listeners & Shares
**Objective:** Design a distributed application using MapReduce which processes Music dataset.
- List the number of unique listeners
- Count number of times the track was shared with others
- Process using pseudo distribution mode on Hadoop platform

### PS 4: Music Dataset - Radio & Skip Analysis
**Objective:** Design a distributed application using MapReduce which processes Music dataset.
- List the number of times the track was listened on Radio
- Count number of times the track was skipped
- Process using pseudo distribution mode on Hadoop platform

### PS 5: Movie Recommendation System
**Objective:** Design a distributed application using MapReduce which processes Movie dataset.
- Recommend movies based on user ratings
- Process using pseudo distribution mode on Hadoop platform

---

## HBase & HiveQL Applications (PS 6-8)

### PS 6: Flight Information System (HBase & HiveQL)
**Objective:** Write an application using HBase and HiveQL for flight information system.

**Tasks:**
- a. Create Flight Info HBase Table (Flight information, schedule, and delay)
- b. Demonstrate Creating, Dropping, and Altering Database tables in HBase
- c. Create external Hive table to connect to HBase for Flight Information Table
- d. Find the total departure delay in Hive
- e. Find the average departure delay in Hive
- f. Create index on Flight Information Table

### PS 7: Customer Information System (HBase & HiveQL)
**Objective:** Write an application using HBase and HiveQL for Customer information system.

**Tasks:**
- a. Create tables: Customer_info (Cust-ID, Cust-Name, OrderID), order_info (OrderID, ItemID, Quantity), item_info (Item-ID, Item-Name, ItemPrice)
- b. Load tables with data from local storage in Hive
- c. Perform Join operations between tables in Hive
- d. Create Index on Customer information system in Hive
- e. Find total and average sales in Hive
- f. Find Order details with maximum cost
- g. Create external Hive table to connect to HBase
- h. Display records of Customer Information Table in HBase

### PS 8: Online Retail Dataset (HBase & HiveQL)
**Objective:** Write an application using HBase and HiveQL for OnlineRetail Dataset.

**Tasks:**
- a. Create and Load table with Online Retail data in Hive
- b. Create Index on Online Retail Table in Hive
- c. Find total and average sales in Hive
- d. Find Order details with maximum cost
- e. Find Customer details with maximum order total
- f. Find Country with maximum and minimum sale
- g. Create external Hive table to connect to HBase
- h. Display records of OnlineRetail Table in HBase

---

## Python Data Manipulation (PS 9-12)

### PS 9: Facebook Metrics Dataset Operations
**Objective:** Perform the following operations using Python on Facebook metrics dataset.
- a. Create data subsets for type of post
- b. Merge two subsets
- c. Sort Data on Page total likes
- d. Transposing Data
- e. Melting Data to long format
- f. Casting data to wide format

### PS 10: Iris Dataset Operations
**Objective:** Perform the following operations using Python on Iris dataset.
- a. Create data subsets for different species
- b. Merge two subsets
- c. Sort Data on Petal Length
- d. Transposing Data
- e. Melting Data to long format
- f. Casting data to wide format

### PS 11: Movie Dataset Operations
**Objective:** Perform the following operations using Python on Movie dataset.
- a. Create data subsets for different languages (Original Language)
- b. Merge two subsets
- c. Sort Data using customer ratings
- d. Transposing Data
- e. Melting Data to long format
- f. Casting data to wide format

### PS 12: Census Bureau Dataset (Adult Dataset) Operations
**Objective:** Perform the following operations using Python on census bureau dataset (Adult dataset).
- a. Create data subsets for different Country, Sex, Race
- b. Merge two subsets
- c. Sort Data using customer ratings
- d. Transposing Data
- e. Melting Data to long format
- f. Casting data to wide format

---

## Python Data Cleaning & Machine Learning (PS 13-16)

### PS 13: Heart Diseases Dataset Analysis
**Objective:** Perform the following operations using Python on Heart Diseases dataset.
- a. Data cleaning (Remove NA, ?, Negative values, etc.)
- b. Error correcting (Outlier detection and removal)
- c. Data transformation
- d. Build Data model using regression and kNN methods and compare accuracy of heart disease prediction

### PS 14: Iris Dataset ML Analysis
**Objective:** Perform the following operations using Python on Iris dataset.
- a. Data cleaning (Remove NA, ?, Negative values, etc.)
- b. Error correcting (Outlier detection and removal)
- c. Data transformation
- d. Build Data model using regression and Naïve Bayes methods and compare accuracy of Iris Species Prediction

### PS 15: Breast Cancer Dataset Analysis
**Objective:** Perform the following operations using Python on Breast Cancer dataset.
- a. Data cleaning (Remove NA, ?, Negative values, etc.)
- b. Error correcting (Outlier detection and removal)
- c. Data transformation
- d. Build Data model using regression and Naïve Bayes methods and compare accuracy of benign and malignant tumors

### PS 16: Census Bureau Dataset (Adult Dataset) Classification
**Objective:** Perform the following operations using Python on census bureau dataset (Adult dataset).
- a. Data cleaning (Remove NA, ?, Negative values, etc.)
- b. Error correcting (Outlier detection and removal)
- c. Data transformation
- d. Build Data model using regression and Naïve Bayes methods for income category prediction (>=50k or <=50k) and compare accuracy

---

## Python Data Visualization (PS 17-18, 21-22)

### PS 17: Heart Disease Dataset Visualization - Set 1
**Objective:** Visualize the Heart disease dataset by plotting the following graphs using Python. (Define objective for every graph)
- a. Histograms
- b. Dot Plots
- c. Bar Plots
- d. Line Charts
- e. Add Histogram and Scatter plot to box plot

### PS 18: Heart Disease Dataset Visualization - Set 2
**Objective:** Visualize the Heart disease dataset by plotting the following graphs using Python. (Define objective for every graph)
- a. Histograms
- b. Pie Charts
- c. Box Plots
- d. Scatter Plots
- e. Add boxplots to a scatterplot

### PS 21: Census Bureau Dataset (Adult Dataset) Visualization - Set 1
**Objective:** Visualize the census bureau dataset (Adult dataset) by plotting the following graphs using Python. (Define objective for every graph)
- a. Histograms
- b. Dot Plots
- c. Bar Plots
- d. Line Charts
- e. Add Histogram and Scatter plot to box plot

### PS 22: Census Bureau Dataset (Adult Dataset) Visualization - Set 2
**Objective:** Visualize the census bureau dataset (Adult dataset) by plotting the following graphs using Python. (Define objective for every graph)
- a. Histograms
- b. Pie Charts
- c. Box Plots
- d. Scatter Plots
- e. Add boxplots to a scatterplot

---

## Tableau Data Visualization (PS 19-20, 23)

### PS 19: Retail Dataset Visualization - Set 1
**Objective:** Perform data visualization operations using Tableau to get answers to various business questions on Retail dataset.
- a. Find and Plot top 10 products based on total sale
- b. Find and Plot product contribution to total sale
- c. Find and Plot month wise sales in year 2010 in descending order
- d. Find and Plot most loyal customers based on purchase order
- e. Find and Plot yearly sales comparison
- f. Find and Plot country wise total sales price and show on Geospatial graph

### PS 20: Retail Dataset Visualization - Set 2
**Objective:** Perform data visualization operations using Tableau to get answers to various business questions on Retail dataset.
- a. Find and Plot country wise popular product
- b. Find and Plot bottom 10 products based on total sale
- c. Find and Plot top 5 purchase orders
- d. Find and Plot most popular products based on sales
- e. Find and Plot half yearly sales for the year 2011
- f. Find and Plot country wise total sales quantity and show on Geospatial graph

### PS 23: Census Bureau Dataset (Adult Dataset) Tableau Visualization
**Objective:** Perform data visualization operations using Tableau to get answers to various questions on the census bureau dataset (Adult dataset).
- a. Find and Plot Income class of People whose education is master's and doctorate
- b. Find and Plot Income class of people who have private jobs
- c. Find and Plot yearly sales comparison
- d. Find and Plot country wise statistics on Geospatial graph
- e. Plot agewise- education vs salary statistics
- f. Plot Countrywise male female ratio
- g. Plot Income class based on workclass (Government and other)

---

## Python Advanced Data Operations (PS 24-26)

### PS 24: ForestFires Dataset Operations
**Objective:** Perform the following operations using Python on ForestFires Dataset.
- a. Create data subsets by making classes for amount of region affected (e.g., NotAffected, Partially affected, Mostly affected)
- b. Merge two subsets
- c. Sort Data using Temperature, Wind, and Area
- d. Transposing Data
- e. Melting Data to long format
- f. Casting data to wide format

### PS 25: Hepatitis Dataset Operations
**Objective:** Perform the following operations using Python on Hepatitis Dataset.
- a. Create data subsets for different sex
- b. Merge two subsets
- c. Sort Data using age, SGOT, PROTIME
- d. Transposing Data
- e. Melting Data to long format
- f. Casting data to wide format

### PS 26: Hepatitis Dataset ML Analysis
**Objective:** Perform the following operations using Python on Hepatitis dataset.
- a. Data cleaning (Remove NA, ?, Negative values, etc.)
- b. Error correcting (Outlier detection and removal)
- c. Data transformation
- d. Build Data model using regression and Naïve Bayes methods for prediction class DIE, LIVE and compare accuracy Prediction

---

## Web Scraping Applications (PS 27-30)

### PS 27: Amazon Review Scraper
**Objective:** Create a review scrapper for https://store.steampowered.com/appreviews 
/730?json=1  website to fetch real time comments, reviews, ratings, comment 
tags, customer name using Python. 

### PS 28: Flipkart Review Scraper
**Objective:** Create a review scrapper for https://webscraper.io/test-sites/e-commerce 
/static website to fetch real time comments, reviews, ratings, comment tags, 
customer name using Python. 

### PS 29: Myntra Review Scraper
**Objective:** Create a review scrapper for PICT-Top Engineering College website to fetch real 
time comments, reviews, ratings, comment tags, customer name using Python.

### PS 30: AJIO Review Scraper
**Objective:** Create a review scrapper for books.toscrape.com website to fetch real time 
comments, reviews, ratings, comment tags, customer name using Python.

---

## Summary Statistics

| Category | Problem Statements | Count |
|----------|-------------------|-------|
| MapReduce & Hadoop | PS 1-5 | 5 |
| HBase & HiveQL | PS 6-8 | 3 |
| Python Data Manipulation | PS 9-12 | 4 |
| Python Data Cleaning & ML | PS 13-16 | 4 |
| Python Data Visualization | PS 17-18, 21-22 | 4 |
| Tableau Data Visualization | PS 19-20, 23 | 3 |
| Python Advanced Operations | PS 24-26 | 3 |
| Web Scraping | PS 27-30 | 4 |
| **TOTAL** | | **30** |

---

## Technologies & Tools Used

### Big Data Technologies
- Apache Hadoop
- MapReduce
- HBase
- Apache Hive
- HiveQL

### Data Analysis & Visualization
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Tableau
- Machine Learning (Scikit-learn, Regression, Naive Bayes, kNN)

### Web Scraping
- Python (BeautifulSoup, Selenium, Requests)

### Datasets Used
- Facebook Metrics Dataset
- Iris Dataset
- Movie Dataset
- Adult/Census Bureau Dataset
- Heart Diseases Dataset
- Breast Cancer Dataset
- ForestFires Dataset
- Hepatitis Dataset
- Online Retail Dataset
- Flight Information Data
- Customer Information Data

---

## Notes

- All MapReduce applications should use **Pseudo Distribution Mode** on Hadoop platform
- All data manipulation operations include: subsetting, merging, sorting, transposing, melting, and casting
- Machine Learning models should compare accuracy across different algorithms
- Web scrapers should fetch real-time data with ethical considerations
- All visualizations should include defined objectives

