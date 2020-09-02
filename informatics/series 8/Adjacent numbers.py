def listRepresentation(word, list_length):
    assert len(word) % list_length == 0, 'invalid string representation'
    word_list = []
    result = []
    for i in word:
        word_list.append(int(i))
        if len(word_list) == list_length:
            result.append(word_list)
            word_list = []
    return result

# print(listRepresentation('1541253263631421', 5))
# print(listRepresentation('111222333', 3))
# print(listRepresentation('123321123', 3))
# print(listRepresentation('424313424', 3))
# print(listRepresentation('1541253263631421', 4))
def neighbours(row, coulmn, matrix):
    assert row < len(matrix), 'invalid position'
    assert coulmn < len(matrix[0]), 'invalid position'
    result = []
    for i in range(3):

        for j in range(3):
            if i == 1 and j == 1:
                continue
            if row-1+i > len(matrix) - 1 or coulmn-1+j > len(matrix[0]) - 1:
                continue
            elif row-1+i < 0 or coulmn-1+j < 0:
                continue

            result.append(matrix[row-1+i][coulmn-1+j])

    return set(result)
# print(neighbours(1, 4, [[3, 4, 5, 6, 4, 5, 3], [1, 2, 1, 3, 2, 1, 2], [3, 4, 5, 6, 4, 5, 3]]))
# print(neighbours(1, 1, [[4, 3], [2, 3], [1, 2], [8, 1], [6, 6]]))
# print(neighbours(4, 3, [[4, 3, 6, 4, 3], [2, 1, 5, 2, 1], [5, 7, 8, 7, 5], [4, 3, 6, 4, 3], [2, 1, 5, 2, 1]]))
# print(neighbours(2, 2, [[1, 5, 4, 1], [2, 5, 3, 2], [6, 3, 6, 3], [1, 4, 2, 1]]))
# print(neighbours(2, 3, [[1, 5, 4, 1], [2, 5, 3, 2], [6, 3, 6, 3], [1, 4, 2, 1]]))
# print(neighbours(0, 0, [[1, 5, 4, 1], [2, 5, 3, 2], [6, 3, 6, 3], [1, 4, 2, 1]]))
# print(neighbours(4, 4, [[1, 5, 4, 1], [2, 5, 3, 2], [6, 3, 6, 3], [1, 4, 2, 1]]))

def isAdjacent(word, list_length):
    matrix = listRepresentation(word, list_length)
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if set([k for k in range(1, matrix[i][j])]) - neighbours(i, j, matrix) != set():
                count += 1

    if count == 0:
        return True
    return False
            #     return False
            # if set([k for k in range(1, matrix[i][j])]) - neighbours(i, j, matrix) == set():
            #     return True
            #print(set([k for k in range(1, matrix[i][j])]) - neighbours(i, j, matrix))
                #print(neighbours(i, j, matrix))
                #print(matrix[i][j])
                #print([k for k in range(1, matrix[i][j])])
    #print(matrix[0].index(1))

print(isAdjacent('313424', 3))
print(isAdjacent('111222333', 3))
print(isAdjacent('123321123', 3))
print(isAdjacent('424313424', 3))
print(isAdjacent('1541253263631421', 4))
print(isAdjacent('1541253263631421', 5))