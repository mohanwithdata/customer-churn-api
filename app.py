import streamlit as st
import requests

st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

input_data = {
    "gender": st.selectbox("gender", [0,1]),
    "SeniorCitizen": st.selectbox("Senior Citizen", [0, 1]),
    "Partner": st.selectbox("Partner", [0,1]),
    "Dependents": st.selectbox("Dependents", [0, 1]),
    "tenure": st.slider("Tenure (Months)", 0, 72, 12),
    "PhoneService": st.selectbox("Phone Service", [0, 1]),
    "MultipleLines": st.selectbox("Multiple Lines", [0, 1]),
    "InternetService": st.selectbox("Internet Service", [0, 1, 2]),
    "OnlineSecurity": st.selectbox("Online Security", [0, 1]),
    "OnlineBackup": st.selectbox("Online Backup", [0, 1]),
    "DeviceProtection": st.selectbox("Device Protection", [0, 1]),
    "TechSupport": st.selectbox("Tech Support", [0, 1]),
    "StreamingTV": st.selectbox("Streaming TV", [0, 1]),
    "StreamingMovies": st.selectbox("Streaming Movies", [0, 1]),
    "Contract": st.selectbox("Contract", [0, 1, 2]),
    "PaperlessBilling": st.selectbox("Paperless Billing", [0, 1]),
    "PaymentMethod": st.selectbox("Payment Method", [0, 1, 2, 3]),
    "MonthlyCharges": st.number_input("Monthly Charges", min_value=0.0, step=0.01),
    "TotalCharges": st.number_input("Total Charges", min_value=0.0, step=0.01)
}

if st.button("Predict Churn"):
    response = requests.post("http://localhost:8000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Churn Prediction: {'Yes' if result['churn'] == 1 else 'No'}")
    else:
        st.error("Error in prediction. Please check the input data.")