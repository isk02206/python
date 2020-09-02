'''
Created on 2016. 2. 5.

@author: User
'''

def onlyletters(word):
    
    """
    >>> onlyletters('what?')
    'what'
    >>> onlyletters('"now!"')
    'now'
    >>> onlyletters('?+="word!,@$()"')
    'word'
    """
   
    result = []
    for x in word:
        if x.isalpha():
            result.append(x)
    return ''.join(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
