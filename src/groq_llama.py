from groq import Groq

class GroqAI:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        # self.model = "llama-3.2-3b-preview" # Groq's fast Llama 3.2
        self.model = "llama-3.1-8b-instant"
        self.name = "Groq Llama 3.2"

    def generate_answer(self, question, context_chunks):
        # Format the chunks into a single string
        context_text = "\n\n".join([c['text'] for c in context_chunks])
        
        prompt = f"""Use the following context to answer the question. 
        If you don't know the answer based on the context, say so.
        
        CONTEXT:
        {context_text}
        
        QUESTION:
        {question}"""

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return {
            "answer": completion.choices[0].message.content,
            "model": self.name,
            "confidence": 0.9
        }
        
        
        # added today 22/01/26 
    def summarize_all(self, chunks):
        """
        Summarizes the entire document by processing all chunks.
        """
        # 1. Join all chunks into a few large blocks (Map phase)
        # We take all chunks to ensure the LLM sees everything
        full_text = " ".join([c['text'] for c in chunks])
        
        # 2. If the text is too long for one prompt, we summarize in parts
        # For your 4-10 page PDFs, we can likely send a larger chunk to Groq
        prompt = f"""Write a comprehensive summary of the following document. 
        Focus on the main topics, key definitions, and the overall structure.
        
        DOCUMENT CONTENT:
        {full_text[:15000]} # Limit to stay within Groq context window
        """
        
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile", # Use the big model for better summaries
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content