# Import modules
import csv
import os

# Set CSV File path
csvpath = os.path.join('..','Instructions','PyBank','Resources','budget_data.csv')

# Open and Read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Print Header and Data for sanity check
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        print(row)

