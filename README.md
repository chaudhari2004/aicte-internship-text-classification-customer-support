# 🌐 AICTE Internship - Text Classification for Customer Support

This project is a **web-based AI tool** developed as part of the AICTE Virtual Internship. It classifies customer support queries into categories such as **technical issue**, **billing issue**, **account issue**, and **general inquiry** using a pre-trained transformer model like `distilbert-base-uncased`. The frontend is built using **Streamlit**, enabling easy and interactive use through a web interface.

---

## 🚀 Features

- 💬 Classifies user-entered customer queries in real time
- 🤖 Powered by Hugging Face Transformers and PyTorch
- 🌐 Deployed as a lightweight, interactive website using Streamlit
- 🔧 Easily customizable with your own fine-tuned model and labels

---



## 🚀 Why This Project?

Customer support teams handle **thousands of queries daily**. Manual triage wastes time and delays responses. 
This AI tool **automatically understands and categorizes queries**, helping support agents respond **faster and smarter**.

---

## ✨ Key Features

- ⚡️ **Real-time query classification** via web interface  
- 🧠 Built using `distilbert-base-uncased` from Hugging Face Transformers  
- 🔥 Powered by **PyTorch** and **Streamlit**  
- 🎯 Pre-trained and ready to use, but easily customizable  
- 📦 Fully open-source and beginner-friendly  

---

## 🎯 Use Cases

- 📩 Customer support automation  
- 💬 Smart ticket tagging  
- 🛠 Backend for chatbot routing  
- 🧪 NLP learning and experimentation  

---

## 🧠 Model Info

- **Model**: `distilbert-base-uncased`  
- **Frameworks**: Hugging Face Transformers, PyTorch  
- **Predicted Categories**:
  - 📶 Technical Issue  
  - 💳 Billing Issue  
  - 🔐 Account Issue  
  - ❓ General Inquiry  

---


## 📤 Sample Output

Here are a few example customer queries and how the model classifies them:

| **Customer Query**                                           | **Predicted Category** |
|--------------------------------------------------------------|--------------------------|
| "Why was I charged twice for the same transaction?"          | 🧾 Billing Issue         |
| "My internet is not working since yesterday."                | 🛠 Technical Issue        |
| "I can't access my account even after resetting my password."| 🔐 Account Issue         |
| "What are your customer care hours?"                         | ❓ General Inquiry        |
| "The app crashes whenever I open it on Android."             | 🛠 Technical Issue        |
| "How can I update my billing information?"                   | 🧾 Billing Issue          |
| "Need help unlocking my account."                            | 🔐 Account Issue         |
| "Do you offer 24/7 support?"                                 | ❓ General Inquiry        |

---

## 🔄 How It Works

```mermaid
graph TD
A[User Input] --> B[Text Tokenization]
B --> C[Transformer Model (DistilBERT)]
C --> D[Prediction: Class Label]
D --> E[Streamlit UI Displays Result]


**Install Dependencies**
pip install -r requirements.txt
Or manually:
pip install streamlit transformers torch

**Run the Website**:


streamlit run app.py
