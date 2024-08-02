import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_prices_data, load_pkl_file
from src.machine_learning.evaluate_regression import (
    regression_performance,
    regression_evaluation,
    regression_evaluation_plots)


def pg_predict_price_ml_body():

    # load regression pipeline files
    vsn = 'v3'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/regression_pipeline.pkl"
    )
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/features_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/y_test.csv").squeeze()

    st.success(
        f" **ML Pipeline: Predict Property Sale Price**\n\n"
        f" A machine learning model has been developed to predict house"
        f" sale prices in Ames, Iowa. "
        f" Data cleaning and feature engineering techniques were carried "
        f" out to prepare the data for modelling."
        f" The ML model was tuned in order to optimise its performance "
        f" by using the best combination of parameters. These parameters "
        f" are listed in the ML pipeline below.\n\n"
        f" The model performance was evaluated by using the R2 metric and "
        f" therefore achieving scores of 0.886 and 0.84 on the train set and "
        f" test set respectively. This suggests that the predictive model is "
        f" effectively capturing the underlying patterns in the data and "
        f" providing accurate sale price predictions. \n"
    )

    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline to predict property sale prices.")
    st.code(sale_price_pipe)
    st.write("---")

    # show best features
    st.write("### The model was trained on the following features:")
    st.write(X_train.columns.to_list())
    st.write("### Features Importance plot:")
    st.image(sale_price_feat_importance)

    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=sale_price_pipe)

    st.write("**Performance Plot**")
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test,
                                y_test=y_test, pipeline=sale_price_pipe,
                                alpha_scatter=0.5
                                )