from pathlib import Path

extensions = {
    ".py", ".js", ".jsx", ".ts",
    ".tsx", ".html", ".css",
    ".json", ".md"
}

def read_files(path:str):
    documents = []

    for file in Path(path).rglob("*"):
        if file.suffix in extensions:
            try:
                text = file.read_text(encoding="utf-8")
                documents.append({
                    "file": str(file),
                    "content": text
                })
            except:
                pass
            
    return documents