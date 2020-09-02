def encodeLetter(letter, number, lang):
    letter = letter.lower()
    lang = lang.lower()
    return lang.find(letter) + number + 1

def encodeWord(word, number, lang):

    result = ''
    for x in word:
        result += str(encodeLetter(x, number, lang))
    return int(result)