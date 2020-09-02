'''
Created on 2015. 9. 7.

@author: User
'''

LTH=int(input())
LTM=int(input())
AFH=int(input())
AFM=int(input())
LFH=int(input())
LFM=int(input())
RHH=int(input())
RHM=int(input())

LTH1=LTH*60+LTM
AFH1=AFH*60+AFM
LFH1=LFH*60+LFM
RHH1=RHH*60+RHM

A=(RHH1-LTH1)%(60*24)
B=(LFH1-AFH1)%(60*24)

C=(A-B)/2

D=(C+LFH1)%(60*24)
      
print(int(D//60))
print(int(D%60))
