import csv
import re

if __name__ == '__main__':

    regex = '[-+]+\d+\.*\d*'

    row = ''

    with open('CSVData.csv', 'r') as f:
        for r in csv.reader(f):
            for item in r:
                row += item

            p = re.compile(regex)
            # p = re.compile('[-+]+\d+\.*\d*')

            m = p.search(row)
            if m:
                print('m is {}'.format(m.group()))
            else:
                print('m is empty, no results')

            row = ''
    f.close()
