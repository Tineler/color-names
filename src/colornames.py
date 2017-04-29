import csv
import os

fn = os.path.join(os.path.dirname(__file__), 'colornames.csv')

by_name = dict()
by_value = dict()

with open(fn, mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        by_name[row[0]] = row[1]
        by_value[row[1]] = row[0]
