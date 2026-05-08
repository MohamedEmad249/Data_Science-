-------------------------------------------------US Traffic Accidents Analysis (CO & OK)--------------------------------------------------------
Overview

This project is part of the AINE 312 Term Project. The goal of the project is to analyze traffic accident data from the United States using Python. For this analysis, the dataset was filtered to only include accidents from:

Colorado (CO)
Oklahoma (OK)

The project includes:

Data cleaning
Statistical analysis
Data visualization
Data storytelling

The analysis focuses on how weather conditions, time patterns, and road infrastructure affect accident severity.

Dataset

The original dataset was taken from the US Accidents dataset available on Kaggle.

Dataset Link on Kaggle:
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

After filtering:

Total rows: ~174,000
States used:
Colorado (CO)
Oklahoma (OK)

The dataset contains:

Accident severity
GPS coordinates
Weather information
Time information
Road features
Traffic infrastructure indicators
Data Cleaning

The following preprocessing steps were applied:

Converted date/time columns to datetime format
Created accident duration feature
Removed invalid duration values
Filled missing numerical values using median
Filled missing categorical values using mode
Removed duplicate rows
Removed outliers using IQR method
Standardized weather condition labels
Statistical Analysis

The project includes:

Mean
Median
Standard deviation
Quartiles
Correlation analysis

Visualizations were created for:

Severity distribution
Weather conditions
Day vs Night accidents
Hourly accident trends
Junction and traffic signal effects
Main Findings

Some important observations from the analysis:

Colorado has more severe accidents than Oklahoma
Night accidents tend to be more severe
Rain and snow increase accident severity
Junctions are associated with higher accident severity
Traffic signals appear to reduce severe outcomes
Most accidents happen during rush hours

libraries Used:

Pandas
NumPy
Matplotlib
Seaborn

How to RUN:
Install required libraries:
RUN this command in the terminal========================>
pip install pandas numpy matplotlib seaborn
============================================
Then RUN==> python Filter.py
RUN==> python Cleaning.py
And  RUN==> python Statistical Analysis.py
Chart of Severity.py is a tepical Charts File you can run at the end to see the representations
=================================================================================================
NOTES:
Some columns had missing values and were cleaned during preprocessing.
The dataset only includes reported accidents.
The analysis is intended for educational purposes.
=================================================================================================
Author:
Mohamed Emadeldin
Data Science – Spring 2025/26
------------------------------------------------------------------------------------------------------------------------------------------------