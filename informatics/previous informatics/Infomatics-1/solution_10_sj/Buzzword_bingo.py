class BuzzBingo():
    
    def __init__(self, n, list1):
        assert n*n == len(list1),
        #정사각형이라 row와 column이 같다
        self.row = n
        self.column = n
        
        grid = ''
        #make the grid  
        for x in range(n):    
            grid += '-'*n + '\n'
        #마지막 '\ㅜ'를 읽지 않기 위해서    
        grid = grid[:-1]
        #for __repr__
        self.grid = grid
        
        list2 = []
        word_grid = []
        
        for word in list1:
            #list안에 list를 만든다
            list2.append(word)
            
            if len(list2) == n:
                #큰list안에 작은 list를 더한다
                word_grid.append(list2)
                list2 = []
                
        self.word_grid = word_grid
        
    def __repr__(self):
        
        return self.grid
    
    def __str__(self):
        
        return self.__repr__()
    