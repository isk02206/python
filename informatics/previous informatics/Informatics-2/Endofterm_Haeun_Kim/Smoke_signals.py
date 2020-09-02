'''
Created on 2015. 11. 20.

@author: Haeun Kim
@Student number: 01413456

'''
def observed(signal, network): 
    
    a = set() #set() creates the empty set
    for x in network: #set the range in this loop
        if x in signal:
            if a == set(): #if a is equal to set()
                a = set(network[x])
            
            else:# if a is not same with set()
                b = set(network[x])
                set1 = set(a).union(b) #set1 contains all the element in both a and b sets
                
                for y in signal: 
                    if y in set1:
                        set1.remove(y) #remove the element from the set1 whose value is y
                    a = set1
                
    if len(list(signal)) != 1: #if the length of the list is not 1 
        return set1
    else: #if it is 1
        return a
    
  
def distribution(watchtower, network):
    
    count = 0 #starting point is zero
    count1 = network[watchtower]
    exclusion = {x for x in count1}
    check_count = 0
    value = set() #set() creates the empty set
    
    len_dictionary = {y for y in network}
    len_dictionary = len(list(len_dictionary))
    
    while watchtower >= 0: #stop when the watchtower is greater than or equal to 0 
        for number in count1:
            a = {watchtower}
            b = {number}
            check_count += 1 #add to the check_count
            check = observed(a.union(b), network) # 
            check = check.difference(exclusion) # elements of check that are not in exclusion

            len_exclusion = len(list(exclusion))
            if check == set() and len_exclusion == len_dictionary-1:
                return count + 1
                break
        
            for c in check: #set the range to stop the loop
                value = value.union({c}) #value contains all the element in both value and c
            
            if check_count == len(list(count1)): #if check_count is equal to length of the list 
                count += 1 #add to the count
                check_count = 0
        count1 = value
        exclusion = exclusion.union(value) #exclusion contains all the element in both exclusion and value
        value = set()