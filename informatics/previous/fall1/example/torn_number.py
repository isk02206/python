n = str(input())

list = []

for i in range(1,len(n)):
    n1 = n[:i]
    n2 = n[i:]
    sum = (int(n1)+int(n2))**2
    if sum == int(n):
        list.append(sum)
    
    if sum in list:
        print('torn')
        break
else:
    print('not torn')
