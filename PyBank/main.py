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
budget_data_path = os.path.join('/Users/jmbruner37/Bootcamp Homework/python-challenge/PyBank/Resources/budget_data.csv')

#create lists
profit = []
date = []
month_changes = []

#declare variables
total_months = 0
total_profit = 0
tot_change_profits = 0
in_profits = 0


#Open CSV
with open(budget_data_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        
        #skip header
        header = next(csvreader)
        
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

            tot_change_profits += month_change_profits
            in_profits = f_profits

            av_change_profits = (tot_change_profits/total_months)
        #greatest inc and dec profits
            gr_inc_profit = max(month_changes)
            gr_dec_profit = min(month_changes)
            in_date = date[month_changes.index(gr_inc_profit)]
            dec_date = date[month_changes.index(gr_dec_profit)]







print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(total_months))
print("Total:" + "$" + str(total_profit))
print("Average Change:" + "$" + str(int(av_change_profits)))
print("Greatest Increase in Profits:" + str(in_date) + "($" + str(gr_inc_profit) + ")")
print("Greatest Decrease in Profits:" + str(dec_date) + "($" + str(gr_dec_profit) + ")")

with open('pybank_analysis.txt', 'w') as text:
    text.write("Financial Analysis")
    text.write("----------------------------")
    text.write("Total Months:" + str(total_months))
    text.write("Total:" + "$" + str(total_profit))
    text.write("Average Change:" + "$" + str(int(av_change_profits)))
    text.write("Greatest Increase in Profits:" + str(in_date) + "($" + str(gr_inc_profit) + ")")
    text.write("Greatest Decrease in Profits:" + str(dec_date) + "($" + str(gr_dec_profit) + ")")