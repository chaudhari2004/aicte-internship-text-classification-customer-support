# 🌐 AICTE Internship - Text Classification for Customer Support

This project is a **web-based AI tool** developed as part of the AICTE Virtual Internship. It classifies customer support queries into categories such as **technical issue**, **billing issue**, **account issue**, and **general inquiry** using a pre-trained transformer model like `distilbert-base-uncased`. The frontend is built using **Streamlit**, enabling easy and interactive use through a web interface.

---

## 🚀 Features

- 💬 Classifies user-entered customer queries in real time
- 🤖 Powered by Hugging Face Transformers and PyTorch
- 🌐 Deployed as a lightweight, interactive website using Streamlit
- 🔧 Easily customizable with your own fine-tuned model and labels

---

## 🧠 Model Details

- **Base Model**: `distilbert-base-uncased` (can be replaced with a custom fine-tuned model)
- **Libraries Used**: `transformers`, `torch`, `streamlit`
- **Categories Predicted**:
  - Technical Issue
  - Billing Issue
  - Account Issue
  - General Inquiry



## 💻 How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/aicte-internship-text-classification-customer-support.git
   cd aicte-internship-text-classification-customer-support


2. **Install Dependencies**:
pip install -r requirements.txt
Or manually:
pip install streamlit transformers torch

**Run the Website**:


streamlit run app.py
