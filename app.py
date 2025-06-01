import streamlit as st
import pickle
import numpy as np
import base64 

def add_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpg;base64,{encoded}");
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# 🖼️ Background image add karo — file name yaha do
add_bg_from_local("—Pngtree—focusing on collaboration_16545643.jpg")  

# 🔍 Load the saved model
model = pickle.load(open('salary_model.pkl', 'rb'))



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
