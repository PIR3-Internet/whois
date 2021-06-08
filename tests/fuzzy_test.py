from fuzzywuzzy import fuzz

if __name__ == '__main__' :

    str1 = 'MarkMonitor Inc.'
    str2 = 'MARKMONITOR Inc.'
    str3 = 'MarkMonitor International Limited'

    Ratio1 = fuzz.partial_ratio(str1.lower(), str2.lower())
    Ratio2 = fuzz.partial_ratio(str1.lower(), str3.lower())
    print(Ratio1)
    print(Ratio2)