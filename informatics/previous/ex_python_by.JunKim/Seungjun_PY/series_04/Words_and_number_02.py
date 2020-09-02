'''
Created on 2015. 10. 1.

@author: Jun Kim
'''
intnum = int(input())
number_name = input()
final = ""
while intnum > 0 :
    number = '0123456789 ,-'
    other_things = ""
    for name_without_numbers in number_name:
        if name_without_numbers.lower() not in number:
            other_things += name_without_numbers.lower()
        
    name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,-'
    other_things = ""
    for name_with_numbers in number_name:
        if name_with_numbers not in name:
            other_things += name_with_numbers
    real_number = int(other_things)
    pos = 0
    remain_number = 0
    
    while pos < len(other_things):
        remain = other_things[pos]
        asci = ord(remain.lower())
        order = asci - 96
        remain_number += order
        pos += 1
        
    if real_number > remain_number:
        ans = (str(real_number)+'['+str(remain_number)+']')
        final = final+ ","+ans
    else:
        pass
    if intnum >1:
            number_name = input()
    else:
        pass
    intnum = -1
print(final.replace(", ","", 1))        
    