def codontable(file):
    #open and read
    reading = open(file, 'r').read()
    #remove space, \n and change stop to * -make it as one line
    reading = reading.replace(' ','').replace('\n','').replace('Stop','*')
    #set variables
    dict1 = {}
    #3개씩 잘라서 seq 채우기
    seq = ''
    x = 0
    
    while x < len(reading):
        #append reading to seq
        seq += reading[x]
        x += 1
        # codon(3)+protein(1) = 4
        if len(seq) == 4:
            #key = codon, value = protein
            dict1[seq[:3]] = seq[-1]
            
            seq = ''
        
    return dict1   
def reverse_codontable(table):
    
    dict1 = {}
    #key,value를 한번에 본다
    for key, value in table.items():
        #value가 key 가되고, 빈set에다 원래 key 가 들어간다
        dict1.setdefault(value, set()).add(key)
        
    return dict1

def mRNA(seq, table):
    
    dict1 = reverse_codontable(table)
    #곱해줘야 하기때문에 1으로 지정
    stop = 1
    #stop codon * protein이나요는 경우뤼수
    for x in seq:
        stop = stop *len(dict1[x])
        
    return stop * len(dict1['*'])
    
print(reverse_codontable(codontable('standard_code.txt')))
print(mRNA('MA',codontable('standard_code.txt') ))