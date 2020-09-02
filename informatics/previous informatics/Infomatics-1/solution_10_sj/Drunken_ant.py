class DrunkenAnt:
    
    #필요항것들을 준비한다
    def __init__(self, textfile):
        #open and read textfile
        reader = open(textfile, 'r').read().split('\n')
        #remove space
        list1 = []
        
        for x in reader:
            #remove the space
            list1.append(x.replace(' ',''))
        #start position 
        row = len[list1[0]]-1
        column = 0
        
        self.row = row
        self.column = column
        
        grid = open(textfile, 'r')
        
        self.grid = grid
        
    def position(self):
        
        return self.row,self.column
    #class가 있을떄 나오는값
    def __repr__(self):
        
        return self.grid
    