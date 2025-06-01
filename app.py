import streamlit as st
import pickle
import numpy as np

# ✅ Inject background using GitHub raw image URL
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/—Pngtree—focusing%20on%20collaboration_16545643.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Load model
model = pickle.load(open('salary_model.pkl', 'rb'))

# ✅ App UI
st.title("💼 Salary Predictor in IT Sector")

years_exp = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1, value=0.0)

if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary for {years_exp} years of experience: ₹{prediction[0]:,.2f}")
