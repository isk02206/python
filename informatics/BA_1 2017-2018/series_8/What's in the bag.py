'''
Name:SungJoon Park
ID: 01514170
'''
def fill(letters):
    #this function organizes the letters into a dictionary that takes the alphabet as key and number of the key as value.
    bag = {}
    for i in letters:
        if i in bag:#adding value if there is the key is present
            bag[i] += 1
        if i not in bag:#adding key if there is no key in the dictionary
            bag[i] = 1
    return bag

def description(bag):
    #this function must return a dictionary that as the key as counting and values as alphabets that has the same counting there is in the bag.
    '''

>>> description({'Z': 1, 'J': 1, '_': 2, 'O': 8, 'W': 2, 'U': 4, 'K': 1, 'R': 6, 'X': 1, 'H': 2, 'F': 2, 'P': 2, 'E': 12, 'I': 9, 'N': 6, 'M': 2, 'V': 2, 'T': 6, 'D': 4, 'C': 2, 'S': 4, 'G': 3, 'Q': 1, 'B': 2, 'L': 4, 'Y': 2, 'A': 9})
{1: {'K', 'Q', 'X', 'J', 'Z'}, 2: {'W', 'C', '_', 'H', 'V', 'M', 'F', 'B', 'P', 'Y'}, 3: {'G'}, 4: {'D', 'S', 'L', 'U'}, 6: {'N', 'R', 'T'}, 8: {'O'}, 9: {'A', 'I'}, 12: {'E'}}
    '''
    result = {}
    new = {}
    for i in bag.keys():#collecting and organizing the keys and values taken by the result of the fuction fill
        if bag[i] in result:
            result[bag[i]] += [i]
        if bag[i] not in result:
            result[bag[i]] = [i]
    for j in result.keys():#changing the set of value as a set
        new[j] = set(result[j])
    return new

def remove(element,bag):
    # this function removes the value that was organized by the function fill.
    x = bag
    a = fill(element)
    for i in a.keys():
        if i in x:
            b = x[i] - a[i]
            x.pop(i)
            if b < 0:#if the element is not in the bag, error message must be shown
                raise AssertionError('not all letters are in the bag')
            if b >0:
                x[i] = b
        else:#if the element is not in the bag, error message must be shown
            raise AssertionError('not all letters are in the bag')
    return x.update()#returning the changed dictionary