from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from security import verify_password, create_access_token, verify_token
from users import users

app = FastAPI(
    title="JWT Authentication API"
)


class Login(BaseModel):
    email: str
    password: str


@app.get("/")
def home():
    return {"message": "JWT Authentication Running"}


@app.post("/login")
def login(data: Login):

    user = users.get(data.email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        data.password,
        user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": data.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@app.get("/profile")
def profile(user=Depends(verify_token)):
    return {
        "message": "Protected route accessed successfully",
        "user": user["sub"]
    }