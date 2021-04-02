# Import modules
import csv
import os

# Set CSV File path
csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('Analysis','Election_Results.txt')

with open(output_path, 'w', newline='') as writetxt:
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #print(csvreader)

        # Print Header and Data for sanity check
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}")
        
        # Define Variables
        voter_count = 0
        khan_count = 0
        correy_count = 0
        li_count = 0
        tooley_count = 0

        # Iterate through each row in csv file.
        for row in csvreader:
            voter_count += 1
            
            # Count votes for each candidate
            if row[2] == 'Khan':
                khan_count += 1
            elif row[2] == 'Correy':
                correy_count += 1
            elif row[2] == 'Li':
                li_count += 1
            elif row[2] == 'O\'Tooley':
                tooley_count += 1

        candidates = {''}

        # Calculate and format percentage of votes per candidate
        khan_percent = "{:.2%}".format(khan_count / voter_count)
        correy_percent = "{:.2%}".format(correy_count / voter_count)
        li_percent = "{:.2%}".format(li_count / voter_count)
        tooley_percent = "{:.2%}".format(tooley_count / voter_count)

        # Printing in terminal
        print('!!! ELECTION RESULTS !!!')
        print('------------------------')
        print(f'Total Votes: {voter_count}')
        print('------------------------')
        print(f'Votes for Khan: {khan_percent} [{khan_count}]')
        print(f'Votes for Correy: {correy_percent} [{correy_count}]')
        print(f'Votes for Li: {li_percent} [{li_count}]')
        print(f'Votes for O\'Tooley: {tooley_percent} [{tooley_count}]')
        print('------------------------')
        #print(f'The winner is... {winner}')

    # Print to txt file
    csvwriter = csv.writer(writetxt, delimiter = ' ')
    csvwriter.writerow(['ELECTION','RESULTS'])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['Votes','for','Khan:',khan_percent, [khan_count]])
    csvwriter.writerow(['Votes','for','Correy:',correy_percent, [correy_count]])
    csvwriter.writerow(['Votes','for','Li:',li_percent, [li_count]])
    csvwriter.writerow(['Votes','for','O\'Tooley:',tooley_percent, [tooley_count]])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['The','Winner','Is','...'])