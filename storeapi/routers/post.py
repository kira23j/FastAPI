from fastapi import APIRouter
from storeapi.models.post import UserPost, UserPostIn
  
router = APIRouter()
post_table = {} 

@router.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post

@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())