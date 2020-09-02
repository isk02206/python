
network = {1:{2, 5}, 2:{1, 5, 3}, 3:{2, 4}, 4:{3, 5, 6}, 5:{1, 2, 4}, 6:{4}}
def observed(signal, network):
    
    a = set()
    for x in network:
        if x in signal:
            if a == set():
                a = set(network[x])
            
            else:
                b = set(network[x])
                set1 = set(a).union(b)
                
                for y in signal:
                    if y in set1:
                        set1.remove(y)
                    a = set1
                
    if len(list(signal)) != 1:
        return set1
    else:
        return a
    
  
    
   
   

def distribution(watchtower, network):
    count = 0
    count1 = network[watchtower]
    exclusion = {x for x in count1}
    check_count = 0
    value = set()
    
    len_dictionary = {y for y in network}
    len_dictionary = len(list(len_dictionary))
    
    while watchtower >= 0:
        for number in count1:
            a = {watchtower}
            b = {number}
            check_count += 1
            check = observed(a.union(b), network)
            check = check.difference(exclusion)

            len_exclusion = len(list(exclusion))
            if check == set() and len_exclusion == len_dictionary-1:
                return count + 1
                break
        
            for c in check:
                value = value.union({c})
            
            if check_count == len(list(count1)):
                count += 1
                check_count = 0
        count1 = value
        exclusion = exclusion.union(value)
        value = set()
print(distribution(1, network))