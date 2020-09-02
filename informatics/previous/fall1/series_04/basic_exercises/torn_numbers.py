n = str(input())

for i in range(1, len(n)):
    first = int(n[0:i])
    second = int(n[i:(len(n)+1)])
    sum = (first + second)**2
    
    if sum == int(n):
        print('torn')
        break
else:
    print('not torn')