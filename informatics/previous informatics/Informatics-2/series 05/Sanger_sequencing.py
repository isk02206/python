'''
Created on 2016. 1. 14.

@author: User
'''
def sanger(seq):
    if len(seq)<= 9:
        for seq in range(1,10):
            print (seq ,end="")
        print ('')
    
    

print(sanger('ATGG'))