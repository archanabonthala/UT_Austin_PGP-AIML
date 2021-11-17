#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:03:51 2021

@author: archana
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle
import os
model = pickle.load(open('iris_updatable_clasifier.pras','rb'))
app = Flask(__name__)
@app.route('/api',methods=['POST'])
def predict():
    data= request.get_json(force=True)
    predict_request = [[data['sl'],data['sw'],data['pl'],data['pw']]]
    predict_request=np.array(predict_request)
    print(predict_request)
    prediction = model.predict(predict_request)
    print(prediction)
    output = prediction[0]
    print(output)
    return jsonify(int(output))

if  __name__ == '__main__':
    app.run(port=8111, debug = True)
    
    