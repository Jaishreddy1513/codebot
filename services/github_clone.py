import os
from git import Repo


def git_clone(repo_url: str):
    
    local_dir = f"./rope_local/{repo_url.split("/")[-1].replace(".git","")}"
    os.system(f'rmdir /s /q rope_local')
    Repo.clone_from(repo_url,local_dir)
    print("Successfully Downloaded the repository")
    return local_dir