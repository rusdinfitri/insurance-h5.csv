import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **insurance expenses** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    age= st.sidebar.slider('age', 0.7, 297.0, 100.0)
    bmi = st.sidebar.slider('bmi', 0, 50.0, 15.0)
    children = st.sidebar.slider('children', 0.3, 114.0, 20.0)
    data = {'age': age,
            'bmi': bmi,
            'children': children}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

    

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("insurance.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader(' expenses Prediction')
st.write(prediction)
