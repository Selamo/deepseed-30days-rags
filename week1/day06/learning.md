# Day 6 – Introduction to LlamaIndex

## Objective

Today I learned how to build a Retrieval-Augmented Generation (RAG) system using LlamaIndex.

Instead of manually loading documents, creating embeddings, storing vectors, and querying ChromaDB, LlamaIndex abstracts these steps into a few high-level components.

---

# What is LlamaIndex?

LlamaIndex is an open-source framework that simplifies building applications powered by Large Language Models (LLMs).

It acts as the bridge between your data and an LLM.

Instead of manually writing the retrieval pipeline, LlamaIndex manages:

- Document loading
- Chunking
- Embedding generation
- Index creation
- Retrieval
- Context preparation

---

# RAG Pipeline with LlamaIndex

Traditional RAG

Document

↓

Chunking

↓

Embeddings

↓

Vector Database

↓

Similarity Search

↓

LLM

↓

Answer

LlamaIndex

Documents

↓

SimpleDirectoryReader

↓

VectorStoreIndex

↓

QueryEngine

↓

Answer

---

# Main Components

## 1. SimpleDirectoryReader

Purpose:

Reads documents from a folder.

Example:

```python
documents = SimpleDirectoryReader("./data").load_data()
```

Supported file types include:

- PDF
- TXT
- Markdown (.md)
- DOCX
- HTML
- CSV

Instead of loading one file manually, LlamaIndex automatically loads every supported document inside the directory.

---

## 2. Document Objects

After loading,

```python
documents
```

becomes a list of Document objects.

Each Document contains:

- text
- metadata
- file information

Example

```python
Document(
    text="Machine Learning...",
    metadata={
        "file_name":"notes.md"
    }
)
```

---

## 3. VectorStoreIndex

Purpose:

Creates an index from documents.

Example

```python
index = VectorStoreIndex.from_documents(documents)
```

Internally this performs:

1. Chunking
2. Embedding generation
3. Index creation

Without LlamaIndex, we previously implemented these steps manually.

---

## 4. Query Engine

Purpose:

Provides an interface for asking questions.

Example

```python
query_engine = index.as_query_engine()
```

The Query Engine performs:

User Question

↓

Embedding

↓

Similarity Search

↓

Retrieve Relevant Chunks

↓

Build Context

↓

Generate Answer

---

## 5. Similarity Top-K

Example

```python
query_engine = index.as_query_engine(
    similarity_top_k=3
)
```

Meaning:

Retrieve the three most relevant chunks before generating an answer.

Larger values provide more context but may introduce irrelevant information.

---

# Workflow

Folder

↓

SimpleDirectoryReader

↓

Documents

↓

VectorStoreIndex

↓

QueryEngine

↓

User Question

↓

Answer

---

# Advantages of LlamaIndex

- Minimal code
- Automatic chunking
- Automatic embeddings
- Automatic indexing
- Automatic retrieval
- Easy integration with LLMs
- Supports many document formats
- Easily connects to vector databases

---

# Day 5 vs Day 6

## Day 5

- Manual PDF loading
- Manual chunking
- Manual embedding generation
- Manual ChromaDB storage
- Manual querying

## Day 6

- Automatic document loading
- Automatic indexing
- Automatic retrieval
- High-level Query Engine
- Much less code

---

# Key Classes Learned

## SimpleDirectoryReader

Reads documents from a folder.

---

## VectorStoreIndex

Creates a searchable vector index from documents.

---

## QueryEngine

Retrieves relevant information and answers user questions.

---

# What I Learned Today

- How LlamaIndex simplifies RAG development.
- How to load multiple documents automatically.
- How to create a vector index with a single command.
- How to build a query engine.
- How to perform semantic search using high-level APIs.
- Why LlamaIndex is useful for production RAG applications.

---

# Challenge

1. Create a `data` folder.
2. Add at least five Markdown (`.md`) files on different topics.
3. Build a `VectorStoreIndex`.
4. Query the index with at least ten different questions.
5. Experiment with `similarity_top_k` values of 1, 3, and 5.
6. Observe how changing `similarity_top_k` affects the quality of the answers.
7. Inspect the `Document` objects and their metadata to understand how LlamaIndex represents loaded files.