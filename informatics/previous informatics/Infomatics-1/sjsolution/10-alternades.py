
class Alternade:
    def __init__(self, words):
        
        if isinstance(words, str):
            self.words = [words]
        
        elif isinstance(words, list):
            self.words = list(words)
        
    def __repr__(self):
        
        if len(self.words) == 1:    
            return "Alternade('{}')".format(self.words[0])
        
        else:
            return "Alternade({})".format(self.words)
    
    def __add__(self, other):
        
        list2 = []
        
        for x in self.words:
            list2.append(x)
        for y in other.words: 
            list2.append(y)
        
        return Alternade(list2)
    
    def __str__(self):
        
        result = ''
        
        count = 0
        
        list1 = []
        
        for x in self.words:
            
            list1.append(len(x))
        
        maxlength = max(list1)
        
        while self.words:
            
            for x in range(len(self.words)):
                
                if count < (len(self.words[x])):
                    
                    result += self.words[x][count]
                    
                else:
                    pass
                
            count += 1

            if count == maxlength:
                break
            
        return result
            

words = ['COLD']
word2 = Alternade(words)
word2.words
print(id(word2.words))
print(id(words))
print(id(words) != id(word2.words))