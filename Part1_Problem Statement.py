#load libraries
import numpy as np         # linear algebra
import pandas as pd        # data processing, CSV file I/O (e.g. pd.read_csv)

# Read the file "data.csv" and print the contents.
df = pd.read_csv('data/data.csv', index_col=False)

df.head()

# Save the cleaner version of dataframe with "id" for future analyis
df.to_csv('data/data_clean_id.csv')

df.info()

# Check for missing variables
df.isnull().any()

df.diagnosis.unique()

# Save the cleaner version of dataframe for future analyis
df.to_csv('data/data_clean.csv')
