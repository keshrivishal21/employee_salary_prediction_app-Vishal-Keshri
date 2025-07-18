import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.pkl")

# Page settings
st.set_page_config(page_title="Salary Classifier using ML", page_icon="💼", layout="wide")

# Title and subtitle
st.markdown("<h1 style='text-align: center;'>💼 Employee Salary Classification App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Predict if an employee earns >50K or ≤50K using ML Algorithms</h4>", unsafe_allow_html=True)
st.markdown("---")

# Input Form
st.sidebar.header("📝 Enter Employee Details")

with st.sidebar:
    age = st.slider("🎂 Age", 18, 90, 30)
    educational_num = st.slider("🎓 Education Level (Numerical)", 1, 16, 10)
    capital_gain = st.number_input("💰 Capital Gain", min_value=0, value=0)
    capital_loss = st.number_input("📉 Capital Loss", min_value=0, value=0)
    hours_per_week = st.slider("⏱ Hours per Week", 1, 99, 40)

    st.markdown("---")

    workclass = st.selectbox("🏢 Workclass", [
        'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 
        'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'
    ])
    marital_status = st.selectbox("💍 Marital Status", [
        'Never-married', 'Married-civ-spouse', 'Divorced', 'Separated', 
        'Widowed', 'Married-spouse-absent'
    ])
    occupation = st.selectbox("💼 Occupation", [
        'Tech-support', 'Craft-repair', 'Other-service', 'Sales', 
        'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct',
        'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv',
        'Protective-serv', 'Armed-Forces'
    ])
    relationship = st.selectbox("👨‍👩‍👧‍👦 Relationship", [
        'Wife', 'Husband', 'Not-in-family', 'Own-child', 'Unmarried', 'Other-relative'
    ])
    race = st.selectbox("🌐 Race", [
        'White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'
    ])
    gender = st.selectbox("⚧ Gender", ['Male', 'Female'])
    native_country = st.selectbox("🌎 Native Country", [
        'United-States', 'Mexico', 'Philippines', 'Germany', 'Canada', 'India',
        'England', 'Cuba', 'Jamaica', 'South', 'China', 'Italy', 'Poland', 
        'Columbia', 'Vietnam', 'Guatemala', 'Japan', 'Other'
    ])

# Collect input in DataFrame
input_data = pd.DataFrame([{
    'age': age,
    'educational-num': educational_num,
    'capital-gain': capital_gain,
    'capital-loss': capital_loss,
    'hours-per-week': hours_per_week,
    'workclass': workclass,
    'marital-status': marital_status,
    'occupation': occupation,
    'relationship': relationship,
    'race': race,
    'gender': gender,
    'native-country': native_country
}])

# Display input
st.markdown("### 🔍 Preview of Input Data")
st.dataframe(input_data)

# Prediction
if st.button("🔮 Predict Salary Class"):
    prediction = model.predict(input_data)
    label = prediction[0]
    emoji = "💸" if label == ">50K" else "👛"
    st.success(f"🎯 Prediction: **{label}** {emoji}")

# Optional Footer
st.markdown("---")
st.markdown("<small style='text-align: center; display: block;'>Made by Vishal Keshri · MCA Student of MANIT BHOPAL</small>", unsafe_allow_html=True)
