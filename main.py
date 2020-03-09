import csv
import os

csv_file = os.path.join("Downloads","election_votes.csv")
votes_per_candidate = {}

with open(csv_file, 'rU') as election:
    csvreader = csv.reader(election, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if not votes_per_candidate.has_key(row[2]):
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
            
total_votes = sum(votes_per_candidate.values())

for cadidate in votes_per_candidate:
    print(cadidate, "{:.2%}".format(float(votes_per_candidate[cadidate]) / float(total_votes)))
    
list_of_cadidates = votes_per_candidate.keys()
winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(total_votes)
print(winner)
print(list_of_cadidates)
print(votes_per_candidate)
file_handler.close()


