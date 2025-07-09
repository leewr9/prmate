from langchain.prompts import PromptTemplate

REVIEW_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["code_report", "language"],
    template=(
        "You are a senior software engineer performing a code review.\n"
        "Below is a summary of the code changes:\n"
        "{code_report}\n\n"
        "Please provide a concise but thorough review in bullet points, pointing out improvements, best practices, and potential bugs.\n\n"
        "Please write your response in {language}."
    )
)

STRICT_REVIEW_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["code_report", "language"],
    template=(
        "[ROLE: Code Review Expert]\n"
        "Review the following code change summary:\n"
        "{code_report}\n\n"
        "Respond strictly in this format:\n\n"
        "- 🟢 What’s Good:\n"
        "- 🟡 Suggestions:\n"
        "- 🔴 Critical Issues:\n\n"
        "Only respond in markdown, no explanations outside this format.\n\n"
        "Please write your response in {language}."
    )
)
