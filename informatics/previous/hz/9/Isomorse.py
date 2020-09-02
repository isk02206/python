def morsecodes(text):
    reader = open(text, 'r')
    data = reader.readlines()
    
    dict_1 = {}
    for d in data:
        d = d.split()
        key,value = d[0],d[1]
        dict_1[key] = value
    return dict_1

codes = morsecodes('morse.txt')

def pattern(word, codes, complement=False, mirror=False):
    code = ''
    for letter in word:
        code+=codes[letter]
    
    if complement == True:
        complement_code = ''
        for c in code:
            if c == '-':
                complement_code += '.'
            elif c == '.':
                complement_code += '-'
        code = complement_code
    if mirror == True:
        mirror_code = code[::-1]
        code = mirror_code
    return code


def isomorse(word_1, word_2, codes, complement=False, mirror=False):
    code_1 = pattern(word_1, codes)
    code_2 = pattern(word_2, codes, complement=complement, mirror=mirror)
    return code_1 == code_2


def groups(text_1, text_2):
    
    codes = morsecodes('morse.txt')
    reader_1 = open(text_1, 'r')
    data_1 = reader_1.readlines()
    
    dict_2 = {}
    for d in data_1:
        d = d.split()
        key=d[0]
        value=pattern(d[0],codes,complement=False,mirror=False)
        dict_2[key] = value
    
    result = {}
    group = []
    for w in dict_2.values():
        group = []
        for a in dict_2.keys():
            if w == pattern(a,codes):
                group.append(a)
                result.update({w:set(group)})
    return result
    
print(groups('words.txt', 'morse.txt'))