import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64
import os, sys

# Go up one directory from /pages to /HireSense2
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Now import from HireSense2 root
from database import fetch_data, init_db

init_db()

st.set_page_config(
    page_title="HireSense Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
/* Hide Streamlit's default page list from sidebar */
section[data-testid="stSidebar"] ul {
    display: none;
}
</style>
""", unsafe_allow_html=True)
############################
# 1) Dark Mode Toggle & Minimal Theming
############################
dark_mode = st.sidebar.toggle("Dark Mode", value=False)

if dark_mode:
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, rgba(81,84,140,1) 0%, rgba(0,0,0,1) 100%) !important;
        color: #e0e0e0 !important;
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
    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, rgba(236,239,255,1) 0%, rgba(207,208,255,1) 100%) !important;
        color: #000000 !important;
    }
    [data-testid="stSidebar"] {
        background: #7378C5 !important;
    }
    [data-testid="stSidebar"] button {
        background-color: #7378C5 !important;
        color: #ffffff !important;
        border: none !important;
        transition: background-color 0.3s ease;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #43467a !important;
    }
    </style>
    """, unsafe_allow_html=True)


############################
# 2) Title at the Top
############################
st.title("Dashboard")

############################
# 3) Prepare Data & Base64 Icons
############################
# Query your data
user_count_query = fetch_data("SELECT COUNT(*) FROM user WHERE active = 1")
total_users = user_count_query[0][0] if user_count_query else 0

feedback_count_query = fetch_data("SELECT COUNT(*) FROM feedback")
total_feedback = feedback_count_query[0][0] if feedback_count_query else 0

recent_users_query = fetch_data("SELECT COUNT(*) FROM user WHERE active = 1 AND created_at >= datetime('now', '-7 days')")
recent_users = recent_users_query[0][0] if recent_users_query else 0

previous_users_query = fetch_data("SELECT COUNT(*) FROM user WHERE active = 1 AND created_at BETWEEN datetime('now', '-14 days') AND datetime('now', '-7 days')")
previous_users = previous_users_query[0][0] if previous_users_query else 0

if previous_users > 0:
    growth_percentage = ((recent_users - previous_users) / previous_users) * 100
    user_growth = f"+{growth_percentage:.0f}%"
else:
    user_growth = "+0%"

# Helper to encode local images (icons) as base64 so they work inside an iframe
def to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Encode your local icon images (adjust paths accordingly)
icon_users_b64 = to_base64(r"C:\Users\Administrator\Desktop\HireSense2\img\dashuser_icon.png")
icon_feedback_b64 = to_base64(r"C:\Users\Administrator\Desktop\HireSense2\img\chart_icon.png")
icon_growth_b64 = to_base64(r"C:\Users\Administrator\Desktop\HireSense2\img\graph_icon.png")

############################
# 4) Inline HTML + CSS for 3 Metric Cards
############################
# Hard-code gauge percentages for demonstration
gauge_users = 81
gauge_fb = 62
try:
    gauge_growth = int(user_growth.replace("+", "").replace("%", ""))
except:
    gauge_growth = 44

html_cards = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      margin: 0; padding: 0;
      font-family: Arial, sans-serif;
      background: transparent;
      color: #000;
    }}
    .cards-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      padding: 10px;
    }}
    .nice-card {{
      background-color: #ffffff;
      color: #000000;
      border-radius: 20px;
      padding: 20px;
      margin: 10px;
      width: 200px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .card-content {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      margin-right: 10px;
    }}
    .icon-container img {{
      width: 35px;
      height: 35px;
      margin-bottom: 10px;
    }}
    .metric-title {{
      font-size: 18px;
      margin: 0;
      font-weight: 600;
    }}
    .metric-value {{
      font-size: 22px;
      font-weight: bold;
      margin: 5px 0 2px 0;
    }}
    .metric-subtitle {{
      font-size: 12px;
      color: #666;
      margin: 0;
    }}
    .donut-chart {{
      position: relative;
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: conic-gradient(#4e79a7 calc(var(--gauge-percent)*1%), #eeeeee 0);
    }}
    .donut-center {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 14px;
      font-weight: bold;
      color: #00000;
    }}
    .my-dashboard-card {{
      background-color: #ffffff;
      border-radius: 20px;
      padding: 20px;
      margin: 30px 10px 20px 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
   }}
    
    /* Table styling for updates inside the card */
    .updates-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: Arial, sans-serif;
      margin-top: 10px;
   }}
    .updates-table th,
    .updates-table td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }}
    .updates-table th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>
