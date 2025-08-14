import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("grades.csv")

names = df["Name"]
grades = df["Grade"]

plt.table(names, grades)
plt.title("Student Grades")
plt.xlabel("Student") 
plt.ylabel("Grades") 
plt.show()  # Display the table
