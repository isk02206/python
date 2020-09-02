'''
ID:01514170
Name: SungJoon Park
'''

a = int(input())
b = int(input())
n = int(input())
t = int(input())

for i in range(0,n+1):
    b += a**i #cell replication in experiment #1
print('experiment #1:',int(b-1),'cells after',n,'seceonds')#cell replicated in experiment1

for w in range(1,n):
    t += w*11 #cell replication in experiment #2
print('experiment #2:',int(t),'cells after',n-1,'seceonds')#cell replicated in experiment #2