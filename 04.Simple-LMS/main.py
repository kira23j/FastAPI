from fastapi import FastAPI


from api import users,sections,cources
from db.db_setup import engine
from db.models import user,cource

user.Base.metadata.create_all(bind=engine)
cource.Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Simple Lms",
    description="LMS for managing students and cources"
)
app.include_router(users.router)
app.include_router(cources.router)
app.include_router(sections.router)
