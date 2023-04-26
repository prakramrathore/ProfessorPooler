import streamlit as st
import pandas as pd

# Load CSV data
data = pd.read_csv("prof.csv")

# Define search function
def search(name):
    result = data[data['name'].str.startswith(name)]
    return result

# Set up Streamlit app
st.title("Professor Search")

# Search bar with autocomplete
query = st.multiselect("Enter professor name", 
                       data['name'].tolist(), 
                       key="search")

# Search button
if st.button("Search"):
    # Perform search
    result = search(query[0])
    
    # Display results
    if len(result) == 0:
        st.write("No results found.")
    else:
        for index, row in result.iterrows():
            st.write("Name:", row['name'])
            st.write("Affiliation:", row['affiliation'])
            st.write("Homepage:", row['homepage'])
