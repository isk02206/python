from urllib.request import urlopen

def isISBN(code):
    last_digit = 0
    if len(code) == 13:
        if code[12] == 'X':
            last_digit = 10
        else:
            last_digit = int(code[12])
        cal = (10 - (int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10]) + 3*(int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])))%10)%10
        
        if last_digit == cal:
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
            T = line[len(marker):].strip()[:-len(marker)-1]
        
        
        marker = '<AuthorsText>'
        line = reader.readline().decode('utf-8')
        while line and not line.startswith(marker):
            line = reader.readline().decode('utf-8')
        if line.startswith(marker):
            A = line[len(marker):].strip()
            A = A.replace("</AuthorsText>","",1)
            if A.endswith(" "):
                A = A[:-2]
        
        marker = '<PublisherText'
        line = reader.readline().decode('utf-8')
        while line and not line.startswith(marker):
            line = reader.readline().decode('utf-8')
        if line.startswith(marker):
            P = line[:-17]
        P = list(P)
        while P[0] != '>':
            del(P[0])
        P = ''.join(P[1:])
        print('Title: '+T)
        print('Authors: '+A)
        print('Publisher: '+P)
    else:
        print('Wrong ISBN-13 code')