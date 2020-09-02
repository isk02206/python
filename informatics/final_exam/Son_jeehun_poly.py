'''
Created on 2018. 11. 30
@Subject : divide_and_conquer
@Author : Son Jee Hun
@Student Number : 01406444
'''
def longestPolydivisiblePrefix(number):
    '''
    >>> longestPolydivisiblePrefix(1234356789)
    123
    >>> longestPolydivisiblePrefix(381654729)
    381654729
    >>> longestPolydivisiblePrefix(381654728)
    38165472
    '''
    string_number = str(number)
    result = ''
    for i in string_number:
        result += i # string add number
        if int(result) % len(result) == 0: #multiple is remainder = 0
            continue
        else:
            return int(result[:-1]) # last number remove
            break

    return int(result)

# print(longestPolydivisiblePrefix(1234356789))
# print(longestPolydivisiblePrefix(381654729))
# print(longestPolydivisiblePrefix(381654728))

def isPolydivisible(number):
    '''
    >>> isPolydivisible(1234356789)
    False
    >>> isPolydivisible(381654729)
    True
    >>> isPolydivisible(381654728)
    False
    '''
    if int(number) == int(longestPolydivisiblePrefix(number)):
        return True # polydivisible is True
    return False # not polydivisible is False
# print(isPolydivisible(1234356789))
# print(isPolydivisible(381654729))
# print(isPolydivisible(381654728))

def polydivisibleExtensions(integer):
    '''
    >>> polydivisibleExtensions(12)
    4
    >>> polydivisibleExtensions(381654729)
    1
    '''
    polydivisible_count = 0 #count polydivisble
    string_integer = str(integer)
    polydivisible_number = ''
    polydivisible_number += string_integer# add string number
    for i in range(10):
        polydivisible_number += str(i) # add 0~9
        if int(polydivisible_number) % len(polydivisible_number) == 0:
            polydivisible_count += 1 # not remainder count+1
        polydivisible_number = polydivisible_number[:-1]# remove last number
    return polydivisible_count
# print(polydivisibleExtensions(12))
# print(polydivisibleExtensions(23))
# print(polydivisibleExtensions(381654729))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

