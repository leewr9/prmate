# PRMate

[![Latest Release](https://img.shields.io/github/v/release/leewr9/prmate)](https://github.com/leewr9/prmate/releases)
[![Build Test](https://github.com/leewr9/prmate/actions/workflows/build-test.yml/badge.svg)](https://github.com/leewr9/prmate/actions/workflows/build-test.yml)
[![Release Test](https://github.com/leewr9/prmate/actions/workflows/release-test.yml/badge.svg)](https://github.com/leewr9/prmate/actions/workflows/release-test.yml)

Your personal AI buddy that automatically reviews your GitHub Pull Requests, offering clear, helpful, and contextual feedback on your code changes.
Perfect for solo developers looking for quick, intelligent code reviews.

## Feature

- Automated AI-powered code review for Pull Requests
- Supports both Ollama (self-hosted) and OpenAI API backends
- Configurable review language (Korean/English) and strict mode formatting

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/leewr9/prmate.git
   cd prmate
   ```

2. **Install Dependencies via uv**

   ```bash
   uv sync
   ```

3. **Run the Application**

   ```bash
   uv run python -m app.main <pr_number> <repo_full_name>
   ```

## Usage

### Basic GitHub Actions Workflow

```yml
on:
  pull_request:
    types: [opened, reopened]
    branches: [master]

permissions:
  contents: read
  issues: write
  pull-requests: write

jobs:
  job:
    steps:
      - name: PRMate Review
        uses: leewr9/prmate@v1
        with:
          pr-number: ${{ github.event.pull_request.number }}
          repository: ${{ github.repository }}
          token: ${{ secrets.GITHUB_TOKEN }}
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          ollama-host: "http://127.0.0.1:11434"
          review-language: "English"
          review-strict: "True"
```

## Advanced Usage

### Choose Your LLM Backend

- Ollama (Self-hosted)

  ```bash
  export OLLAMA_HOST=http://your-ollama-server:11434
  ollama pull llama3
  ```

  - Self-hosted runner registration:

    https://github.com/<your-username>/<your-repository>/settings/actions/runners/new

  - Install Ollama based on OS:
    - Windows (WSL)

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

- OpenAI API

```bash
export OPENAI_API_KEY=your_openai_api_key
```

### Environment Variables

| Variable         | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `GITHUB_TOKEN`   | GitHub access token for API requests and posting comments (required)    |
| `OPENAI_API_KEY` | OpenAI API key (required if not using Ollama)                           |
| `OLLAMA_HOST`    | URL of your Ollama server (default: http://127.0.0.1:11434)             |
| `REVIEW_STRICT`  | Enable strict review formatting (True or leave unset for flexible mode) |
| `REVIEW_LANG`    | Review output language (`Korean` or `English`, default: Korean)         |

### GitHub Actions Configuration

Refer to the [example workflow](https://github.com/leewr9/prmate/blob/master/.github/example-workflow.yml) for advanced usage scenarios such as:

- Trigger conditions customization
- Using self-hosted runners
- Securely managing secrets like `OPENAI_API_KEY`

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
