'''
Name:SungJoon Park
ID: 01514170
'''
def serialNumber(a):
    #the function must add 0 if the length of the argument is smaller than 8
    '''
    >>> serialNumber(834783)
    '00834783'
    >>> serialNumber('47839')
    '00047839'
    >>> serialNumber(834783244839184)
    '834783244839184'
    >>> serialNumber('4783926132432*')
    Traceback (most recent call last):
    AssertionError: invalid serial number
    '''
    if type(a) == str:#finding the type of the argument
        for i in a:
            if i.isdigit() == False:#if there is a element which is not a digit, the function must return a error message
                raise AssertionError('invalid serial number')
        count = 0
        for j in a:#if all digits are 0, the function must return a error message
            if j == '0':
                count += 1
        if count == len(a):
            raise AssertionError('invalid serial number')
        else:
            serial = str(a)
            if len(serial) > 8:#if the length is longer than 8, we return the same number
                return serial
            else:#if the argument's length is shorter than 8, there must be 0 added to the number
                while len(serial) < 8:
                    serial = '0' + serial
        return serial
    if type(a) == int and int(a)>0:
        serial = str(a)
        if len(serial) >8:
            return serial
        else:
            while len(serial) < 8:
                serial = '0'+serial
        return serial
    else:
        raise AssertionError('invalid serial number')

def solid(a):
    #the function must return boolean value indicating whether the number has the same character.
    '''
    >>> solid(44444444)
    True
    >>> solid('44544444')
    False
    '''
    if type(a) == str:
        for i in a:
            if i.isdigit() == False:
                raise AssertionError('invalid serial number')
        count = 0
        for j in a:
            if j == '0':
                count += 1
        if count == len(a):
            raise AssertionError('invalid serial number')
        else:
            x = str(a)#argument must be converted into string type
            x1 = str(x)[0]# the first number which is the standard number of other digits.
            for i in x:#finding if the number is true
                if i != x1:#if digit is different with the standard number, it must return False
                    return False
            else:
                return True
    if type(a) == int and int(a) > 0:
        x = str(a)
        x1 = str(x)[0]
        for i in x:
            if i != x1:
                return False
        else:
            return True
    else:
        raise AssertionError('invalid serial number')

def radar(serial):
    # the function must return a boolean value if the serial number is symmetry, not including 0
    '''
    >>> radar(1133110)
    True
    >>> radar('83289439')
    False
    '''
    if solid(serial) == True:
        return False
    if type(serial) == str:
        if len(serial) < 8:
            serial = serialNumber(serial)
        for i in serial:
            if i.isdigit == False:
                return False
        else:
            fir_half = serial[:len(serial) // 2]
            sec_half = serial[len(serial) // 2:]
            flip_sec_half = sec_half[::-1]
            if fir_half == flip_sec_half:
                return True
            else:
                return False
    if type(serial) == int and int(serial) > 0:
        serial = str(serial)
        if len(serial) < 8:
            serial = serialNumber(serial)
        fir_half = serial[:len(serial)//2]
        sec_half = serial[len(serial)//2:]
        flip_sec_half = sec_half[::-1]
        if fir_half == flip_sec_half:
            return True
        else:
            return False
    else:
        raise AssertionError('invalid serial number')

def repeater(serial):
    #the function must return a boolean value if the serial number is repeating
    '''
    >>> repeater(20012001)
    True
    >>> repeater('83289439')
    False
    '''
    serial = serialNumber(serial)
    fir_half = serial[:len(serial) // 2]
    sec_half = serial[len(serial) // 2:]
    if fir_half == sec_half:
        return True
    if fir_half != sec_half:
        return False

def radarRepeater(serial):
    #the function must return a boolean value if the serial number is repeating and symmetry inside the repeating digits.
    '''
    >>> radarRepeater('12211221')
    True
    >>> radarRepeater('83289439')
    False
    '''
    serial = serialNumber(serial)
    if solid(serial) == True:
        return False
    if repeater(serial) == True:
        half = serial[:len(serial)//2]
        fir_half = half[:len(half)//2]
        sec_half = half[-(len(half)//2):][::-1]
        if fir_half == sec_half:
            return True
        else:
            return False
    else:
        return False

def numismatist(list, kind = None):
    #the function must indicate serial numbers which satisfy the kind condition.
    '''
    >>> numismatist([33333333, 1133110, '77777777', '12211221'])
    [33333333, '77777777']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], radar)
    [1133110, '12211221']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], kind=repeater)
    ['12211221']
    >>> numismatist(['99887799778', 999999399, '12345678', '98798798', 99999999], kind=lambda x : set(str(x)) <= {'7', '8', '9'})
    ['99887799778', '98798798', 99999999]

    '''
    correct = []
    if kind == None or kind == solid:
        for i in list:
            if solid(i) == True:
                correct.append(i)# including the serial number to the correct list if the condition is True.
    if kind == radar:
        for i in list:
            if radar(i) == True:
                correct.append(i)
    if kind == repeater:
        for i in list:
            if repeater(i) == True and solid(i) == False:
                correct.append(i)
    if kind == radarRepeater:
        for i in list:
            if radarRepeater(i) == True:
                correct.append(i)
    if kind != None and kind != solid and kind != radar and kind != repeater and kind != radarRepeater:# if the kind a lambda, it must satisfy the lambda condition
        for i in list:
            if kind(i) == True:
                correct.append(i)
    return correct