def chunk_text(text, size=1000, overlap=60):
    chunks = []

    start = 0

    while start < len(text):
        end = start + size

        chunks.append(text[start:end])

        start += size - overlap

    return chunks


def chunk_file(documents):
    all_chunks = []
    for doc in documents:
        chunks = chunk_text(doc["content"])

        for chunk in chunks:
            all_chunks.append({
                "file": doc["file"],
                "text": chunk
            })
    return all_chunks
