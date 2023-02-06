import streamlit as st
import time
import requests
import json
import plotly.express as px
import pandas as pd

def app():
    #  selected_address = st.session_state["address"]
    #  avaliableChains = st.session_state["chains"]
    st.title("About :information_source:")
    st.write("""
     This project is an entry for ETH Global FVM Space Warp 2023 hackathon

    Use the Sidebar for Navigation through the various use cases of the WebApp!

    
     Working with this project has enabled me to connect to developers in this field and motivated me to look for future opportunities in the field.

    Powered by: Lighthouse SDK and Push Protocol  
     """)
    col1, col2, _ = st.columns([1,1,5])
    with col1:
        st.image("https://www.lighthouse.storage/_next/image?url=%2Flogo.png&w=1920&q=75", width=150)
    with col2:
        st.image("assets/push.png", width=200)