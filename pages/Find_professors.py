import streamlit as st
import pandas as pd

topics = {
    0: ['language', 'text', 'nlp', 'processing'],
    1: ['vision', 'image', 'object', 'recognition'],
    2: ['algorithm', 'optimization', 'learning', 'model'],
    3: ['neural', 'network', 'deep', 'learning'],
    4: ['data', 'big', 'analytics', 'mining'],
    5: ['robotics', 'control', 'autonomous', 'system'],
    6: ['database', 'query', 'sql', 'transaction'],
    7: ['security', 'privacy', 'encryption', 'authentication'],
    8: ['software', 'engineering', 'testing'],
    9: ['web', 'cloud', 'distributed'],
}

# Load professors_topics CSV data
data = pd.read_csv("/home/rishi/myproject/professors_topic.csv")

i = 2
# get the i+1 th column of data
# st.write(data.iloc[:, i].tolist())

# get the first column and i+1 th column of data in descending order
target = data.iloc[:, [0, i+1]]

# sort the taget dataframe in descending order of the values of 1st column
target = target.sort_values(by=[target.columns[1]], ascending=False)

st.write(target)

# # Set up Streamlit app
# st.title("Professor Search")

# # Search bar with autocomplete
# query = st.text_input("Enter a keyword")

# # Search button
# if st.button("Search"):
#     # Perform search
#     result = []
#     for i, key in topics.items():
#         if query in key:
#             result.append(i)
    
#     # Display results
#     if len(result) == 0:
#         st.write("No results found.")
#     else:
#         st.write("Results:")
#         for i in result:
#             # write all the names of the professors in descending order of the values of ith column of data
#             # st.write(data.iloc[i].tolist())
#             st.write(i)
#             # get the entries of "Professors Name" column of data with descending order of the values of ith column of data
#             st.write(data.iloc[:, i+1].tolist())


# Define search function
# def search(keyword):
#     result = []
#     for i, key in keywords.items():
#         if keyword in key:
#             result += data.iloc[i].tolist()
#     return result

# # Set up Streamlit app
# st.title("Keyword Search")

# # Search bar with autocomplete
# query = st.text_input("Enter a keyword")

# # Search button
# if st.button("Search"):
#     # Perform search
#     result = search(query)
    
#     # Display results
#     if len(result) == 0:
#         st.write("No results found.")
#     else:
#         st.write("Results:")
#         for name in result:
#             st.write("- " + name)
