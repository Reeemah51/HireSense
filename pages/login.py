import os, sys

# move one level up from pages/ back into your HireSense2 folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# 2) now you can import database as if it were top-level
from database import init_db, authenticate_user, create_account
import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
def show_login():
    # Initialize the database
    init_db()

    # Page Configuration
    st.set_page_config(page_title="Create an Account", page_icon="📝", layout="wide")

    st.markdown("""
    <style>
    /* Hide Streamlit's default page list from sidebar */
    section[data-testid="stSidebar"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)
    # Add custom CSS
    st.markdown("""
        <style>
        .stApp {
        background: radial-gradient(circle, rgba(236,239,255,1) 0%, rgba(207,208,255,1) 100%) !important;
        color: #000000 !important;
        padding-top: 6rem;
        label {
        color: black !important;
        font-weight: bold;
    }
    }
    </style>
    """, unsafe_allow_html=True)  # shortened for brevity

    # Layout
    col1, col2 = st.columns([2, 3])

    with col1:
        st.image("./img/Rectangle.svg")
        st.image("./img/Group289360.png")
        st.markdown("<p style='text-align: center; color: #000000; font-weight: bold; font-size: 24px;'>Welcome Back!</p>", unsafe_allow_html=True)
        st.image("./img/pager.png")

    with col2:
        st.markdown("<h2 style='text-align: center;'>Login to your account</h2>", unsafe_allow_html=True)
        st.markdown("""
                <style>
                div.stButton > button {
            background: none;
            border: none;
            color: #656ED3;
            text-decoration: underline;
            padding: 0;
            font-size: 0.9rem;
            cursor: pointer;
            }
        </style>
        """, unsafe_allow_html=True)
        if st.button("Don't have an account? Register"):
         switch_page("createaccount")

        st.markdown("<div style='margin-top: 90px;'></div>", unsafe_allow_html=True)  

        username = st.text_input("Username")
        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        password = st.text_input("Password", type="password")

        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True) 
        if st.button("Login"):
            if username and password:
                response = authenticate_user(username, password)
                if response == "Authentication successful!":
                    st.session_state.username = username
                    if username.lower() == "admin":
                        switch_page("dashboard")
                    else:
                        switch_page("choosejob")
                    st.success(f"Welcome, {username}!")
                else:
                    st.error(response)
            else:
                st.error("❌ Please enter both username and password.")

        # ✅ Admin Login Link
        #st.markdown("""
         #   <div style='text-align: left; margin-top: 10px; margin-bottom: 25px;'>
          #      <span style='color: #130231;'>Admin?</span> <a href='#' style='font-weight: bold;'>Login here</a>
          #  </div>
        #""", unsafe_allow_html=True)


show_login()