import os
import csv

diff = []
greatestPct = 0
greatestmonth = ""
leastmonth = ""
leastPct = 99999999999999999999

totalProfitLosses = 0


csv_file = os.path.join("Resources", "budget_data.csv")

print(os.path)


with open(csv_file, 'r') as file_handler:
    file_iterator = csv.reader(file_handler)

#loop through everything except headers
    next(file_iterator)

#Calculate total amount of months
    for i,fields in enumerate(file_iterator):
        
        totalProfitLosses = totalProfitLosses + int(fields[1])

#print("i:", i, "fields[0]:", fields[0], "fields[1]:", fields[1])
        if i!=0:
            delta = int(fields[1]) - prev#
            if delta > greatestPct:
                greatestPct = delta
                greatestmonth = fields[0]

            if delta < leastPct:

                leastPct = delta
                leastmonth = fields[0]


            diff.append(delta)
            prev = int(fields[1])

            diffMean = sum(diff)/len(diff)

print(row_count)
print(diffMean)
print(greatestmonth,greatestPct)
print(leastmonth, leastPct)
print(totalProfitLosses)
file_handler.close()




