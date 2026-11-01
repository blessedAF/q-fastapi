from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int

users = []

@app.get("/")
def root():
    return {"message": "hello"}

@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    new_user = {"id": len(users) + 1, "name": user.name, "age": user.age}
    users.append(new_user)
    return new_user

@app.get("/users")
def list_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            return
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/health")
def health():
    return {"status": "ok"}