<body>
<div class="cards-container">

  <!-- Card 1: Users -->
  <div class="nice-card" style="--gauge-percent:{gauge_users};">
    <div class="card-content">
      <div class="icon-container">
        <img src="data:image/png;base64,{icon_users_b64}" alt="Users Icon">
      </div>
      <span class="metric-title">Total Active Users</span>
      <span class="metric-value">{total_users}</span>
      <span class="metric-subtitle">Last 24 hours</span>
    </div>
    <div class="donut-chart">
      <div class="donut-center">{gauge_users}%</div>
    </div>
  </div>

  <!-- Card 2: Feedback -->
  <div class="nice-card" style="--gauge-percent:{gauge_fb};">
    <div class="card-content">
      <div class="icon-container">
        <img src="data:image/png;base64,{icon_feedback_b64}" alt="Feedback Icon">
      </div>
      <span class="metric-title">Feedback Generated</span>
      <span class="metric-value">{total_feedback}</span>
      <span class="metric-subtitle">Last 24 hours</span>
    </div>
    <div class="donut-chart">
      <div class="donut-center">{gauge_fb}%</div>
    </div>
  </div>

  <!-- Card 3: Growth -->
  <div class="nice-card" style="--gauge-percent:{gauge_growth};">
    <div class="card-content">
      <div class="icon-container">
        <img src="data:image/png;base64,{icon_growth_b64}" alt="Growth Icon">
      </div>
      <span class="metric-title">User Growth Rate</span>
      <span class="metric-value">{user_growth}</span>
      <span class="metric-subtitle">Last 24 hours</span>
    </div>
    <div class="donut-chart">
      <div class="donut-center">{gauge_growth}%</div>
    </div>
  </div>

</div>

</body>
</html>
"""

# Render as an iframe
components.html(html_cards, height=300, scrolling=False)

# Make sure your CSS for .my-dashboard-card and .updates-table
# is inserted into the global environment, not the iframe.

st.markdown("""
<style>
.my-dashboard-card {
  background-color: #ffffff;
  border-radius: 20px;
  padding: 20px;
  margin: 30px 10px 20px 10px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.updates-table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
  margin-top: 10px;
}
.updates-table th,
.updates-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
.updates-table th {
  background-color: #f2f2f2;
}
</style>
""", unsafe_allow_html=True)

# Now query the data
questions_data = fetch_data("""
    SELECT
      q.question                            AS question,
      c.name                                AS category,
      jt.job_name                           AS job_name,
      q.difficulty                          AS difficulty,
      date('now')                           AS last_updated
    FROM questions q
    JOIN specialties s ON q.specialty_id = s.id
    JOIN categories  c ON s.category_id   = c.id
    LEFT JOIN job_title  jt
      ON jt.job_field = c.name
    ORDER BY q.id DESC
    LIMIT 5
""")
if questions_data:
    df = pd.DataFrame(
        questions_data,
        columns=["Question", "Category", "Job Title", "Difficulty", "Last Updated"]
    )
    html_table = df.to_html(classes="updates-table", index=False, border=0)
else:
    html_table = "<p>No data available in the questions table.</p>"

updates_html = f"""
<div class="my-dashboard-card">
  <h2>Database Updates</h2>
  {html_table}
</div>
"""


# Render the dynamic card
st.markdown(updates_html, unsafe_allow_html=True)

##############################
# 7) Sidebar Navigation
##############################
if dark_mode:
    logo_path = r"C:\Users\Administrator\Desktop\HireSense2\img\Rectangle.svg"
    nav_items = [
        ("Dashboard", "dashboard", r"C:\Users\Administrator\Desktop\HireSense2\img\screen_dark.png"),
        ("Users", "users", r"C:\Users\Administrator\Desktop\HireSense2\img\user_dark.png"),
        ("Manage Database", "manage_database", r"C:\Users\Administrator\Desktop\HireSense2\img\db_dark.png"),
        ("Messages", "messages", r"C:\Users\Administrator\Desktop\HireSense2\img\message_dark.png"),
        ("Feedback", "feedback", r"C:\Users\Administrator\Desktop\HireSense2\img\file_dark.png"),
        ("Settings", "settings", r"C:\Users\Administrator\Desktop\HireSense2\img\settings_dark.png"),
    ]
else:
    logo_path = r"C:\Users\Administrator\Desktop\HireSense2\img\Rectangle.svg"
    nav_items = [
        ("Dashboard", "dashboard", r"C:\Users\Administrator\Desktop\HireSense2\img\dashboard_light.png"),
        ("Users", "users", r"C:\Users\Administrator\Desktop\HireSense2\img\user_light.png"),
        ("Manage Database", "manage_database", r"C:\Users\Administrator\Desktop\HireSense2\img\db_light.png"),
        ("Messages", "messages", r"C:\Users\Administrator\Desktop\HireSense2\img\message_lights.png"),
        ("Feedback", "feedback", r"C:\Users\Administrator\Desktop\HireSense2\img\feedback_light.png"),
        ("Settings", "settings", r"C:\Users\Administrator\Desktop\HireSense2\img\settings_light.png"),
    ]

st.sidebar.image(logo_path, width=120)
for label, page_value, icon_path in nav_items:
    cols = st.sidebar.columns([0.2, 0.8])
    with cols[0]:
        st.image(icon_path, width=20)
    with cols[1]:
        if st.button(label, key=label):
            st.query_params["page"] = page_value

st.sidebar.markdown("<hr style='margin: 1rem 0;'>", unsafe_allow_html=True)

# Log Out Button
if st.sidebar.button("Log Out"):
    st.switch_page("pages/login.py")  # Adjust if your login file is named differently
query_params = st.query_params
page = query_params.get("page", ["dashboard"])[0]
