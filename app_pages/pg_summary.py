import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def pg_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Purpose and Motivation**\n\n"
        f"The client, who has inherited four properties in Ames, "
        f"Iowa, is looking to gain insights into the factors that "
        f" influence house sale prices locally. Furthermore, "
        f"they wish to forecast the sale prices of their own properties"
        f" and assess the potential sale prices of other "
        f" homes in Ames, Iowa.\n\n"
        f"The ultimate goal is to create a predictive ML model capable of "
        f"accurately estimating house sale prices based on different house features. "
        f"This model will empower the client to make informed pricing decisions"
        f"for their inherited properties and gain insights into the local "
        f"real estate market in Ames, Iowa.\n\n"
        f"\n\n"
        f"**Project Terminology**\n\n"
        f"* **Client** is someone who engages with this service or product.\n"
        f"* **Sale price** is the anticipated value of a home as "
        f"expected in a regular and straightforward real estate deal. "
        f"The values are represented in US dollars.\n"
        f"* **Property, real estate or house** may be used interchangably, "
        f"and refer to the home being valued. \n"
        f"* **Features, attributes and variables** refer to the "
        f"characteristics of a property. \n\n"
        f"**Project Dataset**\n"
        f"* The dataset can be accessed from [Kaggle]"
        f"(https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)"
        f".\n"
        f"* The dataset comprises approximately 1500 rows of house records "
        f" from Ames, Iowa, providing information on house characteristics "
        f"such as Floor Area, Basement, Garage, Kitchen, Lot, Porch, "
        f"Wood Deck, Year Built) along with their sale prices. "        
    )

    # text based on README file - "Business Requirements" section
    st.success(
        f"**Business Requirements**\n\n"
        f"A client has received an inheritance  of four properties "
        f"located in Ames, Iowa, from a deceased great-grandfather.  "
        f"has requested help in maximising the sales price "
        f"for the inherited properties. \n\n "
        f"The client has an excellent understanding of property prices  "
        f"in her own state and residential area, but she fears that basing "
        f"her estimates for property worth on her current knowledge. "
        f"might lead to inaccurate appraisals. What makes a house desirable "
        f"and valuable where she comes from might not be the same in "
        f"Ames, Iowa.\n\n "
        f"She found a public dataset with house prices for Ames, Iowa, and "
        f"has provided it for this project. \n\n "
        f"The client expectations are: \n\n"
        f"* 1 - Discovering how the house attributes correlate with the sale  "
        f"price. There is an expectation for data visualisations of the  "
        f"correlated variables against the sale price to confirm. \n\n "      
        f"* 2 - Predicting the house sale price of the four inherited houses "
        f"including any other residential properties in Ames, Iowa,"
        f"based on the most important features of the homes. The predictive"
        f"model should aim to acchieve an R2 value of 0.8 or higher."
    )

    # Link to README file, so the users can have access to full
    # project documentation
    st.write(
        f"* For further details about this project, please refer to the "
        f"[README.md](https://github.com/EdsonSMartins/PP5-heritage-housing)"
        f" on GitHub, where the development of this web app is documented. "
    )