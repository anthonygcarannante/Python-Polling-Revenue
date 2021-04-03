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
        #print(f"CSV Header: {csv_header}"

        # Initialize Variables
        voter_count = 0
        poll = {}
        
        # Iterate through each row in csv file.
        for row in csvreader:
            voter_count += 1 
            # Check if the voter exists as a key in the dictionary, if it does, add one to its vote count. if not, add candidate as new key
            if row[2] in poll.keys():
                poll[row[2]] += 1
            else:
                poll[row[2]] = 1

        # Store all of these values into lists for easy accessing
        candidates = []
        votes = []
        percents = []

        # Append dictionary items to new lists
        for key, value in poll.items():
            candidates.append(key)
            votes.append(value)
            percents.append("{:.2%}".format(value/voter_count))

        # Calculate winner based on max number of votes in the Dictionary
        winner = max(poll, key=poll.get)

        # Printing in terminal
        print('------------------------')
        print('!!! ELECTION RESULTS !!!')
        print('------------------------')
        print(f'Total Votes: {voter_count}')
        print('------------------------')
        for i in range(0,4): 
            print(f'Votes for {candidates[i]}: {percents[i]} ({votes[i]})')
        print('------------------------')
        print(f'The winner is... {winner}')

    # Print to txt file
    csvwriter = csv.writer(writetxt, delimiter = ' ')
    csvwriter.writerow(['ELECTION','RESULTS'])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['Total','Votes:',voter_count])
    for i in range(0,4):
        csvwriter.writerow(['Votes','for',candidates[i],':', percents[i], [votes[i]]])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['The','Winner','Is','...',winner])