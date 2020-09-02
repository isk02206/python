def volumes(represent_partitioning):
    new_list = []
    new_list_2 = []
    import string
    upper_case_alphabet = string.ascii_uppercase
    assert type(represent_partitioning) == tuple, 'invalid partitioning'
    count = 0
    volume_check = 0
    for j in represent_partitioning:
        volume_check += j
    assert volume_check == 26, 'invalid partitioning'
    assert j > 0, 'invalid partitioning'

    for i in represent_partitioning:

        new_list = list()

        if i == 1:
            new_list_2.append(upper_case_alphabet[count])
            count += i
            continue

        new_list.append(upper_case_alphabet[count])
        count += i
        new_list.append(upper_case_alphabet[count-1])
        new_list_2.append('-'.join(new_list))
    assert volume_check == 26, 'invalid partitioning'
    #print(new_list_2)

    return ' '.join(new_list_2)

# print(volumes((9, 7, 10, 0)))
# print(volumes((10, 7, 10, -1)))
# print(volumes('A-D E-J K-O P-Z'))
# print(volumes(42))
# print(volumes((26,)))
# print(volumes((4, 6, 5, 11)))
# print(volumes((7, 8, 1, 10)))
# print(volumes((4, 7, 5, 10)))
# print(volumes((8, 3, 9, 7)))

def counts(word):
    assert type(word) == str, 'invalid partitioning'
    import string
    upper_case_alphabet = string.ascii_uppercase
    new_list = []
    result = []
    list_2 = []
    remove_word = word.split()
    #print(remove_word)
    for l in remove_word:
        #print(l)
        list_2.append(l[0])

    #print(list_2)
    string_remove_word = ''.join(remove_word).replace('-', '')
    assert string_remove_word[0] == 'A', 'invalid partitioning'
    #print(string_remove_word)
    ord_list = []
    for k in range(1, len(string_remove_word) - 1):
        #print(k)
        #print(ord(string_remove_word[k]))
        ord_list.append(ord(string_remove_word[k]))
    #print(ord_list)
    #for l in range(len(ord_list)):
        #assert ord_list[l] + 1 == ord_list[l+1], 'invalid partitioning'

    #print(ord_list)
    count = 0
    for i in remove_word:
        #print(i[-1])
        new_list.append(upper_case_alphabet.index(i[-1])+1)

    #print(new_list)
    for j in new_list:
        #print(j)
        assert j-count > 0, 'invalid partitioning'
        result.append(j - count)
        count = j

    count_2 = 0
    check_list = []
    for k in result:
        check_list.append(upper_case_alphabet[count_2])
        count_2 += k
    assert count_2 == 26, 'invalid partitioning'
    #print(check_list)
    #print(result)
    assert check_list == list_2, 'invalid partitioning'
    return tuple(result)

# print(counts('A-D F-K L-P Q-Z'))
# print(counts('B-C D-F G-H I-M N-Z'))
# print(counts(42))
# print(counts('A-D E-I'))
# print(counts('A-V W-O'))
# print(counts('A-D E-J K-O P-Z'))
# print(counts('A-G H-O P Q-Z'))
# print(counts('A-D E-K L-P Q-Z'))
# print(counts('A-D F-K L-P Q-Z'))

def delta(any_type, names):
    if type(any_type) == tuple:
        any_type = volumes(any_type)
    assert type(any_type) != int, 'invalid partitioning'
    count = 0
    for i in names:
        count += i
    #print(count)
    count = count / len(any_type.split())
    #print(count)
    sum_list = []
    count_2 = 0
    for j in counts(any_type):
        #print(j)
        sum_list.append(abs(count - sum(names[count_2:j + count_2])))
        count_2 += j
    #print(sum_list)
    return sum(sum_list[:])



# print(delta('A-D E-J K-O P-Z', (16, 4, 17, 10, 15, 4, 4, 6, 7, 14, 9, 17, 27, 6, 1, 9, 0, 12, 20, 8, 0, 3, 4, 0, 3, 4)))
# print(delta((7, 8, 1, 10), (16, 4, 17, 10, 15, 4, 4, 6, 7, 14, 9, 17, 27, 6, 1, 9, 0, 12, 20, 8, 0, 3, 4, 0, 3, 4)))
# print(delta('A-D E-K L-P Q-Z', (16, 4, 17, 10, 15, 4, 4, 6, 7, 14, 9, 17, 27, 6, 1, 9, 0, 12, 20, 8, 0, 3, 4, 0, 3, 4)))
# print(delta(42, (16, 4, 17, 10, 15, 4, 4, 6, 7, 14, 9, 17, 27, 6, 1, 9, 0, 12, 20, 8, 0, 3, 4, 0, 3, 4)))