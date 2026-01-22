# 🚀 Insight-Stream v2.0
### Cloud-Powered Document Intelligence with Pinecone & Llama 3.3

**Insight-Stream** is a professional-grade RAG (Retrieval-Augmented Generation) application that transforms static PDF documents into interactive, intelligent knowledge bases. 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mohdhuzkhn-insight-stream-pdf.streamlit.app)

---

## 🌟 Key Features

*   **🔍 Semantic Search:** Uses high-dimensional vectors to understand the *meaning* of your questions, not just keywords.
*   **📝 Global Summarization:** Leveraging Llama 3.3-70B to generate comprehensive overviews of entire documents in seconds.
*   **🛡️ Multi-User Isolation:** Implements **Pinecone Namespaces** to ensure user data remains private and isolated per session.
*   **💰 Zero-Budget Architecture:** Utilizes free-tier cloud services (Pinecone, Groq, Streamlit) and open-source models.
*   **🔑 Admin Control Panel:** A secure, password-protected dashboard for global cloud storage management.

---

## 🛠️ Technical Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Web Interface & Deployment |
| **Text Extraction** | PyPDF2 | PDF Parsing & Pre-processing |
| **Embedding Model** | Sentence-Transformers | Local Neural Text Encoding |
| **Vector Database** | Pinecone (Cloud) | Semantic Storage & Retrieval |
| **LLM (Brain)** | Llama 3.3 (via Groq API) | Contextual Q&A & Summarization |

---

## 🏗️ How it Works (RAG Pipeline)

1.  **Ingestion:** PDF text is extracted and divided into overlapping chunks to preserve semantic context.
2.  **Embedding:** Chunks are converted into 768-dimensional vectors using the `all-mpnet-base-v2` model.
3.  **Cloud Storage:** Vectors are uploaded to **Pinecone Cloud** under a unique **Namespace** specific to the user.
4.  **Retrieval:** The system performs a similarity search to find the most relevant chunks for any given question.
5.  **Generation:** The context is fed into **Groq's Llama 3.3** engine to generate a factual, human-like response.

---

🛡️ Privacy & Security
Data Isolation: Every session is assigned a unique UUID namespace.
Manual Purge: Users can clear their specific cloud data with one click.
Secrets Management: API keys are never stored in the code; they are managed via encrypted secrets.

---

👨‍💻 Author
Muhammad Huzaifa Khan | AI Developer 