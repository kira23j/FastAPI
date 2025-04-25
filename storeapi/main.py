from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Store API"}

class UserPostIn(BaseModel):
   body:str  
    
class UserPost(UserPostIn):
    id: int
    
post_table = []

@app.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id + 1}
    post_table[last_record_id] = new_post
    return new_post

@app.get("/posts", response_model=list[UserPost])
async def get_posts():
    return list(post_table.values())