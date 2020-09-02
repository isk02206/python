s1=input()
s2=input()
r=input()

if s1=='value':
    if int(s2) in [1,3,5,7,9]:
        if r==('yes'):
            print("Wrong: cards with",s1,int(s2),"must not be turned.")
        if r==('no'):
            print("Correct: cards with",s1,int(s2),"must not be turned.")
    else: 
        if int(s2) in [2,4,6,8,10]:       
            if r==('yes'):
                print("Correct: cards with",s1,int(s2),"must be turned.")
            if r==('no'):
                print(" Wrong: cards with",s1,int(s2),"must be turned.") 
if s1=='color':
    if s2=='red':
        if r==('yes'):
            print('Wrong: cards with', s1 ,s2 , 'must not be turned.')
        if r=='no':
            print('Correct: cards with', s1 ,s2 , 'must not be turned.')
    else:
        if r==('yes'):
            print('Correct: cards with',s1 , s2,'must be turned.')  
        if r==('no'):
            print('Wrong: cards with',s1 , s2,'must be turned.')  