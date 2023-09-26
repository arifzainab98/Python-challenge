#First we will import us module 
#This will allow us to create file path across operating systems 
import os

#Module for reading CSV files 
import csv

csvpath = os.path.join('..','/Users/zainabarif/Desktop/Module 3/Python-challenge/PyPoll/Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

        #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    #Total number of votes cast 
    (csvreader)
    data = list(csvreader)
    total_votes = len(data)

#total list of candidates who recived the votes 
    candiate_list = list()
    tally = list()
    for i in range (0,total_votes):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candiate_list: 
            candiate_list.append(candidate)
    candidate_count = len(candiate_list)

#Percentatge of votes each candidate won
votes = list()
percentage = list() 
for j in range (0,candidate_count):
    name = candiate_list[j]
    votes.append(tally.count(name))
    vote_percent = votes[j]/total_votes
    percentage.append(vote_percent)

winner = votes.index(max(votes))
winner_name = candiate_list[winner]

  # Print the results to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes:,}")
print("----------------------------")
for k in range (0,candidate_count):
    print(f"{candiate_list[k]}: {percentage[k]:.3%} ({votes[k]})")
print("----------------------------")
print (f"Winner: {winner_name}")

# Print the results to txt file
file_location = '/Users/zainabarif/Desktop/Module 3/Python-challenge/PyPoll/analysis/PyPoll Analysis.txt'
file = open(file_location, 'w')

print("Election Results", file = open(file_location,'a'))
print("----------------------------", file = open(file_location,'a'))
print(f"Total Votes: {total_votes:,}", file = open(file_location,'a'))
print("----------------------------", file = open(file_location,'a'))
for k in range (0,candidate_count):
    print(f"{candiate_list[k]}: {percentage[k]:.3%} ({votes[k]})", file = open(file_location,'a'))
print("----------------------------", file = open(file_location,'a'))
print (f"Winner: {winner_name}", file = open(file_location,'a'))
file.close()

