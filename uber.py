import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NYC")

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATE_COLUMN = "data/time"

def load_data(nrows):
            data=pd.read_csv(DATA_URL,nrows=nrows)
            lowercase=lambda x: str(x).lower()
            data.rename(lowercase, axis="columns", inplace=True)
<<<<<<< HEAD
            data[DATE_COLUMN]=pd.to_datatime(data.[DATE_COLUMN])
            return data

data_load_state=st.text("Loading Data...")
data_load_data(10000)
data_load_state=st.text("Loading Data...Done!")
=======
            data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
            return data

data_load_state=st.text("Loading data...")
data = load_data(10000)
data_load_state=st.text("Loading data...Done!")
st.subheader("Raw Data")
st.write(data)
>>>>>>> fcc4603729b143179fa9bf00ca1b32e725f5f35a
