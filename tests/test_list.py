#!/usr/bin/python3
import whois
import csv

with open("newList3.csv", 'r') as f_in, open("Results.csv", 'w') as f_out:
    
    myReader = csv.reader(f_in)
    myWriter = csv.writer(f_out)

    i=0

    failure = list()

    # domains = ''

    invalidTld = '''
    '''

    failedParsing = '''
    '''

    unknownDateFormat = '''
    '''

    print("start")

    for row in myReader:
        if i<100:
            
            try:
                w = whois.query(row[0], ignore_returncode=1)
                reg =w.registrar
                if ',' in reg :
                    reg =reg.split(",")[0]

                if 'd/b/a' in reg :
                    reg = reg.split('d/b/a')[0]

                if '(Beijing)' in reg :
                    reg = reg.split("(Beijing)")[0]

                string = str(i) +';' +row[0] + ';' + reg
                print(string)
                myWriter.writerow([string])
            except Exception as e:
                failure.append(row[0])
                message = """
                Error : {},
                On Domain: {}
                """.format(str(e), row[0])
                print(message)
        i=i+1


    for d in invalidTld.split('\n'):
        if d:
            print('-'*80)
            print(d)
            try:
                w = whois.query(d, ignore_returncode=1)
            except whois.UnknownTld as e:
                failure.append(d)
                message = """
                Error : {},
                On Domain: {}
                """.format(str(e), d)
                print('Caught UnknownTld Exception')
                print(e)

    for d in failedParsing.split('\n'):
        if d:
            print('-'*80)
            print(d)
            try:
                w = whois.query(d, ignore_returncode=1)
            except whois.FailedParsingWhoisOutput as e:
                failure.append(d)
                message = """
                Error : {},
                On Domain: {}
                """.format(str(e), d)
                print('Caught FailedParsingWhoisOutput Exception')
                print(e)

    for d in unknownDateFormat.split('\n'):
        if d:
            print('-'*80)
            print(d)
            try:
                w = whois.query(d, ignore_returncode=1)
            except whois.UnknownDateFormat as e:
                failure.append(d)
                message = """
                Error : {},
                On Domain: {}
                """.format(str(e), d)
                print('Caught UnknownDateFormat Exception')
                print(e)


    report_str = """
    Failure during test : {}
    Domains : {}
    """.format(len(failure), failure)
    message = '\033[91m' + report_str + '\x1b[0m'
    print(message)
    print("end")


