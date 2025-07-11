from langchain_ollama import ChatOllama

from app.config import OLLAMA_HOST, REVIEW_LANG
from app.llm.prompt import REVIEW_PROMPT_TEMPLATE, STRICT_REVIEW_PROMPT_TEMPLATE


class ReviewChain:
    def __init__(self):
        self.llm_client = ChatOllama(
            model="llama3", temperature=0.8, num_predict=256, base_url=OLLAMA_HOST
        )
        self.chain = REVIEW_PROMPT_TEMPLATE | self.llm_client

    def generate_review(self, code_diff: str) -> list[str]:
        response = self.chain.invoke({"code_report": code_diff, "language": REVIEW_LANG})

        if isinstance(response, str):
            return response
        if hasattr(response, "content"):
            return response.content

        raise ValueError(
            "Unexpected LLM response format: expected str or object with 'content'."
        )
