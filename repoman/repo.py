import subprocess
import sys
import os
import re


class repo:
    
    def __init__(self, repo_file):
        self.repo_file = repo_file
       


    # Load the list of repos, return a list.
    def load_repo_list(self):
        with open(self.repo_file, 'r') as repo:
            repo_list = repo.readlines()
            return repo_list

    # check for repo's that are out of date, return a list of those repos
    def check_repos(self):
        repo_list = self.load_repo_list()
        _updatable_repos = []
        for repo in repo_list:
            repo_dir = repo.strip('\n')
            os.chdir(repo_dir)
            print(f'Updating remote: ')
            subprocess.run(['git', 'remote', 'update'])
            print(f'Checking the status of your repo')
            result = subprocess.run(
                ['git', 'status', '-s', '-uno'],
                capture_output=True,
                text=True
            )

            # Return the output of the git status command
            print(result.stdout)
            
            print(f'Updating repo: {repo_dir}')
            self.update_repo(repo_dir)

    def update_repo(self, repo):

            os.chdir(repo)
            result = subprocess.run(
                ['git', 'pull'],
                capture_output=True,
                text=True
            )
            print("*"*75)
            print(result.stdout)
