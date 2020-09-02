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
    #see the all the contents output ��ü�� �����ְ� roof limit�� ���ߴ�
    while pos < len(output):
        #check =number��ŭ �ڸ���// identifies the prefixes of each of numbers
        check = output[pos][:num]
        #if len(check) is smaller than num ignore
        #prefix�� ������ num�� �������� ������
        if len(check) == num:
            #prefix�� ó�� ���� �༮�̸� �ؿ��ִ� �ĵ��� �����Ų��
            if check not in set1:
                
                set1.add(check)
                #pos 0���� �������� -1������ 3�� ����
                for line in output[pos-1:pos+3]:
                    
                    context += line + '\n'
            
        pos += 4
    #a ������ �ٽ� ���� ���� �ϰ� ���� ��ȸ���̾ƴ�
    #strage ��� text file�� context�� ���´�
    open(storage, 'a').write(context)

def find_longest(textfile, num):
    
    dict1 = dict()
    #open and split by lines
    #one line = one position
    output = open(textfile, 'r').read().split('\n')
    #only consider sequence so start from 1
    pos = 1 
    
    set_check = set()
    #see the all the contents output ��ü�� �����ְ� roof limit�� ���ߴ�
    while pos < len(output):

        check = output[pos][:num]
        
        if len(check) == num:
            
            set_check.add(check)
            
        pos += 4
    
    set_check = list(set_check)
    
    list_check = []
    #prefix�� �ϳ��� ����
    for pre in set_check:
        #output�� line�� ���� ����
        for line in output:
            #�߶��� line�� prefix�� ������
            if line[:num] == pre:
                #line�� ���̸� list�� �������
                list_check.append(len(line))
        #� prefix�� value�� list check �� ���� ū�� �´�
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
                #if ������ �´°��� �ΰ� �̻��϶� ���ϸ��� �����°��� �̰� ����(to remove the duplication) 
                #but it is just stop the second roof
                break
            
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()