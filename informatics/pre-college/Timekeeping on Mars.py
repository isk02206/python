s = int(input())
b = 88775.244 * s
d = b // 3600
m = (b % 3600) // 60
a = (b % 3600) % 60

print(int(s), 'sols =', int(d // 24), 'days,', int((d % 24)), 'hours,', int(m), 'minutes and', int(a), 'seconds')
