class DrunkenAnt:
    def __init__(self, text):
        reader = open(text, 'r')
        data = reader.readlines()
        data = ''.join(data).strip('\n').replace(' ', '').split('\n')
        lis = []
        for x in data:
            lis.append(list(x))

        self.lis = lis
        self.row = len(self.lis) - 1
        self.column = 0
    def position(self):
        return self.row, self.column
        
    def step(self):
        lis = self.lis
        row = self.row
        column = self.column
        if lis[row][column] == '^':
            lis[row][column] = '>'
            if row - 1 >= 0 :
                row -= 1
        elif lis[row][column] == 'v':
            lis[row][column] = '<'
            if row + 1 < len(lis):
                row += 1
        elif lis[row][column] == '<':
            lis[row][column] = '^'
            if column != 0:
                column -= 1
        elif lis[row][column] == '>':
            lis[row][column] = 'v'
            if column != len(lis[0]) - 1:
                column += 1
        
        self.lis = lis
        self.row = row
        self.column = column
        return row, column
    
    def steps(self):
        lis = self.lis
        row = self.row
        column = self.column
        LIS = [(row, column)]
        while True:
            if lis[row][column] == '^':
                lis[row][column] = '>'
                if row - 1 >= 0 :
                    row -= 1
            elif lis[row][column] == 'v':
                lis[row][column] = '<'
                if row + 1 < len(lis):
                    row += 1
            elif lis[row][column] == '<':
                lis[row][column] = '^'
                if column != 0:
                    column -= 1
            elif lis[row][column] == '>':
                lis[row][column] = 'v'
                if column != len(lis[0]) - 1:
                    column += 1
            LIS.append((row, column))
            if row == 0 and column == len(lis[0]) - 1:
                self.row = row
                self.column = column
                break
        return LIS
    
    def __repr__(self):
        lis = self.lis
        result = []
        for x in lis:
            result += x 
            result.append('\n')
        
        answer = ''
        point = 0
        while True:
            if result[point] == '\n' or result[point + 1] == '\n':
                answer += result[point]
            else:
                answer += result[point] + ' '
            point += 1
            if point == len(result):
                break
        return answer.strip('\n')
    
    def __str__(self):
        lis = self.lis
        row = self.row
        column = self.column
        result = []
        STR = lis[row][column]
        lis[row][column] = '*'
        for x in lis:
            result += x 
            result.append('\n')
        answer = ''
        for x in result:
            if x != '\n':
                answer += ' ' + x + ' '
            else:
                answer += x
        answer = list(answer.strip('\n'))
        point = 0
        while True:
            if answer[point] == '*':
                answer[point + 1] = ']'
                answer[point - 1] = '['
                answer[point] = STR
            point += 1
            if point == len(answer):
                break
        
        return ''.join(answer)

if __name__ == '__main__':
    import doctest
    doctest.testmod()