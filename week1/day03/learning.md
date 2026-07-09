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