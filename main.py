from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello"}

class UserCreate(BaseModel):
    name: str
    age: int

users = []

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