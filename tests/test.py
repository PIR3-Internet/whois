#!/usr/bin/python3
import whois

DOMAINS = '''
google.com
panda.tv
mama.cn
'''

for d in DOMAINS.split('\n'):
    if d:
        print(d,end=';')
        domain=whois.query(d)
        print(domain.registrar)

