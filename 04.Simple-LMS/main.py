from fastapi import FastAPI


from api import users,sections,cources

app=FastAPI(
    title="Simple Lms",
    description="LMS for managing students and cources"
)
app.include_router(users.router)
app.include_router(cources.router)
app.include_router(sections.router)
