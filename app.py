import streamlit as st
import requests
import json

# FastAPI server URL (change it to the public IP or domain)
API_URL = "http://54.89.241.159:8000/predict"

def classify_data(data):
    """Send data to the FastAPI model for prediction."""
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        return response.json()  # Return the prediction
    else:
        return {"error": "Failed to get prediction"}

# Streamlit UI
st.title("Real-Time Classification with FastAPI Model")

# Input fields for user to fill
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
under30 = st.selectbox("Under 30", ["Yes", "No"])
senior = st.selectbox("Senior", ["Yes", "No"])
group_flag = st.selectbox("GroupFlag", ["Yes", "No"])
group_size = st.number_input("Group Size", min_value=1, max_value=10, value=1)
intl_active = st.selectbox("International Active", ["Yes", "No"])
intl_plan = st.selectbox("International Plan", ["Yes", "No"])
unlimited_data_plan = st.selectbox("Unlimited Data Plan", ["Yes", "No"])
extra_data_charges = st.number_input("Extra Data Charges", min_value=0, value=0)
extra_international_charges = st.number_input("Extra International Charges", min_value=0.0, value=0.0)
device_protection = st.selectbox("Device Protection", ["Yes", "No"])
contract_type = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
payment_method = st.selectbox("Payment Method", ["Direct Debit", "Paper Check", "Credit Card"])
account_length = st.number_input("Account Length", min_value=1, value=24)
local_calls = st.number_input("Local Calls", min_value=0, value=10)
local_mins = st.number_input("Local Minutes", min_value=0.0, value=100.0)
intl_calls = st.number_input("International Calls", min_value=0, value=5)
intl_mins = st.number_input("International Minutes", min_value=0.0, value=20.0)
customer_service_calls = st.number_input("Customer Service Calls", min_value=0, value=2)
avg_monthly_gb = st.number_input("Average Monthly GB", min_value=0, value=5)
monthly_charge = st.number_input("Monthly Charge", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

# Collect all the inputs into a dictionary
input_data = {
    "Gender": gender,
    "Age": age,
    "Under30": under30,
    "Senior": senior,
    "GroupFlag": group_flag,
    "GroupSize": group_size,
    "IntlActive": intl_active,
    "IntlPlan": intl_plan,
    "UnlimitedDataPlan": unlimited_data_plan,
    "ExtraDataCharges": extra_data_charges,
    "ExtraInternationalCharges": extra_international_charges,
    "DeviceProtection": device_protection,
    "ContractType": contract_type,
    "PaymentMethod": payment_method,
    "AccountLength": account_length,
    "LocalCalls": local_calls,
    "LocalMins": local_mins,
    "IntlCalls": intl_calls,
    "IntlMins": intl_mins,
    "CustomerServiceCalls": customer_service_calls,
    "AvgMonthlyGB": avg_monthly_gb,
    "MonthlyCharge": monthly_charge,
    "TotalCharges": total_charges
}

# When the button is pressed, send the data to the FastAPI model
if st.button("Get Prediction"):
    result = classify_data(input_data)
    
    if "error" in result:
        st.error(f"Error: {result['error']}")
    else:
        if result==0:
            st.success(f"Prediction Result: No")
        else:
            st.success(f"Prediction Result: Yes")
