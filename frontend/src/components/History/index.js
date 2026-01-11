import { useEffect, useState } from "react";
import "./index.css";

export default function History() {
  const [items, setItems] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    fetch("https://wiki-quiz-backend-kxzw.onrender.com/history")
      .then(res => res.json())
      .then(data => setItems(data));
  }, []);

  async function loadQuiz(id) {
    const res = await fetch(`https://wiki-quiz-backend-kxzw.onrender.com/quiz/${id}`);
    const json = await res.json();
    setSelected(json);
  }
  return (
    <div className="history-layout">

      {/* LEFT — Library */}
      <div className="history-list">
        <h2>Past Quizzes</h2>

        {items.map(q => (
          <div
            key={q.id}
            className={`history-row ${selected?.id === q.id ? "active" : ""}`}
            onClick={() => loadQuiz(q.id)}
          >
            <div className="row-text">
              <b>{q.title}</b>
              <div className="url">{q.url}</div>
            </div>
          </div>
        ))}
      </div>

      {/* RIGHT — Viewer */}
      <div className="history-detail">
        {!selected && (
          <div className="empty">
            Select a quiz to view it
          </div>
        )}

        {selected && (
          <div className="quiz-view">
            <h2>{selected.title}</h2>

            {/* Related Topics — REQUIRED BY ASSIGNMENT */}
            <div className="related-topics">
              <h4>Related Topics</h4>
              <div className="topics">
                {selected.related_topics.map((t, i) => (
                  <span key={i} className="topic-chip">{t}</span>
                ))}
              </div>
            </div>

            {selected.quiz.map((q, i) => (
              <div key={i} className="quiz-card">
                <h3>{i + 1}. {q.question}</h3>

                <ul className="options">
                  {q.options.map((o, j) => (
                    <li key={j}>{o}</li>
                  ))}
                </ul>

                <span className={`difficulty ${q.difficulty}`}>
                  {q.difficulty}
                </span>

                <div className="answer">
                  <p><b>Answer:</b> {q.answer}</p>
                  <p>{q.explanation}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  );
}
