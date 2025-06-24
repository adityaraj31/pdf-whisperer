from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_split_pdf(pdf_path, chunk_size=1000, chunk_overlap=200):
    """
    Loads a PDF and splits it into smaller chunks for embeddings.
    
    Args:
        pdf_path (str): Path to the PDF file.
        chunk_size (int): Max token/char size of each chunk.
        chunk_overlap (int): Overlap between chunks to preserve context.

    Returns:
        List[Document]: List of chunked documents ready for embedding.
    """

    # 1. Load PDF using LangChain's PyPDFLoader
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # 2. Chunk text using RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(pages)

    return chunks
