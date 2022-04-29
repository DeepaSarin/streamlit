# -*- coding: utf-8 -*-
"""Zeroshot_anger_label_streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GZCaVupofyN3isegi89dQCNgPilswaNg
"""

!pip install streamlit

!pip install transformers==3.1.0

import streamlit as st
from transformers import pipeline

user_input=st.text_area("                ","Enter the sentence here")
user_labels=st.text_area("                 ","Enter the labels seperated by comma")
user_label_split=user_labels.split(',')

classifier = pipeline("zero-shot-classification")
user_labels = ["politics", "public health", "economics"]

classifier(user_input, user_labels,multi_class=True)

