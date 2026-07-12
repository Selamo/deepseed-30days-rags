# Day 5 – Introduction to ChromaDB

## Objective

Today I learned how to replace manual vector storage with a real vector database.

Instead of storing embeddings inside a Python list, I stored them inside ChromaDB, allowing efficient similarity search and persistent storage.

---

# Key Concepts

## 1. Vector Database

A vector database stores embeddings and retrieves similar vectors efficiently.

Unlike a relational database, it is optimized for semantic search rather than exact matching.

Examples include:

- ChromaDB
- Pinecone
- Qdrant
- Milvus
- Weaviate

---

## 2. ChromaDB Collection

A collection is similar to a SQL table.

It stores:

- Documents
- Embeddings
- Metadata
- IDs

Example:

Collection
    ├── Document
    ├── Embedding
    ├── Metadata
    └── ID

---

## 3. PersistentClient

Using

```python
chromadb.PersistentClient()
```

stores vectors permanently on disk.

The database remains even after closing Python.

---

## 4. Embeddings

Every chunk is converted into a vector using

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

Both documents and user queries must use the same embedding model.

---

## 5. Metadata

Metadata is information about a document.

Example:

```python
{
    "source": "machine_learning.pdf",
    "chunk": 4
}
```

Metadata helps identify where retrieved information came from and enables filtering.

---

## 6. Querying

The query process is:

User Question

↓

Embedding

↓

ChromaDB Search

↓

Top-k Results

↓

Returned Chunks

---

## 7. Distances

ChromaDB returns a distance score for each retrieved document.

Smaller distances generally indicate greater similarity.

---

# Difference Between Day 4 and Day 5

Day 4

- Manual cosine similarity
- Python list
- No persistence
- O(n) search

Day 5

- ChromaDB
- Persistent storage
- Automatic similarity search
- Metadata support
- Faster retrieval

---

# What I Learned Today

- How to create a ChromaDB database.
- How to create collections.
- How to store embeddings.
- How to store metadata.
- How to perform semantic search.
- How ChromaDB replaces manual similarity calculations.

---

# Challenge

- Store two different PDFs in separate collections.
- Add page numbers as metadata.
- Retrieve the top 5 chunks.
- Print the metadata with every retrieved chunk.
- Compare retrieval quality for different chunk sizes.