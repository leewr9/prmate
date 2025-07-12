# PRMate

Your personal AI buddy that automatically reviews your GitHub Pull Requests, offering clear, helpful, and contextual feedback on your code changes.  
Perfect for solo developers looking for quick, intelligent code reviews.

---

This action runs PRMate’s code review engine on a specified Pull Request.  
It fetches metadata and code diffs via GitHub's API, then uses an LLM to generate structured review feedback.

[Advanced Usage](#advanced-usage) — including local CLI execution, debugging, and self-hosted workflows.

## What's new

Please refer to the [release page](https://github.com/leewr9/prmate/releases/latest) for the latest release notes.

## Usage
```yml
on:
  pull_request:
    # Trigger the workflow when a Pull Request is opened or reopened
    types: [opened, reopened]

    # Only run the workflow for Pull Requests targeting the master branch
    branches: [master]

permissions:
  # Read access to repository contents
  contents: read

  # Write access to issues (needed for posting review comments)
  issues: write

  # Write access to pull requests (needed for posting review comments)
  pull-requests: write

jobs:
  job:
    steps:
    - name: PRMate Review
      uses: leewr9/prmate@v1
      with:
        # The number of the Pull Request that PRMate will analyze.
        # This value is typically passed from the event payload.
        pr-number: ${{ github.event.pull_request.number }}

        # The full name of the repository to analyze, in the format 'owner/repository'.
        # Default: ${{ github.repository }}
        repository: ${{ github.repository }}

        # The token used for GitHub API authentication.
        # Usually, this is set to the GITHUB_TOKEN secret provided by GitHub Actions.
        #
        # Default: ${{ github.token }}
        token: ${{ secrets.GITHUB_TOKEN }}

        # The OpenAI API key.
        # Required if you are not using Ollama.
        #
        # Make sure to store this securely as a secret.
        openai-api-key: ${{ secrets.OPENAI_API_KEY }}

        # The host URL of a locally running Ollama server, if you use Ollama.
        # Default: http://127.0.0.1:11434
        ollama-host: 'http://127.0.0.1:11434'

        # The language for the code review output.
        # Specify either "Korean" or "English".
        #
        # Default: Korean
        review-language: 'English'

        # Whether to enable strict review formatting.
        # Set to 'True' to activate strict mode.
        #
        # Default: False
        review-strict: 'True'
```

## Advanced Usage
This project requires either a **Ollama llama3** instance or an **OpenAI API key** to generate automated code reviews.

1. **Clone the repository**
    ```bash
    git clone https://github.com/leewr9/prmate.git
    cd prmate
    ```

2. **Install dependencies via uv**
    ```bash
    uv sync
    ```

3. **Run the application**
    ```bash
    uv run python -m app.main <pr_number> <repo_full_name>
    ```

### Choose Your LLM Backend
You can choose one of the following two options to power the review engine

#### Use Ollama
If you have your own `Ollama` server running, you can connect to it directly via HTTP by setting the environment variable

```bash
export OLLAMA_HOST=http://your-ollama-server:11434
```

If you don’t have a server yet, you can register a `self-hosted` runner on GitHub and run Ollama locally on your machine.

- **Register your GitHub runner**
    - `https://github.com/<your-username>/<your-repository>/settings/actions/runners/new`
    - ex) `https://github.com/leewr9/prmate/settings/actions/runners/new`

- **Run Ollama locally (self-hosted runner)**
    - **Set Environment Variable**
        ```bash
        export OLLAMA_HOST=http://127.0.0.1:11434
        ```

    - **Install Ollama (based on OS)**
        - Windows (via WSL)
            - Install WSL: [Microsoft Docs](https://learn.microsoft.com/en-us/windows/wsl/install)
            - Inside WSL terminal
                ```bash
                curl -fsSL https://ollama.com/install.sh | sh
                ollama serve
                ```

        - macOS
            ```bash
            brew install ollama
            ollama serve
            ```

        - Linux
            ```bash
            curl -fsSL https://ollama.com/install.sh | sh
            ollama serve
            ```
    - **Pull the Required Model**
        ```bash
        ollama pull llama3
        ```
        This will download the llama3 model used for generating code review comments.

#### Use OpenAI
If you're not using a self-hosted runner, you will need to use `OpenAI’s API`.

```bash
export OPENAI_API_KEY=your_openai_api_key
```
You do not need to install anything locally in this case.


### Environment Variables
To configure this project, you need to define several environment variables. These can be set in your local .env file, in your shell environment, or as GitHub Actions secrets.

- `GITHUB_TOKEN` **(required)**
This is your GitHub access token, used to authenticate API requests and post comments on pull requests.
In GitHub Actions, you can use the default `${{ secrets.GITHUB_TOKEN }}`.

- `OPENAI_API_KEY` **(optional)**
Set this if you want to use OpenAI as the backend for code review generation.
If you are **not using Ollama**, this variable must be provided.

- `OLLAMA_HOST` **(optional)**
Defines the base URL of your local or remote Ollama server.
The default is `http://127.0.0.1:11434`.
You only need this if you're running the model locally, typically on a self-hosted GitHub Actions runner.

- `REVIEW_STRICT` **(optional)**
Controls whether to use the strict review format.
Set this to `True` to enable structured output with strict rules.
Any other value will fall back to the default, more flexible prompt.

- `REVIEW_LANG` **(optional)**
Defines the output language for the code review.
Use `Korean` or `English` depending on your target audience.
If not set, it defaults to `Korean`.


### GitHub Actions Configuration
This project includes a pre-configured GitHub Actions workflow for running PR reviews.

[Example Workflow](https://github.com/leewr9/prmate/blob/master/.github/workflows/example.yml)

**Customizing the Workflow**
- Trigger on specific pull requests
- Set environment variables for Ollama or OpenAI
- Run on a self-hosted or GitHub-hosted runner

Make sure your secrets (like `OPENAI_API_KEY`) are added to the repository's GitHub Actions secrets tab.


## License  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  
