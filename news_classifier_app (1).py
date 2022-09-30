# -*- coding: utf-8 -*-
"""News_classifier_app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13kg-I6ZqBeH8Zm4QFyHninb9-zcMfJko
"""
! pip install transformers==2.4.1
!pip install --upgrade pip
!pip install rust
! pip install streamlit



# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:31:28 2022
@author: p.santosh.dandale
"""
import pandas as pd
import streamlit as st
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
from PIL import Image

pickle_in = open(r"/content/drive/My Drive/PRACTICE/2022SepNewsProject/News Classification Code Files/news_classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def predict_news_category(News):
    Tfidf_vect = TfidfVectorizer(max_features=5000)
    News_tr=Tfidf_vect.transform([News])
    prediction=(Encoder.inverse_transform(Naive.predict(News_tr))[0])
    print(prediction)
    return prediction  
    
def Input_Output():
    st.title("News Category Prediction")
    st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2F736x%2F80%2F0d%2F23%2F800d23c71a4fa03a3280402193978a8d--latest-jokes-website-software.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Ftechcruiser%2F&tbnid=tIL3MKDaEsrwoM&vet=12ahUKEwiWg5X9kL36AhUOktgFHWaMA74QMyghegUIARCvAg..i&docid=vDjLB-YVZRL1OM&w=351&h=199&q=online%20news%20images&ved=2ahUKEwiWg5X9kL36AhUOktgFHWaMA74QMyghegUIARCvAg", width=600)
    
    st.markdown("You are using Streamlit...",unsafe_allow_html=True)
    st.markdown("Coal,Petroleum,Agriculture...",unsafe_allow_html=True)
                
    news  = st.text_input("Enter News to be classified " , ".")
    
    result = ""
    if st.button("Click here to Predict"):
        result = predict_news_category(news)
        st.balloons()     
    st.success('The output is {}'.format(result))
   
if __name__ ==  '__main__':
    Input_Output()

pip freeze requirements.txt

