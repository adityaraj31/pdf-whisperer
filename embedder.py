from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def embed_chunks_with_faiss(chunks, faiss_path="embeddings/faiss_index"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(faiss_path)
    return vectorstore

def load_faiss_vectorstore(faiss_path="embeddings/faiss_index"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(faiss_path, embeddings=embedding_model, allow_dangerous_deserialization=True)
