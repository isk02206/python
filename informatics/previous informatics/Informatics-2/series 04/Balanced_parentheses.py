
t = int(input())
counter = 0
for x in range(t):
   parenthesis = input()
   for y in parenthesis:
        if y == '(' or y =='[' or y =='{' or y =='<':
            count +=1
        elif y == ')' or y ==']' or y =='}' or y =='>':
            count-=1  
        if counter < 0:
            break
   
   if counter == 0:
        print('balanced')
   else:
        print('unbalanced')
   counter = 0    