import os 
import csv 
import statistics
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    vote_count = 0 
    khan_count = 0 
    correy_count = 0 
    li_count = 0 
    tooley_count = 0 
        # Read each row of data after the header
    for row in csvreader:
        vote_count = vote_count + 1 

        if row[2]=="Khan":
            khan_count = khan_count + 1
        
        elif row[2]=="Correy":
            correy_count = correy_count + 1
        
        elif row[2]=="Li":
            li_count = li_count + 1
        else: 
            tooley_count = tooley_count + 1
    
    list = [khan_count,correy_count,li_count,tooley_count]
    if max(list)==list[0]:
        Winner = "Khan"
    elif max(list)==list[1]:
        Winner = "Correy"
    elif max(list)==list[2]:
        Winner = "Li"
    else:
        Winner = "O'Tooley"

    khan_percentage = round(khan_count / vote_count*100,3)
    correy_percentage = round(correy_count / vote_count*100,3)
    li_percentage = round(li_count / vote_count*100,3)
    tooley_percentage = round(tooley_count / vote_count*100,3)
    
    #print(str(correy_count))
    #print(str(li_count))
    #print(str(tooley_count))
    #print(str(vote_count))
    #print(str(khan_percentage))



    
    print("Election Results")
    print("---------------------------")
    print("Total Votes: " + str(vote_count))
    print("---------------------------")
    print("Khan: " +str(khan_percentage)+"% (" +str(khan_count) + ")" )
    print("Correy: "+ str(correy_percentage)+"% (" +str(correy_count) + ")" )
    print("Li: " + str(li_percentage)+"% (" +str(li_count) + ")" )
    print("O'Tooley: " + str(tooley_percentage)+"% (" +str(tooley_count) + ")" )
    print("---------------------------")
    print("Winner: "+ Winner)
    print("---------------------------")
