class BuzzBingo():
    
    def __init__(self, n, list1):
        assert n*n == len(list1),
        #���簢���̶� row�� column�� ����
        self.row = n
        self.column = n
        
        grid = ''
        #make the grid  
        for x in range(n):    
            grid += '-'*n + '\n'
        #������ '\��'�� ���� �ʱ� ���ؼ�    
        grid = grid[:-1]
        #for __repr__
        self.grid = grid
        
        list2 = []
        word_grid = []
        
        for word in list1:
            #list�ȿ� list�� �����
            list2.append(word)
            
            if len(list2) == n:
                #ūlist�ȿ� ���� list�� ���Ѵ�
                word_grid.append(list2)
                list2 = []
                
        self.word_grid = word_grid
        
    def __repr__(self):
        
        return self.grid
    
    def __str__(self):
        
        return self.__repr__()
    