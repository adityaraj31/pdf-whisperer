from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
import streamlit as st
import os


def load_faiss_vectorstore(faiss_path="embeddings/faiss_index", embedding_model=None):
    """
    Load FAISS index from local path using the embedding model.
    """
    return FAISS.load_local(faiss_path, embeddings=embedding_model, allow_dangerous_deserialization=True)

def get_groq_llm(model_name="llama3-70b-8192"):
    groq_api_key = os.getenv("GROQ_API_KEY")  # Make sure it's set
    return ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name=model_name)

def build_qa_chain(vectorstore, llm):
    """
    Create a Conversational QA chain with retriever + memory.
    """
    retriever = vectorstore.as_retriever()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )

    return qa_chain
