
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pdfplumber
import os

# Step 1: Extract raw text
with pdfplumber.open("data/Object-Oriented Programming in C++ (4th Edition) by Robert Lafore.www.eeeuniversity.com (2).pdf") as pdf:
    texts = []
    for i, page in enumerate(pdf.pages):
        content = page.extract_text() or ""
        texts.append(content)

text = "\n".join(texts)

# Step 2: Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.create_documents([text])



# Step 3: Embeddings
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chrome_langchain_db"
# we set add_documents to true if path/database does not exist
add_documents = not os.path.exists(db_location)

# Step 4: Chroma DB
vector_store = Chroma(
    collection_name="oop_cpp_book",#name of collection
    persist_directory=db_location,#location
    embedding_function=embeddings
)
# if database does not exist we add documents to it now
if add_documents:
    print(f"[DEBUG] Adding {len(chunks)} documents to vector store...")
    vector_store.add_documents(chunks)
    print("[DEBUG] Done saving documents.")

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
#top 5 similar results
