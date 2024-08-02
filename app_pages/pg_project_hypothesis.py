import streamlit as st
import matplotlib.pyplot as plt


def pg_project_hypothesis_body():
    st.write("### Project Hypotheses and Validation")

    # Hypothesis 1
    st.success(
        f" **H1 - The sale price of a property is assumed to be correlated"
        f" with all features of the house.**\n"
        f" * Correlation study present a differente information where not all "
        f" features have significant correlation with the "
        f" sale price of a property. "
        f" The Study also shows that sale price "
        f" correlates strongly with features "
        f" that are commom to most properties such as Groundlevel Living area "
        f"(GrLivArea), Garage Area(GarageArea),"
        f" Total Basement Area (TotalBsmtSF), "
        f" Year Built(YearBuilt), and 1st Floor"
        f" squarefootage (1stFlrSF).  \n\n"
    )

    # Hypothesis 2
    st.success(
        f" **H2 - We expect a higher price for "
        f" properties with larger built up area.**\n"
        f" * This is correct, according to pearson"
        f" correlation studies, we can identify "
        f" a linear relation between sale price "
        f" and Above Ground Living Area(GrLivArea) "
        f" Total square feet of Basement "
        f" Area(TotalBsmtSF), 1st floor square feet (1stFlrSF) "
        f" and Garage Area (GarageArea). \n\n"
    )

    # Hypothesis 3
    st.success(
        f" **H3 - The quality and condition of "
        f" a property, as indicated by features like "
        f" OverallQual, show a positive correlation "
        f" with the sale price. Higher-quality "
        f" properties generally command higher sale prices.**\n"
        f" * The correlation study shows that "
        f" Overall quality is one of most correlated "
        f" feature with the target Sale Price. "
        f" The modeling and evalation shows that "
        f" Overall quality is the most important "
        f" feature to predict the Sale Price. \n\n"
    )