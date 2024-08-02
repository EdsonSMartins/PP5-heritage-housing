import streamlit as st
import matplotlib.pyplot as plt


def pg_project_hypothesis_body():
    st.write("### Project Hypotheses and Validation")

    
    # Hypothesis 1
    st.success(
        f" **H1 - The sale price of a property is assumed to be correlated with"
        f" all features of the house.**\n"
        f" * Correlation study present a differente information where not all "
        f" features have significant correlation with the sale price of a property. "
        f" The Study also shows that sale price correlates strongly with features "
        f" that are commom to most properties such as Groundlevel Living area "
        f" (GrLivArea), Garage Area (GarageArea), Total Basement Area (TotalBsmtSF), "
        f" Year Built (YearBuilt), and 1st Floor squarefootage (1stFlrSF).  \n\n"
    )

    # Hypothesis 2
    st.success(
        f" **H2 - We expect a higher price for properties with larger built up area.**\n"
        f" * This is correct, according to pearson correlation studies, we can identify "
        f" a linear relation between sale price and Above Ground Living Area (GrLivArea) " 
        f" Total square feet of Basement Area (TotalBsmtSF), 1st floor square feet (1stFlrSF) "
        f" and Garage Area (GarageArea). \n\n"
    )

    # Hypothesis 3
    st.success(
        f" **H3 - The quality and condition of a property, as indicated by features like "
        f" OverallQual, show a positive correlation with the sale price. Higher-quality "
        f" properties generally command higher sale prices.**\n"
        f" * The correlation study shows that Overall quality is one of most correlated "
        f" feature with the target Sale Price. The modeling and evalation shows that "
        f" Overall quality is the most important feature to predict the Sale Price. \n\n"
    )