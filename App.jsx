import React, { useState } from "react";
import PHQ9Page from "./PHQ9Page";
import GAD7Page from "./GAD7Page";

export default function App() {
  const [tool, setTool] = useState("PHQ9"); // default page

  return (
    <div>
      {/* Switch buttons */}
      <div style={{ display: "flex", gap: "1rem", justifyContent: "center", margin: "1rem" }}>
        <button onClick={() => setTool("PHQ9")}>PHQ-9 (Depression)</button>
        <button onClick={() => setTool("GAD7")}>GAD-7 (Anxiety)</button>
      </div>

      {/* Render selected page */}
      {tool === "PHQ9" ? <PHQ9Page /> : <GAD7Page />}
    </div>
  );
}
