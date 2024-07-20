from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def index():
    return "hello world"
@app.post('/nice')
def index_two():
    return "Nice"