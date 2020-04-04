import os 
import csv 
import statistics
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    total = 0
    count = 0
    top_increase = 0 
    top_decrease = 0 
    previous_row = 0
    top_increase_month = ""
    top_decrease_month = ""
    list = []
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total = total + int(row[1])
        count = count + 1 
    
        current_increase =  int(row[1])-previous_row   
        if current_increase > top_increase:
            top_increase = current_increase
            top_increase_month = row[0]
        list.append(current_increase)
        
        if current_increase < top_decrease:
            top_decrease = current_increase
            top_decrease_month = row[0]
        
        
        
        
        previous_row = int(row[1])

    #print(total)
    #print(statistics.mean(list))
    #print(top_increase)
    #print(top_increase_month)
    #print(top_decrease_month)
    #print(top_decrease)
print("\n")
print("Financial Analysis")
print("-------------------------------")
print("Total Month: " + str(count))
print("Total: $" + str(total))
print("Average Change: $" + str(statistics.mean(list)) )
print("Greatest Increase in Profits: "+ top_increase_month + " ($" + str(top_increase) + ")")
print("Greatest Decrease in Profits: "+ top_decrease_month + " ($" + str(top_decrease) + ")")
