import random
def fitness(word1, word2):
    assert len(word1) == len(word2), 'strings must have equal length'    
    count = 0
    # assert x as position number
    for x in range(len(word1)):
        if word1[x] == word2[x]:
            count += 1
    return count


def mutation(word1, mutations = 1):
    
    assert len(word1) >= mutations, 'invalid number of mutations'
    # sample(���� 1���� �����¾���� ������ �ι��� ���ڷ� �̾Ƴ�)
    # ���� �� 1������ 10���� �ι����� 2�̸�
    # 1���� 10������ ���ڸ� �ΰ��� �̾Ƴ� 
    # ��ġ�� ���ڴ� ����
    list1 = random.sample(range(len(word1)), mutations)
    #range(len(word1)) �� list
    new = ''
    # pos�� word1��0�����ͳ�����
    for pos in range(len(word1)):
            #�����̽� �־��ֱ�
        if not pos in list1:
                
            new += word1[pos]
        #pos�� list�ȿ� ������
        #
        else: 
            #lower case�ð�� ���� ����ߵ�
            #�ڵ� �̿ϼ�
            new += chr(random.sample(range(65,91), 1)[0])
        
    return new

def crossover(word1, word2, point = None):
    
    assert len(word1) == len(word2), 'strings must have equal length'
    
    if point == None:
        
        point = random.randint(0,len(word1)-1)
        
    assert 0 < point <= len(word1)-1, 'invalid crossover point'
    
    new1 = word1[:point] + word2[point:]
    new2 = word2[:point] + word1[point:]
    
    return new1, new2
        
    

        
print(crossover('WEASEL', 'METHINKS'))