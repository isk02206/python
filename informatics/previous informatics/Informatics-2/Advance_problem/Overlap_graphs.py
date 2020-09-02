'''
Created on 2015. 11. 20.

@author: Haeun Kim
@Student number: 01413456

'''
def overlap(read1, read2, k):

    check1 = read1[-k:] #beginning at index -6 and continuing through the end of the read1
    check2 = read2[:k] #from the beginning of the read1 up to, but not including, the character at index k
    if check1 == check2: #if check1 is equal to check2
        return True
    else:
        return False
def maximalOverlap(read1, read2):
    k = len(read1) #k is length of read1
    while True: #loop forever
        if overlap(read1, read2, k) == True: #if function overlap is True
            return k
        else:# if it is False
            k -= 1 # k = k - 1
            
        if k == 0: #if k is equal to 0
            return k
            break         
def overlapGraph(reads, k):
    dict = {} #initialize a dictionary to be empty
    for read1 in reads:  #set the range to stop the loop
        for read2 in reads:  #set the range to stop the loop
            if read1 != read2 and 0 < k <= maximalOverlap(read1, read2): #if read1 is not equal to read2 and k is greater than 0 and less than or equal to the second function
                dict.setdefault(read1,set()).add(read2)  #returns read1 value available in the dictionary add add with read2
    return dict