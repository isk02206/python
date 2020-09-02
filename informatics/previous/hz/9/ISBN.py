from urllib.request import urlopen

def isISBN(code):
    last_digit_2 = 0
    if len(code) == 13:
        if code[12] == 'X':
            last_digit_2 = 10
        else:
            last_digit_2 = int(code[12])
        cal_2 = (10 - (int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10]) + 3*(int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])))%10)%10
        if last_digit_2 == cal_2:
            return True
        else:
            return False
    else:
        return False


def displayBookInfo(code):
    if isISBN(code) == True:
        url = 'http://isbndb.com/api/books.xml?access_key=ZFD8L2Z5&index1=isbn&value1='
        accession = code
        
        reader = urlopen(url+accession)
        
        marker = '<Title>'
        line = reader.readline().decode('utf-8')
        while line and not line.startswith(marker):
            line = reader.readline().decode('utf-8')
        
        if line.startswith(marker):
            Title = line[len(marker):].strip()[:-len(marker)-1]
        
        
        marker = '<AuthorsText>'
        line = reader.readline().decode('utf-8')
        while line and not line.startswith(marker):
            line = reader.readline().decode('utf-8')
        
        if line.startswith(marker):
            Authors = line[len(marker):].strip()
            Authors = Authors.replace("</AuthorsText>","",1)
            if Authors.endswith(" "):
                Authors = Authors[:-2]
        
        
        marker = '<PublisherText'
        line = reader.readline().decode('utf-8')
        while line and not line.startswith(marker):
            line = reader.readline().decode('utf-8')
        
        if line.startswith(marker):
            Publisher = line[:-17]
        Publisher = list(Publisher)
        while Publisher[0] != '>':
            del(Publisher[0])
        Publisher = ''.join(Publisher[1:])
        print('Title: '+Title)
        print('Authors: '+Authors)
        print('Publisher: '+Publisher)
    else:
        print('Wrong ISBN-13 code')
        
print(displayBookInfo('9780136110675'))