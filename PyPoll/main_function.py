# Import modules
import csv
import os

# Set CSV File path
csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('Analysis','Election_Results_function.txt')

# Store all of these values into lists for easy accessing
candidates = []
votes = []
percents = []
winner = []

def poll_calc():
    voter_count = 0
    poll = {}

    for row in csvreader:
        voter_count += 1
        # Check if the voter exists as a key in the dictionary, if it does, add one to its vote count. if not, add candidate as new key
        if row[2] in poll.keys():
            poll[row[2]] += 1
        else:
            poll[row[2]] = 1

    # Append dictionary items to new lists
    for key, value in poll.items():
        candidates.append(key)
        votes.append(value)
        percents.append("{:.2%}".format(value/voter_count))
    
    # Store in a dictionary
    poll_results = {"Candidates":candidates,"Votes":votes,"Percents,":percents}

    # Calculate winner based on max number of votes in the Dictionary
    winner.append(max(poll, key=poll.get))
    winner.append(voter_count)

    return candidates, percents, votes, winner, poll_results

with open(output_path, 'w', newline='') as writetxt:
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Print Header and Data for sanity check
        csv_header = next(csvreader)

        # Iterate through each row in csv file.
        poll_calc()
        
    # Printing in terminal
    print('------------------------')
    print('!!! ELECTION RESULTS !!!')
    print('------------------------')
    print(f'Total Votes: {winner[1]}')
    print('------------------------')
    for i in range(0,4): 
        print(f'Votes for {candidates[i]}: {percents[i]} ({votes[i]})')
    print('------------------------')
    print(f'The winner is... {winner[0]}')
    
    # Print to txt file
    csvwriter = csv.writer(writetxt, delimiter = ' ')
    csvwriter.writerow(['ELECTION','RESULTS'])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['Total','Votes:',winner[1]])
    for i in range(0,4):
        csvwriter.writerow(['Votes','for',candidates[i],':', percents[i], [votes[i]]])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['The','Winner','Is','...',winner[0]])