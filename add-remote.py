from git_get import get_all_remote_repos
import subprocess
import re


def add_remote_repo(**kwargs):
    remote_repos =  get_all_remote_repos()
    print("Enter the remote ssh link/links of the repository. Separated by space. For example: name1=ssh_link1 name2=ssh_link2")
    remote_links = input().split()

    if not remote_links:
        print("No remote link provided")
        return
    
    for link in remote_links:
        try:
            name, link = link.split("=")
            for remote in remote_repos:
                ssh_pattern = r"^git@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+\.git$"
                if not re.match(ssh_pattern, link):
                    print(f"Invalid SSH format for {link}. Skipping this entry.")
                    continue
           
                platform_name = remote['platform_name']
                if name == platform_name and link != remote['ssh_link']:
                    print(f"Remote {name} already exists, please use a different name")
                    break
                elif link == remote['ssh_link']:
                    print(f"Remote {remote['ssh_link'] } already exists")
                    break   
                else:
                    print(subprocess.run(["git", "remote", "add", name, link], check=True))

        except ValueError:
            print("Invalid input. Please provide the remote name and link in the format name=link")
            return
        except subprocess.CalledProcessError:
            print("Error: Please make sure you are in a git repository")
            return
        

        
          

if __name__ == "__main__":
    add_remote_repo()


