import os
import csv

diff = []
greatestPct = 0
greatestmonth = ""
leastmonth = ""
leastPct = 99999999999999999999
totalProfitLosses = 0
totalmonths = 0


csv_file = os.path.join("Resources", "budget_data.csv")

with open(csv_file, 'r') as file_handler:
    file_iterator = csv.reader(file_handler)

#loop through everything except headers
    next(file_iterator)
    

#Calculate total amount of months
    for i,fields in enumerate(file_iterator):
        
        totalmonths += 1
        
        totalProfitLosses = totalProfitLosses + int(fields[1])

        if i!=0:
            
            delta = int(fields[1]) - prev
            
            if delta > greatestPct:
                greatestPct = delta
                greatestmonth = fields[0]

            if delta < leastPct:

                leastPct = delta
                leastmonth = fields[0]


            diff.append(delta)
            
        prev = int(fields[1])

    diffMean = sum(diff)/len(diff)

print(totalmonths)
print(totalProfitLosses)
print(diffMean)
print(greatestmonth,greatestPct)
print(leastmonth, leastPct)
file_handler.close()

hw = f"""
  Financial Analysis
  ----------------------------
  Total Months: {totalmonths}
  Total: ${totalProfitLosses}
  Average  Change: ${diffMean:.2f}
  Greatest Increase in Profits: {greatestmonth}, (${greatestPct:,})
  Greatest Decrease in Profits: {leastmonth}, (${leastPct:,})
"""
print(hw)

with open('New_PyBank', 'w') as new_file:
    csv_writier = csv.writer(new_file)
    
       
    # Initialize csv.writer
    csvwriter = csv.writer(new_file, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow([f"Total Months: {totalmonths}"])
    csvwriter.writerow([f"Total: ${totalProfitLosses}"])
    csvwriter.writerow([f"Average  Change: ${diffMean:.2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatestmonth}, (${greatestPct:,})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {leastmonth}, (${leastPct:,})"])
    
print(new_file)
