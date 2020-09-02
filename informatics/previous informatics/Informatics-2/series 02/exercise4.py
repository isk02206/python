p1=str(input())
p2=str(input())

if p1==p2:
    print('draw')
    
elif p1=='paper':
    if p2=='rock' or p2=='Spock':
        print('player1 wins')
    else:
        print('player2 wins')
        
elif p1=='rock':
    if p2=='scissors' or p2=='lizard':
        print('player1 wins')
    else:
        print('player2 wins')

elif p1=='lizard':
    if p2=='paper'or p2=='Spock':
        print('player1 wins')
    else:
        print('player2 wins')

elif p1=='Spock':
    if p2=='rock'or p2=='scissors':
        print('player1 wins')
    else:
        print('player2 wins')

elif p1=='scissors':
    if p2=='paper' or p2=='lizard':
        print('player1 wins')
    else:
        print('player2 wins')