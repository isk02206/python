'''
Created on 2018. 11. 30
@Subject : snowball_numbers
@Author : Son Jee Hun
@Student Number : 01406444
'''
def letterDistribution(sentence):
    '''
    >>> letterDistribution('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE')
    {'U': 7, 'I': 11, 'T': 10, 'L': 6, 'O': 5, 'Q': 2, 'N': 13, 'E': 14, 'D': 9, 'A': 1, 'R': 12, 'F': 4, 'H': 8, 'Y': 3}
    >>> letterDistribution('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE')
    {'W': 3, 'V': 4, 'U': 6, 'I': 7, 'T': 8, 'A': 2, 'O': 4, 'Q': 1, 'N': 7, 'E': 9, 'D': 8, 'R': 6, 'S': 1, 'F': 5, 'H': 5, 'Y': 3, 'L': 2}
    >>> letterDistribution('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND')
    {'W': 1, 'X': 2, 'V': 3, 'U': 5, 'I': 9, 'T': 7, 'A': 2, 'O': 3, 'Q': 1, 'N': 9, 'E': 9, 'D': 8, 'R': 6, 'S': 5, 'F': 3, 'H': 5, 'Y': 3, 'L': 4}
    '''
    dictionary = {}
    for word in sentence:
        if not word.isalpha():
            continue
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
# print(letterDistribution('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE'))
# print(letterDistribution('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE'))
# print(letterDistribution('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND'))

def snowball(sentence):
    '''
    >>> snowball('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE')
    True
    >>> snowball('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE')
    False
    >>> snowball('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND')
    False
    '''
    snowball_number = '1234567891011121314'
    matching_number = ''
    observations = letterDistribution(sentence)
    numbers = sorted(list(observations.values())) # sorting number
    for number in numbers:
        matching_number += str(number) #
    if int(snowball_number) == int(matching_number):
        return True
    return False

# print(snowball('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE'))
# print(snowball('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE'))
# print(snowball('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND'))

def pyramid(sentence):
    '''
    >>> pyramid('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE')
    False
    >>> pyramid('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE')
    True
    >>> pyramid('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND')
    False
    '''
    pyramid_number = '11223344556677889' # twice number without highest number
    matching_number = ''
    observations = letterDistribution(sentence)
    numbers = sorted(list(observations.values()))  # sorting number
    for number in numbers:
        matching_number += str(number)
    if int(pyramid_number) == int(matching_number):
        return True #pyramid_number = matching_number
    return False
# print(pyramid('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE'))
# print(pyramid('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE'))
# print(pyramid('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND'))

def pi(sentence):
    '''
    >>> pi('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE')
    False
    >>> pi('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE')
    False
    >>> pi('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND')
    True
    '''
    pi_number = '314159265358979323'
    pi_number_list = sorted([x for x in pi_number]) # make list pi_number
    sort_pi_number = ''
    for number in pi_number_list:
        sort_pi_number += number # make string sorting pi number
    matching_number = ''
    observations = letterDistribution(sentence)
    numbers = sorted(list(observations.values()))  # sorting number
    for number in numbers:
        matching_number += str(number)
    if int(sort_pi_number) == int(matching_number):
        return True #sort pi number == matching number
    return False

# print(pi('THREE HUNDRED THIRTEEN QUINTILLION THREE HUNDRED FORTY QUADRILLION THREE HUNDRED FIFTY TRILLION FOUR HUNDRED NINETY-NINE'))
# print(pi('TWO HUNDRED TWENTY-FOUR QUADRILLION FIVE HUNDRED TWENTY-FIVE THOUSAND FIVE HUNDRED THIRTY-FIVE'))
# print(pi('FIVE HUNDRED TWENTY QUADRILLION SIX HUNDRED THIRTY-SIX TRILLION SEVEN HUNDRED FIFTY-SEVEN THOUSAND'))

if __name__ == '__main__':
    import doctest
    doctest.testmod()