n = int(input())#generation

female = 1
male = 0
total = 1

for i in range(1,n):
    male = female
    female = total
    total = female + male

if n == 0:
    female = 0
    male = 1
elif n == 1:
    female = 1
    male = 0

print('number of female bees:',female)
print('number of male bees:',male)
print('total number of bees:',total)

'''
x = number of female bees
y = number of male bees
z = total number of bees
'''