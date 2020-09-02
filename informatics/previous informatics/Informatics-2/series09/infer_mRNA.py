'''
Created on 2015. 12. 2.

@author: User
'''

def codontable(file):
    reading = open(file,'r').read()
    reading = reading.replace(' ','').replace('\n','').replace('stop','*')
    dict = {}
    seq = ''
    x = 0
    while x< len(reading):
        seq += reading[x]
        x += 1
        if len(seq) == 4:
            dict[seq[:3]] = seq[-1]
            seq = ''
    return dict
def reverse_codontable(table):
    dict = {}
    for key, value in table.items:
        dict.setdefault(value,set()).add(key)
        
    return dict

def mRNA(seq,table):
    dict = reverse_codontable(table)
    stop = 1
    for x in seq:
        stop = stop*len(dict[x])
    return stop*len(dict['*'])
