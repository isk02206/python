'''
Created on 2015. 11. 5.

@author: User
'''


def network(file):
    reader = open(file, 'r',encoding = 'utf-8')
    result = dict()
    list1 = []

    for line in reader:
        line = line.split('\t')    
        line[1] = line[1][:-1]
        list1 += [line]
    
    for x in list1:
        for y in list1:
                
            result.setdefault(x[0],set()).add(x[1])
            result.setdefault(x[1],set()).add(x[0])
            
            if x[0] == y[1]:
                result[x[0]].add(y[0])
                
    return result

def hubs(tower1,tower2,network):
    
    if tower2 not in network.keys() or tower1 not in network.keys():
        
        raise (AssertionError( 'city not in network'))
    
    else:
    
        U = [tower1]
        
        P = {tower1: 0}
        
        d = 0
        
        while tower2 not in P.keys():

            a = U.pop(0)

            net = network[a]    
                
            for x in net:
                
                if not x in P.keys():
                    
                    d = P[a]+ 1
                    
                    P[x] = d
                    U.append(x)
            if U == []:
                
                return -1
        
        return P[tower2]
