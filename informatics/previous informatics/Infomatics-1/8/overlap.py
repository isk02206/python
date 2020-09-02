'''
Created on 2015. 12. 3.

@author: User
'''
8.6 Overlap graph
41
def overlap(first, second, k):
"""
>>> overlap(¡¯AAATTTT¡¯, ¡¯TTTTCCC¡¯, 3)
True
>>> overlap(¡¯AAATTTT¡¯, ¡¯TTTTCCC¡¯, 5)
False
>>> overlap(¡¯ATATATATAT¡¯, ¡¯TATATATATA¡¯, 4)
False
>>> overlap(¡¯ATATATATAT¡¯, ¡¯TATATATATA¡¯, 5)
True
"""
assert 0 < k <= min(len(first), len(second)), ¡¯invalid arguments¡¯
# check if the first read ends in the same k bases that are found at the
# start of the second read
return first != second and first[-k:] == second[:k]
def maximalOverlap(first, second):
"""
>>> maximalOverlap(¡¯AAATTTT¡¯, ¡¯TTTTCCC¡¯)
4
>>> maximalOverlap(¡¯ATATATATAT¡¯, ¡¯TATATATATA¡¯)
9
"""
# find first overlap, starting with the longest possible overlap
for k in range(min(len(first), len(second)), 0, -1):
if overlap(first, second, k):
return k
# no overlap found
return 0
def overlapGraph(reads, k):
"""
>>> reads = [¡¯AAATAAA¡¯, ¡¯AAATTTT¡¯, ¡¯TTTTCCC¡¯, ¡¯AAATCCC¡¯, ¡¯GGGTGGG¡¯]
>>> overlapGraph(reads, 3)
{¡¯AAATTTT¡¯: {¡¯TTTTCCC¡¯}, ¡¯AAATAAA¡¯: {¡¯AAATTTT¡¯, ¡¯AAATCCC¡¯}}
>>> overlapGraph(reads, 4)
{¡¯AAATTTT¡¯: {¡¯TTTTCCC¡¯}}
>>> reads = [¡¯GACCTACA¡¯, ¡¯ACCTACAA¡¯, ¡¯CCTACAAG¡¯, ¡¯CTACAAGT¡¯, ¡¯TACAAGTT¡¯, ¡¯ACAAGTTA¡¯, ¡¯
CAAGTTAG¡¯, ¡¯TACAAGTC¡¯, ¡¯ACAAGTCC¡¯, ¡¯CAAGTCCG¡¯]
>>> overlapGraph(reads, 6)
{¡¯CTACAAGT¡¯: {¡¯ACAAGTCC¡¯, ¡¯ACAAGTTA¡¯, ¡¯TACAAGTC¡¯, ¡¯TACAAGTT¡¯}, ¡¯TACAAGTT¡¯: {¡¯CAAGTTAG¡¯, ¡¯
ACAAGTTA¡¯}, ¡¯ACCTACAA¡¯: {¡¯CTACAAGT¡¯, ¡¯CCTACAAG¡¯}, ¡¯ACAAGTCC¡¯: {¡¯CAAGTCCG¡¯}, ¡¯ACAAGTTA
¡¯: {¡¯CAAGTTAG¡¯}, ¡¯GACCTACA¡¯: {¡¯CCTACAAG¡¯, ¡¯ACCTACAA¡¯}, ¡¯TACAAGTC¡¯: {¡¯ACAAGTCC¡¯, ¡¯
CAAGTCCG¡¯}, ¡¯CCTACAAG¡¯: {¡¯CTACAAGT¡¯, ¡¯TACAAGTC¡¯, ¡¯TACAAGTT¡¯}}
"""
# construct overlap graph by determining the maximal overlap between any
# pair of different reads
graph = {}
for first in reads:
for second in reads:
if maximalOverlap(first, second) >= k:
if first not in graph:
graph[first] = {second}
else:
graph[first].add(second)
# return the constructed overlap graph
return graph
if __name__ == ¡¯__main__¡¯:
42
import doctest
doctest.testmod()