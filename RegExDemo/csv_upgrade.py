import csv
import re

def parse_csv():


if __name__ == "main":

    with open('CSVData.csv', 'r') as f:
        for r in csv.reader(f):
            print(r)

    f.close()

