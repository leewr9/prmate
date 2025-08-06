import requests
from app.config import GITHUB_TOKEN


class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"token {GITHUB_TOKEN}",
                "Accept": "application/vnd.github.v3+json",
            }
        )

    def get_pr_files(self, repo_full_name: str, pr_number: int) -> list:
        url = f"{self.BASE_URL}/repos/{repo_full_name}/pulls/{pr_number}/files"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_pr_diff(self, repo_full_name: str, pr_number: int) -> str:
        url = f"{self.BASE_URL}/repos/{repo_full_name}/pulls/{pr_number}"
        headers = self.session.headers.copy()
        headers["Accept"] = "application/vnd.github.v3.diff"
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    def post_pr_comment(self, repo_full_name: str, pr_number: int, body: str) -> dict:
        url = f"{self.BASE_URL}/repos/{repo_full_name}/issues/{pr_number}/comments"
        data = {"body": body}
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
