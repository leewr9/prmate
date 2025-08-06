import sys
from app.github import GitHubClient
from app.llm.chain import ReviewChain


def main(pr_number: int, repo_full_name: str):
    gh_client = GitHubClient()
    review_chain = ReviewChain()

    pr_diff_text = gh_client.get_pr_diff(repo_full_name, pr_number)

    review_comments = review_chain.generate_review(pr_diff_text)
    gh_client.post_pr_comment(repo_full_name, pr_number, review_comments)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python -m app.main <pr_number> <repo_full_name>")
        sys.exit(1)

    pr_number = int(sys.argv[1])
    repo_full_name = sys.argv[2]
    main(pr_number, repo_full_name)
