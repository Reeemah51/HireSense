import streamlit as st
from database import fetch_data, init_db, update_user_profile
from model import evaluate_user_response
from streamlit_extras.switch_page_button import switch_page
# ✅ MUST BE FIRST — Set page config
st.set_page_config(page_title="Edit Profile", layout="wide")
from database import insert_user_profile

# ✅ Initialize DB (after config)
init_db()

# ==== Theme Utilities ====
def get_categories():
    return fetch_data("SELECT id, name FROM categories WHERE name != 'Soft Skills'")

def get_specialties_by_category(category_id):
    return fetch_data("SELECT name FROM specialties WHERE category_id = ?", (category_id,))

st.markdown("""
<style>
/* Hide Streamlit's default page list from sidebar */
section[data-testid="stSidebar"] ul {
    display: none;
}
</style>
""", unsafe_allow_html=True)
def apply_theme(dark_mode: bool):
    if dark_mode:
        st.markdown("""<style>
            :root {
                --main-bg: linear-gradient(90deg, rgba(81,84,140,1) 0%, rgba(81,84,140,1) 35%, rgba(0,0,0,1) 91%);
                --text-color: #e0e0e0;
            }
            .stApp {
                background: var(--main-bg) !important;
                color: var(--text-color) !important;
            }
            [data-testid="stSidebar"] {
                background: #000000 !important;
                padding: 2rem 1.2rem !important;
                border-top-right-radius: 25px;
                border-bottom-right-radius: 25px;
            }
                [data-testid="stSidebar"] button {
                background-color: transparent !important;
                color: white !important;
                border: none !important;
                font-weight: bold;
            }
            [data-testid="stSidebar"] button:hover {
                background-color: rgba(255,255,255,0.1) !important;
            }
        </style>""", unsafe_allow_html=True)
    else:
        st.markdown("""<style>
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
                padding: 2rem 1.2rem !important;
                border-top-right-radius: 25px;
                border-bottom-right-radius: 25px;
            }
                [data-testid="stSidebar"] button {
                background-color: transparent !important;
                color: white !important;
                border: none !important;
                font-weight: bold;
            }
            [data-testid="stSidebar"] button:hover {
                background-color: rgba(255,255,255,0.1) !important;
            }
        </style>""", unsafe_allow_html=True)

def apply_custom_styles(dark_mode):
    apply_theme(dark_mode)

    dropdown_bg = "#1c1c26" if dark_mode else "white"
    dropdown_text = "white" if dark_mode else "black"
    arrow_color = "white" if dark_mode else "black"

    st.markdown(f"""
    <style>
        .stApp {{
            padding: 2rem;
            border-radius: 20px;
        }}
        input, select, textarea {{
            background-color: white !important;
            border: 1px solid #ccc !important;
            border-radius: 10px !important;
            padding: 10px !important;
            font-size: 16px !important;
        }}
        label {{
            font-weight: 600 !important;
            color: #4F378A !important;
        }}
        h2 {{
            color: #4F378A;
            text-align: center;
            font-size: 30px;
            margin-bottom: 30px;
        }}
        button[type="submit"] {{
            border-radius: 10px !important;
            padding: 0.6em 1.5em !important;
            font-weight: bold;
            background-color: white !important;
            color: #4F378A !important;
            border: 2px solid #AFB3FF !important;
        }}

        /* Dropdown (selectbox) styling */
        .stSelectbox > div > div {{
            background-color: white !important;
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid #ccc !important;
            padding: 10px !important;
            font-size: 16px !important;
        }}
        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: white !important;
        }}
        .stSelectbox svg {{
            color: {arrow_color} !important;
        }}
    </style>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        font-weight: bold;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: rgba(255,255,255,0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)
# ==== Main Profile Editor ====
def show_edit_profile():
    with st.sidebar:
        if st.button("Start New Chat"):
            switch_page("choosejob")
    dark_mode = st.sidebar.toggle("Enable Dark Mode", value=False)
    apply_custom_styles(dark_mode)
    st.markdown(f"""
        <style>
        /* Style Submit buttons inside forms */
        div.stButton > button {{
            background-color: white !important;
            color: #4F378A !important;
            border: 2px solid #AFB3FF !important;
            padding: 0.6em 1.5em !important;
            border-radius: 10px !important;
            font-weight: bold !important;
            transition: background-color 0.3s ease;
        }}

        div.stButton > button:hover {{
            background-color: #f3f4ff !important;
            color: #2f2f75 !important;
        }}
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h2>Edit Profile</h2>", unsafe_allow_html=True)

    categories = get_categories()
    category_names = [c[1] for c in categories]
    category_ids = {c[1]: c[0] for c in categories}

    if "selected_category" not in st.session_state:
        st.session_state.selected_category = category_names[0]

    with st.form(key="full_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name", value="")
        with col2:
            last_name = st.text_input("Last Name", value="")

        col3, col4 = st.columns(2)
        with col3:
            excluded_category = fetch_data("SELECT id FROM categories WHERE name = 'Soft Skills'")
            excluded_id = excluded_category[0][0] if excluded_category else -1
            all_specialties = fetch_data("SELECT name FROM specialties WHERE category_id != ?", (excluded_id,))
            specialty_names = [s[0] for s in all_specialties]

            if "selected_specialty" not in st.session_state or st.session_state.selected_specialty not in specialty_names:
                st.session_state.selected_specialty = specialty_names[0]

            selected_specialty = st.selectbox("Job Title", specialty_names, index=specialty_names.index(st.session_state.selected_specialty))
            st.session_state.selected_specialty = selected_specialty

        with col4:
            selected_category = st.selectbox("Job Field", category_names, index=category_names.index(st.session_state.selected_category))
            st.session_state.selected_category = selected_category

        email = st.text_input("Email", value="")
        level_of_education = st.selectbox("Level of Education", ["High School", "Associate Degree", "Bachelor degree", "Master's Degree", "PhD"], index=0)
        contact_number = st.text_input("Contact Number", value="")
        password = st.text_input("Password", type="password", value="")

        space1, col_cancel, space2, col_save, space3 = st.columns([1, 2, 8, 2, 1])
        with col_cancel:
            cancel = st.form_submit_button("Cancel")
        with col_save:
            save = st.form_submit_button("Save")

        if cancel:
            st.warning("Changes not saved.")
        if save:
            user_id = 1  # Replace with actual logged-in user ID
            try:
                update_user_profile(
                    user_id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    level_of_education=level_of_education,
                    contact_number=contact_number,
                    job_field=st.session_state.selected_category,
                    job_title=st.session_state.selected_specialty,
                    password=password
                )
                insert_user_profile(
                    user_id=1 ,
                    job_name=st.session_state.selected_specialty,
                    name=f"{first_name} {last_name}",
                    fieldOfWork=st.session_state.selected_category,
                    skills="",  # Add actual skills if available
                    education_level=level_of_education,
                    workExperience="",  # Optional field
                    certifications=""
                )
                st.success("✅ Profile updated successfully!")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")

# ✅ Always render the page when this file is loaded
show_edit_profile()
