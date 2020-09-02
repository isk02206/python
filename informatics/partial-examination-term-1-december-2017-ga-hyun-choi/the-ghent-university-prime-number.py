def findchar(character1, character2, sequence):
    '''
    find character other than the characters given within the string
    if there is no exceptional character in the string, return None
    :param character1:
    :param character2:
    :return:
    >>> findchar('.','8','........88..88..88..88..88..82..88.........')
    ('2', 30)
    >>> findchar('.','8','...........................................')
    False
    '''
    sequence1 = list(sequence)
    exception, e_index = '', 0
    for element in sequence1:
        if element != character1 and element != character2:  # if the element is an exception, indicate
            exception, e_index = element, sequence.index(element)
            break
    if exception or e_index:  # if there is an exception, return the exception and the column number
        return exception, e_index+1
    else:
        return False


character1, character2 = input()  # separate the first input
rows = input()  # the string that should go in the findchar function
row = 0  # indicate the row
exception = ()
while rows:
    row += 1
    exception = findchar(character1, character2, rows)
    if exception:  # found the exceptional character
        break
    rows = input()  # move on to the next row
# template the output
template = "character '{}' only occurs at row {} and column {}".format(exception[0], row, exception[1])
print(template)




if __name__ == "__main__":
    import doctest
    doctest.testmod()