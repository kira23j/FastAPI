from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional,List
app=FastAPI()
users=[]

class User(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]

@app.get('/users',response_model=List[User])
def get_user():
    return users

@app.post('/users')
def create_user(user:User):
    users.append(user)
    return "sucess"

@app.get("/users/{id}")
async def get_user(id:int = Path(...,description="The ID of user to retrieve",gt=2)):
    return users[id]

