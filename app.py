import numpy as np
import pandas as pd
import pickle as pk
import streamlit as st

# Load model 
model = pk.load(open('health.pkl', 'rb'))


st.header('Health insurance charges estimation')

# Input fields
gender = st.selectbox('Choose Gender',['Female','Male'])
smoker=st.selectbox("Are you Smoker ?",['Yes','No'])
region=st.selectbox("Choose Region",['SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.slider("Enter Age", 5, 80)
bmi = st.slider('Enter BMI', 5, 100)
children = st.slider('Choose No.Of Childrens', 0, 5)

if gender == 'Female':
    gender = 0
else:
    gender = 1    
    
if smoker == 'No':
    smoker = 0
else:
    smoker = 1    
    
if region ==  'SouthEast' :
    region = 0
if region == 'SouthWest'  :
    region = 1
if region == 'NorthEast'  :
    region = 2
else :
    region = 3     
       
# Prepare input data for prediction
text_data = (age,gender,bmi,children,smoker,region)
text_data = np.asarray(text_data)
text_data = text_data.reshape(1,-1)
# Predict button
if st.button('Predict'): 
    # Ensure that all values are the same type (numeric) for prediction
    prediction = model.predict(text_data)
    
    # Display the prediction
    display = 'Health insurance charges will be ' + str(np.round(prediction[0], 2)) + ' USD'
    st.markdown(display)

