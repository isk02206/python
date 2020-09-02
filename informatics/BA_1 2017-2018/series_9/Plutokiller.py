def coordinates(text):
    reader = open(text, 'r')
    row, col = 0, 0
    place = []
    for line in reader:
        line = line.rstrip()
        for i in line:
            a = (col, row)
            row += 1
            if '-' is not i:
                place.append(a)
        row = 0
        col += 1
    return set(place)

def divergence(text1, text2):
    return (coordinates(text1)-coordinates(text2), coordinates(text2)-coordinates(text1))

def calcul(first, second):
    return (first[0] - second[0])**2 + (first[1] - second[1])**2

def planets(text1, text2):
    text, dict = divergence(text1, text2), {}

    for key in text[1:]:

        for i in text[:1]:

            for key1 in key:
                min_d = None
                position = set()
                for value in i:
                    a = calcul(key1, value)
                    if min_d is None or a < min_d:
                        min_d = a
                        position = {value}
                    if a == min_d:
                        position.add(value)
                dict[key1] = position
    if dict.values() == {}:
        dict.values = set()
    return dict

def comparator(text1, text2):
    reader1, reader2 = open(text1, 'r'), open(text2, 'r')
    candidate = ''
    for line1, line2 in zip(reader1, reader2):
        line1 = line1.rstrip()
        line2 = line2.rstrip()
        for i in range(0, len(line1)):
            a = line1[i]
            b = line2[i]
            if a == '*' and b == '*':
                candidate += '*'
            elif a == '*' and b == '-':
                candidate += 'o'
            elif a == '-' and b == '*':
                candidate += 'n'
            else:
                candidate += '-'
        candidate += '\n'
    return candidate.rstrip()