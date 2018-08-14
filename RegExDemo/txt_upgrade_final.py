import csv
import re
from decimal import Decimal


def search_csv_by_row(regex_dollar_val, balance, f, f2):

    # row = ''
    for r in f:
        # for item in r:
        #     row += item

        p = re.compile(regex_dollar_val)

        m = p.search(r)
        if m:
            print('m is {}'.format(m.group()))
        else:
            print('m is empty, no dollar value results')
            row = ''
            continue

        dollar_val = m.group()

        balance = write_upgraded_csv(dollar_val, balance, r, f2)

        # row = ''


def write_upgraded_csv(dollar_val, balance, r, f2):

    if dollar_val[-1] == '-':
        # dollar_val = float(dollar_val[1:]) * -1
        print('whats here ...')
        dollar_val = dollar_val.split(',')
        val_str = ''.join(dollar_val)
        dollar_val = float(val_str[:-1]) * -1
        print('and whats here')
    else:
        dollar_val = float(dollar_val)


    balance = balance + dollar_val

    # r.append(str(round((Decimal(balance)), 2)) + '\n')

    # somestring = ','.join(r)
    somestring = r[:-2] + ' ' + str(round((Decimal(balance)), 2)) + '\n'

    f2.write(somestring)

    return balance


if __name__ == '__main__':

    # regex_dollar_val = '[-+]+\d+\.*\d\d'
    regex_dollar_val = '\d+,*\d*\.\d\d-*'#other txt format


    balance = float(input('Enter starting balance: $') or '4000')
    input_csv = input('Enter input CSV filename: ') or 'shorter2463DecJan2017.txt'
    output_csv = input_csv[:-4] + 'new' + '.csv'
    # row = ''

    with open(input_csv, 'r') as f:
        with open(output_csv, 'w') as f2:

            f2.write('Starting balance is ${}\n'.format(balance))

            search_csv_by_row(regex_dollar_val, balance, f, f2)

    f2.close()

f.close()
