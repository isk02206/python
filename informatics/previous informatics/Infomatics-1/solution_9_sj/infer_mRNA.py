def codontable(file):
    #open and read
    reading = open(file, 'r').read()
    #remove space, \n and change stop to * -make it as one line
    reading = reading.replace(' ','').replace('\n','').replace('Stop','*')
    #set variables
    dict1 = {}
    #3���� �߶� seq ä���
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
    #key,value�� �ѹ��� ����
    for key, value in table.items():
        #value�� key ���ǰ�, ��set���� ���� key �� ����
        dict1.setdefault(value, set()).add(key)
        
    return dict1

def mRNA(seq, table):
    
    dict1 = reverse_codontable(table)
    #������� �ϱ⶧���� 1���� ����
    stop = 1
    #stop codon * protein�̳���� �����
    for x in seq:
        stop = stop *len(dict1[x])
        
    return stop * len(dict1['*'])
    
print(reverse_codontable(codontable('standard_code.txt')))
print(mRNA('MA',codontable('standard_code.txt') ))