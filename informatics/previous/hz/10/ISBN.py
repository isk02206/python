class ISBN13:
    def __init__(self, isbn, number=1):
        self.isbn = str(isbn)
        self.number = number
    
    def __str__(self):
        return "{}".format(self.isbn[:3]+'-'+self.isbn[3]+'-'+self.isbn[4:12]+'-'+self.isbn[12])
    
    def __repr__(self):
        return "ISBN13({}, {})".format(self.isbn, self.number)
    
    def isValid(self):
        last_digit = 0
        if len(self.isbn) == 13:
            last_digit = int(self.isbn[12])
            cal = (10 - (int(self.isbn[0])+int(self.isbn[2])+int(self.isbn[4])+int(self.isbn[6])+int(self.isbn[8])+int(self.isbn[10]) + 3*(int(self.isbn[1])+int(self.isbn[3])+int(self.isbn[5])+int(self.isbn[7])+int(self.isbn[9])+int(self.isbn[11])))%10)%10
            if last_digit == cal:
                return True
            else:
                return False
        else:
            return False
    
    def asISBN10(self):
        if self.isbn[:3] == '979':
            return None
        elif int(self.isbn[12]) != (10 - (int(self.isbn[0])+int(self.isbn[2])+int(self.isbn[4])+int(self.isbn[6])+int(self.isbn[8])+int(self.isbn[10]) + 3*(int(self.isbn[1])+int(self.isbn[3])+int(self.isbn[5])+int(self.isbn[7])+int(self.isbn[9])+int(self.isbn[11])))%10)%10:
            return None
        else:
            isbn_10 = (int(self.isbn[3])+2*int(self.isbn[4])+3*int(self.isbn[5])+4*int(self.isbn[6])+5*int(self.isbn[7])+6*int(self.isbn[8])+7*int(self.isbn[9])+8*int(self.isbn[10])+9*int(self.isbn[11]))%11
            isbn_10 = str(isbn_10)
            return "{}".format(self.isbn[3]+'-'+self.isbn[4:12]+'-'+isbn_10)