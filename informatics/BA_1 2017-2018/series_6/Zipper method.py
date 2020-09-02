def merge(list1,list2):
    '''
    >>> merge(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> merge(['A'], [1, 2, 3, 4])
    ['A', 1]
    >>> merge(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2]
    >>> merge(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2]
    '''
    mergeList = []
    pos = 0
    if len(list1) <= len(list2):
        for i in list1:
            mergeList.append(i)
            mergeList.append(list2[pos])
            pos += 1
    if len(list1) > len(list2):
        for j in list2:
            mergeList.append(list1[pos])
            mergeList.append(j)
            pos += 1
    return mergeList

def weave(list1, list2):
    '''
    >>> weave(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> weave(['A'], [1, 2, 3, 4])
    ['A', 1, 'A', 2, 'A', 3, 'A', 4]
    >>> weave(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 'A', 3, 'B', 4]
    >>> weave(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C', 1]
    '''

    weaveList = []
    if len(list1) < len(list2):
        count = len(list1)
        list1 = list1[::-1]
        for i in list2:
            weaveList.append(list1[count-1])
            weaveList.append(i)
            count -= 1
            if count == 0:
                count = len(list1)
    if len(list1) > len(list2):
        count = len(list2)
        list2 = list2[::-1]
        for j in list1:
            weaveList.append(j)
            weaveList.append(list2[count-1])
            count -= 1
            if count == 0:
                count = len(list2)
    if len(list1) == len(list2):
        pos = 0
        for k in list1:
            weaveList.append(k)
            weaveList.append(list2[pos])
            pos += 1
    return weaveList

def zipper(list1, list2):
    '''
    >>> zipper(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> zipper(['A'], [1, 2, 3, 4])
    ['A', 1, 2, 3, 4]
    >>> zipper(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 3, 4]
    >>> zipper(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C']
    '''
    zipperList = []
    if len(list1) == len(list2):
        zipperList = merge(list1,list2)
    else:
        if len(list1) > len(list2):
            zipperList = merge(list1,list2)
            a = len(list1) - len(list2)
            b = len(list1) - a
            for i in list1[b:]:
                zipperList.append(i)
        if len(list1) < len(list2):
            zipperList = merge(list1, list2)
            a = len(list2) - len(list1)
            b = len(list2) - a
            for j in list2[b:]:
                zipperList.append(j)
    return zipperList