import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Open my budget file
with open(budget_csv,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
   
    # I like to explicitly declare all my variables
    total_months = 0
    net_total = 0.00
    monthly_changes = 0.00
    changes = []
    total_changes = 0.00
    previous_pl = 00
    current_pl = 00
    current_month = ""
    pl_difference = 0.00

    #Iterates over each row and calculates the different values requested
    for row in csv_reader:
        total_months += 1
        current_month= row[0]
        current_pl = float(row[1])
        net_total += current_pl
        temp_list = []

        #Takes current row profit/loss value and sustracts the previous p/l value
        if previous_pl !=0:
            pl_difference = current_pl - previous_pl

            #appends this values to the list changes with the corresponding month

            temp_list = [current_month,pl_difference]
            changes.append(temp_list)

        #we update previous p/l with the current p/l value so we can move to the next row
        previous_pl = current_pl

    GOAT_increaseV = 0.00
    GOAT_increaseM = ""
    GOAT_decreaseV = 0.00
    GOAT_decreaseM = ""
    total_changes = 0.00

    #adds all the pl differences in the changes list together, calculates the average and the greatest decrease and increase
    for row in changes:
        total_changes += row[1]
        #finds the greates increase by comparing all the positive changes
        if row[1] > 0 and row[1] > GOAT_increaseV:
            GOAT_increaseV = row[1]
            GOAT_increaseM = row[0]
        #finds the greates decrease by comparing all the negative changes
        if row[1] < 0 and row[1] < GOAT_decreaseV:
            GOAT_decreaseV = row[1]
            GOAT_decreaseM = row[0]

    average = total_changes / (len(changes))

    #List to store the analysis
    analysis_list = ["\nFinancial Analysis \n",
                     "------------------------------------------------- \n",
                     "Total Months: " + str(total_months) +"\n",
                     "Net total: " + str(net_total)+ "\n",
                     "Average Change: " + str(round(average,2)) + "\n",
                     "Greatest Increase in Profits: " + str(GOAT_increaseM) + " $" + str(GOAT_increaseV) + "\n", 
                     "Greatest Decrease in Profits: " + str(GOAT_decreaseM) + " $" + str(GOAT_decreaseV)+ "\n"
                     ]
#opens the file, writes each section and prints it to the screen

analysis_csv = os.path.join('Analysis', 'Financial_analysis.txt')
with open(analysis_csv, 'w') as txt_file:
    for items in analysis_list:
        print(items)
        txt_file.write(items)

print("Output saved to \Analysis\Financial analysis.txt")
    