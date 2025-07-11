# PRMate

Your personal AI buddy that automatically reviews your GitHub Pull Requests, offering clear, helpful, and contextual feedback on your code changes.  
Perfect for solo developers looking for quick, intelligent code reviews.


## Setup Instructions
This project requires either a **Ollama llama3** instance or an **OpenAI API key** to generate automated code reviews.

### Usage
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
export OPEN_API_KEY=your_openai_api_key
```
You do not need to install anything locally in this case.


## Environment Variables
To configure this project, you need to define several environment variables. These can be set in your local .env file, in your shell environment, or as GitHub Actions secrets.

- `GITHUB_TOKEN` **(required)**
This is your GitHub access token, used to authenticate API requests and post comments on pull requests.
In GitHub Actions, you can use the default `${{ secrets.GITHUB_TOKEN }}`.

- `OPEN_API_KEY` **(optional)**
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


## GitHub Actions Configuration
This project includes a pre-configured GitHub Actions workflow for running PR reviews.

```bash
.github/workflows/prmate-review.yml   
```

### Customizing the Workflow
- Trigger on specific pull requests
- Set environment variables for Ollama or OpenAI
- Run on a self-hosted or GitHub-hosted runner

Make sure your secrets (like `OPEN_API_KEY`) are added to the repository's GitHub Actions secrets tab.


## License  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  
