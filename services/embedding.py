from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
print("Database")   

def delete():
    try:
        model.client.delete_collection(name="repo")
    except Exception:
        pass


def data_embedding(data):
    return model.encode(data)