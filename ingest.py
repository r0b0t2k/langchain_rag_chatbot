# ingest.py
from langchain_community.document_loaders import (
        TextLoader,
        DirectoryLoader,
        PyPDFLoader,
        )
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY=os.environ["GEMINI_API_KEY"]
GEMINI_PROJECT_NAME=os.environ["GEMINI_PROJECT_NUMBER"]
GEMINI_PROJECT_NUMBER=os.environ["GEMINI_PROJECT_NUMBER"]
LANGSMITH_API_KEY=os.environ["LANGSMITH_API_KEY"]

print(GEMINI_API_KEY)
print(GEMINI_PROJECT_NUMBER)
print(GEMINI_PROJECT_NAME)
print(LANGSMITH_API_KEY)
