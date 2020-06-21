#You will be give a set of poll data called election_data.csv. 
#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:


#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.


#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#Modules
import os
import csv

#variables
candidates = []
vote_counts = []
number_votes = 0

#set path for file and file_name 
pypoll_path = 'election_data.csv'
filepath = os.path.join('python-challenge/PyPoll/Resources/election_data.csv')

#open file
with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    row_1 = next(csvreader,None)

    #go through each vote
    for row_1 in csvreader:

        #total number of votes
        number_votes += + 1

        #candidate voted for
        candidate = row_1[2]

        #add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#percentage vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/number_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {number_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {number_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()