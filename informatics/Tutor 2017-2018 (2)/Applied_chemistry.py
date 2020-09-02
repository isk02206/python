'''
Created on 2018. 7. 4.

@author: TaeWoo
'''

import string

def isValid(symbol, chemical, length=False):
    
    # lowercase = map(chr, range(97, 123))
    # uppercase = map(chr, range(65, 91))
    # Import uppercase letter
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    
    # First letter of symbol must be uppercase
    if symbol[0] not in uppercase:
        return False
    
    # Beside from first letter all letters should be lowercase
    for letter in symbol[1:]:
        if letter not in lowercase:
            return False
    
    #Make sure all letters are lowercase
    symbol = symbol.lower()
    chemical = chemical.lower()
    
    # Make list containing each letter of chemical
    letters = list(chemical)
    
    # If optional parameter is given, check whether length of symbol is equal to given length
    if length is not False and len(symbol) != length:
        return False
    
    counter = 0
    
    # Check whether symbol is valid
    for letter in symbol:
        # if letter in symbol is in chemical
        if letter in letters:
                    
            # Discard all letter(s) from chemical that comes before the letter
            letters = letters[letters.index(letter)+1:]
            counter += 1
    
    # If all letters from symbol is valid
    if len(symbol) == counter:
        return True
    
    # If is not valid
    return False

def symbols(chemical):
    
    # Empty set which will contain symbol generated from chemical name
    possible_symbols = set()
    
    # Set for loop to define first letter
    for start in range(len(chemical) - 1):
        
        # This will be starting letter of the symbol (Make sure it is uppercase letter)
        start_letter = chemical[start].upper()
        
        # Set for loop to define second letter
        for end in range(start+1, len(chemical)):
            
            # Generate symbol with two letter and add it to set
            possible_symbols.add(start_letter + chemical[end])

    return possible_symbols

def preference(chemical, last=False):
    
    # Using function symbol to generate possible symbols and range them in alphabetical order
    possible_symbols = sorted(symbols(chemical))
    
    # If optional parameter last is given as True, it will return last symbol from the list
    if last is True:
        return possible_symbols[-1]
    
    # If optional parameter is not given, it will return first symbol from the list
    return possible_symbols[0]

print(isValid('ZeR', 'Zeddemorium'))
print(preference('Iron', True))