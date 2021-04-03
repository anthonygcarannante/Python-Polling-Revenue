# Import modules
import csv
import os

# Set CSV File path
csvpath = os.path.join('..','Instructions','PyBank','Resources','budget_data.csv')
output_path = os.path.join('Analysis','Results.txt')

# Open and Read CSV file
with open(output_path, 'w', newline='') as writetxt:
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #print(csvreader)

        # Print Header and Data for sanity check
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}")
        
        # Set variables
        net_total, net_change, max_change, min_change = 0.0, 0.0, 0.0, 0.0
        month_count = 0
        max_month, min_month = '', ''
        average_change, monthly_profits, greatest, lowest = [], [], [], []

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
        
        # Store values in lists
        greatest.append(max_month)
        greatest.append(max_change)
        lowest.append(min_month)
        lowest.append(min_change)

        # Average Change
        average_change = net_total / month_count

        # Printing
        print("---------------------------------")
        print("Financial Analysis of My Company")
        print("---------------------------------")
        print(f"Total Months: {month_count}")
        print("Total Profits: ${:.2f}".format(net_total))
        print("Average Change: ${:.2f}".format(average_change))
        print(f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})")
        print(f"Greatest Decrease in Profits: {lowest[0]} (${lowest[1]})")

    # Write to a text file
    csvwriter = csv.writer(writetxt, delimiter = ' ')
    csvwriter.writerow(['Financial','Analysis','of','My','Company'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow(['Total','Months:', month_count])
    csvwriter.writerow(['Total','Profits:','${:.2f}'.format(net_total)])
    csvwriter.writerow(['Average','Change:','${:.2f}'.format(average_change)])
    csvwriter.writerow(['Greatest','Increase','In','Profits:',max_month,'(${:.2f})'.format(max_change)])
    csvwriter.writerow(['Greatest','Decrease','In','Profits:',min_month,'(${:.2f})'.format(min_change)])