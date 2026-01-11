import { useState } from "react";
import "./index.css";

export default function Generate() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);

  async function generateQuiz() {
  if (!url.trim()) {
    alert("Please paste a Wikipedia URL");
    return;
  }

  setLoading(true);

  try {
    const res = await fetch("https://wiki-quiz-backend-kxzw.onrender.com/generate?url=" + url, {
      method: "POST"
    });

    const json = await res.json();
    setData(json);
  } catch (err) {
    alert("Failed to generate quiz");
  }

  setLoading(false);
}


  return (
    <div className="generate-container">
      <div className="input-row">
        <input
          placeholder="Paste Wikipedia URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={generateQuiz} disabled={loading}>
          {loading ? "Generating..." : "Generate Quiz"}
        </button>
      </div>

      {data && (
        <div className="quiz-result">
          <h2>{data.title}</h2>
          <p className="summary">{data.summary}</p>
          <div className="related-topics">
            <h4>Related Topics</h4>
            <div className="topics">
              {data.related_topics.map((t, i) => (
                <span key={i} className="topic-chip">{t}</span>
              ))}
            </div>
          </div>  


          <div className="quiz-list">
            {data.quiz.map((q, index) => (
              <div key={index} className="quiz-card">
                <h3>
                  {index + 1}. {q.question}
                </h3>

                <ul className="options">
                  {q.options.map((opt, i) => (
                    <li key={i}>{opt}</li>
                  ))}
                </ul>

                <div className="meta">
                  <span className={`difficulty ${q.difficulty}`}>
                    {q.difficulty}
                  </span>
                </div>

                <div className="answer">
                  <p><b>Answer:</b> {q.answer}</p>
                  <p><b>Explanation:</b> {q.explanation}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
