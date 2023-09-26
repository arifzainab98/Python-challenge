#First we will import us module 
#This will allow us to create file path across operating systems 
import os

#Module for reading CSV files 
import csv

total_months = 0
net_total = 0
total_change = 0
max_increase = 0
max_decrease = 0
previous_profitloss = None
max_increase_date = ''
max_decrease_date = '' 

csvpath = os.path.join('..','/Users/zainabarif/Desktop/Module 3/Python-challenge/PyBank/Resources', 'budget_data.csv')
 
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')

#     print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Read each row of the data after the header 
    for row in csvreader:
         date, profit_loss = row 
         profit_loss  = int(profit_loss) 
         total_months += 1 
         net_total += profit_loss 
         if previous_profitloss is not None :
              profit_loss_change = profit_loss - int(previous_profitloss) 
              total_change += profit_loss_change 
              if profit_loss_change > max_increase :
                   max_increase = profit_loss_change
                   max_increase_date = date 
              if profit_loss_change < max_decrease :
                   max_decrease = profit_loss_change
                   max_decrease_date = date
         previous_profitloss = profit_loss
average_change = total_change / (total_months-1) 

net_total = "${:,.2f}".format(net_total)
average_change = "${:,.2f}".format(average_change)
max_increase = "${:,.2f}".format(max_increase)
max_decrease = "${:,.2f}".format(max_decrease)

print("Financial Analysis")
print("----------------------------")

print (f"Total Months: {total_months}") 
print (f"Total: {net_total}")
print (f"Average Change: {average_change}")
print (f"Greatest Increase in Profits: {max_increase_date} ({max_increase})")
print (f"Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})")

# Print the results to txt file
file_location = '/Users/zainabarif/Desktop/Module 3/Python-challenge/PyBank/analysis/PyBank Analysis.txt'
file = open(file_location, 'w')

print("Financial Analysis", file = open(file_location,'a'))
print("----------------------------", file =open(file_location,'a'))

print (f"Total Months: {total_months}", file = open(file_location,'a')) 
print (f"Total: {net_total}", file = open(file_location,'a'))
print (f"Average Change: {average_change}", file = open(file_location,'a'))
print (f"Greatest Increase in Profits: {max_increase_date} ({max_increase})", file = open(file_location,'a'))
print (f"Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})", file = open(file_location,'a'))

file.close()
