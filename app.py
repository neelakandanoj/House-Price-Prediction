# import necessary librairies
import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('model.pkl','rb'))
st.set_page_config(page_title='Retail', layout='wide', page_icon="🛒")
from streamlit_option_menu import option_menu


st.write("""
<div style='text-align:center'>
    <h1 style='color:#009999;'>USA House Price Prediction</h1>
</div>
""", unsafe_allow_html=True)
selected = option_menu(None, ['HOME',"PRICE PREDICTION"],
                           icons=["house",'cash-coin','trophy'],orientation='horizontal',default_index=0)

if selected=='HOME':
        st.write('## **WELCOME TO USA House Price Prediction**')
        st.markdown('##### ***This project focuses on modelling USA House Price Prediction using Python and various libraries such as pandas, numpy, scikit-learn. The objective of the project is to preprocess the data, handle missing values, and handle skewness. Additionally, regression and classification models will be built to predict the selling price. The trained models will be saved as a pickle file for later use in a Streamlit application.***')
        st.write('### TECHNOLOGY USED')
        st.write('- PYTHON   (PANDAS, NUMPY)')
        st.write('- SCIKIT-LEARN')
        st.write('- DATA PREPROCESSING')
        st.write('- EXPLORATORY DATA ANALYSIS')
        st.write('- STREAMLIT')

elif selected=='PRICE PREDICTION':

  Per_Capita_GDP = st.text_input(" Per Capita GDP(Min: 45000.00 Max: 70000.00)")
  UNRATE = st.text_input("Input the Unemployment rate(Min: 4.0 Max: 15.0)")
  Cons_Materials = st.text_input("Enter the Construction_Price (Min: 500.00,Max:2500.00)")
  FEDFUNDS = st.slider("Enter the Intrest-rate",0,10)
  Per_Capita_GDP=(type=='True')
  UNRATE=(type=='True')
  Cons_Materials=(type=='True')
  inputs = [[Per_Capita_GDP, UNRATE, Cons_Materials, FEDFUNDS]]

  if st.button('Predict'):
    result = model.predict(inputs)
    result = float(result)
    result=round(result,2)
    st.success(f'The Estimated price of the house is {result} per unit area')


