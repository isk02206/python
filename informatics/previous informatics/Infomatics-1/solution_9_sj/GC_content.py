import statistics
def readFasta(textfile):
    
    #>�� �������� �ؽ�Ʈ�� ������  >�� �ڶ����� ��ĭ�� ���⋚���� 1���� ����
    reader = open(textfile, 'r').read().split('>')[1:]
    
    result = []
    
    for series in reader:
        #0���� ������ ���� �͵��� dna seq �� �ȴ�
        list1 = series.split('\n')
        #id,�̸���  ������
        list2 = list1[0].split('|')
        #id
        accession = list2[1]
        #�̸�
        generic_name = list2[2]
        
        seq = ''
        #seq�� �̾Ƴ��� �ϱ⋚���� 1 ������ 0���� �̸��̶� id���
        for sub in list1[1:]:
            seq += sub
        #\n �� �����ش� (sring������ ��밡��)   
        seq = seq.replace('\n','')
        
        result.append((accession, generic_name, seq))
    return result

def percentGC(seq):
    # g�� c�� �� %���� ���ϴ°�
    #seq���� c�� g�� ã�´�
    countC = seq.count('C')
    countG = seq.count('G')
    
    return ((countC + countG)/ len(seq))*100

def showOverview(textfile):
    
    list1 = readFasta(textfile)
    
    list2 = []
    
    for series in list1:
        #2���� �ٸ��� seq�� �ֱ⶧����
        list2.append(percentGC(series[2]))
        #�����̸�(series[1], �Ҽ��� �ι�° �ڸ����� ��Ÿ���� (.2)  
        line = series[1] + '\t' + '{:.2%}'.format((percentGC(series[2])/100)) + ' ' + '({})'.format(series[0])
        
        print(line)
    
    print('\nminimum\t{}'.format('{:.2%}'.format(min(list2)/100)))
    print('maximum\t{}'.format('{:.2%}'.format(max(list2)/100)))
    #list�ȿ��ִ� ��� variables�� ���ؼ� average�� ���ϴ°�
    print('mean\t{}'.format('{:.2%}'.format(statistics.mean(list2)/100)))
print(showOverview('seq1.fasta.txt'))
