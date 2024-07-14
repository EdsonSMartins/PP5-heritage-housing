# Heritage Housing Issues

![I am responsive image]()

## Table of Contents
- [Introduction](#introduction)
- [Business Requirements](#business-requirements)
- [Dataset Content](#dataset-content)
- [Hypotheses for Case Study](#hypotheses-for-case-study)
- [Mapping the business requirements to the Data Visualisations and ML tasks](#mapping-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
    + [Predict House Sales Prices](#predict-house-prices-in-ames--iowa)
- [Dashboard Design](#dashboard-design)
- [Testing](#testing)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Technologies](#technologies)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## Introduction
This is the fifth project portfolio developed during the Code Institute's Full Stack Developer program. 

The project purpose is to build build a Data App with a Machine Learning User Interface (UI) combining: (1) Python packages for Machine Learning, Data Analysis and Data Visualisations; and (2) Streamlit for fast Machine Learning prototyping. 

The Maching Learning and Data Analysis toolkit is applied to a real estate data set and developed with the specific purpose to allow a user to predict the portencial sales price of a property based on certain features of the home.

## Business Requirements

A client who has received an inheritance of four properties from a deceased great-grandfather located in Ames, Iowa, has requested help in maximising the sales price for the inherited properties.

The client has an excellent understanding of property prices in her own state and residential area, but she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and has provided it for this project.

The client expectations are:

1 - Discovering how the house attributes correlate with the sale price. There is an expectation for data visualisations of the correlated variables against the sale price to confirm.
  
2 - Predicting the house sale price of the four inherited houses including any other residential properties in Ames, Iowa, based on the most important features of the homes. The predictive model should aim to acchieve an R2 value of 0.8 or higher.

3 - To access required information through an deplyed app that is easily accessible online and userfriendly.

User Story

User Story 1: As an end user, I want to be able to discover how features of a home correlate with the sale price, so that I can gain insight into the importance of a homes features in determining the sale price.
User Story 2: As an end user, I want to be able to determine the likely sale price of a home based on certain features, so that I can gain insight into the likely values of a given home in the area.
User Story 3: As an end user, I want to be able to access the required information easily online, so that I can find relevant information any time in a user friendly fashion.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
- We then created user stories where predictive analytics can be applied in a workplace. 
- The dataset consists of almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profiles made up of, but not limited to (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Hypotheses for Case Study
The following are the hypotheses that I have made for this project:

1. 

2. 

## Mapping the business requirements to the Data Visualisations and ML tasks

## Business Requirement 1:
Data Visualization and Correlation.

-
-
-

## Business Requirement 2:
Regression and Data Analysis.

-
-
-

## Business Requirement 3:
Online APP and Deployment.

## ML Business Case
#### Predict House Prices in Ames, Iowa

1. What are the business requirements?
    * The client wants to identify the correlation(s) between the features of a property, and the sale price of a speciic property.
    * The client wants to be able to estimate/predict the sale price of their 4 inherited houses, or any other houses in Ames, Iowa, as a cosideration for future property investments.
2. Is there any business requirement that can be answered with conventional data analysis?
    * We can use Data Analasys to identify those property features most closely correlated to the sale price of a house.
3. Does the client need a dashboard or an API endpoint?
    * The client only needs a dashboard in this instance.
4. What does the client consider as a successful project outcome?
    * A dashboard showing the most closely correlated features of a house, to the sale price.
    * The ability to estimate/predicts the sale price for the 4 inherited houses or any other house in Ames, Iowa.
5. Can you break down the project into Epics and User Stories?
    * Gathering requirements and collecting data.
    * Datacleaning, visualization and preparation.
    * Model training and optimization.
    * Dashboard designing and development.
    * Dashboard deployment.
6. Ethical or Privacy concerns?
    * As the data is a public data set, there are not concerns.
7. Does the data suggest a particular model?
    * The data suggests a regressor where the target is the sale price.
8. What are the model's inputs and intended outputs?
    * The inputs consist of the public data set including house features and sale price.
    * The outputs are the correlation studies and visualizations, as well as the ability to estimate/predict a properties' sale price.
9. What are the criteria for the performance goal of the predictions?
    * An R2 score of at least 0.75 on the train set and  the test set.
10. How will the client benefit?
    * The client will be able to estimate the sale price of the inherited properties, based on data analysis and not just opinion.
    * The client will also be able to estimate/predict the sale price of future investment properties. This can help in deciding which properties to buy, what changes to make to properties to get a higher sale price etc...
## Dashboard Design

This section introduces the use of the Streamlit dashboard APP that would be delivered to the client as requested.

### Page 1: Project Summary

This page will incude:

- Statement of the project purpose.
- Project terms and jargon.
- Brief description of the data set.
- Statement of business requirements.
- Links to further information.

### Page 2: Sale Price Correlation Analysis

This page will fullfill the first business requirement. It includes checkboxes so the client has the ability to display the following visual guides to the data features:

- A sample of data from the data set.
- Pearson and spearman correlation plots between the features and the sale price.
- Histogram and scatterplots of the most important predictive features.
- Predictive Power Score analysis.

### Page 3: Sale Price Prediction

This page will satisfy the second Business Requirement. It will include:

- Input feature of property attributes to produce a prediction on the sale price.
- Display of the predicted sale price.
- Feature to predict the sale prices of the clients specific data in relation to her inherited properties.

### Page 4: Hypothesis and Validation

This page will include:

- A list of the project's hypothesis and how they were validated.

### Page 5: Machine Learning Model

This page will include

- Information on the ML pipeline used to train the model.
- Demonstration of feature importance.
- Review of the pipeline performance.

## Testing
### PEP8 Compliance Testing 
The python code from all .py files was passed through the [CI Python Linter](https://pep8ci.herokuapp.com/). Code passed with no errors in most cases. However, there was one exception where the code could not be split across multiple lines whilst maintaining readability.
* In page_sale_price_analysis - line 286:
    * pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T

### Manual Testing
The deployed app has been thoroughly tested to ensure data visualisations are properly displayed and sale price predictions run correctly.

## Unfixed Bugs
- The app does not currently contain any unfixed bugs.

## Deployment
### Heroku

1. Before deployment to Heroku, check that the project contains the following files and information.
    * setup.sh file containing streamlit configuration requirements.
    * Procfile containing 'web: sh setup.sh && streamlit run app.py'
    * runtime.txt file which sets the Python environment to 3.8.17, which will reduce any environment conflicts from development to production.
2. Log into the Heroku command line interface through the Gitpod terminal to set the stack to Heroku-20 and avoid 'unsupported version of Python' errors during deployment.
    * Install heroku with this command: 'curl https://cli-assets.heroku.com/install.sh | sh'
    * Log in to Heroku using your Heroku API as the password.
    * Use command to set tech stack: 'heroku stack:set heroku-20'
3. Log in to the Heroku website and create a new app
    * At the Deploy tab, select GitHub as the deployment method.
    * Select your GitHub repository name and click Search. When it locates the correct repo, click Connect.
    * Select Main branch, then Deploy Branch.
    * Watch the build log for any errors during deployment. Once successfully built, click to Open App.

## Technologies

## Credits

## Acknowledgements
