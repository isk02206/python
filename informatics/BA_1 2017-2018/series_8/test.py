a = {'H': 10, 'C': 3}
b = {'C': 4, 'H': 10}
for i in a:
    if a[i] == b[i]:
        print('a')
    if a[i] != b[i]:
        print('b')