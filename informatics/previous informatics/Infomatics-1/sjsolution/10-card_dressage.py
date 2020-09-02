class CardDressage:
    def __init__(self, row, column = None):
        
        if column != None:
            self.x = row
            self.y = column
        
        else:
            self.x = row
            self.y = row
        
        card = ''
        
        for count in range(self.x):
        
            card += '#'*self.y + '\n'
        
        self.card = card
    
        
    def __repr__(self):
        
        
        return self.card[:-1]
    
    def __str__(self):
        
        return self.__repr__()
    
    def turnCard(self, pos):
        
        self.pos = pos
        
        if pos > (self.x * self.y):
            raise AssertionError('invalid card number')
        
        else:
            list1 = self.__str__().split()
            list2 = []
            
            for line in list1:
                list2.append(list(line))
            
            
            row_pos, column_pos = (pos//self.y) , pos % self.y
            
            if pos % self.y == 0:
                
                row_pos = row_pos -1
            
                column_pos = column_pos + self.y
            
            if list2[row_pos][column_pos - 1] == '#':
                list2[row_pos].pop(column_pos- 1)
                list2[row_pos].insert(column_pos - 1, '-')
            elif list2[row_pos][column_pos - 1] == '-':
                list2[row_pos].pop(column_pos- 1)
                list2[row_pos].insert(column_pos - 1, '#')
                
            
            if row_pos -1 >= 0:
                if list2[row_pos - 1][column_pos - 1] == '#':
                    list2[row_pos -1 ].pop(column_pos-1)
                    list2[row_pos - 1].insert(column_pos -1, '-' )
                    
                elif list2[row_pos - 1][column_pos - 1] == '-':
                    list2[row_pos - 1].pop(column_pos- 1)
                    list2[row_pos - 1].insert(column_pos - 1, '#')
                    
            
            if row_pos +1 < self.x:
                if list2[row_pos + 1][column_pos - 1] == '#':
                    list2[row_pos + 1 ].pop(column_pos - 1)
                    list2[row_pos + 1].insert(column_pos - 1, '-' )
                    
                elif list2[row_pos + 1][column_pos - 1] == '-':
                    list2[row_pos + 1].pop(column_pos -  1)
                    list2[row_pos+ 1].insert(column_pos - 1, '#')
            
            if column_pos < self.y:
                if list2[row_pos][column_pos] == '#':
                    list2[row_pos].pop(column_pos)
                    list2[row_pos].insert(column_pos, '-')
                elif list2[row_pos][column_pos] == '-':
                    list2[row_pos].pop(column_pos)
                    list2[row_pos].insert(column_pos, '#')
                
            
            if column_pos -2 >= 0:
                if list2[row_pos][column_pos - 2] == '#':
                    list2[row_pos].pop(column_pos- 2)
                    list2[row_pos].insert(column_pos - 2, '-')
                elif list2[row_pos][column_pos - 2] == '-':
                    list2[row_pos].pop(column_pos- 2)
                    list2[row_pos].insert(column_pos - 2, '#')
            
            result = ''
                    
            for line2 in list2:
                for z in line2:
                    result += str(z)
                result += '\n'
        
            self.card = result
            
            return self.card[:-1]
    def turnCards(self, list3):
        
        for x in list3[:-1]:
            self.turnCard(x)
            
        self.turnCard(list3[-1])
        
    def won(self):
    
        check = self.card.replace('\n','')
        
        for x in check:
            if x != '-':
                return False
        else:
            return True
    
    