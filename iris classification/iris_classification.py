# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:14:06 2021

@author: shubh
"""

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flowr Prediction App based on IRIS Dataset         
         """)

st.sidebar.header('User Input Parameter')

def user_input_features():
    sepal_length = st.sidebar.slider('sepal_length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('sepal_width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('petal_length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('petal_width', 0.1, 2.5, 0.2) 
    data = {'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width':petal_width}
    features=pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User input parameter')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class headers and their corresponding index')
st.write(iris.target_names)

st.subheader('Predictions')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)  