from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# STEP 1: Load Documents
documents = SimpleDirectoryReader(
    input_dir="./data"
).load_data()

# STEP 2: Build the Vector Index

index = VectorStoreIndex.from_documents(documents)

# STEP 3: Create a Query Engine

query_engine = index.as_query_engine(
    similarity_top_k=3
)

# STEP 4: Ask Questions Continuously

print("=" * 60)
print("LlamaIndex RAG System")
print("Type 'exit' to quit.")
print("=" * 60)

while True:
    question = input("\nAsk a Question: ")
    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    response = query_engine.query(question)
    print("\nAnswer:")
    print(response)
    print("\n" + "=" * 60)