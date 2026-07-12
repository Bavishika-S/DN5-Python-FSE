from fastapi import FastAPI, HTTPException
from schemas import CourseCreate, CourseUpdate

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API",
    version="1.0"
)

courses = []


@app.get("/")
def home():
    return {"message": "Course Management API Running"}


@app.get("/api/courses/")
def get_courses():
    return courses


@app.post("/api/courses/")
def create_course(course: CourseCreate):
    new_course = {
        "id": len(courses) + 1,
        **course.model_dump()
    }
    courses.append(new_course)
    return new_course


@app.get("/api/courses/{course_id}")
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")


@app.put("/api/courses/{course_id}")
def update_course(course_id: int, updated: CourseUpdate):
    for course in courses:
        if course["id"] == course_id:
            course.update(updated.model_dump(exclude_unset=True))
            return course

    raise HTTPException(status_code=404, detail="Course not found")


@app.delete("/api/courses/{course_id}")
def delete_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return {"message": "Course deleted"}

    raise HTTPException(status_code=404, detail="Course not found")