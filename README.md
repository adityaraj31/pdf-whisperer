# 📄 PDF Whisperer – AI Assistant for PDFs / Research Papers / JDs

**PDF Whisperer** is an AI-powered chatbot that lets you upload PDFs (research papers, resumes, job descriptions, etc.) and ask intelligent, ChatGPT-style questions — all powered locally using LangChain, FAISS, Groq LLMs, and Sentence Transformers.

---

### 🚀 Demo Screenshot
![Screenshot (214)](https://github.com/user-attachments/assets/a216ed24-3824-481e-a53f-2009fa67dfd5)
![Screenshot (215)](https://github.com/user-attachments/assets/e8d95a11-d88b-4098-9835-36d71c8ed7cf)



## ⚙️ How to Use

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/pdf-whisperer.git
cd pdf-whisperer
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

Or set it temporarily in your terminal:

```bash
export GROQ_API_KEY=your_actual_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

