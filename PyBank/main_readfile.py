# Import modules
import csv
import os

# Set CSV File path
csvpath = os.path.join('..','Instructions','PyBank','Resources','budget_data.csv')

# Open and Read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Print Header and Data for sanity check
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Set variables
    net_total = 0.0
    month_count = 0
    net_change = 0.0
    max_change = 0.0
    min_change = 0.0
    max_month = ''
    min_month = ''
    average_change = 0.0
    monthly_profits = []

    # Iterate through each row in csv file.
    for row in csvreader:
        month_count += 1
        net_total = float(row[1])
        monthly_profits.append(float(row[1]))

        # Created new list of monthly profits. then iterate through to calculate the difference between each month
        for i in range(1,len(monthly_profits)):
            net_change = monthly_profits[i] - monthly_profits[i-1]
            
            # Find and store the biggest increase/decrease in profits over data set
            if float(net_change) > float(max_change):
                max_change = net_change
                max_month = row[0]
            elif float(net_change) < float(min_change):
                min_change = net_change
                min_month = row[0]
    
    # Average Change
    average_change = net_total / month_count

    # Printing
    print("Financial Analysis of Company")
    print("_______________________________")
    print(f"Total Months: {month_count}")
    print("Total Profits: ${:.2f}".format(net_total))
    print("Average Change: ${:.2f}".format(average_change))
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest decrease in Profits: {min_month} (${min_change})")
    print("_______________________________")

    print("Over " + str(month_count) + " months, the net P/L of the company is ${:.2f}".format(net_total))
    print("The average P/L over that time frame is ${:.2f}".format(average_change))
    ### NEED TO FIX THE calculation of MIN AND MAX CHANGE
    print(f"The greatest increase in profits is ${max_change}. This occurred in {max_month}.")
    print(f"The greatest decrease in profits is ${min_change}. This occurred in {min_month}.")