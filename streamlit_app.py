import streamlit as st
import os
import sys

sys.path.append("src")
from pdf_processor import process_pdf_file
from pinecone_store import PineconeVectorStore
from groq_llama import GroqAI

import uuid  # Standard Python library for unique IDs

if "user_namespace" not in st.session_state:
    # Generate a unique 8-character ID for this visitor
    st.session_state.user_namespace = f"user_{str(uuid.uuid4())[:8]}"

# When calling search or add_documents, ALWAYS pass this namespace
# Example: vector_store.search(prompt, top_k=8, namespace=st.session_state.user_namespace)
# 1. UI Setup
st.set_page_config(page_title="Insight-Stream v2.0", page_icon="🚀")
st.title("🚀 Insight-Stream: Cloud Document Intelligence")
st.markdown("Upload a PDF and ask questions about it!")

# 2. Get Secrets (We will set these on the Streamlit Cloud dashboard)
PINECONE_KEY = st.secrets["PINECONE_API_KEY"]
GROQ_KEY = st.secrets["GROQ_API_KEY"]


# 3. Initialize Engines
@st.cache_resource  # This prevents the model from reloading on every click
def init_engines():
    vector_store = PineconeVectorStore(api_key=PINECONE_KEY)
    ai = GroqAI(api_key=GROQ_KEY)
    return vector_store, ai


vector_store, ai = init_engines()

# 4. Sidebar: PDF Upload
with st.sidebar:
    st.header("📥 Document Management")
    
    # 1. User Upload logic ... (already exists)
    
    st.divider()
    
    # 2. User Reset (Only deletes THEIR data)
    if st.button("🧹 Clear My Session"):
        with st.spinner("Deleting your files..."):
            success = vector_store.delete_user_data(st.session_state.user_namespace)
            if success:
                st.session_state.messages = [] # Clear their chat too
                st.success("Your data has been removed from the cloud.")
                st.rerun()

    st.divider()

    # 3. ADMIN PANEL (Only for YOU)
    with st.expander("🔑 Admin Tools"):
        admin_password = st.text_input("Enter Admin Password", type="password")
        # In a no-budget project, you can hardcode a simple password 
        # or better, add it to st.secrets["ADMIN_PASSWORD"]
        if admin_password == st.secrets.get("ADMIN_PASSWORD", "School_Project_2024"):
            st.warning("Warning: This will delete data for ALL users!")
            if st.button("🚨 MASTER DELETE ALL CLOUD DATA"):
                if vector_store.master_clear_all_data():
                    st.success("Global Cloud Storage has been wiped.")
                else:
                    st.error("Wipe failed.")
# 5. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask something about your document..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):
        with st.spinner("Searching Cloud & Thinking..."):
            # Increased top_k=8 to see more context (solves the Chapter 3 issue!)
            result = ai.generate_answer(prompt, vector_store.search(prompt, top_k=8))
            response = result["answer"]
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
