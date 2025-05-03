import pandas as pd
import re
# Import the lists of dictionaries from the three files.
# These files are assumed to define a variable named `data` containing the list of dictionaries.
from AI_questions import data as ai_data
from It_questions import data as it_data
from webdevloper_questions import data as webdev_data
from data_science import data as dsdata
# Combine all dictionaries into one list
combined_data = ai_data + it_data + webdev_data + dsdata

# Drop the ID key if it exists in any dictionary.
for entry in combined_data:
    entry.pop("ID", None)
    entry.pop("id", None)

# Normalize keys so that all entries have the same column names.
# The AI_questions data uses lowercase keys while the others use title-case.
def normalize_keys(entry):
    # Create a new dictionary with keys standardized to: Category, Specialty, Difficulty, Question, Answer
    return {
        "Category": entry.get("Category") or entry.get("category"),
        "Specialty": entry.get("Specialty") or entry.get("specialty"),
        "Difficulty": entry.get("Difficulty") or entry.get("difficulty"),
        "Question": entry.get("Question") or entry.get("question"),
        "Answer": entry.get("Answer") or entry.get("answer")
    }
def clean_text(text):
    if text is None:
        return ""
    # Replace newline characters with a space
    text = text.replace('\n', ' ')
    # Replace multiple whitespace (spaces, tabs, etc.) with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove non-letter characters (anything not A–Z)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Strip leading/trailing whitespace
    return text.strip()

normalized_data = [normalize_keys(entry) for entry in combined_data]

# Define the desired column order
columns_order = ["Category", "Specialty", "Difficulty", "Question", "Answer"]

# Create a DataFrame with the proper column order
df = pd.DataFrame(normalized_data, columns=columns_order)
df['Answer']=df['Answer'].apply(clean_text)
# Write the combined data to a CSV file without the index
df.to_csv("combined_tech_questions.csv", index=False)

print("CSV file 'combined_questions.csv' created successfully!")