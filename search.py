import pandas as pd

# Load CSV "pubblications.csv" data
data = pd.read_csv("pubblications.csv")

# COnvert into DataFrame
df = pd.DataFrame(data)

# Show the first 5 rows
df.head()
