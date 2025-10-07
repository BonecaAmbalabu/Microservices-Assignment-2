import React, { useEffect, useState } from 'react'

const COURSE_API = 'http://localhost:5002'

export default function Courses() {
  const [courses, setCourses] = useState([])

  const fetchCourses = () => {
    fetch(`${COURSE_API}/courses`).then(r => r.json()).then(setCourses)
  }

  useEffect(() => { fetchCourses() }, [])

  return (
    <section style={{ marginTop: 24 }}>
      <h2>Courses ({courses.length})</h2>
      {courses.map(c => (
        <div key={c.code}>
          <strong>{c.code}</strong> – {c.title} ({c.credits} credits)
        </div>
      ))}
    </section>
  )
}
