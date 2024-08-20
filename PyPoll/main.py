#import os
#import csv


# Path to collect data from the Resources folder
#election_csv = os.path.join('Resources', 'election_data.csv')

# Open the election data file
# with open(election_csv,'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")

#     # Read the header row first
#     csv_header = next(csv_file)

     # I like to explicitly declare all my variables

csv_reader = []
csv_reader=[2405206,"Denver","Charles Casper Stockham"],[2161244,"Denver","Charles Casper Stockham"],[2795423,"Denver","Charles Casper Stockham"],[2549433,"Denver","Charles Casper Stockham"], [2429624,"Denver","Charles Casper Stockham"],[2348406,"Denver","Charles Casper Stockham"],[6459937,"Denver","Diana DeGette"],[7586282,"Denver","Diana DeGette"],[7272742,"Denver","Diana DeGette"],[5361931,"Denver","Diana DeGette"],[6072352,"Denver","Diana DeGette"],[5702090,"Denver","Diana DeGette"],[6586685,"Denver","Diana DeGette"],[7822125,"Denver","Diana DeGette"],[7323845,"Denver","Diana DeGette"]
total_votes = 0
candidate_results = {}
candidate_total = 0
candidate_name = ""

#Iterates over each row and calculates the different values requested

#candidate_list = [candidate_name,0]

for row in csv_reader:
    total_votes += 1
    candidate_name = row[2]
    if candidate_name in candidate_results:
        candidate_results[candidate_name] += 1
    else:
        candidate_results[candidate_name] = 1

print("List of candidates who received votes:")

print(candidate_results)
for candidate_name, votes in candidate_results.items():
    print(f"{candidate_name}: {votes} votes")

print(f"Total Votes: {total_votes}")

    #candidate_list.append(candidate_name, candidate_total)

    #if candidate_list:
    # if str(candidate_name) == str(candidate_list[0]):
    #     candidate_total =+ 1
        
    #     #temp_list = ([candidate_name,candidate_total])
    #     #candidate_list.append(temp_list)
    # else:
    #     print("not it isn't")
    #     candidate_list.append([candidate_name,candidate_total])
    #     #candidate_list.append({row[2],0})
    

#print(candidate_results)
#print(total_votes)

