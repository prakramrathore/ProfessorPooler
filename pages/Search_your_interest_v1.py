import pandas as pd
import streamlit as st
import random

# Load CSV "professors.csv" into the dataframe: df
df = pd.read_csv('professors_topic_new.csv')

# Put title
st.set_page_config(page_title='Professor Search', page_icon=':mag_right:')
st.title('Professor Search')

topics = {
    0: ['language', 'text', 'nlp', 'processing', 'sentiment', 'speech', 'linguistics', 'translation', 'retrieval',],
    1: ['vision', 'image', 'object', 'recognition', 'detection', 'segmentation', 'tracking', 'extraction'],
    2: ['algorithm', 'optimization', 'complexity','automata','cryptography'],
    3: ['neural', 'network', 'deep', 'learning'],
    4: ['data', 'big', 'analytics', 'mining', 'visualization', 'statistics', 'analytics', 'modeling',],
    5: ['robotics', 'control', 'autonomous', 'system'],
    6: ['database', 'query', 'sql', 'transaction', 'scheduling'],
    7: ['security', 'privacy', 'encryption', 'authentication', 'wireless','protocols','topology','routing','firewalls','architecture'],
    8: ['web', 'cloud', 'distributed','parallel','grid','scalability','tolerance','databases','middleware'],
    9: ['rendering','animation','virtual','shading','ray', 'tracing','texture'],
    10: ['compilers', 'interpreters', 'syntax'],
}

# Put search box
search_term = st.text_input('Search')

# convert to small letters
search_term = search_term.lower()

# Search button
if st.button('Search'):
    # Perform search
    result = []
    for i, key in topics.items():
        if search_term in key:
            result.append(i)
    
    # Display results
    if len(result) == 0:
        st.write('No results found.')
    else:
        st.write('Results:')
        for i in result:
            # write all the names of the professors in descending order of the values of ith column of data
            # st.write(data.iloc[i].tolist())
            st.write(i)
            # get the entries of "Professors Name" column of data with descending order of the values of i+1th column of data
            # st.write(df.iloc[:, i+1].tolist())
            target = df.iloc[:, [0, i+1, -2]]

            # sort the taget dataframe in descending order of the values of 1st column
            target = target.sort_values(by=[target.columns[1]], ascending=False)
            
            target = target.iloc[:11, [0,2]]


            # sort them by value of column "Score" in descending order
            target = target.sort_values(by=[target.columns[1]], ascending=False)

            target = target.iloc[:, 0].tolist()


            for j in target:
                link = df.loc[df['Professor Name'] == j, 'Home Page'].iloc[0]
                st.write(f"- {j}, [Home Page]({link})")


