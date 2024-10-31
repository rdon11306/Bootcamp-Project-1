# AI Bootcamp - Project 1.  Investigating the impact of weather and influenza as well as population growth

## Table of Contents
*  [**Background**](#background)
*  [**Data Source**](#data-source)
*  [**Files**](#files)
*  [**Technical Requirements**](#technical-requirements)
*  [**Run the code**](#run-the-code)
*  [**Credits**](#credits)

## Background
The goal of this project is to perform an analysis on weather data combined with influenza hospitalization data and census data.  All data sets are specific to Columbus, Cleveland, and Cincinnati Ohio. This Exploratory Data Analysis (EDA) looks at data on the three topics for the three cities. The goal is to determine if there are any discernible patterns or relationships contained within the data. 

### EDA Questions/Topic
#### Data explored is for Columbus, Cleveland, and Cincinnati
1. Do the number of influenza hospitalizations rise with falling temperatues?
2. Does the weather data show a warming trend over 40 years?
3. Are weather trends related to population growth/decrease?

## Data Source

[Ohio Weather for Columbus, Cincinnati, and Cleveland](https://openweathermap.org/)

[Ohio influenza data](https://odh.ohio.gov/know-our-programs/seasonal-influenza/ohio-flu-activity/ohio-flu-activity)

[Ohio Census data](https://data.census.gov/)

## Files

Ohio Influenza Hospitalizations, [ohio_influenza.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/ohio_influenza.csv)

Columbus Ohio Weather, [columbus.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/columbus.csv)

Cincinnati Ohio Weather, [cincinnati.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/cincinnati.csv)

Cleveland Ohio Weather, [cleveland.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/cleveland.csv)

Ohio Census 2000-2010, [census_2000-2010.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/census_2000-2010.csv)

Ohio Census 2010-2019, [census_2010-2019.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/census_2010-2019.csv)

Ohio Census 2020-2023, [census_2020-2023.csv](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/data/census_2020-2023.csv)

Influenza & Weather jupyter notebook [influenza_analysis.ipynb](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/influenza_analysis.ipynb)

Census analysis jupyter notebook [census_analysis.ipynb](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/census_analysis.ipynb)

Weather trend analysis jupyter notebook [ryans project.ipynb](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/ryans%20project.ipynb)

This repository contains three directories: data, util, and oldfiles. The `data` directory contains various files that hold the data that the team obtained for the project. The `util` directory contains some utility code that may or maynot be used within the project. The `oldfiles` directory contains files that were created as part of the project but not used in the final solution (they were kept for historical purposes and just in case team members wanted to go back and look at old code).

## Technical requirements
The EDA was done using Jupyter Notebooks. This requires python (at least 3.10), Jupyter Notebooks, anaconda, pandas, matplotlib, Prophet, datetime, and the pytz.

## Run the code
The code can be executed inside of an IDE or within Google Colab. Team members all built and executed the project using Visual Studio Code. All necessary libraries are pre-installed, outside of the IDE.

All project Jupyter Nodebooks use a similar import block of code to set up projects to be able to analyze and use the data:
![Screenshot 2024-07-18 at 5 17 30 PM](https://github.com/user-attachments/assets/c259aa45-0983-49f9-ac90-d2ee39b419e5)

Each Notebook and be executed by clicking on the `Run All` button at the top of each Notebook:
![Screenshot 2024-07-18 at 5 14 46 PM](https://github.com/user-attachments/assets/7727ead6-9528-4908-b41c-477717aafb62)

The final presentation will be presented in PowerPoint.  The file can be found [here](https://github.com/brian-campbell/ai-bootcamp-project-1/blob/main/Project-1-Presentation.pptx)

## Credits
### Mike Saunders
### Ryan Donegan
### Brian Campbell

