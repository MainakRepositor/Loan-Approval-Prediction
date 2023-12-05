"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Loan Approval Prediction System.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    col1,col2 = st.columns(2)
    with col1:
        no_of_dependents = st.slider("Number of dependents", int(df["no_of_dependents"].min()), int(df["no_of_dependents"].max()))
        self_employed = st.slider("Self employed", int(df["self_employed"].min()), int(df["self_employed"].max()))
        income_annum = st.slider("Annual Income", int(df["income_annum"].min()), int(df["income_annum"].max()))
        loan_amount = st.slider("Loan Amount", int(df["loan_amount"].min()), int(df["loan_amount"].max()))
        loan_term = st.slider("Loan Term", int(df["loan_term"].min()), int(df["loan_term"].max()))
        
        

    with col2:
        cibil_score = st.slider("Cibil Score", int(df["cibil_score"].min()), int(df["cibil_score"].max()))
        residential_assets_value = st.slider("Residendial Asset Valuation",int(df["residential_assets_value"].min()), int(df["residential_assets_value"].max()))
        commercial_assets_value = st.slider("Commercial Asset Valuation", int(df["commercial_assets_value"].min()), int(df["commercial_assets_value"].max()))
        luxury_assets_value = st.slider("Luxury Asset Valuation", int(df["luxury_assets_value"].min()), int(df["luxury_assets_value"].max()))
        bank_asset_value = st.slider("Bank Asset Valuation", int(df["bank_asset_value"].min()), int(df["bank_asset_value"].max()))
       
           


    # Create a list to store all the features
    features = [no_of_dependents,self_employed,income_annum,loan_amount,loan_term,cibil_score,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value]

    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Detected Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The person is eligible for the loan")
        else:
            st.error("The person is not eligible for the loan")

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by analysts and has an accuracy of ", round((score*100)),"%")
