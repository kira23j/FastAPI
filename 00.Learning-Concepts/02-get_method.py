from fastapi import FastAPI
from enum import Enum
from typing import Optional
app=FastAPI()


@app.get('/sample/all')
def get_all_samples(page=1,page_size:Optional[int] =None):
    return {'message':f'All {page_size} samples on {page}'}

@app.get('/sample/{id}/comment/{comment_id}')
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


