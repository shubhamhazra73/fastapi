#pip install fastapi uvicorn

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def index() :
    return {'message' : 'Hello World'}

@app.get('/connect')
def check_connection(name : str) :
    return {'Connection established by ' : name}
#####################################################

###########################################################################
from params import question_pairs
import numpy as np
import pickle
import pandas as pd

pickle_in = open('model.pkl', "rb")
algo = pickle.load(pickle_in)

@app.post('/predict')
def predict_same_or_different(data : question_pairs) :
    data = data.dict()

    question1 = data['question1']
    question2 = data['question2']

    return {
        'prediction' : 'result predicted successfully : '
    }
#########################################################
if __name__ == '__main__' :
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
#python -m uvicorn main:app --reload



