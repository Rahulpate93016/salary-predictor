import streamlit as st
import pickle
import numpy as np

# ✅ CSS for background + profile photo + developer text
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/—Pngtree—focusing%20on%20collaboration_16545643.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .profile-container {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        text-align: center;
        z-index: 9999;
    }}

    .profile-pic {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }}

    .dev-text {{
        color: white;
        font-weight: bold;
        font-size: 16px;
        margin-top: 8px;
        text-shadow: 1px 1px 2px black;
    }}
    </style>

    <!-- ✅ HTML: Your uploaded photo + text -->
    <div class="profile-container">
        <img src="https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/Uniform%20Photo.jpg" class="profile-pic">
        <div class="dev-text">Developed By Rahul Patel</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ Load model
model = pickle.load(open('salary_model.pkl', 'rb'))

# ✅ Title
st.title("💼 Salary Predictor in IT Sector")

# ✅ Input
years_exp = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1, value=0.0)

# ✅ Prediction
if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary for {years_exp} years of experience: ₹{prediction[0]:,.2f}")
