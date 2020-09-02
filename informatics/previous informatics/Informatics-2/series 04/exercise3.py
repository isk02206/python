a=input()
even=(a.count('0')+a.count('2')+a.count('4')+a.count('6')+a.count('8'))
odd=(a.count('1')+a.count('3')+a.count('5')+a.count('7')+a.count('9'))
total=(odd+even)
a1=(str(even)+str(odd)+str(total))
print(a1)

if a==a1:
    print('')
else:
    a=a1
    while a:
        even=(a.count('0')+a.count('2')+a.count('4')+a.count('6')+a.count('8'))
        odd=(a.count('1')+a.count('3')+a.count('5')+a.count('7')+a.count('9'))
        total=(odd+even)
        a1=(str(even)+str(odd)+str(total))

        if a==a1:
            break
        else:
            print(a1)
            a=a1
