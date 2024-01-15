from typing import Union
from fastapi import FastAPI
import json

# Open model.json data as default data to return
f = open('../../model.json')
data = json.load(f)

# Initialize app
app = FastAPI()

# GET request
@app.get('/rest_fastapi')
def read_root():
    global data
    return data

# Run with uvicorn