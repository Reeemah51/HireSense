import streamlit as st
from database import fetch_data, init_db
import sqlite3
from datetime import datetime
import uuid

# Page Configuration
st.set_page_config(page_title="Chat UI", layout="wide")
init_db()

st.markdown("""
    <style>
    /* Hide Streamlit's default page list from sidebar */
    section[data-testid="stSidebar"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)
# Session States Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Dark Mode Toggle from Sidebar
dark_mode = st.sidebar.toggle("Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode

# Apply Theme Based on Dark Mode
def apply_theme(dark_mode: bool):
    if dark_mode:
        st.markdown("""
            <style>
            :root {
                --main-bg: linear-gradient(90deg, rgba(81,84,140,1) 0%, rgba(81,84,140,1) 35%, rgba(0,0,0,1) 91%);
                --text-color: #000000;
            }
            .stApp {
                background: var(--main-bg) !important;
                color: var(--text-color) !important;
            }
            [data-testid="stSidebar"] {
                background: #000000 !important;
                color: #000000 !important;
            }
            .recent-chat, .category-card, .profile-box {
                color: #000000 !important;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            :root {
                --main-bg: linear-gradient(180deg, #f0f3ff 0%, #cfd0ff 100%);
                --text-color: #000000;
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
            text-align: left;
        }
        .category-card, .recent-chat, .profile-box {
            width: 100%;
            margin-bottom: 20px;
            box-sizing: border-box;
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

        <!-- Categories -->
        <div class="category-card"><div class="category-label"><div class="color-dot" style="background-color:#f48fb1;"></div><span>Medical</span></div><span>⋯</span></div>
        <div class="category-card"><div class="category-label"><div class="color-dot" style="background-color:#81d4fa;"></div><span>Engineering</span></div><span>⋯</span></div>
        <div class="category-card"><div class="category-label"><div class="color-dot" style="background-color:#aed581;"></div><span>Technology</span></div><span>⋯</span></div>
        <div class="category-card"><div class="category-label"><div class="color-dot" style="background-color:#ffab91;"></div><span>Others</span></div><span>⋯</span></div>

        <!-- Recent Chats -->
        <div style="margin-top: 30px; font-size: 13px; font-weight: 600;">Recent Chats</div>
    """, unsafe_allow_html=True)

    recent_chats = fetch_data("SELECT session_id, job_field FROM live_chat ORDER BY startTime DESC LIMIT 5")
    if recent_chats:
        for chat in recent_chats:
            session_id, category = chat
            st.markdown(f"<div class='recent-chat'>🗨 {category} Session {session_id}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='recent-chat'>No recent chats found</div>", unsafe_allow_html=True)

    user_name_result = fetch_data("SELECT username FROM users WHERE id = 1")
    user_name = user_name_result[0][0] if user_name_result else "Guest"
    st.markdown(f"<div class='profile-box'>👤 {user_name}</div>", unsafe_allow_html=True)

# Chat Message Display
for msg in st.session_state.chat_history:
    st.markdown(f"<p style='margin-bottom:10px;'>🧑‍💻 You: {msg}</p>", unsafe_allow_html=True)

# Chat Bar Input and Send Button
with st.form("real_chat_bar", clear_on_submit=True):
    col1, col2 = st.columns([9, 1])

    with col1:
        user_message = st.text_input(
            "",
            key="chat_input_key",
            placeholder="Type your message...",
            label_visibility="collapsed"
        )

    with col2:
        send = st.form_submit_button("➤")

    if send and user_message.strip():
        st.session_state.chat_history.append(user_message)

        conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
        cursor = conn.cursor()
        now = datetime.now()
        selected_category = st.session_state.get("selected_category", "General")

        cursor.execute("SELECT session_id FROM live_chat WHERE session_id = ?", (st.session_state.session_id,))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO live_chat (session_id, user_id, job_field, startTime, endTime)
                VALUES (?, ?, ?, ?, ?)
            """, (st.session_state.session_id, "U001", selected_category, now, now))

        conn.commit()
        conn.close()

# Button and Input Styling
st.markdown("""
<style>
div[data-testid="stForm"] {
    position: fixed;
    bottom: 2.2rem;
    width: 67%;
    right: 2rem;
    background: transparent;
    z-index: 9999;
}
div[data-testid="stTextInput"] input {
    background: white;
    color: black;
    padding: 12px;
    border-radius: 12px;
    border: none;
}
button[kind="formSubmit"] {
    height: 48px;
    width: 48px;
    background-color: white !important;
    border-radius: 12px;
    border: 1px solid #ccc;
    color: black !important;
    font-size: 20px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)
