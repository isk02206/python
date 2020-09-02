'''
Created on 2015. 12. 1.

@author: USER
'''
def overflow(contigs, size, decreasing=True):
    """
    returns first element from the sorted contigs that makes the cumulative
    sum reach half of the given length; if no length is given, the total sum
    of all numbers in the list is considered as the contigs; if the value
    of the decreasing parameter is True (the default) the largest number needs to
    come first in the sorted contigs; otherwise the smallest number needs to
    come first in the sorted contigs
    >>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
    >>> overflow(contigs, 32)
    8
    >>> overflow(contigs, 32, decreasing=False)
    4
    """
    # calculate sum of the lengths of the contigs is no length was given
    if size is None:
        size = sum(contigs)
    # sort the list of contig lengths
    sorted_contigs = sorted(contigs, reverse=decreasing)
    # add contig lengths one by one, until half of the given length is reached
    p, running_size = 0, 0.0
    while running_size < (size / 2):
        running_size += sorted_contigs[p]
        p += 1
    return sorted_contigs[p - 1]
def N50_decreasing(contigs, size=None):
    """
    >>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
    >>> N50_decreasing(contigs)
    8
    """
    return overflow(contigs, size)
def N50_increasing(contigs, size=None):
    """
    >>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
    >>> N50_increasing(contigs)
    4
    """
    return overflow(contigs, size, decreasing=False)
def N50(contigs, size=None):
    """
    >>> contigs = (2, 2, 2, 3, 3, 4, 8, 8)
    >>> N50(contigs)
    6.0
    """
    29
    return (N50_decreasing(contigs, size) + N50_increasing(contigs, size)) / 2
if __name__ == '__main__':
    import doctest
    doctest.testmod()
