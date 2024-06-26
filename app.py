import pandas as pd
import streamlit as st
import pickle
import sklearn
import json
import numpy as np

model = pickle.load(open('bangalore_home_prices_model.pickle', 'rb'))
locations = json.load(open('columns.json','r'))
st.title('Real Estate House Price Prediction')
st.text('Bangalore House Data')

location = st.selectbox('Location', locations['data_columns'][3:])

col1, col2, col3 = st.columns(3)

with col1:
    sqft = st.number_input('Square Foot Area', step=100)
with col2:
    bhk = st.number_input('BHK', step=1)
with col3:
    bath = st.number_input('No. of Bathrooms', step=1)

if st.button('Predict Price'):
    loc_index = np.where(pd.Series(locations['data_columns']) == location)[0][0]

    x = np.zeros(len(locations['data_columns']))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    result = model.predict([x])[0]
    st.text(f'The price would be around {round(result,2)} lakhs')
