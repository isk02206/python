'''
Name:SungJoon Park
ID: 01514170
'''
def digits(phone_number):
    #extracting out only the digits in the phone number
    '''
    >>> digits('0472/91.39.17')
    '0472913917'
    >>> digits('++32 (0)9 264 4779')
    '32092644779'
    '''
    number = []
    for i in phone_number:
        if i.isdigit() == True: #finding only number in phone number
            number.append(i)
    return ''.join(number)

def replace(phone_number,digit):
    #replacing the phone number's digits into given digits in the second argument
    #if there is less digits in the second argument, we must replace with 0
    #if there is more digits in the second argument , we must limit the digits in the second argument
    '''
    >>> replace('0472/91.39.17', 1234567890)
    '1234/56.78.90'
    >>> replace('++32 (0)9 264 4779', 123456789)
    '++00 (1)2 345 6789'
    '''
    replaced = []
    digit = str(digit)
    pos = 0

    if len(digits(phone_number)) > len(digit):#when there are more digits in the first argument
        y = (len(digits(phone_number)) - len(digit))
        digit = '0' * y + digit #replace phone number digits with 0
        for i in phone_number:
            if i.isdigit() == True:#if the element of first argument is a digit, they we replace it with the second argument's digit
                x = digit[pos]
                replaced.append(x)
                pos += 1
            else:
                replaced.append(i)#if the element is not a digit, we keep them by placing the symbol in the replaced list
    else: # if there are less digits in the second argument
        for i in phone_number:#loop must run as much as the length of the first argument
            if i.isdigit() == True:
                x = digit[pos]
                replaced.append(x)
                pos += 1
            else:
                replaced.append(i)
    return ''.join(replaced)

def upstairsNeighbour(phone_number):
    #we upper one level of the integer of the whole digit part
    '''
    >>> upstairsNeighbour('0472/91.39.17')
    '0472/91.39.18'
    >>> upstairsNeighbour('++32 (0)9 264 4779')
    '++32 (0)9 264 4780'
    '''
    up_neighbor = int(digits(phone_number))+1#extract the digits in the phone number, then add one to the number
    upstairsNeighbour = replace(phone_number, up_neighbor)#replace the one upper number by the original phone number
    return upstairsNeighbour

def downstairsNeighbour(phone_number):
    '''
    >>> downstairsNeighbour('0472/91.39.17')
    '0472/91.39.16'
    >>> downstairsNeighbour('++32 (0)9 264 4779')
    '++32 (0)9 264 4778'
    '''
    down_neighbor = int(digits(phone_number)) - 1#extract the digits in the phone number, then minus one to the number
    downstairsNeighbour = replace(phone_number, down_neighbor)#replace the one lower number by the original phone number
    return downstairsNeighbour
