import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('loan_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
def main():
    st.title("Loan Eligibility Prediction App")
    st.write("This app predicts whether a loan application is eligible based on the provided details.")

    # Input fields
    st.header("Enter Applicant Details:")
    applicant_income = st.number_input("Applicant Income (in Rs.)", min_value=0, value=5000, step=1000)
    coapplicant_income = st.number_input("Coapplicant Income (in Rs.)", min_value=0, value=0, step=1000)
    loan_amount = st.number_input("Loan Amount (in Rs.)", min_value=0, value=100000, step=10000)
    loan_amount_term = st.number_input("Loan Amount Term (in months)", min_value=0, value=360, step=12)
    credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", options=[1, 0])
    gender = st.selectbox("Gender", options=["Male", "Female"])
    married = st.selectbox("Marital Status", options=["Yes", "No"])
    dependents = st.selectbox("Number of Dependents", options=["0", "1", "2", "3+"])
    education = st.selectbox("Education", options=["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", options=["Yes", "No"])
    property_area = st.selectbox("Property Area", options=["Urban", "Semiurban", "Rural"])

    # Map categorical variables to numerical values
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    self_employed = 1 if self_employed == "Yes" else 0
    education = 0 if education == "Graduate" else 1
    property_area_mapping = {"Urban": 2, "Semiurban": 1, "Rural": 0}
    property_area = property_area_mapping[property_area]
    dependents = 3 if dependents == "3+" else int(dependents)

    # Prepare input features
    features = np.array([[
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        gender,
        married,
        dependents,
        education,
        self_employed,
        property_area
    ]])

    # Predict eligibility
    if st.button("Predict Loan Eligibility"):
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.success("Congratulations! You are eligible for the loan.")
        else:
            st.error("Sorry, you are not eligible for the loan.")

if __name__ == "__main__":
    main()
