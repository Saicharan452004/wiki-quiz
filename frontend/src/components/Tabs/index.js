import "./index.css";

export default function Tabs({ active, onChange }) {
  return (
    <div className="tabs">
      <button
        className={`tab-btn ${active === "generate" ? "active" : ""}`}
        onClick={() => onChange("generate")}
      >
        Generate Quiz
      </button>

      <button
        className={`tab-btn ${active === "history" ? "active" : ""}`}
        onClick={() => onChange("history")}
      >
        History
      </button>
    </div>
  );
}
