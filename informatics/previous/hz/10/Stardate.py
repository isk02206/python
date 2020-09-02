import datetime
from datetime import date
from math import floor
class Stardate:
    def __init__(self, date=datetime.date.today(), convert='new'):
        self.date = date
        self.convert = convert
    
    def __repr__(self):
        return "Stardate(datetime.date({}, {}, {}))".format(self.date.year, self.date.month, self.date.day)
    
    def __str__(self):
        if self.convert == 'new':
            date = self.date - datetime.date(self.date.year, 1, 1)
            date = date.days
            
            year = str(datetime.date(self.date.year, 12, 31)-datetime.date(self.date.year, 1, 1))
            group_year = ''
            for y in year:
                if y != ' ':
                    group_year+=y
                else:
                    break
            group_year = int(group_year)+1
            
            self.new = date / group_year
            
            self.new = floor((self.date.year + self.new)*100)/100
            self.new = '{:.2f}'.format(self.new)
            return str(self.new)
        
        else:
            self.old = '{:02d}'.format(int(self.date.year)-1900)+'{:02d}'.format(int(self.date.month))+'.'+'{:02d}'.format(int(self.date.day))
            return self.old
        
    def switch(self):
        if self.convert == 'new':
            self.convert = 'old'
        else:
            self.convert = 'new'

        

date = Stardate(datetime.date(1904, 4, 5))
print(str(date))
print(date.switch())