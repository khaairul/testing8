import streamlit as st
import pandas as pd
import numpy as np

st.title('Testing pickups in JB')

streamlit run uber_pickups.py

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
