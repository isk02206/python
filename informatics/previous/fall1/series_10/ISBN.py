class ISBN13:
    def __init__(self, code, digit=1):
        self.code = str(code)
        self.digit = digit
    
    def __str__(self):
        return '{}'.format(self.code[:3]+'-'+self.code[3]+'-'+self.code[4:12]+'-'+self.code[12])
    
    def __repr__(self):
        return 'ISBN13({}, {})'.format(self.code, self.digit)
    
    def isValid(self):
        last_digit = int(self.code[12])
        cal = (10 - (int(self.code[0])+int(self.code[2])+int(self.code[4])+int(self.code[6])+int(self.code[8])+int(self.code[10]) + 3*(int(self.code[1])+int(self.code[3])+int(self.code[5])+int(self.code[7])+int(self.code[9])+int(self.code[11])))%10)%10
        if last_digit == cal:
            return True
        else:
            return False
    
    def asISBN10(self):
        if int(self.code[12]) != (10 - (int(self.code[0])+int(self.code[2])+int(self.code[4])+int(self.code[6])+int(self.code[8])+int(self.code[10]) + 3*(int(self.code[1])+int(self.code[3])+int(self.code[5])+int(self.code[7])+int(self.code[9])+int(self.code[11])))%10)%10:
            return None
        elif self.code[:3] == '979':
            return None
        else:
            code_10 = (int(self.code[3])+2*int(self.code[4])+3*int(self.code[5])+4*int(self.code[6])+5*int(self.code[7])+6*int(self.code[8])+7*int(self.code[9])+8*int(self.code[10])+9*int(self.code[11]))%11
            return "{}".format(self.code[3]+'-'+self.code[4:12]+'-'+str(code_10))
