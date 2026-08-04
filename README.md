# 🤖 GitHub Code Chatbot (RAG)

An AI-powered chatbot that lets you **chat with any public GitHub repository**. Simply provide a GitHub repository URL, and the chatbot clones the repository, indexes the source code using embeddings, stores it in ChromaDB, and answers your questions using a Large Language Model (LLM).

> ⚡ Built **without LangChain** using Python, FastAPI, ChromaDB, Sentence Transformers, and Groq/OpenAI.

---

## ✨ Features

- 🔗 Clone any public GitHub repository
- 📂 Automatically read source code files
- ✂️ Smart code chunking
- 🧠 Generate embeddings using Sentence Transformers
- 💾 Store embeddings in ChromaDB
- 🔍 Semantic code search
- 💬 Ask questions about the repository
- 🤖 AI-generated answers with repository context
- ⚡ Fast and lightweight architecture
- 🚫 No LangChain dependency

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
| GitPython | Clone GitHub repositories |
| Sentence Transformers | Generate embeddings |
| ChromaDB | Vector database |
| Groq/OpenAI/Gemini | Large Language Model |
| GitHub | Source code retrieval |

---

## 📁 Project Structure

```
genai/
│
├── main.py
│
└── services/
    ├── chatbot.py
    ├── chunk_files.py
    ├── database.py
    ├── embedding.py
    ├── file_loader.py
    ├── github_clone.py
    └── __init__.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jaishreddy1513/codebot.git
```

### 2. Navigate to the project

```bash
cd <codebot>
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key
```

---

## ▶️ Run the Project

```bash
uvicorn main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 How It Works

1. Enter a GitHub repository URL.
2. Clone the repository locally.
3. Read supported source code files.
4. Split files into smaller chunks.
5. Generate embeddings for each chunk.
6. Store embeddings in ChromaDB.
7. Ask questions about the repository.
8. Retrieve the most relevant code snippets.
9. Send the retrieved context to the LLM.
10. Receive an AI-generated answer.

---

## 🧠 Architecture

```
                User
                  │
                  ▼
         Enter GitHub URL
                  │
                  ▼
          Clone Repository
                  │
                  ▼
           Load Source Files
                  │
                  ▼
             Chunk Source Code
                  │
                  ▼
        Generate Embeddings
                  │
                  ▼
          Store in ChromaDB
                  │
                  ▼
           User Asks Question
                  │
                  ▼
       Semantic Similarity Search
                  │
                  ▼
      Retrieve Relevant Code Chunks
                  │
                  ▼
         Send Context to LLM
                  │
                  ▼
           AI Generated Answer
```

---

## 📌 Supported File Types

- Python
- Java
- JavaScript
- TypeScript
- C
- C++
- Go
- HTML
- CSS
- JSON
- Markdown
- Text files

---

## 💡 Example Questions

- How does authentication work?
- Explain the project architecture.
- Where is the database connection created?
- Which API handles user login?
- Explain the `main.py` file.
- How are embeddings generated?
- What libraries are used in this project?
- Show me where FastAPI is initialized.
- Explain this function.
- How does the chatbot retrieve answers?

---

## 🔮 Future Improvements

- Private GitHub repository support
- GitHub OAuth authentication
- Conversation memory
- Repository update detection
- Hybrid Search (BM25 + Vector Search)
- Function-level code chunking
- Streaming responses
- Multi-repository support
- Docker support
- React frontend
- User authentication
- Code citations with line numbers

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Jaish Reddy**

If you found this project helpful, consider giving it a ⭐ on GitHub!