import { useState } from "react";
import CourseCard from "../components/CourseCard";
import courses from "../data/courses";

function Courses() {
  const [search, setSearch] = useState("");

  const filteredCourses = courses.filter(course =>
    course.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <h2>Courses</h2>

      <input
        type="text"
        placeholder="Search Course"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {filteredCourses.map(course => (
        <CourseCard
          key={course.id}
          name={course.name}
          credits={course.credits}
        />
      ))}
    </>
  );
}

export default Courses;