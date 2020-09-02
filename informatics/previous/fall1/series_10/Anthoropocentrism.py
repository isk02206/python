from math import floor
class WordSquare:
    def __init__(self, num, string):
        self.num = num
        self.string = string.upper()
        assert len(self.string)==(self.num*(self.num+1))//2, 'invalid square'
    
    def letter(self, row, column):
        self.row = row
        self.column = column
        assert self.row and self.column in range(self.num), 'invalid index'
        if self.row < self.column:
            self.row, self.column = self.column, self.row
        return self.string[self.row*(self.row+1)//2 + self.column]
    
    def word(self, number):
        assert number in range(self.num), 'invalid index'
        group_word = ''
        for g in range(self.num):
            group_word += self.letter(number, g)
        return group_word
    
    def __str__(self):
        group_str = ''
        for i in range(self.num):
            group_str += self.word(i) + '\n'
        return group_str.rstrip()
    
    def valid(self, text):
        reader = open(text, 'r')
        data = reader.read()
        data = data.split('\n')
        
        for o in range(self.num):
            word = self.word(o).lower()
            if word in data:
                pass
            else:
                return False
        return True