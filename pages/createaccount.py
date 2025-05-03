import streamlit as st
from database import create_account
from streamlit_extras.switch_page_button import switch_page
# Define reusable function to render this page
def show_create_account():
    st.set_page_config(page_title="Create an Account", page_icon="📝", layout="wide")

    st.markdown("""
        <style>
            :root {
                --main-color: #7378c5;
                --button-hover-color: #5a4dbc;
                --border-radius: 20px;
                --input-padding: 15px;
                --font-size: 16px;
            }
                /* Hide Streamlit's default page list from sidebar */
            section[data-testid="stSidebar"] ul {
            display: none;
                }
            .st-emotion-cache-b95f0i {
                margin-left: 15%;
                margin-right: 15%;
                width: 70%;
                height: 100vh;
            }
            .stHorizontalBlock, .stColumn {
                margin: 0 !important;
                padding: 0 !important;
                background-color: #f4f4f9;
            }
            .st-emotion-cache-1yekdrm {
                padding-top: 10% !important;
                background-color: var(--main-color);
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }
            .st-emotion-cache-ps7s80 {
                padding-top: 20px !important;
                height: 100vh;
                background-color: #f4f4f9;
            }
            input {
                background-color: rgba(0, 0, 0, 0);
                width: 100%;
                padding: var(--input-padding);
                margin: 8px 0;
                border-radius: var(--border-radius);
                border: 1px solid var(--main-color);
                font-size: var(--font-size);
            }
            .stImage img {
                max-width: 100%;
                height: auto;
            }
            .stTextInput > div {
                border: 2px solid #656ED3 !important;
                border-radius: var(--border-radius) !important;
            }
            .stTextInput > div > div > button svg path {
                fill: #656ED3 !important;
            }
            .register-btn {
                background-color: var(--main-color);
                color: white;
                text-align: center;
                font-size: var(--font-size);
                padding: 10px;
                border-radius: var(--border-radius);
                border: none;
                width: 100%;
                cursor: pointer;
            }
            .register-btn:hover {
                background-color: var(--button-hover-color);
            }
            .google-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                border: 1px solid #ccc;
                padding: 10px;
                border-radius: var(--border-radius);
                width: 100%;
                cursor: pointer;
                background-color: white;
            }
            .google-btn img {
                width: 20px;
                height: 20px;
            }
            label {
            color: black !important;
            font-weight: bold;
                }
                
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 3])

    with col1:
        st.image("img/Rectangle.svg")
        st.image("img/Group289360.png")
        st.markdown("<p style='text-align: center; color: #130231; font-weight: bold; font-size: 24px;'>Your AI Interview Assistant</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #130231; font-size: 24px;'>Just a couple of clicks and we start</p>", unsafe_allow_html=True)
        st.image("img/pager.png")

    with col2:
        st.markdown("<h2 style='text-align: center;'>Create an account</h2>", unsafe_allow_html=True)
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

        if st.button("Already a member? Log in"):
         switch_page("login")

        full_name = st.text_input("Full name")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Create Account"):
            if password == confirm_password:
                response = create_account(username, email, password)
                if "successfully" in response:
                    st.success(response)
                    # ← Here’s the redirect:
                    if st.button("Go to Login Page"):
                        switch_page("login")
                else:
                    st.error(response)
            else:
                st.error("Passwords do not match!")

# Allow import
if __name__ == "__main__":
    show_create_account()
