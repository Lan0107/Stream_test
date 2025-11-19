import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NYC")

DATAURL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATECOLUMN = "data/time"

def load_data(nrows):
            data=pd.read_csv(DATA_URL,nrows=nrows)
            lowercase=lambda x: str(x).lower()
            data.rename(lowercase, axis="columns", inplace=True)
            data[DATECOLUMN]=pd.to_datatime(data.[DATECOLUMN])
            return data

dataloadstate=st.text("Loading Data...")
dataloaddata(10000)
dataloadstate=st.text("Loading Data...Done!")
___