def isZigzag(list_or_tuple):
    for count in range(0, len(list_or_tuple)-1):
        if count % 2 == 0 and list_or_tuple[count] < list_or_tuple[count + 1]:
            type = False
            break
        if count % 2 == 1:
            if list_or_tuple[count] > list_or_tuple[count -1]:
                type = False
                break
            if list_or_tuple[count] > list_or_tuple[count + 1]:
                type = False
                break
        else:
            type = True

    return type
# print(isZigzag([-11, -32, 49, 9, 100, 55, 43, -33, 46]))
# print(isZigzag([10, 5, 6, 3, 2, 20, 100, 80]))
# print(isZigzag((10, 5, 6, 2, 20, 3, 100, 80)))
# print(isZigzag([20, 5, 10, 2, 80, 6, 100, 3]))


def zigzagSlow(seq):
    seq.sort()
    for count in range(0, len(seq)-1):
        if count % 2 == 0:
            seq[count], seq[count+1] = seq[count+1], seq[count]

#print(zigzagSlow(([10, 90, 49, 2, 1, 5, 23])))

seq = [10, 90, 49, 2, 1, 5, 23]
zigzagSlow(seq)
print(seq)

def zigzagFast(seq):
    for count in range(0, len(seq)-1):
        if count % 2 == 0:
            if seq[count] < seq[count-1] and count != 0:
                seq[count-1], seq[count] = seq[count], seq[count-1]
                #print(seq)

            if seq[count] < seq[count+1]:
                seq[count], seq[count+1] = seq[count+1], seq[count]
                #print(seq)
        if count % 2 == 1:
            if seq[count] > seq[count + 1]:
                seq[count], seq[count + 1] = seq[count + 1], seq[count]
    #return seq
    #print(seq)
#print(zigzagFast([10, 90, 49, 2, 1, 5, 23]))
#print(zigzagFast([79, 68, 73, -27, 16, -3, 45, 62, -12, -13, 35, 49, -31]))