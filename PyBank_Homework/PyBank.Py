import os
import csv

#set path to your csv file 
csv_path = os.path.join('Resources','budget_data.csv')

#this is where the "lists" will be stored by using []
profit = []
month = []
monthly_changes = []
 
#set the variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#read the csv file 
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 
#start your loop!!
    for row in csvreader:    
    #count months in dataset
      count = count + 1 
      month.append(row[0])
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      average_change_profits = (total_change_profits/count)
    
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = month[monthly_changes.index(greatest_increase_profits)]
      decrease_date = month[monthly_changes.index(greatest_decrease_profits)]
#print out your financial analysis     
    print(f"------------------------------------------")
    print(f"Financial Analysis")
    print(f"------------------------------------------")
    print(f"Total Months:" + str(count))
    print(f"Total Profits:" + "$" + str(total_profit))
    print(f"Average Change:" + "$" + str(int(average_change_profits)))
    print(f"Greatest Increase in Profits:" + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print(f"Greatest Decrease in Profits:" + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print(f"------------------------------------------")

#write results to text file 
    analysis_file = open("financial_analysis.txt", "w")

    analysis_file.write(f"------------------------------------------ \n")
    analysis_file.write(f"Financial Analysis\n")
    analysis_file.write(f"------------------------------------------\n")
    analysis_file.write(f"Total Months:" + str(count)+"\n")
    analysis_file.write(f"Total Profits:" + "$" + str(total_profit) + "\n")
    analysis_file.write(f"Average Change:$" + str(int(average_change_profits)+ "\n"))
    analysis_file.write(f"Greatest Increase in Profits:" + str(increase_date) + " ($" + str(greatest_increase_profits) + ")" + "\n")
    analysis_file.write(f"Greatest Decrease in Profits:" + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")" + "\n")
    analysis_file.write(f"------------------------------------------\n")
