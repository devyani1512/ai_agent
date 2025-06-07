# main.py
import streamlit as st
from pyngrok import ngrok
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# LLM model
model = OllamaLLM(model="llama3.2")

# Prompt template
template = """
You are a highly knowledgeable AI assistant helping answer questions from a textbook on Object-Oriented Programming using C++.

Your ONLY source of information is the following excerpts from the book.
If the answer is not explicitly found in the excerpts, respond with:
"I don’t know based on the provided content."

Excerpts:
--------------------
{reviews}
--------------------

Question:
{question}

Answer:"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to format retrieved documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

public_url = ngrok.connect(8501)
print("Streamlit app is live at:", public_url)
# Streamlit UI
st.set_page_config(page_title="OOP in C++ Chatbot", page_icon="💿")
st.title("🔍 Ask about OOP in C++")

question = st.text_input("Type your question here:")

if question:
    docs = retriever.invoke(question)

    # Optional: Show retrieved documents
    with st.expander("🔍 Retrieved Context"):
        for i, doc in enumerate(docs):
            st.markdown(f"**Document {i+1}:**")
            st.write(doc.page_content.strip())

    # Run the LLM chain
    full_prompt_input = {
        "reviews": format_docs(docs),
        "question": question
    }
    result = chain.invoke(full_prompt_input)

    st.subheader("👻 Answer")
    st.write(result)
