from repoman.repo import repo

def main():
    r = repo('repo_list')

    r.check_repos()    
    
    

if __name__ == "__main__":
    main()