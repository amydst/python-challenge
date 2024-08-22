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

#Iterates over each row and calculates the different values requested
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidate_results:
            candidate_results[candidate_name] += 1
        else:
            candidate_results[candidate_name] = 1

print("\n Election Results: \n")
print("--------------------------\n")
print("Total votes: " + str(total_votes) +"\n")
print("--------------------------\n")

winner_votes = 0
for candidate_name, votes in candidate_results.items():
    if votes > winner_votes:
        winner_votes = votes
        winner_name = candidate_name

    percentage = votes/total_votes
    #format(percentage, ".2%")
    print(f"{candidate_name}: {votes} votes ({percentage:.2%})\n")

print("--------------------------\n")
print("Winner:" + winner_name +"\n")
print("--------------------------\n")

with open('ElectionResult.txt', 'w') as txt_file:

    txt_file.write("\nElection Results: \n")
    txt_file.write("--------------------------\n")
    txt_file.write("Total votes: " + str(total_votes) +"\n")
    txt_file.write("--------------------------\n")

    winner_votes = 0
    for candidate_name, votes in candidate_results.items():
        if votes > winner_votes:
            winner_votes = votes
            winner_name = candidate_name

        percentage = votes/total_votes
        
        txt_file.write(f"{candidate_name}: {votes} votes ({percentage:.2%})\n")

    txt_file.write("--------------------------\n")
    txt_file.write("Winner: " + winner_name +"\n")
    txt_file.write("--------------------------\n")

print("Output saved to ElectionResult.txt")
    
