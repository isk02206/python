a = 'asjkasjbasfjbacsbqweg'
'''
for pos, char in enumerate(a):
    #print(pos, char)
    if a[pos] == 'a':
        print(pos)
'''        
b = []
bset = set(b)
position = {}     

for i in a:
    b.append(i)
    for char, posi in enumerate(a):
        pos = []
        if a[posi] == char:
            pos.append(posi)
        v.setdefault(pos,[].append(char))
print(position)       





for char, pos in enumerate(a):
    if char == position[char]:
        position[char] += (pos+1)
    else:
        position[char] =pos+1
print(position)