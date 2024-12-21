import streamlit as st
import requests

# Define the FastAPI server URL (replace with your EC2 public IP or domain)
api_url = "http://54.89.241.159:8000/predict_churn/"

# Streamlit user input form
st.title('Churn Prediction')

# Inform the user about the purpose of the form
st.write("""
    **Welcome to the Churn Prediction App!**  
    To help us predict whether a customer is likely to leave, please input the following details about the customer.  
    Based on the information you provide, we will predict if the customer is at risk of leaving or not.
""")

# User input fields using sliders
age = st.slider("Age", min_value=0, max_value=100, value=30)
group_size = st.slider("Group Size", min_value=1, max_value=10, value=2)
monthly_charge = st.slider("Monthly Charge", min_value=0.0, max_value=1000.0, value=50.0, step=0.1)
total_charges = st.slider("Total Charges", min_value=0.0, max_value=10000.0, value=200.0, step=0.1)
local_calls = st.slider("Local Calls", min_value=0, max_value=100, value=5)
local_mins = st.slider("Local Minutes", min_value=0.0, max_value=1000.0, value=20.0, step=0.1)
intl_calls = st.slider("International Calls", min_value=0, max_value=100, value=3)
intl_mins = st.slider("International Minutes", min_value=0.0, max_value=1000.0, value=10.0, step=0.1)
customer_service_calls = st.slider("Customer Service Calls", min_value=0, max_value=10, value=1)
avg_monthly_gb = st.slider("Average Monthly GB", min_value=0, max_value=1000, value=10)
gender = st.selectbox("Gender", ["Male", "Female"])
under30 = st.selectbox("Under 30?", ["Yes", "No"])
senior = st.selectbox("Senior?", ["Yes", "No"])
group_flag = st.selectbox("Group Flag", ["Yes", "No"])
intl_active = st.selectbox("International Active?", ["Yes", "No"])
intl_plan = st.selectbox("International Plan?", ["Yes", "No"])
unlimited_data_plan = st.selectbox("Unlimited Data Plan?", ["Yes", "No"])
device_protection = st.selectbox("Device Protection?", ["Yes", "No"])
contract_type = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
payment_method = st.selectbox("Payment Method", ["Direct Debit", "Paper Check", "Credit Card"])
extra_international_charges = st.slider("Extra International Charges", min_value=0.0, max_value=1000.0, value=5.0, step=0.1)
account_length = st.slider("Account Length", min_value=0, max_value=1000, value=50)
extra_data_charges = st.slider("Extra Data Charges", min_value=0, max_value=1000, value=10)

# Button to trigger prediction
if st.button('Predict Churn'):
    # Prepare the data
    input_data = {
        "Age": age,
        "GroupSize": group_size,
        "MonthlyCharge": monthly_charge,
        "TotalCharges": total_charges,
        "LocalCalls": local_calls,
        "LocalMins": local_mins,
        "IntlCalls": intl_calls,
        "IntlMins": intl_mins,
        "CustomerServiceCalls": customer_service_calls,
        "AvgMonthlyGB": avg_monthly_gb,
        "Gender": gender,
        "Under30": under30,
        "Senior": senior,
        "GroupFlag": group_flag,
        "IntlActive": intl_active,
        "IntlPlan": intl_plan,
        "UnlimitedDataPlan": unlimited_data_plan,
        "DeviceProtection": device_protection,
        "ContractType": contract_type,
        "PaymentMethod": payment_method,
        "ExtraInternationalCharges": extra_international_charges,
        "AccountLength": account_length,
        "ExtraDataCharges": extra_data_charges
    }

    # Send the request to the FastAPI server
    response = requests.post(api_url, json=input_data)

    if response.status_code == 200:
        prediction = response.json()
        churn_status = prediction.get('Predicted Churn')

        # Provide a more meaningful result
        if churn_status == "Yes":
            st.error(f"The customer is at risk of leaving (Churn Prediction: **Yes**).")
            st.write("### Suggested actions:")
            st.write("- Offer retention deals or discounts.")
            st.write("- Review customer service interactions to improve satisfaction.")
            st.write("- Investigate the reasons behind the customer’s dissatisfaction.")
        else:
            st.success(f"The customer is likely to stay (Churn Prediction: **No**).")
            st.write("### Suggested actions:")
            st.write("- Continue providing excellent service.")
            st.write("- Encourage loyalty programs or upsell additional services.")
            st.write("- Monitor the customer’s behavior for any future risk signals.")

    else:
        st.error("Error: Unable to get prediction")
