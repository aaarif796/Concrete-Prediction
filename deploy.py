# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:41:58 2023

@author: aaari
"""

import streamlit as st
import joblib


model=joblib.load('c_s.joblib')



def app():
    st.title("This is the model to predict the strength of Concrete")
    cement=st.number_input("Enter cement amount(Range:100 to 550)",min_value=100,max_value=550)
    slag=st.number_input("Enter slag amount(Range:0 to 355)",min_value=0,max_value=335)
    ash=st.number_input("Enter ash amount(Range:0 to 201",min_value=0,max_value=201)
    water=st.number_input("Enter water amount(Range:120 to 246)",min_value=120,max_value=246)
    superplastic=st.number_input("Enter superplastic value(Range:0 to 25)",min_value=0,max_value=25)
    coarseagg=st.number_input("Enter coarseagg value(Range:80 to 1145)",min_value=800,max_value=1145)
    fineagg=st.number_input("Enter fineagg value(Range:590 to 1000)",min_value=590,max_value=1000)
    age=st.number_input("Enter age(Range(0 to 365)",min_value=0,max_value=365)
    if st.button("Predict"):
        strength=model.predict([[cement,slag,ash,
                             water,superplastic,coarseagg,
                             fineagg,
                             age]])
        st.write("The Strength of Concrete:",strength[0])

if __name__=='__main__':
    app()