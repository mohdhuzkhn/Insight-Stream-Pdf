import os
from PyPDF2 import PdfReader

def process_pdf_file(pdf_path, chunk_size=700, chunk_overlap=100):
    """
    Extracts text from PDF and splits it into overlapping chunks.
    
    Args:
        pdf_path: Path to the PDF file
        chunk_size: Target character count for each chunk
        chunk_overlap: How many characters to repeat from the previous chunk
        
    Returns:
        List of dicts: [{'text': '...', 'metadata': {'page': 1, 'source': '...'}}]
    """
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File not found at {pdf_path}")
        return [], None

    try:
        reader = PdfReader(pdf_path)
        filename = os.path.basename(pdf_path)
        all_chunks = []
        
        print(f"📄 Processing: {filename} ({len(reader.pages)} pages)")

        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if not page_text:
                continue
            
            # Basic cleaning: remove extra whitespace
            page_text = " ".join(page_text.split())
            
            # Split page into chunks
            start = 0
            while start < len(page_text):
                # Calculate end of the chunk
                end = start + chunk_size
                
                # Extract chunk
                chunk_content = page_text[start:end]
                
                # Store chunk with metadata
                all_chunks.append({
                    "text": chunk_content,
                    "metadata": {
                        "source": filename,
                        "page": i + 1
                    }
                })
                
                # Move start point forward (minus overlap)
                start += (chunk_size - chunk_overlap)

        print(f"✅ Successfully created {len(all_chunks)} chunks.")
        return all_chunks, filename

    except Exception as e:
        print(f"❌ Error processing PDF: {e}")
        return [], None

# --- Quick Test ---
if __name__ == "__main__":
    # Test with a sample file if it exists
    test_path = "data/raw/sample.pdf"
    if os.path.exists(test_path):
        chunks, fname = process_pdf_file(test_path)
        if chunks:
            print(f"Sample Chunk 1: {chunks[0]['text'][:100]}...")