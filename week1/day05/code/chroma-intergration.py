from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

# STEP 1: Load Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")
# STEP 2: Create ChromaDB Client
client = chromadb.PersistentClient(path="./chroma_db")

# STEP 3: Create Collection
collection = client.get_or_create_collection(
    name="machine_learning_notes"
)

# STEP 4: Load PDF
reader = PdfReader("data/machine_learning.pdf")
text = ""
for page in reader.pages:
    extracted_text = page.extract_text()
    if extracted_text:
        text += extracted_text + "\n"

# STEP 5: Chunk Function

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks
chunks = chunk_text(text)
# STEP 6: Store Chunks in ChromaDB

for index, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(
        ids=[f"chunk_{index}"],
        documents=[chunk],
        embeddings=[embedding],
        metadatas=[
            {
                "chunk": index,
                "source": "machine_learning.pdf"
            }
        ]
    )

print(f"\nStored {len(chunks)} chunks successfully.\n")

question = input("Ask a question: ")

# STEP 8: Generate Query Embedding
query_embedding = model.encode(question).tolist()

# STEP 9: Search ChromaDB

results = collection.query(

    query_embeddings=[query_embedding],

    n_results=3

)

# STEP 10: Display Results

print("\n========== RETRIEVED CHUNKS ==========\n")

documents = results["documents"][0]

metadatas = results["metadatas"][0]

distances = results["distances"][0]


for doc, metadata, distance in zip(
    documents,
    metadatas,
    distances
):

    print("----------------------------------------")

    print(f"Chunk : {metadata['chunk']}")

    print(f"Source: {metadata['source']}")

    print(f"Distance: {distance}")

    print()

    print(doc)

    print()


print("======================================")