#!/usr/bin/env python
# coding: utf-8
# @author M. Stella Tavella mstella.tavella@gmail.com

import numpy as np
from transformers import pipeline

from config_models.sentiment import model_config_get

class Sentiment:

    def __init__(self):
        self.model_config = model_config_get()
    
    def load(self):
        self.model = pipeline(self.model_config['type'], model=self.model_config['path'], tokenizer=self.model_config['path'])

    def inference(self, input:str):
        prediction = self.model(input)
        return prediction
    
    def worker(self, input:list):
        prediction = self.inference(input)
        return prediction


