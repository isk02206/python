s1 = str(input())
v1 = str(input())
s2 = str(input())
v2 = str(input())

if s1 == 'clubs':
    if s2 == 'clubs':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    elif s2 == 'spades':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    else:
        print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
elif s1 == 'spades':
    if s2 == 'spades':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    elif s2 == 'clubs':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    else:
        print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
elif s1 == 'diamonds':
    if s2 == 'diamonds':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    elif s2 == 'hearts':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    else:
        print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
elif s1 == 'hearts':
    if s2 == 'hearts':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    elif s2 == 'diamonds':
        if v1 == v2:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are mates")
        else:
            print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
    else:
        print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
else:
    print("the",v1,"of",s1,"and the",v2,"of",s2,"are not mates")
