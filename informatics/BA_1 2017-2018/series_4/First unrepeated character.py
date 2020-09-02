x = str(input())

for i in x:
    if x.count(i) == 1:
        print(x.index(i))
        break
else:
    print('-1')