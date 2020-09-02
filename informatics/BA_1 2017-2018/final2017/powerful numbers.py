m = int(input())
result = 0
power = 0
after_result = 1
while result < m:
    result = 0
    for i in str(m):
        i = int(i)
        result += i**power
    after_result = result
    if m == result:
        print(m,'is a powerful number of order',power)
    else:
        power += 1
if result > m:
    print(m,'is not a powerful number')