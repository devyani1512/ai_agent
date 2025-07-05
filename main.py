
import streamlit as st
from pyngrok import ngrok
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


model = OllamaLLM(model="llama3.2")


template = """
You are a highly knowledgeable AI assistant helping answer questions from a textbook on Object-Oriented Programming in C++(4th Edition) by Robert Lafore.

Your ONLY source of information regarding the concepts of object oriented programming in cpp is the following excerpts from the book.
If question or statement is not regarding object oriented programming in cpp use your interlligence  to answer.
If the answer to the question regarding oops in cpp is not explicitly found in the excerpts, respond with:
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


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# public_url = ngrok.connect(8501)
# print("Streamlit app is live at:", public_url)
# Streamlit UI
st.set_page_config(page_title="OOP in C++ Chatbot", page_icon="💿")
st.title("🔍 Ask about OOP in C++")

question = st.text_input("Type your question here:")

if question:
    docs = retriever.invoke(question)

    
    with st.expander("🔍 Retrieved Context"):
        for i, doc in enumerate(docs):
            st.markdown(f"**Document {i+1}:**")
            st.write(doc.page_content.strip())

    
    full_prompt_input = {
        "reviews": format_docs(docs),
        "question": question
    }
    result = chain.invoke(full_prompt_input)

    st.subheader("📘 Answer")
    st.write(result)

# import streamlit as st
# from pyngrok import ngrok
# from langchain_huggingface import HuggingFaceEndpoint  # ✅ NEW
# from langchain_core.prompts import ChatPromptTemplate
# from vector import retriever
# import os  # 
# from dotenv import load_dotenv  # ✅ NEW

# # ✅ Load environment variables
# load_dotenv()

# # ✅ HuggingFace LLM model
# model = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",  # or another chat model
#     temperature=0.5,
#     max_new_tokens=512,
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# # ✅ Prompt template
# template = """
# You are a highly knowledgeable AI assistant helping answer questions from a textbook on Object-Oriented Programming using C++.

# Your ONLY source of information is the following excerpts from the book.
# If the answer is not explicitly found in the excerpts, respond with:
# "I don’t know based on the provided content."

# Excerpts:
# --------------------
# {reviews}z
# --------------------

# Question:
# {question}

# Answer:"""

# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model

# # ✅ Format retrieved documents
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)#why did we do this?

# # ✅ Start ngrok tunnel
# public_url = ngrok.connect(8501)
# print("Streamlit app is live at:", public_url)#not needed

# # ✅ Streamlit UI
# st.set_page_config(page_title="OOP in C++ Chatbot", page_icon="🍙")
# st.title("🔍 Ask about OOP in C++")

# question = st.text_input("Type your question here:")

# if question:
#     docs = retriever.invoke(question)

#     # ✅ Optional: Show retrieved documents
#     with st.expander("🔍 Retrieved Context"):
#         for i, doc in enumerate(docs):
#             st.markdown(f"**Document {i+1}:**")
#             st.write(doc.page_content.strip())

#     # ✅ Run the LLM chain
#     full_prompt_input = {
#         "reviews": format_docs(docs),
#         "question": question
#     }
#     result = chain.invoke(full_prompt_input)

#     st.subheader("📘 Answer")
#     st.write(result)

