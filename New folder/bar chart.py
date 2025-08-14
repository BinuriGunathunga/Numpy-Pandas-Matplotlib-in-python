import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("grades.csv")

names = df["Name"]
grades = df["Grade"]

plt.bar(names, grades)
plt.title("Student Grades")
plt.xlabel("Student") # X axis label 
plt.ylabel("Grades") # Y axis label
plt.show()  # Display the bar chart
