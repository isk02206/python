import random
def check_length(colors, fruits):
    if len(colors) > len(fruits):
        length = len(fruits)
    elif len(colors) < len(fruits):
        length = len(colors)
    elif len(colors) == len(fruits):
        length = len(colors)
    return length
def combine(colors, fruits, amount=None):
    result = []
    colors = list(colors)
    fruits = list(fruits)
    if amount is None:
        amount = check_length(colors, fruits)
        for i in range(amount):
            word1 = random.choice(colors)
            word2 = random.choice(fruits)
            new_word = 'a ' + word1 + ' ' + word2
            result.append(new_word)
            colors.remove(word1)
            fruits.remove(word2)
        return result
    else:
        if amount > len(colors):
            amount = check_length(colors, fruits)
        for i in range(amount):
            word1 = random.choice(colors)
            word2 = random.choice(fruits)
            new_word = 'a ' + word1 + ' ' + word2
            result.append(new_word)
            colors.remove(word1)
            fruits.remove(word2)
        return result
print(combine(['purple', 'yellow', 'green'], ('grape', 'banana', 'apple'), amount=4))