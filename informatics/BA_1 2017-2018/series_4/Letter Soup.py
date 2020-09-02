n = int(input())
result = ''
for i in range(n):
    line = input()
    for j in line:
        if 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
            result += j
print(result)