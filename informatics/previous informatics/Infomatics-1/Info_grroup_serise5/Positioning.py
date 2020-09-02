'''
Created on 2016. 1. 22.

@author: User
'''
def degrees2GMS(num):
    
    G = int(num)
    
    M = int((num - G)*60)
    
    S = round((((num - G)*60) - M)*60)
    
    return "{}*{}'{}".format(G,M,(str(int(S))+'"'))