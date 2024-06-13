import pandas as pd
import numpy as np

import streamlit as st
import pickle as pkl

pipe = pkl.load(open("Pipeline.pkl" ,"rb"))

st.header("Spam Mail Detector" ,divider="rainbow")

txt = [st.text_area("Past Your Email Below for Detect Spam or Ham Mail")]


if st.button("Detect", type="primary"):
    predict = pipe.predict(txt)
    st.header("",divider="orange")
    if(predict[0] == 1):
        st.title("Spam Mail")
    else:
        st.title("Ham Mail")

    
