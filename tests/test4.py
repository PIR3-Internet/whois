#!/usr/bin/python3
import whois

DOMAINS = '''
login.tmall.com
360.cn
sina.com.cn
panda.tv
mama.cn
google.com.hk
zhanqi.tv
twitch.tv
'''

failure = list()

# domains = ''

invalidTld = '''
'''

failedParsing = '''
'''

unknownDateFormat = '''
'''

for d in DOMAINS.split('\n'):
    if d:
        print(d,end=';')
        try:
            w = whois.query(d, ignore_returncode=1)
            print(w.registrar)
        except Exception as e:
            failure.append(d)
            message = """
            Error : {},
            On Domain: {}
            """.format(str(e), d)
            print(message)

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
