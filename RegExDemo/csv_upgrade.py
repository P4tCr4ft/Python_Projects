import csv
import re

# def parse_csv():
#     # parse function
#     pass


if __name__ == '__main__':

    row = ''
    text = 'Guido will be -+ out of the office from 12/15/2012 - 1/3/2013.'

    with open('CSVData.csv', 'r') as f:
        for r in csv.reader(f):
            # print(r)
            for item in r:
                row += item
            # print(row)
            # p = re.compile('\d+')# works for first date number using match
            # p = re.compile(r'[DRA]')
            # p = re.compile('a[bcd]*b')# works as per python docs example (with match)
            # p = re.compile(r'\d\d\d')# No doesn't work

            # p = re.compile('\d+/\d+/\d+')# Yes this works with finditer
            p = re.compile('[- +]+')# Yes this works with finditer and findall
                                    # finds - and space and + individually

            p = re.compile('-\+')# this finds -+, so escapes the special character +

            # m = p.match(text)# I think match starts from the start, may not be best option

            # for m in p.finditer(text):# Yes this works
            #     print(m.group())

            m = p.findall(text)# yes this works, not limited to matching from the beginning of string


            # m = p.match(row)
            # m = p.match('abcbd')# works as per python docs example
            if m:
                # print(m.group())
                print(m)
            else:
                print('m is empty, nothing found')
            row = ''

    f.close()

