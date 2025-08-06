import pytest
from unittest.mock import patch
from app.github import GitHubClient


@patch("app.github.requests.Session.get")
def test_get_pr_files_mock(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            "sha": "719be62e9382eaed6b25ec98d8190e141ce329eb",
            "filename": "README",
            "status": "modified",
            "additions": 6,
            "deletions": 1,
            "changes": 7,
            "blob_url": "https://github.com/octocat/Hello-World/blob/7044a8a032e85b6ab611033b2ac8af7ce85805b2/README",
            "raw_url": "https://github.com/octocat/Hello-World/raw/7044a8a032e85b6ab611033b2ac8af7ce85805b2/README",
            "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/README?ref=7044a8a032e85b6ab611033b2ac8af7ce85805b2",
            "patch": '@@ -1 +1,6 @@\n-Hello World!\n\\ No newline at end of file\n+Hello World!\n+$ mkdir ~/Hello-WorldCreates a directory for your project called "Hello-World" in your user directory\n+$ cd ~/Hello-WorldChanges the current working directory to your newly created directory\n+$ git initSets up the necessary Git files\n+Initialized empty Git repository in /Users/your_user_directory/Hello-World/.git/\n+$ touch README\n\\ No newline at end of file',
        }
    ]

    client = GitHubClient()
    files = client.get_pr_files("octocat/Hello-World", 1)

    assert len(files) == 1
    assert files[0]["filename"] == "README"


@patch("app.github.requests.Session.get")
def test_get_pr_diff_mock(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = """
diff --git a/README b/README
index c57eff55..719be62e 100644
--- a/README
+++ b/README
@@ -1 +1,6 @@
-Hello World!
\\ No newline at end of file
+Hello World!
+$ mkdir ~/Hello-World
+$ cd ~/Hello-World
+$ git init
+Initialized empty Git repository
+$ touch README
\\ No newline at end of file
"""

    client = GitHubClient()
    diff = client.get_pr_diff("octocat/Hello-World", 1)

    assert isinstance(diff, str)
    assert "diff --git" in diff
    assert "+$ mkdir" in diff
