class Cowsay:
    def __init__(self, ST, text = 'cow.cow', eyes = 'oo'):
        self.text = text
        self.eyes = eyes
        self.ST = ST
        lis = []
        for x in self.ST:
            lis.append(len(x))
        lis.sort()
        maxi = lis[-1]
        w = ''
        w += '+' + '-' * (maxi +2 ) + '+' + '\n'
        for x in self.ST:
            w += '|' + x.center(maxi + 2, ' ') + '|' + '\n'
        w += '+' + '-' * (maxi +2 ) + '+'
        self.w = w        
    def __repr__(self):
        return self.w 
    
    def setEyes(self, eyes = 'oo'):
        assert (len(str(eyes)) == 2), "invalid eyes" 
        assert (type(eyes) == str), "invalid eyes"
        self.eyes = eyes
        
    def setImage(self, text = 'cow.cow'):
        self.text = text
        
    def __str__(self):
        reader = open(self.text, 'r')
        data = reader.readlines()
        self.data = data
        V = ''
        for x in data:
            if '{}' in x:
                x = x[:x.index('{}')] + self.eyes[0] + x[x.index('{}')+2 :]
                x = x[:x.index('{}')] + self.eyes[1] + x[x.index('{}')+2 :]
            V += x
        self.V = V
        Z = self.w + '\n' + V
        self.Z = Z
        return self.Z.strip('\n')
        
        
a = Cowsay(['Moo may represent an idea,', 'but only the cow knows.'])

print(a.setEyes('^^'))