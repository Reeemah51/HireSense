from transformers import BertTokenizer, BertModel
from sklearn.linear_model import Lasso
from sklearn.metrics.pairwise import cosine_similarity
import torch
import pandas as pd
import numpy as np
from transformers import pipeline

pipe = pipeline("text-classification", model="zaina-e/hiresense-model", return_all_scores=False)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert = BertModel.from_pretrained("bert-base-uncased")

# Optional: Load EmoLex and keyword list
emolex_df = pd.read_csv(r'C:\Users\Administrator\Desktop\HireSense2\model\NRC-Emotion-Lexicon-Wordlevel-v0.92.txt',
                         delimiter="\t", names=['Word', 'Emotion', 'Association'])
emolex_words = emolex_df[emolex_df['Association'] == 1].groupby('Emotion')['Word'].apply(list).to_dict()
positive_keywords = pd.read_csv(r"C:\Users\Administrator\Desktop\HireSense2\data\cleaned\categorized_words.csv")["Professional"].tolist()

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = bert(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def evaluate_user_response(user_answer, question, model_answer=None):
    full_input = f"{question} [SEP] {user_answer}"

    # Predict score using the model
    result = pipe(full_input)[0]
    predicted_score = float(result["score"])

    # Keyword matching
    used_keywords = [kw for kw in positive_keywords if kw in user_answer.lower()]
    keyword_count = len(used_keywords)

    # Return the answer, score, and keyword count for final summary
    return user_answer, predicted_score, keyword_count