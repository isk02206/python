n = int(input())


for i in range(n):
    statement = input()
    counter = 0
    for j in statement:
        if j == '(' or j == '{' or j == '[' or j == '<':
            counter += 1
        if j == ')' or j == '}' or j == ']' or j == '>':
            counter -= 1
        if counter == -1:
            counter = 9999999999999999999999999999999999999
            break
    if counter != 0:
        print('unbalanced')
    if counter == 0:
        print('balanced')