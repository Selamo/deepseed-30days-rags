from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np

#Load the pdf
def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

#Fixed Size chunking
def chunk_text(text, chunk_size=500, overlap=50):
    
    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks

#Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

#Generate embeddings
def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings

#Manual cosine 
def cosine_similarity(vec1, vec2):
    
    dot_product = np.dot(vec1, vec2)

    norm_vec1 = np.linalg.norm(vec1)

    norm_vec2 = np.linalg.norm(vec2)

    similarity = dot_product / (norm_vec1 * norm_vec2)

    return similarity

#Retrieval
def retrieve(query, chunks, embeddings, top_k=3):
    
    query_embedding = model.encode(query)

    similarities = []

    for i, embedding in enumerate(embeddings):

        score = cosine_similarity(query_embedding, embedding)

        similarities.append((score, chunks[i]))

    similarities.sort(reverse=True)

    return similarities[:top_k]


pdf_text = load_pdf("data/RAG.pdf")

chunks = chunk_text(pdf_text)

embeddings = create_embeddings(chunks)

question = input("Ask a question: ")

results = retrieve(question, chunks, embeddings)

print("\nTop Retrieved Chunks\n")

for score, chunk in results:

    print("="*80)

    print(f"Similarity: {score:.4f}")

    print()

    print(chunk)

    print()