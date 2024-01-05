import os
import requests
import yaml

def get_pull_request_comments(repo_owner, repo_name, pr_number, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments'
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    github_repository = os.environ.get('GITHUB_REPOSITORY')
    repo_owner, repo_name = github_repository.split('/')

    github_pr_number = os.environ.get('GITHUB_EVENT_NUMBER')
    github_token = os.environ.get('GITHUB_TOKEN')

    comments = get_pull_request_comments(repo_owner, repo_name, github_pr_number, github_token)

    output_file = 'pr_comments.yaml'
    with open(output_file, 'w') as f:
        yaml.dump(comments, f)

if __name__ == "__main__":
    main()
