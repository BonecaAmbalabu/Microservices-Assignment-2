import React from "react";
import Students from "./Students";
import Courses from "./Courses";

export default function App() {
  return (
    <div style={{ maxWidth: 900, margin: '0 auto', padding: 24 }}>
      <h1>Admin Portal</h1>
      <Students />
      <Courses />
    </div>
  )
}
