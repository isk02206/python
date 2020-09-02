def translate(gender,translations):
    '''
    >>> translations = {'he':'she', 'brother':'sister'}
    >>> translate('he', translations)
    'she'
    >>> translate('HE', translations)
    'SHE'
    >>> translate('He', translations)
    'She'
    >>> translate('brother', translations)
    'sister'
    >>> translate('my', translations)
    'my'
    '''
    pos = 0
    for x in gender:
        if
    if gender.lower() in translations:
        if gender in translations:
            return translations[gender]
        if gender not in translations:
            letter = []
            for i in gender:
                if i.isupper() == True:
                    letter.append(1)
                if i.islower() == True:
                    letter.append(0)
            if letter[0] == 1 and letter[1] == 0 :
                x = translations[gender.lower()]
                x = x[0].upper() + x[1:]
            if letter[0] == 1 and letter[1] == 1:
                x = translations[gender.lower()]
                x = x.upper()
        return x

    if gender.lower() not in translations:
        return gender

def sexChange(statement,translations):
    '''
    >>> translations = {'he':'she', 'brother':'sister'}
    >>> sexChange('He is my brother.', translations)
    'She is my sister.'
    '''
    words = []
    word = ''
    for i in range(len(statement)):
        if statement[i] !=' ':
            word += statement[i]
        if statement[i] == ' ':
            words.append(word)
            word = ''
    new_statement = []
    for j in words:
        new = translate(j,translations)
        new_statement.append(new)
    new_statement = ' '.join(new_statement)
    new_statement = new_statement.rstrip()
    return new_statement