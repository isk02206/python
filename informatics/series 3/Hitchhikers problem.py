n = int(input()) #encounter n hitchhikers along the way

a = 0 #comparison value
high_score = 0 # high score change value
for a in range(a, int(n/2)): # integer division (n/2) compare for a high score
    #print(a)
    good_person = float(input())

    if good_person > high_score:
        high_score = good_person
    a += 1

check = False
for a in range(int(n / 2) + 1, n + 1): # except for (n/2)
    #print(a)
    good_person = float(input())
    if good_person > high_score and check == False:
        high_score = good_person
        check = True

if check == False:
    high_score = good_person #

print('{0:.4f}'.format(float(high_score)))

