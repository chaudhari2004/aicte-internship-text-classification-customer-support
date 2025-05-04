# app.py

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Load the model and tokenizer
# 👉 Change the path if your fine-tuned model is saved in a specific folder
MODEL_NAME = "distilbert-base-uncased"  # or path to your fine-tuned model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Labels mapping (put your actual mapping here from your notebook)
label2id = {
    "technical issue": 0,
    "billing issue": 1,
    "account issue": 2,
    "general inquiry": 3
    # Add more if needed
}
id2label = {v: k for k, v in label2id.items()}

st.title("🛠️ Issue Category Prediction App")

st.write("Enter your query and let the AI classify it!")

user_input = st.text_area("Enter your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class_id = torch.argmax(logits, dim=-1).item()
            predicted_label = id2label.get(predicted_class_id, "Unknown")
        
        st.success(f"### Predicted Category: `{predicted_label}`")
