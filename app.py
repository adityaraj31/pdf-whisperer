import streamlit as st
from loader import load_and_split_pdf
from embedder import embed_chunks_with_faiss, load_faiss_vectorstore
from qa_chain import get_groq_llm, build_qa_chain
from langchain.embeddings import HuggingFaceEmbeddings
import os
import tempfile

st.set_page_config(page_title="AI PDF Assistant", layout="wide")

# Sidebar for upload and info
with st.sidebar:
    st.title("📄 PDF Whisperer")
    st.markdown(
        """
        Upload a PDF (research paper, JD, etc.) and ask questions about its content.
        - Supports English PDFs
        - Powered by LLM + embeddings
        """
    )
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if st.button("Clear Session"):
        st.session_state.clear()
        st.experimental_rerun()

# Main layout
st.title("🤖 AI Assistant for PDFs")
st.markdown("Ask questions about your uploaded document. The assistant will read, embed, and answer contextually.")

user_question = st.text_input("💬 Type your question here:")

# Session state for QA chain
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# File upload and processing
if uploaded_file:
    with st.spinner("🔄 Processing PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_path = tmp_file.name
            tmp_file.write(uploaded_file.read())

        chunks = load_and_split_pdf(tmp_path)
        embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = embed_chunks_with_faiss(chunks)
        llm = get_groq_llm()
        st.session_state.qa_chain = build_qa_chain(vectorstore, llm)

    st.success("✅ PDF processed! You can now ask questions.")

    # Show PDF info
    st.info(f"**File:** {uploaded_file.name} | **Size:** {uploaded_file.size/1024:.1f} KB")

# Q&A interaction
if user_question and st.session_state.qa_chain:
    with st.spinner("🤔 Generating answer..."):
        answer = st.session_state.qa_chain.run(user_question)
    st.markdown("### 📝 Answer:")
    st.write(answer)
elif user_question and not st.session_state.qa_chain:
    st.warning("Please upload and process a PDF first.")

# Optional: Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit, LangChain, and Groq LLM.")
