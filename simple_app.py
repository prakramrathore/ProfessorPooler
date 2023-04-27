import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')



topics = {
    0: ['language', 'text', 'nlp', 'processing', 'sentiment', 'speech', 'linguistics', 'translation', 'retrieval',],
    1: ['vision', 'image', 'object', 'recognition', 'detection', 'segmentation', 'tracking', 'extraction'],
    2: ['algorithm', 'optimization', 'complexity','automata','cryptography'],
    3: ['neural', 'network', 'deep', 'learning'],
    4: ['data', 'big', 'analytics', 'mining', 'visualization', 'statistics', 'analytics', 'modeling',],
    5: ['robotics', 'control', 'autonomous', 'system'],
    6: ['database', 'query', 'sql', 'transaction', 'scheduling'],
    7: ['security', 'privacy', 'encryption', 'authentication', 'wireless','protocols','topology','routing','firewalls','architecture'],
    9: ['web', 'cloud', 'distributed','parallel','grid','scalability','tolerance','databases','middleware'],
    10: ['rendering','animation','virtual','shading','ray', 'tracing','texture'],
    11: ['compilers', 'interpreters', 'syntax'],
}

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# st.subheader('Map of all pickups')
# st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

hour_to_filter = st.slider('hour', 0, 23, 17)

