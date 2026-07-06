# RETRIEVAL AUGMENTED GENERATION(RAG)
**RAG is an AI framework that allows a Large Language Model to answer questions using information from external documents instead of relying only on what it learned during training.**
*Think of it this way*
- Without RAG, an LLM answers from its memory.
- with RAG, the LLM first searches for relevant information, the uses that information to answer.

*Imagine asking an LLM*:

> What are the requirements for Cameroon Presidential election?

A normal LLM might not know because the information changed after it was trained.
**A RAG system will**:
1. Search State Documents and websites.
2. Find the relevant pages.
3. Give those pages to the LLM.
4. The LLM answers using the retrived information.

## Why RAG Exist
LLMs have limitaions:
- They have knowledge cutoff.
- They sometimes hallucinate.
- They cannot know your private documents unless you provide them.

RAG solves thses problems by connecting the LLM to external knowledge.
*Examples*:
- Company documents
- Medical records
- Research papers
- PDFs
- Websites
- Databases
- Internal company manuals

## Pillars of RAG
 **Stage 1 Indexing**
Indexing is the process of preparing documents so they can be searched efficiently.
*Think of a lubrary*:
Imagine placing 20,000 books randomly in one room.

Can you quickly find one book? No

A libarian organizes them by title, subjects, and authors.
That is similar to indexing. 

Suppose we have this document:

```txt
Artificial intelligenceis changing healthcare.

Hospitals now use AI for disease detection.

Machine learning predicts patient outcome

```
**The system performs several steps**

1. **Read the document**: The pdf, word file, or website is loaded

2. **Chunking**: The document is divided into smaller pieces.

Example:
chenk 1

```txt

Artificial intelligenceis changing healthcare.

```

chunk 2:
```txt
Hospitals now use AI for disease detection.

```

chunk 3:
```txt
Machine learning predicts patient outcome
```
*Large documents are broken down because LLMs cannot efficiently process huge texts all at once*

3. **Embedding**
Each chunk is converted into numbers called embeddings.

```txt
Chunk
Hospitals now use AI for disease detection.

Embedding
[0.12, 0.05, 0.33, 0.67, ...]
```
An embedding is a mathematical representation of meaning.
Similar sentences produce similar embeddings.

4. **Store the Embeddings**
These embeddings are stored in a vector database such as ChromaDB, Pinecone,pqVector.

**Stage 2: Retrieval**
Retrieval means finding the most relevant document chunks for a user's question.

Suppose the user asks:
```txt
How is AI used in hospitals?
```

The question is also converted into an embedding.
The system compares the embedding with all stored document embeddings.
It calculates similarity and retrieves the closest matches.

Example:

Stored chunks:
```txt

Chunk A
AI in farming

similarity = 10%

```

```txt

Chunk B
Hospitals use AI for diagnosis

similarity = 98%

```

The system reeturns Chunk B because it is the most relevant.

**Stage 3: Generation**
After retrieval, the system already has the relevant document chunks.

Now the LLM generates the final answer using those retrieved chunks.
Instead of asking the LLM:

```txt

Answer this question

```

The prompt becomes:

```txt

Use the folllowing context.

Context:

Hospitals use AI for diagnosis

Question:

How is AI use in hospitals?

```

The model now answers based on the provided context.

This greatly reduces hallucinations.

## RAG vs Fine - Tuning
- When the RAG dataset becomes too large, it makes it combersome and hard to manage.
- Also you can't fine tune a model with dynammic data ( Rapid changing data) like weather forcasting, stock market values.

The decision wether to use RAG or fine tuning lies on the proportion of parametric versus non - parametric information.

- Parametric: Here the model's knowledge is stored in parameters(weights and biases). The original training data is  transformed into a mathematical form called parametric expression. Fine tuning is suitable here.

- Non Parametric: Involves storing data that can be accessed directly, unlike parametric where data is embedded.
RAG is suitable here.