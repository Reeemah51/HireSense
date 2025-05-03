import os, sys
# move one level up from pages/ back into your HireSense2 folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# 2) now you can import database as if it were top-level
from database import init_db, authenticate_user, create_account
import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
import base64
st.set_page_config(page_title="HireSense", layout="wide")
# === Function to be used in routing ===
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# — 2) Load your SVG as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

svg_b64 = get_base64_image(r"C:\Users\Administrator\Desktop\HireSense2\img\Group289360.svg")

# — 3) Global CSS
st.markdown("""
<style>
  .stApp {
    background: radial-gradient(circle, #ECEFFF 0%, #CFD0FF 100%) !important;
    margin: 0; padding: 0;
  }
   [data-testid="stSidebar"] {
        display: none !important;
    }
  .hero-flex {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 4rem 6rem;
    min-height: 80vh;
  }
  .hero-title {
    font-size: 3rem; font-weight: 800;
    color: #2e2e8f !important; line-height: 1.2;
    margin: 0 0 2rem 0;
  }
  /* Hide Streamlit's default page list from sidebar */
    section[data-testid="stSidebar"] ul {
        display: none;
  }
  .stButton > button {
    width: 180px;
    padding: 0.8rem;
    border-radius: 10px;
    background-color: #656ED3;
    color: white;
    font-weight: 600;
    transition: background-color 0.2s;
  }
  .stButton > button:hover {
    background-color: #4E57C0;
  }
  .hero-image {
    max-width: 100%; height: auto;
  }
</style>
""", unsafe_allow_html=True)

# — 4) Hero section (mix markdown + columns + image)
with st.container():
    # raw HTML wrapper for flex
    st.markdown('<div class="hero-flex">', unsafe_allow_html=True)

    # left half: title + buttons
    left, right = st.columns([1,1])
    with left:
        st.markdown('<h1 class="hero-title">A Job Interview Chatbot<br>That Asks Like A Real Interviewer!</h1>',
                    unsafe_allow_html=True)

        # Buttons will now naturally sit under the heading
        if st.button("Login"):
            switch_page("login")
        if st.button("Create Account"):
            switch_page("createaccount")

    # right half: hero image
    with right:
        st.markdown(f'<img class="hero-image" src="data:image/svg+xml;base64,{svg_b64}" />',
                    unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
