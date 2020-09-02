'''
Created on 2015. 12. 3.

@author: User
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
#p, running_size = 0, 0.0
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

    return (N50_decreasing(contigs, size) + N50_increasing(contigs, size)) / 2
if __name__ == ¡¯__main__¡¯:
    import doctest
    doctest.testmod()
'''
Write a function N50_decreasing that takes a collection (list, tuple, collection, ¡¦) of integers. These integers represent the lengths of the contigs obtained after genome assembly. The function also has a second optional parameter size to which the genome size can be passed. If no value is passed to this parameter, the sum of the given contig lengths is used as an estimate of the genome size. The function must return the approximation of the N50 statistic (as an integer) that is obtained if the procedure described above is applied with the contig lengths added in decreasing order.
Write a function N50_increasing that takes same parameters as the function N50_decreasing, with the same meaning. The function must return the approximation of the N50 statistic (as an integer) that is obtained if the procedure described above is applied with the contig lengths added in increasing order.
Use the functions N50_decreasing and N50_increasing to write a function N50 that has the same parameters as the previous two functions, with the same meaning. The function must return the N50 statistic of the given collection of contig lengths as a floating point number.
'''