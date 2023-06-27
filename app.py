# Importing Libraries
import streamlit as st
import pandas as pd
import os

# Importing Pandas Modules
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2019/12/ONE-POINT-01-1.png")
    st.title("Automation of Exploratory Data Analysis")
    choice = st.radio("Navigation", ["Upload", "Profiling - EDA"])
    st.info("This Application Allows You to Build an Automated EDA Pipeline using Streamlit and Pandas Profiling")
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

    if choice == "Upload":
      st.title("Upload Your Data for EDA!")
      file = st.file_uploader("Upload Your Dataset Here")
      if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)
        
    
    if choice == "Profiling - EDA":
      st.title("Automated Exploratory Data Analysis")
      profile_report = df.profile_report()
      st_profile_report(profile_report)
  
