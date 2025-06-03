import streamlit as st
import pickle
import numpy as np

# ====== BACKGROUND IMAGE + PROFILE PHOTO + LINKEDIN ======
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                          url("https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/pexels-photo-585752.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }

    .profile-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        text-align: center;
        z-index: 9999;
    }

    .profile-pic {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 0 10px rgba(0,0,0,0.6);
    }

    .dev-text {
        color: white;
        font-weight: bold;
        font-size: 16px;
        margin-top: 10px;
        text-shadow: 1px 1px 2px black;
    }

    .linkedin-link {
        color: #00acee;
        font-size: 14px;
        text-decoration: none;
    }

    .linkedin-link:hover {
        text-decoration: underline;
        color: #ffffff;
    }
    </style>

    <div class="profile-container">
        <img src="https://raw.githubusercontent.com/Rahulpate93016/salary-predictor/main/Uniform%20Photo.jpg" class="profile-pic" alt="Rahul Patel">
        <div class="dev-text">Developed By Rahul Patel</div>
        <a href="https://www.linkedin.com/in/rahul-patel-607b29247/" target="_blank" class="linkedin-link">
            🔗 LinkedIn Profile
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ====== LOAD MODEL ======
model = pickle.load(open('salary_model.pkl', 'rb'))

# ====== APP TITLE ======
st.markdown("<h1 style='text-align: center; color: white;'>💼 Salary Predictor in IT Sector through your experience</h1>", unsafe_allow_html=True)

# ====== USER INPUT ======
years_exp = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1, value=0.0)

# ====== PREDICT BUTTON ======
if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])
    prediction = model.predict(input_data)
    salary = float(prediction[0])
    st.success(f"For {years_exp} years of experience, your predicted monthly salary is ₹{salary:,.2f}")
