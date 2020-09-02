'''
Created on 2015. 11. 20.

@author: Haeun_Kim , Minki_Hong
'''

def overlap(read1, read2, k):

    check1 = read1[-k:]
    check2 = read2[:k]
    if check1 == check2:
        return True
    else:
        return False
def maximalOverlap(read1, read2):
    k = len(read1)
    while True:
        if overlap(read1, read2, k) == True:
            return k
        else:
            k -= 1
            
        if k == 0:
            return k
            break         
def overlapGraph(reads, k):
    dict = {}
    for read1 in reads:
        for read2 in reads:
            if read1 != read2 and 0 < k <= maximalOverlap(read1, read2):
                dict.setdefault(read1,set()).add(read2)
    return dict
