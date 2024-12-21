import streamlit as st
import requests

# Define the FastAPI server URL (replace with your EC2 public IP or domain)
api_url = "http://54.89.241.159:8000/predict_churn/"

# Custom CSS for styling the Streamlit app
st.markdown("""
    <style>
        /* Set a dark purple background for the body */
        body {
            background-color: #2C3E50; /* Deep Purple */
            color: white;
            font-family: 'Arial', sans-serif;
        }

        /* Main title */
        .title {
            color: #E74C3C; /* Bright Red for a modern touch */
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            padding-top: 30px;
        }

        /* Main container for user input form */
        .main {
            background-color: #34495E;  /* Darker gray background for form */
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
        }

        /* Section titles */
        .header {
            font-size: 24px;
            color: #ECF0F1;  /* Light gray color */
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Input labels */
        .label {
            font-size: 16px;
            color: #ECF0F1; /* Light gray color for input labels */
            font-weight: bold;
        }

        /* Prediction and suggestion sections */
        .prediction-section {
            margin-top: 20px;
            padding: 20px;
            background-color: #1ABC9C;  /* Teal color */
            border: 1px solid #16A085;
            border-radius: 8px;
        }

        /* Prediction text styles */
        .prediction-text {
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
        }

        /* Suggestion section styles */
        .suggestion-section {
            margin-top: 20px;
            padding: 15px;
            background-color: #F39C12;  /* Bright Yellow */
            border-radius: 8px;
            color: #2C3E50;
        }

        /* Error and Success styles */
        .error {
            color: #E74C3C; /* Red for error */
            font-weight: bold;
        }

        .success {
            color: #2ECC71; /* Green for success */
            font-weight: bold;
        }

        /* Button styling */
        .btn {
            background-color: #16A085;  /* Teal button color */
            color: white;
            padding: 12px 20px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        .btn:hover {
            background-color: #1ABC9C;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit user input form
st.markdown('<div class="title">Churn Prediction App</div>', unsafe_allow_html=True)

# Inform the user about the purpose of the form
st.markdown("""
    <div class="main">
        <p class="header">Welcome! To predict if a customer is likely to leave, please input the following details:</p>
    </div>
""", unsafe_allow_html=True)

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
if st.button('Predict Churn', key="predict_button"):
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

        # Prediction Section
        st.markdown(f"""
        <div class="prediction-section">
            <p class="prediction-text { 'error' if churn_status == 'Yes' else 'success' }">
                The customer is {'at risk of leaving (Churn Prediction: Yes)' if churn_status == 'Yes' else 'likely to stay (Churn Prediction: No)'}.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Suggested actions Section
        if churn_status == "Yes":
            st.markdown("""
            <div class="suggestion-section">
                <p><strong>Suggested Actions:</strong></p>
                <ul>
                    <li>Offer retention deals or discounts.</li>
                    <li>Review customer service interactions to improve satisfaction.</li>
                    <li>Investigate the reasons behind the customer’s dissatisfaction.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="suggestion-section">
                <p><strong>Suggested Actions:</strong></p>
                <ul>
                    <li>Continue providing excellent service.</li>
                    <li>Encourage loyalty programs or upsell additional services.</li>
                    <li>Monitor the customer’s behavior for any future risk signals.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.error("Error: Unable to get prediction")
