class ISBN13:
    def __init__(self, code, length=1):
        
        
        self.code = code
        self.length = length
    
        assert isinstance(self.code, int)
        assert len(str(self.code)) == 13 
        assert 1 <= length <= 5 
    def __str__(self):
        
        code = str(self.code)
        a = code[:3]
        b = code[3:3+self.length]
        c = code[3+self.length:-1]
        d = code[-1]
        
        return '{}-{}-{}-{}'.format(a,b,c,d)
    
    def __repr__(self):
        
        return 'ISBN13({}, {})'.format(str(self.code), str(self.length))

    def isValid(self):
        code = str(self.code)
        count = 0
        for x in range (12):
            if x%2:
                count += 3*int(code[x])
            else:
                count += int(code[x])
            
        count = ((10-(count % 10))%10)
        
        return count == int(code[12])
    
    def asISBN10(self):
        if self.isValid() == False or str(self.code)[:3] != '979':
            return None
        else:
            code = str(self.code)[3:-1]
            count = 0
            for x in range (9):
                count += int(code[x]) * (x+1)
            count = count % 11
            if count == 10:
                count = 'X'
            else:
                count = str(count)
            a = code[:self.length]
            b = code[self.length:]
            c = count   
            
            return '{}-{}-{}'.format(a,b,c)
                