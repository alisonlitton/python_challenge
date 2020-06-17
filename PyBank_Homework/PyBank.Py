import os
import csv

csv_path = os.path.join('..','Resources','budget_data.csv')

total_months = []
total_profits = []
average_profits = []

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 
