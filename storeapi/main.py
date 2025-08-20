from fastapi import FastAPI
from storeapi.routers.post import router as post_router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Store API"}

app.include_router(post_router)

