import os
import csv

#Path to collect data from the Resources folder

election_csv = os.path.join('Resources', 'election_data.csv')

# Open the election data file
with open(election_csv,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Read the header row first
    csv_header = next(csv_file)

# I like to explicitly declare all my variables
    total_votes = 0
    candidate_results = {}
    candidate_total = 0
    candidate_name = ""

#Iterates over each row to get the total votel cast, and how many each candidate got.
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidate_results:
            candidate_results[candidate_name] += 1
        else:
            candidate_results[candidate_name] = 1
#List to store the first section of the analysis

header = ["\n Election Results: \n",
          "--------------------------\n",
          "Total votes: " + str(total_votes) +"\n",
          "--------------------------\n"]

#Iterates over the results to check who has the highest vote count and declare them the winner
winner_votes = 0
results_summary = []

for candidate_name, votes in candidate_results.items():
        if votes > winner_votes:
            winner_votes = votes
            winner_name = candidate_name
    
        percentage = round((votes/total_votes) * 100,2)
        
        #List containing the summary of the results for each candidate
        results_summary.append(candidate_name +": " + str(votes) + " votes " + str(percentage)+"%" +"\n")

#List containin the winner section
winner = ["--------------------------\n",
          "Winner: " + winner_name +"\n",
          "--------------------------\n"]

#Finds path  and creates the text file for the analysis of the results
analysis_csv = os.path.join('Analysis', 'Election_result.txt')

#Opens the file, writes each section and prints it to screen
with open(analysis_csv, 'w') as txt_file:
    for items in header:
        txt_file.write(items)
        print(items)
    for items in results_summary:
        txt_file.write(items)
        print(items)
    for items in winner:
        txt_file.write(items)
        print(items)
print("Output saved to \Analysis\Election_result.txt")