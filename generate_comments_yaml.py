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

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch comments. Status code: {response.status_code}")
        return None

def main():
    repo_owner = os.environ.get('GITHUB_REPOSITORY_OWNER')
    repo_name = os.environ.get('GITHUB_REPOSITORY_NAME')
    pr_number = os.environ.get('GITHUB_PR_NUMBER')
    access_token = os.environ.get('GITHUB_TOKEN')

    comments = get_pull_request_comments(repo_owner, repo_name, pr_number, access_token)

    if comments:
        output_file = 'pr_comments.yaml'
        with open(output_file, 'w') as f:
            yaml.dump(comments, f)

if __name__ == "__main__":
    main()
