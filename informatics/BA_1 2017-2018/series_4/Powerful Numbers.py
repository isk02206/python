m = int(input())

memo = [-1]
sum = 0
order = 0
if m ==0:
    print(m, 'is a powerful number of order 1')
while m > sum:
    for i in str(m):
        i = int(i)
        sum += i ** order
    memo.append(sum)
    if m < sum:
        print(m, 'is not a powerful number')
        break
    if m != sum:
        order += 1
        sum = 0
    if m == sum:
        print(m, 'is a powerful number of order', order)
    if memo[-1] == memo[-2]:
        print(m, 'is not a powerful number')
        break
