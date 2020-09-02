def retain_first(textfile, storage, num):
    '''
    retain_first('sample.fq.txt', 'first.fq,txt', 10)
    print(open('first.fq.txt', 'r').read().rstrip())
    @sample sequence 1
    GGAAGTCCATGGAGTTATTTGCGGTAACCGGGACCGGCCT
    +sample sequence 1
    ba^aaabaa`]baaaaa_aab]D^^`b`aYDW]abaa`^a
    @sample sequence 2
    CTCCTTATAGCATCATACGCACAGCTGGTATCCCCATTGCTTATTAGGGTTCAGCCCTGTCGCTCTCCCC
    +sample sequence 2
    ababa``aaaababaaaabaa_``aa``]^aa_`aa_Z_aaaaa^baaaaaaaaaaaaaaaaaa`^```a
    '''
    #open and split by lines
    #one line = one position
    output = open(textfile, 'r').read().split('\n')
    #only consider sequence so start from 1
    pos = 1
    #remove duplicate-use set(uniqueness)
    set1 = set()
    
    context = ''
    #see the all the contents output 전체를 볼수있게 roof limit을 정했다
    while pos < len(output):
        #check =number만큼 자른다// identifies the prefixes of each of numbers
        check = output[pos][:num]
        #if len(check) is smaller than num ignore
        #prefix가 지정된 num에 만족되지 않을떄
        if len(check) == num:
            #prefix가 처음 보는 녀석이면 밑에있는 식들을 실행시킨다
            if check not in set1:
                
                set1.add(check)
                #pos 0번을 기준으로 -1번부터 3번 까지
                for line in output[pos-1:pos+3]:
                    
                    context += line + '\n'
            
        pos += 4
    #a 를쓰면 다시 쓰고 저장 하고 가능 일회용이아님
    #strage 라는 text file에 context를 적는다
    open(storage, 'a').write(context)

def find_longest(textfile, num):
    
    dict1 = dict()
    #open and split by lines
    #one line = one position
    output = open(textfile, 'r').read().split('\n')
    #only consider sequence so start from 1
    pos = 1 
    
    set_check = set()
    #see the all the contents output 전체를 볼수있게 roof limit을 정했다
    while pos < len(output):

        check = output[pos][:num]
        
        if len(check) == num:
            
            set_check.add(check)
            
        pos += 4
    
    set_check = list(set_check)
    
    list_check = []
    #prefix를 하나씩 보기
    for pre in set_check:
        #output의 line을 전부 본다
        for line in output:
            #잘라진 line이 prefix와 같으면
            if line[:num] == pre:
                #line의 길이를 list에 집어넣음
                list_check.append(len(line))
        #어떤 prefix에 value는 list check 중 가장 큰놈만 온다
        dict1[pre] = max(list_check)
        #for append new 
        list_check = []
    
    return dict1

def retain_longest(textfile, storage, num):
    '''
    retain_longest('sample.fq', 'longest.fq', 10)
    print(open('longest.fq', 'r').read().rstrip())
    @sample sequence 2
    CTCCTTATAGCATCATACGCACAGCTGGTATCCCCATTGCTTATTAGGGTTCAGCCCTGTCGCTCTCCCC
    +sample sequence 2
    ababa``aaaababaaaabaa_``aa``]^aa_`aa_Z_aaaaa^baaaaaaaaaaaaaaaaaa`^```a
    @sample sequence 3
    GGAAGTCCATGGAGTTATTTGCGGTAACCGGGACCGGCCTGGGGTTAGATTTTATGTCGT
    +sample sequence 3
    ba^aaabaa`]baaaaa_aab]D^^`b`aYDW]abaa`^ababbaaabaaaaa`]`ba`]
    '''

    dict1 = find_longest(textfile, num)
    #split by @ 
    reader = open(textfile, 'r').read().split('@')[1:]
    #prefix = key, value = biggest number
    for pre, biggest in dict1.items():
        
        for series in reader:
            
            list1 = series.split('\n')
            #position 1 is sequence
            if list1[1][:num] == pre and biggest == len(list1[1]):
                #open and append the contents to the storage
                #rewrite @
                open(storage, 'a').write('@' + series)
                #if 조건이 맞는것이 두개 이상일때 제일먼저 나오는것을 뽑고 끝남(to remove the duplication) 
                #but it is just stop the second roof
                break
            
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()