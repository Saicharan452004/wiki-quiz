import { useState } from "react";
import Tabs from "./components/Tabs";
import Generate from "./components/Generate";
import History from "./components/History";

function App() {
  const [tab, setTab] = useState("generate");

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h2>Wiki Quiz App</h2>

      <Tabs active={tab} onChange={setTab} />

      {tab === "generate" && <Generate />}
      {tab === "history" && <History />}
    </div>
  );
}

export default App;
