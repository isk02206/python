line = int(input())

counter_to_the_value = 0
for i in range(line):
    #print(i)
    parentheses = str(input())
    #print(parentheses)
    for j in parentheses:
        #print(j)
        if j == '(' or j == '{' or j == '[' or j == '<':
            counter_to_the_value += 1
        elif j == ')' or j == '}' or j == ']' or j == '>':
            counter_to_the_value -= 1
        if counter_to_the_value < 0:
            break
    if counter_to_the_value == 0:
        print('balanced')
    else:
        print('unbalanced')
    counter_to_the_value = 0 # refresh value