import json
import re
from llm import get_llm
from quiz_prompt import quiz_prompt


def extract_json(llm_output):
    import json, re

    # Gemini sometimes returns list of message parts
    if isinstance(llm_output, list):
        llm_output = llm_output[0]["text"]

    # Remove markdown code blocks
    cleaned = re.sub(r"```json|```", "", llm_output).strip()

    return json.loads(cleaned)



def generate_quiz(article_text: str):
    llm = get_llm()
    chain = quiz_prompt | llm
    response = chain.invoke({"content": article_text})

    raw_text = response.content
    return extract_json(raw_text)
