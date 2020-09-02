class phoneword:
    def __init__(self, word):
        self.letters = {'a' : 2, 'b' : 2, 'c' : 2,
                        'd' : 3, 'e' : 3, 'f' : 3,
                        'g' : 4, }
        self.word = word.lower()
    def key(self):
        phone = ''
        for letter in self.word:
            phone += str(self.letters[letter])
        return phone

phone_1 = phoneword('flowers')
print(phone_1.key())
