import pandas as pd
df = pd.read_csv("grades.csv")
print(df.head())  # Display the first few rows of the DataFrame
print(df.describe())  # Get a statistical summary of the DataFrame