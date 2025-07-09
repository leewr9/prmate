import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "not_set")
OPEN_API_KEY = os.getenv("OPEN_API_KEY", "not_set")

if not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")
if not OPEN_API_KEY :
    raise EnvironmentError("OPEN_API_KEY environment variable is not set.")
