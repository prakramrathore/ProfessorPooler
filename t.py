import pandas as pd

# read "professors_topic.csv" 
profInterest_matrix = pd.read_csv('professors_topic_new.csv', index_col=0)

# get the list of professors
professors = profInterest_matrix.index.tolist()

# store the list of professors in a dataframe
professors = pd.DataFrame(professors)

# create a csv file from the dataframe
professors.to_csv('prof_here.csv', index=False, header=False)