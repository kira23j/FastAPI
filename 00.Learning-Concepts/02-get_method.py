from fastapi import FastAPI , status,Response
from enum import Enum
from typing import Optional
app=FastAPI()


@app.get('/sample/all')
def get_all_samples(page=1,page_size:Optional[int] =None):
    return {'message':f'All {page_size} samples on {page}'}
@app.get('sample.all',tags=["sample"])

@app.get('/sample/{id}/comment/{comment_id}',tags=["comment","sample"])
def get_comment(id:int , comment_id:int,valid:bool=True,username:Optional[str]=None):
    return {'message':f'sample_id{id},comment_id{comment_id},valid{valid},username{username}'}

@app.get('/sample/notype')
def get_all_samples():
    return {'message':'all samples are returned'}

class SampleType(str,Enum):
    short='short'
    story='story'
    howto='howto'
    
@app.get('/sample/type/{type}')
def get_sample_type(type:SampleType):
    return {'message':f'sample type {type}'}

# using type annotation
@app.get('/sample/{id}')
def show_sample(id:int):
    return {'message':f'sample with id no {id}' }

@app.get("/sample/{id}",status_code=status.HTTP_404_NOT_FOUND)
def get_blog(id:int,response:Response):
    if id>5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"error":f"blog {id} not found"}
    else:
        response.status_code=status.HTTP_200_OK
        return {"message":f"blog with id {id}"}
