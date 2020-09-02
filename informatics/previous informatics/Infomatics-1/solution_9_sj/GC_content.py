import statistics
def readFasta(textfile):
    
    #>를 기준으로 텍스트를 나눈다  >로 자랐을떄 빈칸이 오기떄문에 1부터 시작
    reader = open(textfile, 'r').read().split('>')[1:]
    
    result = []
    
    for series in reader:
        #0번을 제외한 남은 것들이 dna seq 가 된다
        list1 = series.split('\n')
        #id,이름을  나눈다
        list2 = list1[0].split('|')
        #id
        accession = list2[1]
        #이름
        generic_name = list2[2]
        
        seq = ''
        #seq를 뽑아내야 하기떄문에 1 번부터 0번은 이름이랑 id등등
        for sub in list1[1:]:
            seq += sub
        #\n 을 없애준다 (sring에서만 사용가능)   
        seq = seq.replace('\n','')
        
        result.append((accession, generic_name, seq))
    return result

def percentGC(seq):
    # g와 c가 몇 %인지 구하는것
    #seq에서 c와 g를 찾는다
    countC = seq.count('C')
    countG = seq.count('G')
    
    return ((countC + countG)/ len(seq))*100

def showOverview(textfile):
    
    list1 = readFasta(textfile)
    
    list2 = []
    
    for series in list1:
        #2번쨰 다리에 seq가 있기때문에
        list2.append(percentGC(series[2]))
        #동물이름(series[1], 소숫점 두번째 자리까지 나타내줌 (.2)  
        line = series[1] + '\t' + '{:.2%}'.format((percentGC(series[2])/100)) + ' ' + '({})'.format(series[0])
        
        print(line)
    
    print('\nminimum\t{}'.format('{:.2%}'.format(min(list2)/100)))
    print('maximum\t{}'.format('{:.2%}'.format(max(list2)/100)))
    #list안에있는 모든 variables를 더해서 average를 구하는것
    print('mean\t{}'.format('{:.2%}'.format(statistics.mean(list2)/100)))
print(showOverview('seq1.fasta.txt'))
