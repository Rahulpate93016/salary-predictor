import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('salary_model.pkl', 'rb'))

st.title("Salary Predictor in IT Sector")

# Input from user
years_exp = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1, value=0.0)

# Predict button
if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])  # Model expects 2D array
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary for {years_exp} years of experience: ₹{prediction[0]:,.2f}")
