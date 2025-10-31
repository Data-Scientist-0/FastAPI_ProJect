from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, AnyUrl, Field, EmailStr
from typing import Annotated, Optional
from fastapi.responses import JSONResponse
import json
from starlette import status

app = FastAPI()

def load_data():#read mode sy data read and load karaya
    with open("students_detail.json","r") as u:
        data = json.load(u)
        return data

def save_data(data):#dump data write mode mn save kraya taky new entries mn koi masla na aye
    with open("students_detail.json", "w") as f:
        json.dump(data, f, indent=4)

class Api(BaseModel):# baese model bnanya jis mn class define ki taky is base per data save hojy
    Student_ID: str
    Name: Annotated[str, Field(description="Student Name")]
    Father_Name: Annotated[str, Field(max_length=30)]
    Course: Optional[str] = None
    Contact:str
    Gmail: EmailStr

@app.get("/") # app ko get kya or homage bnaya jis pr yeah message show
def homepage():
    return {'Message':'Student Management System API!'}#message kuch rkh skty hn apni mrzi sy dfine krskty hn

@app.get("/About/")#about page bnaya
def about():
    return {'Message':'A fullyfunctional API to manage student data!'}# jis mn ek message chla dya k kya kam krha ha app

@app.get("/get")# app command page bnaya jahan sy data get krsky
def get_data():
    data = load_data()
    return JSONResponse(content={"message":"data has been added\n", "data":data})

@app.post("/post")# post ka page bnaya jahan new entries ho sky
def post_data(students_detail: Api):
    data = load_data()
    for student in data: # 1 loop chlaya
        if student["Student_ID"] == students_detail.Student_ID:# student id agr entry mn match krjy to
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student already exists") #message chly
    new_student = students_detail.model_dump()  # Data dictionary mein convert kiya
    data.append(new_student)

# Save function ko call kiya
    save_data(data)

    # Loop ke bahar return kiya
    return JSONResponse(
        content={
            "message": "new student has been added",
            "student_id": new_student
        }
    )
