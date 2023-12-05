"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Customer Churn Predictor")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            A Random Forest model is employed in a bank loan approval system to assess applicant eligibility. By utilizing a collection of decision trees, it analyzes various factors such as credit history, income, and debt-to-income ratio to predict loan approval likelihood. The algorithm’s ensemble nature enhances accuracy by aggregating multiple tree predictions, offering a robust evaluation method. Through this approach, the system efficiently determines loan eligibility, contributing to informed and reliable lending decisions.
        </p>
    """, unsafe_allow_html=True)