import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.pg_summary import pg_summary_body
from app_pages.pg_sale_price_analysis import pg_sale_price_analysis_body
from app_pages.pg_sale_price_predictor import pg_sale_price_predictor_body
from app_pages.pg_project_hypothesis import pg_project_hypothesis_body
from app_pages.pg_predict_price import pg_predict_price_ml_body

# Create an instance of the app
app = MultiPage(app_name="Heritage Housing Sale Price Predictor")

# Add your app pages here using .add_page()
app.add_page("Project Summary", pg_summary_body)
app.add_page("Sale Price Correlation Analysis", pg_sale_price_analysis_body)
app.add_page("Sale Price Predictor", pg_sale_price_predictor_body)
app.add_page("Project Hypothesis and Validation", pg_project_hypothesis_body)
app.add_page("ML: Price Prediction", pg_predict_price_ml_body)

app.run()  # Run the  app