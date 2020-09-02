class Alternade:
    #필요한 variable을 준바함ㅁ
    #return 하면 안됨
    def __init__(self, words):
        
        if isinstance(words, str):
            
            self.words = [words]
            
        elif isinstance(words, list):
            
            self.words = list(words)
    #이 class 자체가 나타내는지 나오는것  without print
    def __repr__(self):
        
        if len(self.words) == 1:
            
            return "Alternade('{}')".format(self.words[0])
        
        else:
            return 'Alternade({})'.format(self.words)

    #add 같은 경우에는 return 으로 나와야 한다    
    #e.g) other = alternade+ numbers
    def __add__(self, other):
        
        list = []
        
        for x in self.words:
            list.append(x)
            
        for y in other.words:
            list.append(y)
            
        return Alternade(list)
     #print the class 했을떄 나오는 값   
    def __str__(self):
        
        result = ''
        count = 0
        
        maxlen = len(max(self.words, key=len))
        
        while True:
            
            for x in self.words:
                
                if count < len(x):
                
                    result += x[count]
                else:
                    pass
                
            count += 1
            
            if count == maxlen:
                break
            
        return result
            
print(Alternade('shoe'))

word4 = Alternade('DEMO') + Alternade('RABAT')

print(word4)