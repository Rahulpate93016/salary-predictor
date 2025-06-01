import streamlit as st
import pickle
import numpy as np
from PIL import Image
import base64

# Load model
model = pickle.load(open('salary_model.pkl', 'rb'))

# === Convert uploaded image to base64 ===
with open("3d6aa47b-1dc6-42cf-ae77-247032bec556.png", "rb") as f:
    img_bytes = f.read()
    b64_image = base64.b64encode(img_bytes).decode()

# === Inject CSS for background and developer profile ===
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
                    url('https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/—Pngtree—focusing%20on%20collaboration_16545643.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}

    .developer-box {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        text-align: center;
        z-index: 9999;
    }}

    .profile-img {{
        width: 110px;
        height: 110px;
        border-radius: 50%;
        border: 4px solid white;
        object-fit: cover;
        box-shadow: 0px 0px 10px #000;
    }}

    .dev-text {{
        color: white;
        font-weight: bold;
        margin-top: 10px;
        font-size: 17px;
        text-shadow: 1px 1px 3px black;
    }}

    .linkedin {{
        font-size: 14px;
        color: #0A66C2;
        text-decoration: none;
    }}

    .linkedin:hover {{
        text-decoration: underline;
    }}
    </style>

    <style>


    <div class="developer-box">
        <img class="profile-img" src="data:image/png;base64,{b64_image}" alt="Developer">
        <div class="dev-text">Developed by Rahul Patel</div>
        <a href="https://www.linkedin.com/in/rahul-patel-607b29247/" class="linkedin" target="_blank">🔗 LinkedIn</a>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
/* CSS code here */
.stAlert {
    background-color: rgba(0, 0, 0, 0.6) !important;
    border-left: 5px solid #21c55d;
    color: white !important;
    font-weight: bold;
    font-size: 16px;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 0 10px black;
}
</style>
""", unsafe_allow_html=True)


# === App title ===
st.markdown("<h1 style='text-align: center;'>💼 Salary Predictor in IT Sector</h1>", unsafe_allow_html=True)

# === Input ===
years_exp = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1, value=0.0)

# === Predict button ===
if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary for {years_exp} years of experience: ₹{prediction[0]:,.2f}")
