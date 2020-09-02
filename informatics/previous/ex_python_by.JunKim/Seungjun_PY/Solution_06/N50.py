'''
Created on 2015. 12. 1.

@author: USER
'''
def median(collection):
    """
    returns the median of a given collection of numbers
    >>> median((2, 2, 2, 3, 3, 4, 8, 8))
    3.0
    """
    collection = sorted(collection)
    if len(collection) % 2:
        return float(collection[len(collection) // 2])
    else:
        middle = len(collection) // 2
    return (collection[middle - 1] + collection[middle]) / 2
def extend(collection):
    """
    returns the extended list in wich each value n from the given collection
    is added n times
    >>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
    >>> extend(contigs)
    [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    8, 8]
    """
    extended = []
    for number in collection:
        extended += [number] * number
    return extended
def N50(collection):
    """
    computes the N50 statistic as the median of the extended list 21
    >>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
    >>> N50_median(contigs)
    6.0
    """
    return median(extend(collection))
if __name__ == '__main__':
    import doctest
    doctest.testmod()