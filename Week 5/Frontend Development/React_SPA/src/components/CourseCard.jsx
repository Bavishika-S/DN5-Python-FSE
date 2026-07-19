function CourseCard({ name, credits }) {
  return (
    <div>
      <h3>{name}</h3>
      <p>Credits: {credits}</p>
      <button>Enroll</button>
    </div>
  );
}

export default CourseCard;