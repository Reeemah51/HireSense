import os, sys

# move one level up from pages/ back into your HireSense2 folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# 2) now you can import database as if it were top-level
from database import init_db, fetch_data
import streamlit as st 
from streamlit_extras.switch_page_button import switch_page

# Page Configuration
st.set_page_config(page_title="Interview Question Fetcher", layout="wide")
init_db()
st.markdown("""
    <style>
    /* Hide Streamlit's default page list from sidebar */
    section[data-testid="stSidebar"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)
# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

dark_mode = st.sidebar.toggle("Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode

# Theme Styling
def apply_theme(dark_mode: bool):
    if dark_mode:
        st.markdown("""
            <style>
            :root {
                --main-bg: linear-gradient(90deg, rgba(81,84,140,1) 0%, rgba(81,84,140,1) 35%, rgba(0,0,0,1) 91%);
                --text-color: #e0e0e0;
                --btn-bg: #444;
                --btn-hover: #666;
                --btn-text: #fff;
            }
            .stApp {
                background: var(--main-bg) !important;
                color: var(--text-color) !important;
            }
            [data-testid="stSidebar"] {
                background: #000000 !important;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            :root {
                --main-bg: linear-gradient(180deg, #f0f3ff 0%, #cfd0ff 100%);
                --text-color: #000000;
                --btn-bg: #1976d2;
                --btn-hover: #135ba1;
                --btn-text: #fff;
            }
            .stApp {
                background: var(--main-bg) !important;
                color: var(--text-color) !important;
            }
            [data-testid="stSidebar"] {
                background: #51548c !important;
            }
            </style>
        """, unsafe_allow_html=True)

apply_theme(dark_mode)

# Sidebar Layout
with st.sidebar:
    if st.button("Edit Profile"):
        switch_page("editprofile")
    new_chat = st.button("Start a New Chat", key="new_chat_btn")

    st.markdown("""
        <style>
        [data-testid="stSidebar"] button[kind="secondary"] {
            background-color: white;
            color: #333;
            border: none;
            border-radius: 25px;
            padding: 10px 16px;
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 15px;
            width: 100%;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.08);
            text-align: left;
        }
        .category-card, .recent-chat, .profile-box {
            width: 100%;
            margin-bottom: 20px;
            box-sizing: border-box;
            color: #000000 !important;
        }
        .category-card {
            background-color: white;
            padding: 10px 15px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 14px;
            font-weight: 500;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        }
        .category-label {
            display: flex;
            align-items: center;
        }
        .color-dot {
            width: 4px;
            height: 30px;
            border-radius: 6px;
            margin-right: 10px;
        }
        .recent-chat {
            background-color: white;
            padding: 10px 12px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 400;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
        }
        .profile-box {
            background-color: white;
            padding: 10px 16px;
            border-radius: 25px;
            text-align: center;
            font-size: 13px;
            font-weight: 500;
            margin-top: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        }
        </style>
    """, unsafe_allow_html=True)


    recent_chats = fetch_data("SELECT session_id FROM live_chat ORDER BY startTime DESC LIMIT 5")
    if recent_chats:
        for chat in recent_chats:
            st.markdown(f"<div class='recent-chat'>🗨 Session {chat[0]} ⋯</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='recent-chat'>No recent chats found</div>", unsafe_allow_html=True)

    user_name_result = fetch_data("SELECT username FROM users WHERE id = 1")
    user_name = user_name_result[0][0] if user_name_result else "Guest"
    st.markdown(f"<div class='profile-box'>👤 {user_name}</div>", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div style='text-align:center'>
        <h1 style='margin-bottom:0;'>How can we assist you today?</h1>
        <p style='font-size: 1.1rem;'>Get expert help powered by AI for job interview preparation. Choose the job field that aligns with your career goals and start practising tailored interview questions with ease.</p>
    </div>
""", unsafe_allow_html=True)

# Category Cards Section
category_info = {
    "Business": "Learn how to prepare for business job interviews, including finance, HR, and strategy questions.",
    "Technology": "Practice for tech interviews with guidance on coding, system design and key topics.",
    "Engineering": "Get help to prepare for engineering job interviews with tips on technical question and problem-solving.",
    "Medical": "Learn how to prepare for medical job interviews, including patient care and common questions."
}

categories = fetch_data("SELECT id, name FROM categories")
category_map = {name: cid for cid, name in categories if name in category_info}
cols = st.columns(4)

for i, (cat_name, cat_id) in enumerate(category_map.items()):
    with cols[i % 4]:
        with st.container():
            description = category_info.get(cat_name, "")
            st.markdown(f"""
                <div class='custom-card'>
                    <h4>{cat_name}</h4>
                    <p>{description}</p>
            """, unsafe_allow_html=True)
            specialties = fetch_data("SELECT id, name FROM specialties WHERE category_id = ?", (cat_id,))
            spec_map = {name: sid for sid, name in specialties}
            if spec_map:
                selected_specialty = st.selectbox(f"Select a {cat_name} Specialty", [""] + list(spec_map.keys()), key=f"spec_{cat_id}")
                if selected_specialty:
                    st.session_state.selected_specialty_id = spec_map[selected_specialty]
                    st.session_state.selected_category = cat_name
                    st.session_state.username = user_name
                    switch_page("interview_chat")
            st.markdown("</div>", unsafe_allow_html=True)

# Styling
st.markdown("""
<style>
.custom-card {
    background-color: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.06);
    min-height: 240px;
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.custom-card h4 {
    margin: 0 0 10px 0;
    color: #2e2e2e;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
}
.custom-card p {
    font-size: 12px;
    color: #444;
    text-align: center;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)
