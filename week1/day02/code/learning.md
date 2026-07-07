# TEXT CHUNKING STRATEGIES

*learning Objectives*
By the end of today, you should understand:
- What chunking is
- Why chunking is necassary
- What makes a good chunk
- Fixed -size chunking
- Recursive chunking
- Semantic Chunking
- Chunk Overlap
- Chunk size
- How chunking affects retrieval
- Best Practices

## 1. What is Chunking?

> Chunking is the breaking down of large documents into smaller pieces called chunks before storing them in a vectore database.

Imagine a 1000 page book.
Can you embed the entire book as one vector?

Yes

*But you should not because*
**One embedding will try to represent the meaning of the entire book, which is far too broad and will turn to give fulty answers if used**

So to solve this, we split it into smaller pieces called chunks.

Example

```txt
Artificial intelligenceis changing healthcare.

Hospitals now use AI for disease detection.

Machine learning predicts patient outcome

Doctors use AI to analyse medical scans

AI reduces diagnostic errors

```

Instead of storing everything together, we split it into chunks.

```txt
chunk1
Artificial intelligenceis changing healthcare.

Hospitals now use AI for disease detection.

```

```txt
chunk2
Machine learning predicts patient outcome

Doctors use AI to analyse medical scans

```
```txt
chunk 3
AI reduces diagnostic errors

```
Now each chunk here get's it's own embedding

## Why Chunking is Critical
*Chunking affects:*
- Retrieval accuracy
- Response quality
- Search Speed
- Context provided to the LLM

Poor CHunking can cause:
- Missing imporatnt info during the retrieval process
- Hallucinations
- wrong answers
- Incomplete context.

## Types Of Chunking

**1. Fixed-Size Chunking**
This is the simplest approach.
The document is split into equal-sized chunks.

Example:

Suppose each chunk is 100 words.
Document = 1000 words

The system creates:

```txt
Chunk 1 - Words 1 - 100
chunk 2 - Words 101 - 200
Chunk 3 - Words 201 - 300
...
chunk 10 - Words 901 - 1000
```

**Advantages**
- Easy to implement
- Fast
- Consistent chunk sizes
- Good for simple documents

**Disadvantages**
The main disadvantage here is that it ignores meaning.

**2. Recursive Chunking**

This is much smarter.

Instead of blindly splitting every 512 tokens, the system tries to preserve natural structure.
Suppose we want chunks of 300 characters.
The algorithm checks 
Can i split by paragraph?

If yes it proceeds

I the paragraph is too large:
split by sentence.

And if the sentence appears to be too large it proceeds to split by words.

**This one is better because it preserves meaning and tries to balance chunk size and readability**

**3. Semantic Chunking**
This the most intelligent strategy. Instead of splitting by size, it splits by meaning.
This type tries to group similar ideas rather than counting tokens.

*Here each chunnk contains one coherent topic, and this makes retrieval very much more accurate because you won't be mixing different topics in a single context*

**Disadvantages**

- It is slow
- It is more complex
- Often requires embeddings during the chunking process.
- Uses more computing resources.

**Chunk Overlap**
This another very important concept.
Suppose your chunk size is 100 words.

Wihout overlap, chunk 1 starts from 1 - 100

What if an important sentence starts at word 95 and ends at word 110
it get splitted between 2 chunks.

Overlap tries to preserbe context accross boundaries