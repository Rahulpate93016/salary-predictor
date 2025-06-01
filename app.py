import streamlit as st
import pickle
import numpy as np
from PIL import Image
import base64

# ✅ Load ML model
model = pickle.load(open('salary_model.pkl', 'rb'))

# ✅ Load and convert local image to base64
with open("3d206f3d-dbfa-448c-bb58-d6d656d4a4c0.png", "rb") as f:
    img_bytes = f.read()
    b64_image = base64.b64encode(img_bytes).decode()

# ✅ Custom CSS + Developer Profile Box with Embedded Image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                          url("https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/—Pngtree—focusing%20on%20collaboration_16545643.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }}

    .profile-container {{
        position: fixed;
        bottom: 60px; /* upar shift kar diya */
        right: 20px;
        text-align: center;
        z-index: 9999;
    }}

    .profile-pic {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 0 12px rgba(0,0,0,0.6);
    }}

    .dev-text {{
        color: white;
        font-family: "Times New Roman";
        font-weight: bold;
        font-size: 20px;
        margin-top: 10px;
        text-shadow: 2px 2px 3px black;
    }}

    .linkedin-link {{
        font-size: 14px;
        color: #00acee;
        text-decoration: none;
    }}

    .linkedin-link:hover {{
        text-decoration: underline;
        color: #ffffff;
    }}
    </style>

    <div class="profile-container">
        <img src="data:image/png;base64,{b64_image}" class="profile-pic">
        <div class="dev-text">Developed By Rahul Patel</div>
        <a href="https://www.linkedin.com/in/rahul-patel-607b29247/" target="_blank" class="linkedin-link">
            🔗 LinkedIn Profile
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ App Title
st.markdown("<h1 style='text-align: center; color: white;'>💼 Salary Predictor in IT Sector</h1>", unsafe_allow_html=True)

# ✅ Input
years_exp = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1, value=0.0)

# ✅ Predict Button
if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary for {years_exp} years of experience: ₹{prediction[0]:,.2f}")
