# EMBEDDINGS DEEP DIVE

*What is an Embedding?*
An embedding is a numerical representation of data that preserves its meaning(semantics).
Instead of storing text as words, an embedding model converts the text into numbers.

**Example**
Sentence

```txt

Artificial intelligence is transforming healthcare.

```
Embedding:

```txt

[0.142, -0.283, 0.305, ... 0.331]

```
This list of numbers is called a vector.

**Note**: *Sentences with similar meanings produce vectors that are close together in mathematical space*

## Why Do We Need Embeddings?
Because when using keyword search, the model fail too understand the meaning of some words in the sentence which can push it to hallucinate.

## WHAT IS A VECTOR?
A vector is simply an ordered list of numbers.
Or geometrically it is a point in high-dimensional space.
Example

```txt
[2,5,9]
```
Each position in the vector represents a dimension.

## What is a Dimension?

uppose we describe a student using only 2 characteristics:
- Height
- Weight

Then the student can be represented as:
```txt
[160,55]
```
This is a **2-dimensional vector**

Now if we add 
- AGe
the vector becomes
```txt
[160,55,19]
```
And it has **3-dimensions**

## Embedding Dimension
When ever we see
```txtall-MiniLM-LM-v2

384 dimensions
```
This means every sentence is represented using **384 numbers.**

## Does More Dimensions Mean Better?

Think of dimensions like the amount of detail in  a photograph
A low-resolution image has a fewer pixels.
A high-resoluution image has more pixels.

Similarly:
- 384 dimensions capture meaning using fewer numerical features.
- 768 dimensions capture more detail.
- 1024 can capture  richer semantic information


Example Embedding Models

Model	Dimensions	Explanation

all-MiniLM-L6-v2	384	Small, fast, and ideal for learning or lightweight RAG systems.
bge-base-en	768	Captures more semantic detail than MiniLM, often improving retrieval quality.
bge-large-en	1024	Even richer semantic representations, but uses more memory and computation.
text-embedding-3-small	1536	High-quality embedding model suitable for many production applications.



---

 How Embeddings are Generated

Suppose we have:

Machine Learning predicts diseases.

The process is

Sentence

↓

Tokenizer

↓

Tokens

↓

Embedding Model

↓

Vector

Internally the embedding model uses a transformer network.

It analyzes:

grammar

context

word relationships

sentence meaning


before producing the vector.


---

 Semantic Space

Imagine every sentence is placed inside a huge mathematical space.

Instead of using latitude and longitude, we use hundreds of dimensions.

Example

Sentence A

Cats are animals.

↓

(near)

Sentence B

Dogs are animals.

↓

(near)

Sentence C

Python programming

↓

(far away)

Similar meanings are close together.

Different meanings are farther apart.


---

 Similarity Search

Suppose ChromaDB contains

Chunk A

Heart disease treatment

Chunk B

Football World Cup

User asks

How are cardiac diseases treated?

Embedding Model

↓

Query Vector

↓

Compare with stored vectors

↓

Highest similarity

↓

Return Chunk A


---

 Cosine Similarity

Now comes the most important mathematics in RAG.

Suppose we have two vectors

A

[1,2]

B

[2,4]

Notice

B points in exactly the same direction as A.

Cosine similarity measures how similar the directions of two vectors are, not their lengths.


---

Formula

The cosine similarity between vectors A and B is

\text{Cosine Similarity} =
\frac{A \cdot B}{\|A\| \times \|B\|}

Where:

 = Dot product of the two vectors

 = Magnitude (length) of vector A

 = Magnitude (length) of vector B



---

Step 1: Dot Product

Suppose

A=[1,2]

B=[2,4]

Dot Product

A\cdot B=(1\times2)+(2\times4)

=2+8

=10


---

Step 2: Magnitude

Magnitude means the length of a vector.

Formula

\|A\|=\sqrt{x^2+y^2}

For A

\sqrt{1^2+2^2}

=\sqrt5

For B

\sqrt{2^2+4^2}

=\sqrt{20}


---

Step 3: Final Calculation

\frac{10}
{\sqrt5 \times \sqrt{20}}

Since

\sqrt5 \times \sqrt{20}
=
10

We obtain

\boxed{1}

A cosine similarity of 1 means the vectors point in exactly the same direction.


---

Another Example

Suppose

A=[1,0]

B=[0,1]

Their dot product is

0

Therefore

Cosine Similarity

0

This means the vectors are unrelated (orthogonal).


---

Suppose

A=[1,0]

B=[-1,0]

Cosine Similarity

-1

They point in opposite directions.


---

Interpretation

Cosine Similarity	Meaning

1.0	Identical direction (very similar meaning)
0.8–0.99	Highly similar
0.5–0.79	Moderately related
0–0.49	Weak similarity
-1	Opposite direction


In many embedding models used for RAG, similarity scores are often non-negative because of how the embeddings are trained, but the mathematical definition of cosine similarity ranges from -1 to 1.


---

Why Use Cosine Similarity Instead of Euclidean Distance?

Imagine

A=[1,2]

B=[2,4]

Although B is longer, both vectors point in the same direction.

Cosine Similarity:

1

Perfect semantic match.

Euclidean Distance:

Not zero

because the lengths differ.

In semantic search, the direction of a vector represents meaning, while its length is usually less important.

That's why cosine similarity is widely used in RAG systems.
