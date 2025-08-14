import csv

# Writing to CSV
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price"]) 
    writer.writerow(["Pen", 50])
    writer.writerow(["Notebook", 250])
    writer.writerow(["Eraser", 35])

# Reading from CSV
with open("products.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
