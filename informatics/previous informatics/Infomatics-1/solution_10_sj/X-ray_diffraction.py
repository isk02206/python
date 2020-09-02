#while roof ������ lew line���� �����
#len(board)�� ����
#count �� place�� ���������� new���ٰ�slash�߰�
#r.strip = �����ʿ��ִ°� �������
class Molecule:
    
    def __init__(self, row, column):
        
        grid = []
        board = ''
        
        for x in range(row):
            
            grid.append(('. ' * column)[:-1])
        
        for list1 in grid:
            board += list1
        
        self.row = row
        self.column = column    
        self.board = board
        self.grid = grid
        
        
    def atom(self, pos, forward = True):
        
        x,y = pos
        
        if forward:
            slash = '\\'
            
        else:
            slash = '/'
        
        board = self.board
        
        board = board.replace(' ','')
        
        place = x*self.column + y
        
        assert place <= (self.column*self.row), 'invalid position'
        
        counter = 0
        
        new = ''
        
        while counter != len(board):
            
            if place != counter:
               new += board[counter]
               
            else:
                new += slash
                
            counter += 1
            
        grid = ''  
        line = ''
        
        for char in new:
            
            line += char + ' '
            
            if len(line) == (self.column*2)-1:
                
                grid += line[:-1] + '\n'
                
                line = ''
            
        self.grid = grid.rstrip('\n')
        
    def atoms(self, list1):
        
        for pos in list1:
            
            self.atom(pos)
    
    def __str__(self):
        
        return self.grid