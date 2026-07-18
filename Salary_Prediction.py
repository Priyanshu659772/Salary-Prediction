import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Employee Salary Prediction",
    layout="centered"
)

# -----------------------------
# Load Model & Scaler
# -----------------------------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("Employee Salary Prediction")
st.write("Fill in the employee details below to predict the Annual Salary (LPA).")

st.divider()

# -----------------------------
# Input Fields
# -----------------------------

age = st.number_input("Age", min_value=18, max_value=65, value=25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education",
    ["Diploma", "Bachelor", "Master", "PhD"]
)

experience = st.number_input(
    "Experience (Years)",
    min_value=0.0,
    max_value=40.0,
    value=2.0
)

department = st.selectbox(
    "Department",
    [
        "Operations",
        "IT",
        "Finance",
        "Sales",
        "HR",
        "Marketing"
    ]
)

job_level = st.selectbox(
    "Job Level",
    [
        "Junior",
        "Mid",
        "Senior",
        "Lead",
        "Manager"
    ]
)

performance = st.slider(
    "Performance Rating",
    min_value=1,
    max_value=5,
    value=3
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=20,
    value=1
)

overtime = st.number_input(
    "Overtime Hours",
    min_value=0,
    max_value=200,
    value=10
)

remote = st.selectbox(
    "Remote Work",
    ["Yes", "No"]
)

city = st.selectbox(
    "City",
    [
        "Hyderabad",
        "Mumbai",
        "Pune",
        "Chennai",
        "Bangalore",
        "Delhi"
    ]
)

company_tenure = st.number_input(
    "Company Tenure",
    min_value=0,
    max_value=40,
    value=2
)

projects = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=100,
    value=5
)

skill_score = st.slider(
    "Skill Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

st.divider()

# -----------------------------
# Encoding
# -----------------------------

gender = 1 if gender == "Male" else 0

education = {
    "Diploma": 0,
    "Bachelor": 1,
    "Master": 2,
    "PhD": 3
}[education]

department = {
    "Operations": 0,
    "IT": 1,
    "Finance": 2,
    "Sales": 3,
    "HR": 4,
    "Marketing": 5
}[department]

# Notebook mapping
job_level = {
    "Junior": 1,
    "Mid": 2,
    "Senior": 3,
    "Lead": 4,
    "Manager": 5
}[job_level]

remote = 1 if remote == "Yes" else 0

city = {
    "Hyderabad": 0,
    "Mumbai": 1,
    "Pune": 2,
    "Chennai": 3,
    "Bangalore": 4,
    "Delhi": 5
}[city]

# -----------------------------
# Create DataFrame
# -----------------------------

input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Education": [education],
    "Experience_Years": [experience],
    "Department": [department],
    "Job_Level": [job_level],
    "Performance_Rating": [performance],
    "Certifications": [certifications],
    "Overtime_Hours": [overtime],
    "Remote_Work": [remote],
    "City": [city],
    "Company_Tenure": [company_tenure],
    "Projects_Completed": [projects],
    "Skill_Score": [skill_score]
})

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Salary", use_container_width=True):

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    st.success(f"Predicted Annual Salary: ₹ {prediction[0]:.2f} LPA")