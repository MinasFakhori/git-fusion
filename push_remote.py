import subprocess
from git_get import get_all_remote_repos

def push_all(branch): 
    remote_repos = get_all_remote_repos()
    if not remote_repos:
        print("No remote repositories found.")
        return

    for remote in remote_repos:
        try:
            subprocess.run(["git", "push", remote["platform_name"], branch], check=True, text=True)
            print(f"Pushed {branch} to remote '{remote['platform_name']}' successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
            
def push_one(platform_name, branch="main"): 
    remote_repos = get_all_remote_repos()
    if not remote_repos:
        print("No remote repositories found.")
        return

    remote = next((remote for remote in remote_repos if remote['platform_name'] == platform_name), None)
    if not remote:
        print(f"Remote '{platform_name}' not found.")
        return

    try:
        subprocess.run(["git", "push", remote["platform_name"], branch], check=True, text=True)
        print(f"Pushed {branch} to remote '{remote['platform_name']}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
