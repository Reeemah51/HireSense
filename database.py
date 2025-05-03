import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from datetime import datetime
import uuid
# Initialize the database
def init_db():
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
    cursor = conn.cursor()
    # Create the users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    # Create Tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS account (
            account_id CHAR(10) PRIMARY KEY,
            username VARCHAR(50),
            password VARCHAR(50),
            email VARCHAR(100)
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        user_id CHAR(10) PRIMARY KEY,
        account_id CHAR(10),
        job_name VARCHAR(100),
        name VARCHAR(25),
        fieldOfWork VARCHAR(100),
        skills VARCHAR(500),
        education_level VARCHAR(55),
        workExperience TEXT,
        certifications TEXT,
        active INTEGER DEFAULT 1,
        created_at TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES account(account_id)
    )
""")


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
        feedback_id CHAR(10) PRIMARY KEY,
        session_id CHAR(10),
        communication_score FLOAT,
        problem_solving_score FLOAT,
        domain_knowledge_score FLOAT,
        confidence_score FLOAT,
        overall_score FLOAT,
        question VARCHAR(2000),
        strengths VARCHAR(2000),
        weaknesses VARCHAR(2000)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS live_chat (
            session_id CHAR(10) PRIMARY KEY,
            user_id CHAR(10),
            endTime DATE,
            startTime DATE,
            job_field TEXT,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS model (
            Model_id CHAR(10) PRIMARY KEY,
            Model_name VARCHAR(100),
            pretrained_model_path VARCHAR(100),
            tokenizer_list TEXT,
            language_list TEXT,
            sentiment_lexicon_list TEXT,
            context_history_list TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_title (
            job_name VARCHAR(100) PRIMARY KEY,
            job_field VARCHAR(100)
        )
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS specialties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    specialty_id INTEGER,
    difficulty TEXT,
    question TEXT,
    answer TEXT,
    FOREIGN KEY(specialty_id) REFERENCES specialties(id)
);
    """)
    #the followin alterations have been added through sql db browser code
    #cursor.execute("ALTER TABLE feedback ADD COLUMN communication_score FLOAT")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN problem_solving_score FLOAT")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN domain_knowledge_score FLOAT")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN confidence_score FLOAT")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN overall_score FLOAT")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN question VARCHAR(2000)")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN strengths VARCHAR(2000)")
    #cursor.execute("ALTER TABLE feedback ADD COLUMN weaknesses VARCHAR(2000)")    
    conn.commit()
    conn.close()
    

# Authenticate an existing user
def authenticate_user(username, password):
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_password = result[0]
        if check_password_hash(stored_password, password):
            return "Authentication successful!"
        else:
            return "Invalid password."
    else:
        return "User not found."

# Create a new user account
def create_account(username, email, password):
    try:
        conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
        cursor = conn.cursor()

        # Hash the password for security
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        # Insert user details into the database
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                       (username, email, hashed_password))
        conn.commit()
        conn.close()
        return "Account created successfully!"
    except sqlite3.IntegrityError as e:
        return f"Error: {e}"

# Fetch data helper
def fetch_data(query, params=None):
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result



def update_user_profile(user_id, first_name, last_name, email, level_of_education, contact_number, job_field, job_title, password):
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    cursor.execute("""
        UPDATE users
        SET username = ?, email = ?, password = ?
        WHERE id = ?
    """, (f"{first_name} {last_name}", email, hashed_password, user_id))
    conn.commit()
    conn.close()


def insert_user_profile(user_id, job_name, name, fieldOfWork, skills, education_level, workExperience, certifications):
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\HireSense2\database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user (user_id, job_name, name, fieldOfWork, skills, education_level, workExperience, certifications)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, job_name, name, fieldOfWork, skills, education_level, workExperience, certifications))
    conn.commit()
    conn.close()

