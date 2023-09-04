import os
from typing import List
from uuid import uuid4
from fastapi import FastAPI
import uvicorn
from models import User, Gender, Role

prefixed_path = os.getenv("PATH_PREFIX") if os.getenv("PATH_PREFIX") is not None else "/"

db: List[User] = [
    User(
        id=uuid4(),
        first_name="ariel",
        last_name="agranovich",
        # middle_name="borisovich",
        gender=Gender.male,
        roles=[Role.admin]
    ),
     User(
         id=uuid4(),
         first_name="deez",
         last_name="nuts",
         # middle_name="borisovich",
         gender=Gender.male,
         roles=[Role.admin]
     )
]
app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "banana"}


@app.get(f"/api/v1{prefixed_path}users")
async def fetch_users():
    return db


@app.post(f"/api/v1{prefixed_path}users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


