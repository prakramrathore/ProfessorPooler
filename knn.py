from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Read the cosine similarity matrix from the file cosine_sim.csv
profInterest_matrix = pd.read_csv('professors_topic_new.csv', index_col=0)

# Remove last three columns from the dataframe
profInterest_matrix = profInterest_matrix.iloc[:, :-8]
# print(profInterest_matrix)

# For each professor in profInterest_matrix, find the top 2 values in the row and make them 1 and rest 0.
for i in range(len(profInterest_matrix)):
    profInterest_matrix.iloc[i] = profInterest_matrix.iloc[i].apply(lambda x: 1 if x >= profInterest_matrix.iloc[i].nlargest(3).min() else 0)

# find the cosine similarity between each professor using sklearn
sim_matrix = cosine_similarity(profInterest_matrix)
# print(sim_matrix)

# Make rows and columns of the sim_matrix as professor names
sim_matrix = pd.DataFrame(sim_matrix, index=profInterest_matrix.index, columns=profInterest_matrix.index)

# Convert the sim_matrix to a dataframe and create a csv file from it
sim_matrix = pd.DataFrame(sim_matrix)
sim_matrix.to_csv('featurized_cosine_sim.csv')

# Implement KNN algorithm to find nearest neighbors of a given professor.
def knn(sim_matrix, professor, k):
    k = k+1
    # Get the index of the professor in the dataframe
    idx = sim_matrix.index.get_loc(professor)
    # Get the similarity scores of the professor
    sim_scores = list(enumerate(sim_matrix.iloc[idx]))
    # Sort the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the k most similar professors
    sim_scores = sim_scores[0:k]
    # Get the indices of the k most similar professors
    professor_indices = [i[0] for i in sim_scores]
    # Return the names of the k most similar professors
    return sim_matrix.index[professor_indices]

# Get the list of 5 most similar professors to PROF
PROF = 'Vinay P. Namboodiri'
k = 10
list_sim_prof = knn(sim_matrix, PROF, k).to_list()

# remove PROF from the list_sim_prof and print the list
if PROF in list_sim_prof:
  list_sim_prof.remove(PROF)
else:
  list_sim_prof = list_sim_prof[:k]

print(list_sim_prof)