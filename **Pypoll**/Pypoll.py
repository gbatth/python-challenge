
import os
import csv

file = os.path.join("Resources", "election_data.csv")

#declare variables
Election_Results = {}
num_of_votes =[]
tot_votes = 0
candidates = []
vote_Percent = []
winner_list = []

#read the csv data
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next(csvreader)

#loop thru data to read and summarize    
    for row in csvreader:
        tot_votes = tot_votes + 1

        if row[2] in Election_Results.keys():
            Election_Results[row[2]] = Election_Results[row[2]] + 1
        else:
        
            Election_Results[row[2]] = 1

for key, value in Election_Results.items():
    candidates.append(key)
    num_of_votes.append(value)

for n in num_of_votes:
    vote_Percent.append(round(n/tot_votes*100, 1))

    Election_Results_data = list(zip(candidates,num_of_votes,vote_Percent))

for name in Election_Results_data:
    if max(num_of_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]
            
if len(winner_list) > 1:
    for w in range(1,len(winner_list[w])):
        winner = winner + "," + winner_list[w]

#results and output file
output_file = os.path.join('election_results' + 'txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('election Results \n----------------------------------- \nTot Votes: ' + str(tot_votes) +'\n--------------------------------\n')
    for entry in Election_Results_data:
        txtfile.writelines(entry[0] + ":" + str(entry[2]) + '% (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------ \nWinner: ' + winner + '\n-----------------------')

with open (output_file,'r') as readfile:
    print(readfile.read())
