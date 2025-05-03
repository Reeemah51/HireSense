import streamlit as st
import pandas as pd
import re
from together import Together
import plotly.graph_objects as go
import random
import sqlite3

#database config
db_path=r"C:\Users\Administrator\Desktop\HireSense2\database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
#def fetch_qa_from_db(db_path):
 #   cursor.execute("SELECT question, user_answer FROM live_chat WHERE user_id = ?", (1,))  # Adjust user_id as needed
 #   rows = cursor.fetchall()
 #   conn.close()
 #   return {q: a for q, a in rows if q and a}

# --- إعداد API ---
together_ai_key = "415f1c0f6cdf2b59fc0d758e5f896c49dae73272fda8fbea64ae8b71abc42910"
client = Together(api_key=together_ai_key)
st.set_page_config(page_title="Your Interview Feedback", layout="wide")
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

st.markdown("""
<style>
/* Hide Streamlit's default page list from sidebar */
section[data-testid="stSidebar"] ul {
    display: none;
}
</style>
""", unsafe_allow_html=True)
# Toggle for dark mode in sidebar
dark_mode = st.sidebar.toggle("Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode  # Update session state
# --- تهيئة الصفحة ---


# ---------- Session State Initialization ----------
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Performance"

# ---------- Sidebar Navigation ----------
st.sidebar.image(r"C:\Users\Administrator\Desktop\HireSense2\img\Rectangle.svg", use_container_width=True)
def nav_button(label, image_path, key):
    cols = st.sidebar.columns([1, 4])
    with cols[0]:
        st.image(image_path, width=100)  # Adjust width if needed
    with cols[1]:
        clicked = st.button(label, key=key)
    if clicked:
        st.session_state.selected_page = label
    return clicked

 

# Image URLs (could be local paths or online links)
nav_button("Performance", r"C:\Users\Administrator\Desktop\HireSense2\img\arrow.png", "perf_btn")
nav_button("Tips", r"C:\Users\Administrator\Desktop\HireSense2\img\bulb.png", "tips_btn")
nav_button("Summary", r"C:\Users\Administrator\Desktop\HireSense2\img\book.png", "summary_btn")
# --- Logout button ---
st.markdown("""<hr style="border:1px solid #ccc; margin:20px 0;">""", unsafe_allow_html=True)

logout_col = st.sidebar.columns([1, 4])
with logout_col[0]:
    st.image(r"C:\Users\Administrator\Desktop\HireSense2\img\user_dark.png", width=100)  # Make sure this image exists
with logout_col[1]:
    if st.button("Logout", key="logout_btn"):
        st.switch_page("pages/login.py")  # Use your actual login page name here

# Detect manual query param changes
query_params = st.query_params
if "page" in query_params:
    page_param = query_params["page"][0] if isinstance(query_params["page"], list) else query_params["page"]
    if page_param in ["Performance", "Tips", "Summary"]:
        st.session_state.selected_page = page_param

# --- ستايل حسب الوضع المختار ---
if dark_mode:
    st.markdown("""
        <style>
        
        :root {
            --bg-gradient: linear-gradient(90deg, rgba(81,84,140,1) 0%, rgba(81,84,140,1) 35%, rgba(0,0,0,1) 91%);
            --text-color: #FFFFFF;
            --dropdown-color: #000000;
        }
        
        .stApp {
            background: var(--bg-gradient) !important;
            color: var(--text-color) !important;
        }
        .my-dashboard-card-dark {
            background-color: #000000;  /* black card background */
            border-radius: 16px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(255,255,255,0.05);
            color: #e0e0e0;
        }
        .my-dashboard-card-dark h2 {
            color: #5B5BD6;
            margin-bottom: 15px;
        }
        [data-testid="stSidebar"] {
            background: #000000 !important;
        }
        [data-testid="stSidebar"] button {
        background-color: #000000 !important;
        color: #e0e0e0 !important;
        border: none !important;
        transition: background-color 0.3s ease;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #1a1a1a !important;
        }
            .stTable th, .stTable td {
            color: #5B5BD6 !important;
            border: 1px solid #5B5BD6 !important;
        }
        .my-table-card {
            background-color: #000000;  /* black background */
            border-radius: 16px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            color: #FFFFFF; /* dark text for contrast */
        }
        .my-table-card h2 {
            color: #5B5BD6;
            margin-bottom: 15px;
        }
        /* Dropdown color override */
        div[data-baseweb="select"] > div {
            background-color: #000000 !important;
            color: white !important;
            border-radius: 8px;
        }
        .updates-table {
            width: 100%;
            border-collapse: collapse;
        }
        .updates-table th,
        .updates-table td {
            padding: 12px;
        
            text-align: left;
            vertical-align: top;
            word-wrap: break-word;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        :root {
            --bg-gradient: linear-gradient(90deg, rgba(175,179,255,1) 0%, rgba(175,179,255,1) 35%, rgba(255,255,255,1) 92%);
            --text-color: #000000;
            --dropdown-color: #ffffff !important;
        }
        .stApp {
            background: var(--bg-gradient) !important;
            color: var(--text-color) !important;
        }
        [data-testid="stSidebar"] {
            background: #7378C5 !important;
        }
        /* Dropdown color override */
        div[data-baseweb="select"] > div {
        background-color: #7378C5 !important;
        color: white !important;
        border-radius: 8px;
        }
        /* Sidebar buttons - light mode */
        [data-testid="stSidebar"] button {
            background-color: #7378C5 !important;
            color: #ffffff !important;
            border: none !important;
            transition: background-color 0.3s ease;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #43467a !important;
        }
        .stTable th, .stTable td {
            color: #5B5BD6 !important;
            border: 1px solid #5B5BD6 !important;
        }
        .my-dashboard-card {
            background-color: #ffffff;  /* white background */
            border: 1px solid #5B5BD6;
            border-radius: 16px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            color: #2c3e50; /* dark text for contrast */
        }
        .my-dashboard-card h2 {
            color: #5B5BD6;
            margin-bottom: 15px;
        }
        .updates-table {
            width: 100%;
            border-collapse: collapse;
        }
        .updates-table th,
        .updates-table td {
            padding: 12px;
            border: 1px solid #5B5BD6;
            text-align: left;
            vertical-align: top;
            word-wrap: break-word;
        }
        </style>
    """, unsafe_allow_html=True)

# --- دوال المساعدة ---
def extract_percentage(text, label):
    pattern = rf"\*\*{label}.*?\*\*\s*\(?(\d+)%\)?"
    match = re.search(pattern, text, re.IGNORECASE)
    return int(match.group(1)) if match else None

def evaluate_answer(question, user_answer):
    prompt = f"""
    You are an AI evaluator analyzing interview answers.
    Assess the response based on:
    - communication skills
    - problem solving skills
    - domain knowledge
    - confidence
    - Strengths in the answer
    - Weaknesses in the answer
    - Tips for an ideal answer

    Provide feedback in this structured format:
    - **overall score of performance** (in %)
    - **communication level** (in %)
    - **problem solving level** (in %)
    - **domain knowledge** (in %)
    - **confidence** (in %)
    - **Strengths:** (List strength points)
    - **Weaknesses:** (List weak points)
    - **Tips:** (list tips)
    - **Summary:** (General evaluation summary of this answer in a paragraph of 5 sentences)
    - **Question:** {question}
    - **User's Answer:** {user_answer}
    """
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": "You are a professional evaluator for a job interview assessment."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- البيانات ---
#########################################replace with #qa_dict = fetch_qa_from_db()#

if "chat_history" in st.session_state and st.session_state.chat_history:
    qa_dict = {
        entry["question"]: entry["user_answer"]
        for entry in st.session_state.chat_history
    }
else:
    st.error("No chat history found. Please complete an interview session first.")
    qa_dict = {}  # Prevent crash

# --- التقييم ---
score_totals = {"overall": 0, "communication": 0, "problem_solving": 0, "domain_knowledge": 0, "confidence": 0}
feedback_data = []
num_evaluated = 0

for q, a in qa_dict.items():
    result = evaluate_answer(q, a)
    overall = extract_percentage(result, "overall score of performance")
    communication = extract_percentage(result, "communication level")
    problem_solving = extract_percentage(result, "problem solving level")
    domain_knowledge = extract_percentage(result, "domain knowledge")
    confidence = extract_percentage(result, "confidence")

    if None not in [overall, communication, problem_solving, domain_knowledge, confidence]:
        score_totals["overall"] += overall
        score_totals["communication"] += communication
        score_totals["problem_solving"] += problem_solving
        score_totals["domain_knowledge"] += domain_knowledge
        score_totals["confidence"] += confidence
        num_evaluated += 1

    strengths = re.search(r"\*\*Strengths:\*\*(.*?)\*\*", result, re.DOTALL | re.IGNORECASE)
    weaknesses = re.search(r"\*\*Weaknesses:\*\*(.*?)\*\*", result, re.DOTALL | re.IGNORECASE)
    tips = re.search(r"\*\*Tips:\*\*(.*?)\*\*", result, re.DOTALL | re.IGNORECASE)
    summary_match = re.search(r"\*\*Summary:\*\*(.*?)($|\*\*)", result, re.DOTALL | re.IGNORECASE)

    feedback_data.append({
        "Question": q,
        "Strengths": strengths.group(1).strip() if strengths else "",
        "Weaknesses": weaknesses.group(1).strip() if weaknesses else "",
        "Tips": tips.group(1).strip() if tips else "",
        "Summary": summary_match.group(1).strip() if summary_match else ""
    })

average = {k: round(v / num_evaluated, 2) for k, v in score_totals.items()} if num_evaluated else {k: 0 for k in score_totals}
feedback_df = pd.DataFrame(feedback_data)
avr_overall =average["overall"]
# --- صفحات التطبيق ---
page = st.session_state.selected_page
if page == "Performance":
    st.markdown("<h1 style='color:#e0e0e0;'>Your Interview Feedback</h1>" if dark_mode 
                else "<h1 style='color:#34495e;'>Your Interview Feedback</h1>",
                 unsafe_allow_html=True)

    colA, colB = st.columns([1, 1])
    with colA:
        st.selectbox("Time Frame:", ["All-time", "Last 6 months", "Last month"])
    with colB:
        st.selectbox("Job Title:", ["IT Specialist", "Data Scientist", "Software Engineer"])

    col1, col2 = st.columns([1.2, 2])
    with col1:
        st.markdown("### Overall Score")
        donut_colors = ["#000000", "#FFFFFF"] if dark_mode else ["#7378C5", "#FFFFFF"]
        donut = go.Figure(data=[go.Pie(
            labels=["Performance", "Remaining"],
            values=[avr_overall, 100 - avr_overall],
            hole=0.6,
            marker=dict(colors=donut_colors),
            textinfo='none'
        )])

        donut.update_layout(showlegend=False, height=250, margin=dict(t=0, b=0, l=0, r=0),
                            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        donut.add_annotation(text=f"{avr_overall}%", font_size=32, showarrow=False, x=0.5, y=0.5)
        st.plotly_chart(donut, use_container_width=True)
        st.caption("Your overall performance demonstrates a good understanding of key skills. Keep practicing to improve!")

    with col2:
        st.markdown("### Skills Evaluation")
        skill_cols = st.columns(4)
        skills = {
            "Communication": average["communication"],
            "Problem Solving": average["problem_solving"],
            "Domain Knowledge": average["domain_knowledge"],
            "Confidence": average["confidence"]
        }
    # Set style variables based on mode
    card_bg = "#000000" if dark_mode else "#FFFFFF"
    title_color = "#ffffff" if dark_mode else "#2c3e50"
    value_color = "#ffffff" if dark_mode else "#2E0854"

    for i, (label, value) in enumerate(skills.items()):
        with skill_cols[i]:
            st.markdown(
                f"<div style='background-color: {card_bg}; border-radius: 12px; padding: 20px; text-align: center;'>"
                f"<h4 style='color: {title_color};'>{label}</h4>"
                f"<p style='font-size: 20px; font-weight: bold; color: {value_color};'>{value}%</p></div>",
                unsafe_allow_html=True
            )

        # --- بطاقة Detailed Feedback ---
    if not feedback_df.empty:
        feedback_df[["Question", "Strengths", "Weaknesses"]] = feedback_df[["Question", "Strengths", "Weaknesses"]].replace({"\n": " ", "-": " "}, regex=True)
        table_html = feedback_df[["Question", "Strengths", "Weaknesses"]].to_html(
            classes="updates-table", index=False, border=0, escape=False
        )
        detailed_feedback_card = f"""
        <div class="{ 'my-dashboard-card-dark' if dark_mode else 'my-dashboard-card' }">
            <h2>Detailed Feedback</h2>
            {table_html}
        </div>
        """
    else:
        detailed_feedback_card = """
        <div class="my-dashboard-card">
            <h2>Detailed Feedback</h2>
            <p>No feedback available yet.</p>
        </div>
        """
    st.markdown(detailed_feedback_card, unsafe_allow_html=True)

    for index, row in feedback_df.iterrows():
        cursor.execute('''
        INSERT INTO feedback (
            communication_score,
            problem_solving_score,
            domain_knowledge_score,
            confidence_score,
            overall_score,
            question,
            strengths, 
            weaknesses           
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', 
        (
            skills["Communication"],
            skills["Problem Solving"],
            skills["Domain Knowledge"],
            skills["Confidence"],
            avr_overall,
            row["Question"],
            row["Strengths"],
            row["Weaknesses"]
        ))
    conn.commit()
    conn.close()

elif page == "Tips":
    st.title("Interview Tips")
    all_tips = set()  # Use a set to automatically remove duplicates

    for index, row in feedback_df.iterrows():
        tips_list = re.split(r"[\n•\-]+", row['Tips'])
        cleaned = [tip.strip() for tip in tips_list if tip.strip()]
        all_tips.update(cleaned)  # Add to set instead of list

    all_tips = list(all_tips)  # Convert back to list for sampling

    if all_tips:
        random_tips = random.sample(all_tips, min(len(all_tips), 10))
        for tip in random_tips:
            st.markdown(f"- {tip}")
    else:
        st.info("No tips available yet.")


elif page == "Summary":
    st.title("Interview Summary")
    for index, row in feedback_df.iterrows():
        st.markdown(f"**Q:** {row['Question']}")

        summary_text = row['Summary']

        if isinstance(summary_text, str):
            summary_text = summary_text.strip("{}")
            points = re.split(r"[\n\-]+", summary_text)
            cleaned_points = [point.strip() for point in points if point.strip()]
            combined_text = " ".join(cleaned_points)

            st.markdown(combined_text)

        else:
            st.markdown("No summary available.")

        st.markdown("---")

