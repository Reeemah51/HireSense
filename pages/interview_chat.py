# ------------------------ interview_chat.py ------------------------
import streamlit as st
from database import fetch_data, init_db
from model import evaluate_user_response
from datetime import datetime
import sqlite3
import uuid
from streamlit_extras.switch_page_button import switch_page
# ---------------- INIT ------------------
st.set_page_config(page_title="Interview Chat", layout="wide")
init_db()
st.markdown("""
<style>
/* Hide Streamlit's default page list from sidebar */
section[data-testid="stSidebar"] ul {
    display: none;
}
</style>
""", unsafe_allow_html=True)
# ---------------- SESSION STATE ------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "selected_specialty_id" not in st.session_state:
    st.session_state.selected_specialty_id = None
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "General"

# ---------------- THEMING ------------------
def apply_theme(dark_mode):
    if dark_mode:
        st.markdown("""
        <style>
        .stApp { background: linear-gradient(90deg, #51548c 0%, #000000 90%) !important; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp { background: linear-gradient(180deg, #f0f3ff 0%, #cfd0ff 100%) !important; }
        </style>
        """, unsafe_allow_html=True)
apply_theme(st.session_state.dark_mode)

# ---------------- SIDEBAR ------------------
st.sidebar.toggle("Dark Mode", value=st.session_state.dark_mode, key="dark_mode_toggle")
if st.sidebar.button("Start a New Chat"):
    for key in ["chat_history", "current_question_index", "questions"]:
        st.session_state[key] = [] if key != "current_question_index" else 0

st.sidebar.markdown("""
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

recent_chats = fetch_data("SELECT session_id, job_field FROM live_chat ORDER BY startTime DESC LIMIT 5")
st.sidebar.markdown("""<div style='font-size: 13px; font-weight: 600;'>Recent Chats</div>""", unsafe_allow_html=True)
for chat in recent_chats:
    st.sidebar.markdown(f"<div class='recent-chat'>🗨 {chat[1]} Session {chat[0]}</div>", unsafe_allow_html=True)

# ---------------- QUESTIONS ------------------
def get_questions_by_specialty_and_softskills(specialty_id, softskills_id=6, limit_each=5):
    query = """
    SELECT question, answer FROM questions
    WHERE specialty_id = ?
    ORDER BY RANDOM()
    LIMIT ?
    """
    softskills = fetch_data(query, (softskills_id, limit_each))
    specialty = fetch_data(query, (specialty_id, limit_each))
    return [
        {"question": row[0], "answer": row[1]} for row in (softskills + specialty)
    ]

if st.session_state.selected_specialty_id and not st.session_state.questions:
    st.session_state.questions = get_questions_by_specialty_and_softskills(st.session_state.selected_specialty_id)

# ---------------- MAIN CHAT DISPLAY ------------------
st.markdown("""
<style>
.bubble-left {
    background: #f2f2f2;
    padding: 10px 15px;
    border-radius: 16px;
    width: fit-content;
    margin: 8px 0;
    color: #333;
    font-size: 15px;
}
.bubble-right {
    background: #d2e3fc;
    padding: 10px 15px;
    border-radius: 16px;
    width: fit-content;
    margin: 8px 0 8px auto;
    color: #000;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

for msg in st.session_state.chat_history:
    st.markdown(f"<div class='bubble-left'>🤖 Q: {msg['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bubble-right'>🧑‍💻 {msg['answer']}</div>", unsafe_allow_html=True)

questions = st.session_state.questions
idx = st.session_state.current_question_index

if questions and idx < len(questions):
    q = questions[idx]["question"]
    a = questions[idx]["answer"]
    st.markdown(f"<div class='bubble-left'><b>Q{idx+1}:</b> {q}</div>", unsafe_allow_html=True)
else:
    if questions:
        st.success("🎉 Interview Complete!")
        total_score = sum([msg['score'] for msg in st.session_state.chat_history])
        total_keywords = sum([msg['keywords'] for msg in st.session_state.chat_history])
        avg_score = total_score / len(st.session_state.chat_history)
        st.info(f"Your average professionalism score: {round(avg_score * 100, 2)}%")
        st.info(f"Total keywords matched: {total_keywords}")

        def save_chat_session():
            conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
            cursor = conn.cursor()
            now = datetime.now()
            session_id = st.session_state.session_id
            cursor.execute("SELECT session_id FROM live_chat WHERE session_id = ?", (session_id,))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO live_chat (session_id, user_id, job_field, startTime, endTime)
                    VALUES (?, ?, ?, ?, ?)
                """, (session_id, "U001", st.session_state.selected_category, now, now))
            for entry in st.session_state.chat_history:
                cursor.execute("""
                    INSERT INTO feedback (session_id, professionalismScore)
                    VALUES (?, ?)
                """, (session_id, entry["score"]))
            conn.commit()
            conn.close()

        save_chat_session()
        if st.button("View Feedback Report"):
            switch_page("feedback_report")
        if st.button("Restart Interview"):
            for k in ["questions", "chat_history", "current_question_index"]:
                del st.session_state[k]
            st.rerun()

# ---------------- INPUT FORM ------------------
with st.form("real_chat_bar", clear_on_submit=True):
    col1, col2 = st.columns([9, 1])
    with col1:
        user_message = st.text_input("", key="chat_input_key", placeholder="Type your message...", label_visibility="collapsed")
    with col2:
        send = st.form_submit_button("➤")

    if send and user_message.strip():
        if idx < len(questions):
            answer, score, keyword_count = evaluate_user_response(user_message, q, a)
            st.session_state.chat_history.append({
                "question": q,
                "user_answer": user_message,
                "answer": answer,
                "score": score,
                "keywords": keyword_count
            })
            st.session_state.current_question_index += 1
            st.rerun()
