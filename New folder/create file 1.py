# Writing CSV data

import csv

with open('grades.csv', 'w', newline="") as file:

 writer = csv.writer(file)
 writer.writerow(["Name", "Grade"]) # header row 
 writer.writerow(["Alice", 85])
 writer.writerow(["Bob", 92])

# Reading CSV data

with open("grades.csv", "r") as file:
 reader = csv.reader(file)

 for row in reader:
    print(row) 