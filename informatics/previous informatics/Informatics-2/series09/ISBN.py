'''
Created on 2015. 11. 4.

@author: User
'''
from urllib.request import urlopen
def displayBookInfo (x):
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    e = int(x[4])
    f = int(x[5])
    g = int(x[6])
    h = int(x[7])
    i = int(x[8])
    j = int(x[9])   
    k = int(x[10])
    l = int(x[11])
    n = int(x[12])
    check=(10-(a+c+e+g+i+k+3*(b+d+f+h+j+l))%10)%10
    if not n==check or len(x)!=13:
        print('Wrong ISBN-13 code')
    else:
        embl_url = 'http://isbndb.com/api/books.xml?access_key=ZFD8L2Z5&index1=isbn&value1='
        accession = x
        fasta = urlopen(embl_url + accession) 
        
        for line in fasta:
            line = line.decode('utf-8')
            
            if line.startswith('<Title>'):
                print('Title: {}'.format(line[len('<Title>'):line.find('</Title>')]))
            
            if line.startswith('<AuthorsText>'):
                text = line[len('<AuthorsText>'):line.find('</AuthorsText>')]
                print('Authors: {}'.format(text).strip(', '))
            
            if line.startswith('<PublisherText'):
                print('Publisher: {}'.format(line[line.find('>')+1:line.find('</PublisherText>')]))
print(displayBookInfo('9780307885159'))
        