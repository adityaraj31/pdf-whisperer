# 📄 PDF Whisperer – AI Assistant for PDFs / Research Papers / JDs

**PDF Whisperer** is an AI-powered chatbot that lets you upload PDFs (research papers, resumes, job descriptions, etc.) and ask intelligent, ChatGPT-style questions — all powered locally using LangChain, FAISS, Groq LLMs, and Sentence Transformers.

---

### 🚀 Demo Screenshot

![App Screenshot](./demo_screenshot.png)

---

## 🧠 Features

- 📄 Upload any English PDF (JDs, resumes, research papers)
- 🧱 Automatically chunk + embed documents using `all-MiniLM-L6-v2`
- 🔎 Retrieve document-specific answers with FAISS
- 💬 Ask follow-up questions using conversation memory
- ⚡ Super-fast LLMs via Groq (Mixtral, Gemma, LLaMA 3)
- 🌐 Clean Streamlit interface — just upload and chat!

---

## 🛠 Tech Stack

| Tool                  | Use                                             |
|-----------------------|--------------------------------------------------|
| **LangChain**         | RAG, retriever, and memory chains               |
| **Groq**              | Access to hosted Mixtral, Gemma, LLaMA-3 LLMs   |
| **FAISS**             | Local vector store for document embeddings      |
| **Sentence Transformers** | Local embeddings (`all-MiniLM-L6-v2`)   |
| **PyPDF**             | Extract text from PDFs                          |
| **Streamlit**         | Build the user interface                        |

---

## 📂 Folder Structure

```
pdf-whisperer/
│
├── data/                  # Uploaded PDFs (ignored)
├── embeddings/            # FAISS index files (ignored)
├── src/
│   ├── loader.py          # PDF loading and chunking
│   ├── embedder.py        # FAISS embedding and retrieval
│   ├── qa_chain.py        # Groq + memory + retriever chain
│
├── app.py                 # Streamlit frontend
├── requirements.txt       # Python dependencies
├── .env                   # API key storage (ignored)
├── .gitignore             # Files/folders to exclude from Git
└── README.md              # Project documentation
```

---

## ⚙️ Getting Started

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

> Open `http://localhost:8501` in your browser.

---

## 🗂 Example Use Cases

- 👨‍💼 Analyze job descriptions to align resumes
- 📚 Quickly understand large research papers
- 📝 Summarize content-heavy PDFs
- 🧠 Ask follow-up or deep-dive questions from a document

---

## 📄 Sample `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
*.log

# Virtual environments
venv/

# Secrets
.env
.streamlit/secrets.toml

# FAISS Vector DB
embeddings/
*.faiss

# Uploaded PDFs
data/

# System
.DS_Store
Thumbs.db

# Editor
.vscode/
```

---

## 💡 Future Ideas

- [ ] Add multi-PDF upload support
- [ ] Highlight source context in responses
- [ ] Deploy to Hugging Face Spaces or Streamlit Cloud
- [ ] Save and export conversation history

---

## 🙌 Credits

- [LangChain](https://www.langchain.com/)
- [Groq](https://console.groq.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence-Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)

---

## 📜 License

MIT License. Feel free to fork and build on this project.
