class CardDressage:
    def __init__(self,row,column= None):
        if column != None:
            self.x = row
            self.y = column
        else:
            self.x = row
            self.y = row 
        card = ''
        count = 0
        while count < self.x:
        
            card += '#'*self.y + '\n'
            count += 1
        self.card = card
   
    def __repr__(self):   
        return self.card
    
    def __str__(self):
        
        return self.__repr__()
    
    def turnCard(self,num):
        list1 = self.__str__().split()
        list2 = []
            
        for line in list1:
            list2.append(list(line))
            print(list2)




game = CardDressage(5, 3)
print(game.turnCard(2))