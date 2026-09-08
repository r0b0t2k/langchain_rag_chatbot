import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GEMINI_PROJECT_NAME = os.environ.get("GEMINI_PROJECT_NAME")
GEMINI_PROJECT_NUMBER = os.environ.get("GEMINI_PROJECT_NUMBER")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")

api_key = GOOGLE_API_KEY or GEMINI_API_KEY

if not api_key:
    raise ValueError("Neither GOOGLE_API_KEY nor GEMINI_API_KEY is set.")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=api_key,
)

vector = embeddings.embed_query("Authentication test successful.")
print(f"Success! Generated vector with dimension: {len(vector)}")
