\# Wiki Quiz App



An AI-powered web app that generates quizzes from Wikipedia articles using Gemini via LangChain.



\## Features

\- Generate quiz from Wikipedia URL

\- History of all quizzes

\- View full quiz from history

\- Related topics extraction

\- Duplicate URL prevention



\## Tech Stack

Frontend: React  

Backend: FastAPI  

AI: Google Gemini via LangChain  

Database: PostgreSQL  

Hosting: Vercel (frontend), Render (backend)



\## Live URLs

Frontend: https://wiki-quiz-khaki.vercel.app  

Backend: https://wiki-quiz-backend-kxzw.onrender.com  



\## API Endpoints



\### POST /generate?url=

Generates a quiz from a Wikipedia URL.



\### GET /history

Returns list of all past quizzes.



\### GET /quiz/{id}

Returns full quiz details.



\## How to Test

1\. Open frontend

2\. Paste a Wikipedia URL

3\. Click Generate

4\. Open History tab

5\. Click any quiz to view



\## Prompt Templates



\### Quiz Generation Prompt

The model is instructed to:

\- Read Wikipedia content

\- Generate multiple choice questions

\- Include answer, difficulty, and explanation



\### Related Topics Prompt

The model extracts important related concepts from the article.



These prompts are implemented in backend LangChain logic.



