import json
from fastapi import FastAPI
from models import Books

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/summaries/book/{id}")
def getBook(id):
    res = json.dumps(Books[int(id)])
    return res

