import subprocess
from typing import List, Dict
import re


def get_all_remote_repos() -> List[Dict]: 
    try:
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, check=True)
        all_remote = result.stdout

        repo_list = parse_link(all_remote)

        return repo_list

    except:
        print("Error: Please make sure you are in a git repository")
        return []

    

def parse_link(all_remote: str) -> List[Dict]:
    repo_list = []
    all_remote = all_remote.split("\n")
    for remote in all_remote:
        match = re.search(r"(\S+)\s+git@(.*?):(.*?)/(.*?).git", remote)
        if match:
            platform_name = match.group(1) 
            platform = match.group(2)
            user = match.group(3)
            repo_name = match.group(4)
            repo_link = f"https://{platform}/{user}/{repo_name}"

            if ("push" in remote):
                repo_list.append({
                    "platform": platform,
                    "platform_name": platform_name,
                    "user": user,
                    "repo_name": repo_name,
                    "repo_link": repo_link,
                    "ssh_link": remote.removeprefix(platform_name + "\t").removesuffix(" (push)")
                })
    return repo_list
