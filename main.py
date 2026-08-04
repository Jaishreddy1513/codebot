from fastapi import FastAPI
from pydantic import BaseModel
from services.github_clone import git_clone
from services.file_loader import read_files
from services.chunk_files import chunk_file
from services.database import data_base,query,collection
from services.chatbot import llm
from services.embedding import delete

app = FastAPI()


class Github_Repo(BaseModel):
    github_url: str
class Query(BaseModel):
    question: str
    
@app.post("/github_repo")
def github_repo(data : Github_Repo):
    url = data.github_url
    delete()
    repo_path = git_clone(url)
    file_data = read_files(repo_path)
    chunk_data = chunk_file(file_data)
    data_base(chunk_data)
    return{
        "message":"Successfully"
    }
    
@app.post("/query")
def ask(data:Query):
    qus = data.question
    context = query(qus)
    output = llm(context,qus)
    return {
        'query':qus,
        "output":output
    }
    
@app.get("/data")
def get_all_data():
    get_data = collection.get()
    return get_data
    