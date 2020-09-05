
import os
import csv

file = os.path.join("Resources", "election_data.csv")

poll = {}
num_of_votes =[]
tot_votes = 0
candidates = []
vote_Percent = []
winner_list = []


with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next(csvreader)
    
    for row in csvreader:
        tot_votes = tot_votes + 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

for key, value in poll.items():
    candidates.append(key)
    num_of_votes.append(value)

for n in num_of_votes:
    vote_Percent.append(round(n/tot_votes*100, 1))

    clean_data = list(zip(candidates,num_of_votes,vote_Percent))

for name in clean_data:
    if max(num_of_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]
            
if len(winner_list) > 1:
    for w in range(1,len(winner_list[w])):
        winner = winner + "," + winner_list[w]


output_file = os.path.join('election_results' + 'txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('election Results \n----------------------------------- \nTot Votes: ' + str(tot_votes) +'\n--------------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ":" + str(entry[2]) + '% (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------ \nWinner: ' + winner + '\n-----------------------')

with open (output_file,'r') as readfile:
    print(readfile.read())
