'''
N = int(input('a single integer: '))


male0 = 0

female0 = 1

male1 = 1

female1 = 0

for n in range(N-1):

   tempM = male1
   male1 = male1 + male0
   male0 = tempM
   
   tempF = female1
   female1 = female1 + female0
   female0 = tempF
   
total = female1 + male1

print(male1)
print(female1)
print(total)
'''
'''
n = int(input())

x1 = 1
x2 = 1

for i in range(n):
    x1, x2 = x2, x1+x2
print(x1,x2)
'''
generation = int(input())

female0 = 0
female1 = 1
male0 = 1
male1 = 0

for x in range(generation-1):
    female0,female1 = female1, female0+female1
    
    
for y in range(generation-1):
    male0, male1 = male1, male0 + male1
    
    
print('number of female bees:',female1)
print('number of male bees:',male1)
print('total number of bees:',female1+male1)
    
    
    