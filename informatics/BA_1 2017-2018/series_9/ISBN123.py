from urllib.request import urlopen


def isISBN13(code):
    if len(code) != 13:
        return False
    if not code.isdigit():
        return False

    checkdigit = 0
    for i in range(12):
        if i % 2:
            checkdigit += 3 * int(code[i])
        else:
            checkdigit += int(code[i])
    checkdigit = (10 - checkdigit % 10) % 10
    if checkdigit == int(code[12]):
        return True
    else:
        return False


def displayBookInfo(code):
    if isISBN13(code) == True:
        embl_url = 'http://isbndb.com/api/books.xml?access_key=ZFD8L2Z5&index1=isbn&value1='
        accession = code
        url = urlopen(embl_url + accession)
        line = url.readline().decode('utf-8')
        marker = '<Title>'
        while line and not line.startswith(marker):
            line = url.readline().decode('utf-8')
        if line.startswith(marker):
            Title = line[len(marker):].strip()[:-len(marker) - 1]

        line = url.readline().decode('utf-8')
        marker = '<AuthorsText>'
        while line and not line.startswith(marker):
            line = url.readline().decode('utf-8')
        if line.startswith(marker):
            Author = line[len(marker):].strip()
            Author = Author.replace("</AuthorsText>", "", 1)
            if Author.endswith(", "):
                Author = Author[:-2]
        line = url.readline().decode('utf-8')
        marker = '<PublisherText'
        while line and not line.startswith(marker):
            line = url.readline().decode('utf-8')
        if line.startswith(marker):
            Publisher = line[:-17]
        Publisher = list(Publisher)
        while Publisher[0] != '>':
            del (Publisher[0])
        Publisher = ''.join(Publisher[1:])
        print('Title:', Title)
        print('Authors:', Author)
        print('Publisher:', Publisher)
    else:
        print('Wrong ISBN-13 code')