import csv
import re

if __name__ == '__main__':

    # regex_dollar_val = '[-+]+\d+\.*\d*'
    # regex_dollar_val = '[-+]+\d+\.*[\d\d]*'
    regex_dollar_val = '[-+]+\d+\.*\d\d'#this one is correct
    # regex_dollar_val = '[fobar]'# This will only match once from this set, eg, search string 'oo' will only match once on o in [fobar] and return result o
    # regex_dollar_val = 'fobar'# This will only match an exact match, eg, search string 'fobar'
    # regex_dollar_val = '[fobar]+'# This will match one or more times, eg, search string'oooo' will match one or more on o in [fobar] and return result oooo


    balance = float(input('Enter starting balance: $') or '5000')
    input_csv = input('Enter input CSV filename: ') or 'CSVData_July2018.csv'
    output_csv = input_csv[:-4] + 'new' + '.csv'

    row = ''

    with open(input_csv, 'r') as f:

        with open(output_csv, 'w') as f2:

            f2.write('Starting balance is ${}\n'.format(balance))

            for r in csv.reader(f):
                print('r out of csv is {}'.format(r))
                for item in r:
                    row += item

                p = re.compile(regex_dollar_val)
                # p = re.compile('[-+]+\d+\.*\d*')

                # m = p.search(row)
                m = p.search('oooo')
                if m:
                    print('m is {}'.format(m.group()))
                else:
                    print('m is empty, no dollar value results')
                    row = ''
                    continue

                dollar_val = m.group()




                if dollar_val[0] == '-':
                    dollar_val = float(dollar_val[1:]) * -1
                else:
                    dollar_val = float(dollar_val)

                balance = balance + dollar_val

                r.append(str(balance))
                r.append('\n')

                somestring = ''

                somestring = ','.join(r)
                print('somestring is ', somestring)

                f2.write(somestring)

                row = ''

                print('new r is {}'.format(r))

        f2.close()

    f.close()
