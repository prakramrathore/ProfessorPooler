import streamlit as st

# List of keywords
keywords = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango']

# Set the page heading
st.header("Keywords")

# Display the keywords as rectangular boxes
for keyword in keywords:
    st.markdown(f'<div style="background-color: #f0f0f0; color: #000; display: inline-block; margin: 5px; padding: 5px 10px; border-radius: 10px;">{keyword}</div>', unsafe_allow_html=True)
