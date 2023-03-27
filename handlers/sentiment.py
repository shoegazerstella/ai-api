#!/usr/bin/env python
# coding: utf-8
# @author M. Stella Tavella mstella.tavella@gmail.com

from fastapi import FastAPI, HTTPException
from time import time
#import json

from workers.sentiment.worker import Sentiment
from config_models.sentiment import model_config_get

def create_app():

    sentiment = Sentiment()
    
    sentiment.load()

    # create app
    app = FastAPI()

    return app, sentiment

# LOAD MODELS AND CREATE APP
app, sentiment = create_app()

# HANDLER
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/sentiment")
async def get_sentiment(input_data: dict):

    try:
        input_data = input_data['input']

        # do inference
        prediction = sentiment.worker(input_data)

        # serve response
        data_response = {}
        data_response['prediction'] = prediction
        data_response['model'] = model_config_get()

        return data_response
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))