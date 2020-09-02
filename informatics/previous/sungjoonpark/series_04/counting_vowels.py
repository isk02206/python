'''
statement = str(input())



vowels = 'aeiou'
vowel = []

for i in range(len(statement)):
    if statement[i] == vowels:
        vowel.append(statement[i])
        
print(len(vowel))
'''
statement = str(input())


a = statement.count('a')
a1 = statement.count('A')
b = statement.count('e')
b1 = statement.count('E')
c = statement.count('i')
c1 = statement.count('I')
d = statement.count('o')
d1 = statement.count('O')
e = statement.count('u')
e1 = statement.count('U')

x = a+b+c+d+e+a1+b1+c1+d1+e1

print(x)