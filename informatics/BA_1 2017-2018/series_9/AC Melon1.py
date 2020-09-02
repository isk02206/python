def pattern(word):
    result = ''
    vowel = 'aeiouAEIOU'
    for letter in word:
        if letter in vowel:
            result += '_'
        else:
            result += letter
    return result

def bloopers(text,occurrences=1,length=1):
    reader = open(text, 'r')
    bloop = {}
    for word in reader:
        key = pattern(word).rstrip()
        if key not in bloop:
            bloop[key] = set()
        bloop[key].add(word.rstrip())
    delete = []
    for key in bloop.keys():
        if len(key) < length:
            delete.append(key)

        elif len(bloop[key]) < occurrences:
            delete.append(key)

    for k in delete:
        del bloop[k]

    return bloop