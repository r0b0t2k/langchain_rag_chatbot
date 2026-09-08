import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
)

# Load existing vector store
vectorstore = Chroma(
    persist_directory="./vectorstore",
    embedding_function=embeddings,
)

# Test similarity search
query = "What is this documentation about?"
results = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content[:200] + "...")
