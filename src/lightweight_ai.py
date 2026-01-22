"""
Lightweight rule-based AI
"""
from typing import List, Dict, Any
import re

class LightweightAI:
    def generate_answer(self, question: str, context_chunks: List[Dict]) -> Dict[str, Any]:
        if not context_chunks:
            return {
                "answer": "No context found.",
                "sources": [],
                "confidence": 0.0,
                "model": "lightweight"
            }
        
        # Simple answer from first chunk
        answer = f"Based on the document: {context_chunks[0]['text'][:200]}..."
        
        return {
            "answer": answer,
            "sources": [{"text_preview": context_chunks[0]['text'][:100]}],
            "confidence": 0.6,
            "model": "lightweight"
        }