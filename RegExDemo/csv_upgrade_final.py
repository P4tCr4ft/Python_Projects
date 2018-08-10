import csv
import re

if __name__ == '__main__':

    regex_dollar_val = '[-+]+\d+\.*\d*'

    starting_balance = input('Enter starting balance: $')

    row = ''

    with open('CSVData.csv', 'r') as f:
        for r in csv.reader(f):
            print('r out of csv is {}'.format(r))
            for item in r:
                row += item

            p = re.compile(regex_dollar_val)
            # p = re.compile('[-+]+\d+\.*\d*')

            m = p.search(row)
            if m:
                print('m is {}'.format(m.group()))
            else:
                print('m is empty, no results')

            row = ''

            # r += m.group()
            # r.append(m.group())
            dollar_val = m.group()

            if dollar_val[0] == '-':
                dollar_val = float(dollar_val[1:]) * -1
            else:
                dollar_val = float(dollar_val)

            balance = float(starting_balance) + dollar_val

            r.append(balance)


            print('new r is {}'.format(r))

    f.close()
