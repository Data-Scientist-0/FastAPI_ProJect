from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, AnyUrl, Field, EmailStr
from typing import Annotated, Optional
from fastapi.responses import JSONResponse
import json

from starlette import status

app = FastAPI()

def load_data()
    with open("students_detail.json","r") as u:
        data = json.load(u)
        return data

def save_data(data):
    with open("students_detail.json", "w") as f:
        json.dump(data, f, indent=4)


class Api(BaseModel):
    Student_ID: str
    Name: Annotated[str, Field(description="Student Name")]
    Father_Name: Annotated[str, Field(max_length=30)]
    Course: Optional[str] = None
    Contact:str
    Gmail: EmailStr

@app.get("/")
def homepage():
    return {'Message':'Student Management System API!'}

@app.get("/About/")
def about():
    return {'Message':'A fullyfunctional API to manage student data!'}

@app.get("/get")
def get_data():
    data = load_data()
    return JSONResponse(content={"message":"data has been added\n", "data":data})

@app.post("/post")
def post_data(student_id: Api):
    data = load_data()
    for student in data:
        if student.get["Student_ID"] == student_id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student already exists")
        data.append(student_id.dict())


        return JSONResponse(
            content={
                "message": "new studnet has been added",
                "student_id": student_id.dict()

            },
        )

