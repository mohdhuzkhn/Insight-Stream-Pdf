"""
LLM Integration - Core Q&A System
"""

class QASystem:
    def __init__(self, vector_store, llm=None):
        self.vector_store = vector_store
        self.llm = llm

    def ask(self, question, top_k_chunks=5): # Reduced to 3 to speed up Llama
        # 1. Search vector DB for context
        context_chunks = self.vector_store.search(question, top_k=top_k_chunks)
        
        # 2. Generate answer
        if self.llm:
            # We call the LLM's generate_answer method
            result = self.llm.generate_answer(question, context_chunks)
        else:
            # Demo Mode: Just return the first chunk found
            result = {
                "answer": context_chunks[0]['text'] if context_chunks else "No info found.",
                "model": "Demo Mode (Raw Text)",
                "confidence": 0.5
            }
        
        # 3. Format final output
        result["question"] = question
        result["sources"] = context_chunks[:2]
        return result