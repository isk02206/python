t = int(input())

for i in range(t):
    n = int(input())
    if n == 0:
        print(1)
    
    if 1 <= n <= 13:
        num =1
        while 1 <= n <= 13:
            num = num*n
            n = n-1
        print(num)
    if n > 13:
        print('input too large')