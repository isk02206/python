import datetime
from math import floor

class Stardate:
    def __init__(self, date=datetime.date.today(), shift='new'):
        self.date = date
        self.shift = shift
    
    def __repr__(self):
        return "Stardate(datetime.date({}, {}, {}))".format(self.date.year, self.date.month, self.date.day)
    
    def __str__(self):
        if self.shift != 'new':
            self.oldmethod = '{:02d}'.format(int(self.date.year)-1900)+'{:02d}'.format(int(self.date.month))+'.'+'{:02d}'.format(int(self.date.day))
            return self.oldmethod
        else:
            date = (self.date - datetime.date(self.date.year, 1, 1)).days
            
            year = str(datetime.date(self.date.year, 12, 31)-datetime.date(self.date.year, 1, 1))
            group_year = ''
            for i in year:
                if i == ' ':
                    break
                else:
                    group_year+=i
            group_year = int(group_year)+1

            self.newmethod = '{:.2f}'.format(floor((self.date.year + date/group_year)*100)/100)
            return str(self.newmethod)
        
    def switch(self):
        if self.shift == 'new':
            self.shift = 'old'
        elif self.shift == 'old':
            self.shift = 'new'

date = Stardate(datetime.date(1904, 4, 5))
print(str(date))
print(date.switch())