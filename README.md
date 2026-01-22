🚀 Insight-Stream v2.0: Cloud-Powered Document Intelligence

Insight-Stream is a professional-grade RAG (Retrieval-Augmented Generation) application that transforms static PDF documents into interactive, intelligent knowledge bases. Built with a "Zero-Budget" mindset, it leverages high-performance cloud APIs and local embedding models to provide lightning-fast, secure, and cost-effective document analysis.

!\[alt text](https://static.streamlit.io/badges/streamlit\_badge\_black\_white.svg)

🌟 Key Features

Semantic Search: Uses high-dimensional vectors to understand the meaning of your questions, not just keywords.

Global Summarization: Leverages Llama 3.3-70B to generate comprehensive overviews of entire documents.

Multi-User Isolation: Implements Pinecone Namespaces to ensure users' data remains private and isolated during their sessions.

Zero-Budget Architecture: Utilizes free-tier cloud services (Pinecone, Groq, Streamlit) and open-source models (Sentence-Transformers).

Admin Control Panel: Includes a secure, password-protected dashboard for global cloud storage management.

Interactive Chat UI: A clean, modern interface for seamless document interaction.

🛠️ Technical Tech Stack

Component	Technology	Role

Frontend	Streamlit	Web Interface \& Deployment

Text Extraction	PyPDF2	PDF Parsing \& Pre-processing

Embedding Model	Sentence-Transformers (all-mpnet-base-v2)	Local Neural Text Encoding

Vector Database	Pinecone (Cloud)	Semantic Storage \& Retrieval

LLM (Brain)	Llama 3.1/3.3 (via Groq Cloud API)	Contextual Q\&A and Summarization

Deployment	Streamlit Cloud	Global Hosting

🏗️ How it Works (RAG Pipeline)

Ingestion: User uploads a PDF. The system extracts text and divides it into overlapping chunks to preserve context.

Embedding: Chunks are converted into 768-dimensional vectors using the all-mpnet-base-v2 model.

Cloud Storage: Vectors are uploaded to Pinecone Cloud under a unique Namespace specific to the user's session.

Retrieval: When a user asks a question, the system converts the query into a vector and retrieves the most mathematically similar chunks from the cloud.

Generation: The retrieved chunks + the user question are sent to Groq's Llama 3.1/3.3 engine to generate a human-like, accurate response.

🚀 Installation \& Local Setup

If you wish to run this project locally, follow these steps:

Clone the repository:

code

Bash

git clone https://github.com/mohdhuzkhn/Insight-Stream-Pdf.git

cd Insight-Stream-Pdf

Create and Activate a Virtual Environment:

code

Bash

python -m venv venv

venv\\Scripts\\activate

Install Dependencies:

code

Bash

pip install -r requirements.txt

Set Up Environment Variables:

Create a .streamlit/secrets.toml file or set local environment variables for:

PINECONE\_API\_KEY

GROQ\_API\_KEY

ADMIN\_PASSWORD

Run the App:

code

Bash

streamlit run streamlit\_app.py

🛡️ Privacy \& Security

Data Isolation: Every user session is assigned a unique UUID. Data uploaded during that session is stored in a private namespace and is not accessible to other users.

Manual Purge: Users can click "Clear My Session" to immediately delete their data from the cloud.

Secrets Management: All API keys are managed via Streamlit's secure encrypted secrets manager.

👨‍💻 Author

Muhammad Huzaifa Khan

AI School Student \& Passionate AI Developer

LinkedIn | GitHub

