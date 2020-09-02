a = str(input())
b = str(input())

r = 'rock'
p = 'paper'
s = 'scissors'

if a == b:
    print('tie')
elif a == r and b == s:
    print('player1 wins')
elif a == r and b == p:
    print('player2 wins')
elif a == p and b == r:
    print('player1 wins')
elif a == p and b == s:
    print('player2 wins')
elif a == s and b == r:
    print('player2 wins')
elif a == s and b == p:
    print('player1 wins')