import re
import subprocess
from git_get import get_all_remote_repos

SSH_PATTERN = r"^git@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+\.git$"

def validate_ssh_link(link):
    return re.match(SSH_PATTERN, link) is not None

def add_remote_repo():
    remote_repos = get_all_remote_repos()
    print("Enter the remote SSH links in the format: name1=ssh_link1 name2=ssh_link2")
    remote_links = input().strip().split()

    if not remote_links:
        print("No remote links provided.")
        return

    for entry in remote_links:
        try:
            name, link = entry.split("=")
        except ValueError:
            print(f"Invalid input format for '{entry}'. Use the format: name=link")
            continue

        if not validate_ssh_link(link):
            print(f"Invalid SSH format for link: {link}. Skipping this entry.")
            continue

        # Check if the remote already exists
        existing_remote = next((remote for remote in remote_repos if remote['platform_name'] == name), None)
        if existing_remote:
            if link == existing_remote['ssh_link']:
                print(f"Remote '{name}' with the same link already exists.")
            else:
                print(f"Remote '{name}' already exists with a different link. Use a different name.")
            continue

        try:
            subprocess.run(["git", "remote", "add", name, link], check=True, text=True)
            print(f"Remote '{name}' added successfully.")
        except subprocess.CalledProcessError:
            print("Error: Make sure you are in a valid git repository.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    add_remote_repo()