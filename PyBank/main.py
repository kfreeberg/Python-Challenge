import os
import csv


csvpath=os.path.join('Resources', 'budget_data.csv' )

with open (csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)

    Revenue = []
    Date = []
    MonthlyChange = []

    
    for row in csvreader:
        # Create revenue & date lists
        Revenue.append(float(row[1]))
        Date.append(row[0])

        # Find the total number of months and the total revenue
        RevenueSum=int((sum(Revenue)))
        NMonths=int(len(Date))

    
    for month in range(1,len(Revenue)):
        # Get the monthly change for each month
        MonthlyChange.append(Revenue[month] - Revenue[month-1])   
        avg_MonthlyChange = sum(MonthlyChange)/len(MonthlyChange)

        # Get the max and min of the monthly change
        max_MonthlyChange = int(max(MonthlyChange))
        min_MonthlyChange = int(min(MonthlyChange))

        # Get the  month of the max and min of the monthly change
        max_MonthlyChange_Date = str(Date[MonthlyChange.index(max(MonthlyChange))+1])
        min_MonthlyChange_Date = str(Date[MonthlyChange.index(min(MonthlyChange))+1])

  # Print results to the terminal 
    print("")
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months:", str(NMonths))
    print("Total Revenue: $", str(RevenueSum))

    print("Avereage Revenue Change: $", round(avg_MonthlyChange, 2))
    print("Greatest Increase in Revenue:", max_MonthlyChange_Date,"($", max_MonthlyChange,")")
    print("Greatest Decrease in Revenue:", min_MonthlyChange_Date,"($", min_MonthlyChange,")")

# Print to a text file called financials.txt
with open ("financials.txt", "w") as text_file:
    print  ("Financial Analysis", file=text_file)
    print("---------------------------------", file = text_file)
    print("Total Months:", str(NMonths), file = text_file)
    print("Total Revenue: $", str(RevenueSum), file = text_file)

    print("Avereage Revenue Change: $", round(avg_MonthlyChange, 2), file = text_file)
    print("Greatest Increase in Revenue:", max_MonthlyChange_Date,"($", max_MonthlyChange,")", file = text_file)
    print("Greatest Decrease in Revenue:", min_MonthlyChange_Date, file = text_file)
