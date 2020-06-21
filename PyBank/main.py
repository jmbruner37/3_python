##Your task is to create a Python script that analyzes the records to calculate each of the following:



#The total number of months included in the dataset*


#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)


#Modules
import os
import csv


#Set path for file
file_name = 'budget_data.csv'
budget_data_path = os.path.join('python-challenge/PyBank/Resources/budget_data.csv')

#create lists
profit = []
date = []
month_changes = []

#declare variables
total_months = 0
total_profit = 0
tot_change_profits = 0


#Open CSV
with open(budget_data_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        
        #skip header
        header = next(csvreader)
        row_1 = next(csvreader)
        in_profits = int(row_1[1])
        total_profit = in_profits
        date.append(row_1[0])
        
        #Loop though rows and count months
        for row in csvreader:
            total_months += 1
            date.append(row[0])
            
            profit.append(row[1])
            total_profit += int(row[1])
         
         #average change month to month   
            f_profits = int(row[1])
            month_change_profits = f_profits - in_profits
            month_changes.append(month_change_profits)

            tot_change_profits = tot_change_profits + month_change_profits
            in_profits = f_profits

            av_change_profits = (tot_change_profits/total_months)
        #greatest inc and dec profits
            gr_inc_profit = max(month_changes)
            gr_dec_profit = min(month_changes)
            in_date = date[month_changes.index(gr_inc_profit)]
            dec_date = date[month_changes.index(gr_dec_profit)]

av_change_profitts = sum(month_changes) / len(month_changes)

print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(total_months))
print("Total:" + "$" + str(total_profit))
print("Average Change:" + "$" + str(int(av_change_profitts)))
print("Greatest Increase in Profits:" + str(in_date) + "($" + str(gr_inc_profit) + ")")
print("Greatest Decrease in Profits:" + str(dec_date) + "($" + str(gr_dec_profit) + ")")

write_file = f"pybank_results.txt"

filewriter = open(write_file, mode ='w') 
filewriter.write(f"Financial Analysis\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Total Months: {total_months}\n")
filewriter.write(f"Total $ {total_profit}\n")
filewriter.write(f"Average Change: {av_change_profits})\n")
filewriter.write(f"Greatest Increase in Profits: {in_date} (${gr_inc_profit})\n")
filewriter.write(f"Greatest Decrease in Profits: {dec_date}(${gr_dec_profit})\n")

filewriter.close()