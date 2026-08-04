from .embedding import data_embedding
import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("repo")

def data_base(all_chunks):
    print("adding chunks")
    count = 0
    length = len(all_chunks)
    for i, chunk in enumerate(all_chunks):
        vector = data_embedding(chunk["text"])
        
        collection.add(
            ids=[str(i)],
            documents=[chunk["text"]],
            embeddings=[vector],
            metadatas=[{"file": chunk["file"]}]
        )
        count+=1
        print(f"{count}/{length}")
    return "Successfully"


def query(qus):
    query_embeddings = data_embedding(qus)
    result = collection.query(
            query_embeddings=[query_embeddings],
            n_results=1
        )
    return result