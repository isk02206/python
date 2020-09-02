'''
Name:SungJoon Park
ID: 01514170
'''
def factorial(number):#defining a function that calculates the factorial of the number x
    total = 1
    for i in range(number):
        i += 1
        total *= i#multiplying one added number to the number before
    return total

def combination(n,r):#defining a function that calculates the combination of the number.
    comb = factorial(n) / (factorial(r) * factorial(n-r)) #using the factorial to calculate the combination result
    return int(comb)

def triangle(r):
    # must return the rth row of the pascal's triangle
    '''
    >>> triangle(0)
    []
    >>> triangle(1)
    [[1]]
    >>> triangle(2)
    [[1], [1, 1]]
    >>> triangle(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> triangle(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> triangle(-1)
    Traceback (most recent call last):
    AssertionError: invalid number of rows
    >>> triangle(3.14)
    Traceback (most recent call last):
    AssertionError: invalid number of rows
    '''
    total = []
    if type(r) == int and r >= 0:# r must be a natural number
        if r == 0:#if the r is 0 we must return a empty list
            return total
        else:
            for i in range(r):#the secondary list must include lines before the next line
                rowList = []
                for j in range(i+1):#the secondary list must include the combination numbers of the number i
                    element = combination(i,j)
                    rowList.append(element)
                total.append(rowList)
        return total
    else:# if r does not satisfy the given conditions, certain error message must be shown
        raise AssertionError('invalid number of rows')

def hexagon(x,y):
    #the function must return a list of numbers which is collected by a hexagon made along the side of the certain location number x and y
    '''
    >>> hexagon(8, 4)
    [15, 20, 35, 70, 56, 21]
    >>> hexagon(16, 7)
    [2002, 3003, 6435, 11440, 8008, 3003]
    >>> hexagon(3, 3)
    Traceback (most recent call last):
    AssertionError: invalid internal position

    '''
    if x != y and y !=1 and x>2:#there are certain numbers that cannot make a hexagon with numbers around.
        pascal = triangle(x+1)
        a = int(pascal[x-2][y-2])# a number near the location which makes a hexagon.
        b = int(pascal[x-2][y-1])
        c = int(pascal[x-1][y])
        d = int(pascal[x][y])
        e = int(pascal[x][y-1])
        f = int(pascal[x-1][y-2])
        result = [a,b,c,d,e,f]
        return result
    else:
        raise AssertionError('invalid internal position')

def square(x,y):
    #the function must return an equation that showing the multiple of each element, total digit, and the digit that has the same two roots.
    '''
    >>> square(8, 4)
    '15 x 20 x 35 x 70 x 56 x 21 = 864360000 = 29400 x 29400'
    >>> square(16, 7)
    '2002 x 3003 x 6435 x 11440 x 8008 x 3003 = 10643228293383247161600 = 103166022960 x 103166022960'
    >>> square(3, 3)
    Traceback (most recent call last):
    AssertionError: invalid internal position
    '''
    if x != y and y != 1 and x > 2:
        a = hexagon(x,y)
        a1,a2,a3,a4,a5,a6 = int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]),int(a[5]) #converting the elements into a integer collected by the function hexagon
        total = a1*a2*a3*a4*a5*a6#multiplying the elements to get total digit
        root = int(total**0.5)#finding the root of the total digit
        statement = str(a1),'x',str(a2),'x',str(a3),'x',str(a4),'x',str(a5),'x',str(a6),'=',str(total),'=',str(root),'x',str(root)
        return ' '.join(statement)
    else:
        raise AssertionError('invalid internal position')

if __name__ == '__main__':
    import doctest
    doctest.testmod()