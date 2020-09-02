'''
Created on 2018. 1. 16.

@author: TaeWoo
'''

def overlap(read1, read2, length):
    
    return read1[-length:] == read2[:length]

def maximalOverlap(read1, read2):
    
    result = 0
    
    for length in range(1, min([len(read1), len(read2)])+1):
        
        if overlap(read1, read2, length) is True:
            result = length
        
    return result

def overlapGraph(reads, length):
    
    graph = dict()
    
    for read1 in reads:
    
        for read2 in reads:
            
            if read1 != read2:
                
                if maximalOverlap(read1, read2) >= length:
                    
                    if read1 not in graph:
                        graph[read1] = {read2}
                        
                    else:                        
                        graph[read1].add(read2)
        
    return graph

print(overlap('CTTTATC', 'CTTTATCA', 7))
print(maximalOverlap('TGGGGGC', 'TGGGGGCG'))


reads = ['AAATAAA', 'AAATTTT', 'TTTTCCC', 'AAATCCC', 'GGGTGGG']

#print(overlapGraph(reads, 4))