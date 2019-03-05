import os
import csv




csvpath = os.path.join("Resources","election_data.csv")



TotalVoteCount = 0
CandidateVotes = []
Ballot = []
CandidateVoteCount = []
CandidateVotePercentage = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Count the total number of votes
        TotalVoteCount = TotalVoteCount + 1

        # Set the candidate names to candidatelist
        CandidateVotes.append(row[2])

    # List each peron on the ballot once
    for person in set(CandidateVotes):
        Ballot.append(person)

        # Total votes for each candidate
        votes = CandidateVotes.count(person)
        CandidateVoteCount.append(votes)

        # Percent of votes for each candidate
        perVotes = (votes/TotalVoteCount)*100
        CandidateVotePercentage.append(perVotes)
    
    #Find the overall winner   
    WinnerVotes = max(CandidateVoteCount)
    Winner = Ballot[CandidateVoteCount.index(WinnerVotes)]
    
# Print results to the terminal
print("")
print("-------------------------------")
print("Election Results")   
print("-------------------------------")
print("Total Votes :" + str(TotalVoteCount))    
print("-------------------------------")
for i in range(len(Ballot)):
            print(Ballot[i] + ": " + '%.3f'%CandidateVotePercentage[i] +"% (" + str(CandidateVoteCount[i])+ ")")
print("-------------------------------")
print("")
print("-------------------------------")
print("The winner is: " + Winner)
print("-------------------------------")
print("")

# Print to a text file called electionresults.txt
with open ("electionresults.txt", "w") as text_file:
    print("", file = text_file)
    print("-------------------------------", file = text_file)
    print("Election Results", file = text_file)   
    print("-------------------------------", file = text_file)
    print("Total Votes :" + str(TotalVoteCount), file = text_file)    
    print("-------------------------------", file = text_file)
    for i in range(len(Ballot)):
              print(Ballot[i] + ": " + '%.3f'%CandidateVotePercentage[i] +"% (" + str(CandidateVoteCount[i])+ ")", file = text_file)
    print("-------------------------------", file = text_file)
    print("", file = text_file)
    print("-------------------------------", file = text_file)
    print("The winner is: " + Winner, file = text_file)
    print("-------------------------------", file = text_file)
    print("", file = text_file)
