'''
Created on 2018. 11. 05
@Subject : square_routes
@Author : Son Jee Hun
@Student Number : 01406444
'''
def square(length, start_number=None):
    '''
    >>> square(3)
    [[1, 1, 1], [1, 2, 3], [1, 3, 6]]
    >>> square(3, 100)
    [[100, 100, 100], [100, 200, 300], [100, 300, 600]]
    >>> square(4)
    [[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10], [1, 4, 10, 20]]
    '''
    if start_number is None: # if start_number is none start_number is 1
        start_number = 1

    matrix = [[start_number] * length] * length # make matrix
    for i in range(1, len(matrix)):
        update = list()
        for j in range(len(matrix[0])):
            update.append(sum(matrix[i-1][:j+1]))# sum matrix cross sum movement allow
        matrix[i] = list(update) # update matrix
    return matrix

def routes(length, start_number=None):
    '''
    >>> print(routes(3))
     1 1 1
     1 2 3
     1 3 6
    >>> print(routes(3, 100))
     100 100 100
     100 200 300
     100 300 600
    >>> print(routes(4))
      1  1  1  1
      1  2  3  4
      1  3  6 10
      1  4 10 20
    >>> print(routes(6))
       1   1   1   1   1   1
       1   2   3   4   5   6
       1   3   6  10  15  21
       1   4  10  20  35  56
       1   5  15  35  70 126
       1   6  21  56 126 252
    >>> print(routes(8))
        1    1    1    1    1    1    1    1
        1    2    3    4    5    6    7    8
        1    3    6   10   15   21   28   36
        1    4   10   20   35   56   84  120
        1    5   15   35   70  126  210  330
        1    6   21   56  126  252  462  792
        1    7   28   84  210  462  924 1716
        1    8   36  120  330  792 1716 3432
    >>> print(routes(10))
         1     1     1     1     1     1     1     1     1     1
         1     2     3     4     5     6     7     8     9    10
         1     3     6    10    15    21    28    36    45    55
         1     4    10    20    35    56    84   120   165   220
         1     5    15    35    70   126   210   330   495   715
         1     6    21    56   126   252   462   792  1287  2002
         1     7    28    84   210   462   924  1716  3003  5005
         1     8    36   120   330   792  1716  3432  6435 11440
         1     9    45   165   495  1287  3003  6435 12870 24310
         1    10    55   220   715  2002  5005 11440 24310 48620
    '''
    matrix = square(length, start_number) # use square funtion
    matrix_result_length = len(str(matrix[length-1][length-1]))
    result = ''
    count = 0
    for i in matrix:
        for j in i:
            result += "{0:>{spacing}}".format(str(j), spacing=matrix_result_length+1) # add spacing between value
            count += 1 # fill in value
            if count == length:
                result += '\n' # fill in matrix if length equal matrix length. fill in next row
                count = 0 # reset count
    return result.rstrip() # remove last blank

if __name__ == '__main__':
    import doctest
    doctest.testmod()