from math import floor
class WordSquare:
    def __init__(self, order, words):
        self.order = order
        self.words = words.upper()
        assert len(self.words)==(self.order*(self.order+1))//2, str('invalid square')
    
    def letter(self, row, column):
        self.row = row
        self.column = column
        assert self.row in range(self.order) and self.column in range(self.order), str('invalid index')
        if self.row < self.column:
            self.row, self.column = self.column, self.row
        orders = self.row*(self.row+1)//2 + self.column
        return self.words[orders]
    
    def word(self, line):
        assert line in range(self.order), str('invalid index')
        return ''.join(self.letter(line, i) for i in range(self.order))
    
    def __str__(self):
        return '\n'.join(self.word(i) for i in range(self.order))
    
    def valid(self, text):
        reader = open(text, 'r')
        data = reader.read()
        data = data.split("\n")
        
        for j in range(self.order):
            if self.word(j).lower() in data:
                pass
            elif self.word(j).lower() not in data:
                return False
        return True
        

square = WordSquare(3, 'bicten')
print(square.letter(1, 2))
print(square)
print(square.valid('words.txt'))