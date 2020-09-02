x = str(input())
y = str(input())

if ord(x[0]) > ord(y):
    z = 26-(ord(x[0]) - ord(y))
else:
    z = ord(y)- ord(x[0])

result = ""
for i in x:
    t = ord(i)
    result += "\n"
    result = result + chr(t)
    
    for j in range(z-1):
        t = t +1
        if t == 91:
            t =65
        result = result + chr(t+32)
    
    if chr(t) == chr(90):
        t = 64
        result = result + chr(t+1)
    else:
        result = result + chr(t+1)
print(result.strip())