from langchain_core.prompts import ChatPromptTemplate


quiz_prompt = ChatPromptTemplate.from_template("""
You are given Wikipedia article content below.

Rules:
- Use ONLY the provided content
- Do NOT invent facts
- Return STRICT JSON only
- No extra text outside JSON

Generate 5–10 multiple-choice questions.
Each question must include:
- question
- 4 options
- correct answer
- difficulty (easy, medium, hard)
- short explanation

Also suggest 3–5 related Wikipedia topics.

JSON format:
{{
  "quiz": [
    {{
      "question": "",
      "options": ["", "", "", ""],
      "answer": "",
      "difficulty": "",
      "explanation": ""
    }}
  ],
  "related_topics": []
}}

CONTENT:
{content}
""")
