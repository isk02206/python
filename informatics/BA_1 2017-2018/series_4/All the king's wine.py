n = int(input())

pois_bot = 0

for i in range(n):
    x = input()
    x = ord(x) - 65
    pois_bot += 2**x

print('Bottle #'+str(pois_bot),'is poisoned.')