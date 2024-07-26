from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional,List

from api import users,sections,cources
app=FastAPI()
app.include_router(users.router)
app.include_router(cources.router)
app.include_router(sections.router)
