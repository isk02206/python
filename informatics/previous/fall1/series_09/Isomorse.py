def morsecodes(text):
    reader = open(text, 'r')
    data = reader.readlines()
    
    codes = {}
    for code in data:
        code = code.split()
        key,value = code[0],code[-1]
        codes[key] = value
    return codes

codes = morsecodes('morse.txt')

def pattern(name, codes, complement=False, mirror=False):
    result = ''
    for letter in name:
        result+=codes[letter]
    
    if complement == True:
        result_c = ''
        for r in result:
            if r == '-':
                result_c += '.'
            elif r == '.':
                result_c += '-'
        result = result_c
        
    if mirror == True:
        result_m = result[-1::-1]
        result = result_m
    return result


def isomorse(name_1,name_2,codes,complement=False,mirror=False):
    code_1 = pattern(name_1,codes,complement=complement,mirror=mirror)
    code_2 = pattern(name_2,codes)
    
    if code_1 == code_2:
        return True
    else:
        return False


def groups(text_1, text_2):
    codes = morsecodes(text_2)
    reader = open(text_1, 'r')
    data = reader.readlines()
    
    group = {}
    for d in data:
        d = d.split()
        key=d[0]
        value=pattern(d[0],codes,complement=False,mirror=False)
        group[key] = value
    
    result = {}
    
    final = []
    for v in group.values():
        
        final = []
        for k in group.keys():
            if v == pattern(k,codes,complement=False,mirror=False):
                final.append(k)
                result.update({v:set(final)})
    return result