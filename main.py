import uvicorn
from fastapi import FastAPI
# import pandas as pd
# import numpy as np 
from Banknotes import banknote
import pickle
import sklearn

app=FastAPI()

pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.post("/predict")

async def predict_banknote(data:banknote):
    data=data.dict()
    variance=data["variance"]
    skewness=data["skewness"]
    curtosis=data["curtosis"]
    entropy=data["entropy"]
    predictor=classifier.predict([[variance,skewness,curtosis,entropy]])
    if(predictor[0]>0.5):
        predictor="fake note"
    else:
        predictor="ita a bank note"
    return{
        "prediction":predictor
    }