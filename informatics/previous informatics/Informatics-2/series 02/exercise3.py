a=str(input())
b=str(input())
c=int(input())
if a=='black' and b=='white':
    if c==1:
        print('black')
        print('black')
    if c==2:
        print('white')
        print('white') 
if a=='black' and b=='black':
    if c==1:
        print('white')
        print('black')
    if c==2:
        print('black')
        print('white')
if a=='white' and b=='white':
    if c==1:
        print('black')
        print('white')
    if c==2:
        print('white')
        print('black')
if a=='white' and b=='black':
    if c==1:
        print('white')
        print('white')
    if c==2:
        print('black')
        print('black')