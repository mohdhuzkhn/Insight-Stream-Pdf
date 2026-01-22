from pinecone import Pinecone
# NEW: Replace requests with sentence-transformers
from sentence_transformers import SentenceTransformer
import time

class PineconeVectorStore:
    def __init__(self, api_key: str):
        # 1. Connect to Pinecone Cloud
        self.pc = Pinecone(api_key=api_key)
        self.index_name = "insight-stream"
        self.index = self.pc.Index(self.index_name)
        
        # 2. ZERO-BUDGET EMBEDDING ENGINE
        # This model is free, runs locally in your code (no Ollama needed)
        # It produces 768-dimensional vectors (matches your Pinecone index)
        print("🧠 Loading Embedding Model (Zero-Budget Edition)...")
        self.model = SentenceTransformer('all-mpnet-base-v2') 
        print("✅ Model Ready!")

    def _get_embedding(self, text: str):
        """
        Turns text into numbers using sentence-transformers.
        No internet or local server needed for this step!
        """
        # We convert the numpy array to a list for Pinecone
        embedding = self.model.encode(text)
        return embedding.tolist()

    # def add_documents(self, chunks, filename):
    def add_documents(self, chunks, filename, namespace):
        """Upload PDF chunks to the Cloud"""
        vectors = []
        print(f"🔄 Encoding {len(chunks)} chunks using Sentence-Transformers...")
        
        for i, chunk in enumerate(chunks):
            v_id = f"{filename}_{i}"
            embedding = self._get_embedding(chunk['text'])
            
            vectors.append({
                "id": v_id,
                "values": embedding,
                "metadata": {
                    "text": chunk['text'],
                    "source": filename
                }
            })
        
        # Upload to Pinecone Cloud
        # self.index.upsert(vectors=vectors)
        self.index.upsert(vectors=vectors, namespace=namespace)
        print(f"✅ Successfully uploaded to Cloud!")

    def search(self, query, top_k=3 , namespace=None):
        query_vector = self._get_embedding(query)
        results = self.index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        namespace=namespace # Targets only this user's data
    )
        """Search the Cloud using Semantic Meaning"""
        query_vector = self._get_embedding(query)
        
        results = self.index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )
        
        formatted = []
        for match in results['matches']:
            formatted.append({
                'text': match['metadata']['text'],
                'metadata': {'source': match['metadata']['source']},
                'score': match['score']
            })
        return formatted
    # added today 22/01/26
    def delete_user_data(self, namespace: str):
        """Deletes only the data for a specific user session"""
        try:
            self.index.delete(delete_all=True, namespace=namespace)
            print(f"🗑️ Namespace {namespace} cleared.")
            return True
        except Exception as e:
            print(f"❌ Error deleting namespace: {e}")
            return False

    def master_clear_all_data(self):
            """ADMIN ONLY: Deletes ALL data across ALL namespaces"""
            try:
                # For Serverless indexes, we iterate through namespaces to ensure a clean wipe
                stats = self.index.describe_index_stats()
                namespaces = stats.get('namespaces', {}).keys()
                
                if not namespaces:
                    print("ℹ️ No data found in any namespace.")
                    return True
                    
                for ns in namespaces:
                    self.index.delete(delete_all=True, namespace=ns)
                    
                print(f"🚨 MASTER WIPE COMPLETE: Cleared {len(namespaces)} namespaces.")
                return True
            except Exception as e:
                # This will show you the REAL error in your terminal/logs
                print(f"❌ Master Clear Error Details: {e}")
                return False