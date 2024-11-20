import os

import typer

from src.add_remote import add_remote_repo
from src.git_get import get_all_remote_repos
from src.push_remote import push_all,push_one



app = typer.Typer()

@app.command(name="add-repo", help="Adds a git remote repository to the current repository.")
def add_repo():
    add_remote_repo()
    
@app.command(name="list-repos", help="Lists all the remote repositories of the current repository.")
def list_repos(): 
    print(get_all_remote_repos())
    
@app.command(name="push-all", help="Pushes the current branch to all remote repositories.")
def push_everything(branch="main"):
    push_all(branch)

@app.command(name="push-one", help="Pushes the current branch to a specific remote repository.")
def push_one_thing(platform_name: str, branch="main"):
    push_one(platform_name, branch)

    
    
    
if __name__ == "__main__":
    app()