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
    # sample(열고 1번쨰 들어오는얘수를 가지고 두번쨰 숫자로 뽑아냄)
    # 예를 들어서 1번쨰가 10개고 두번쨰가 2이면
    # 1부터 10사이의 숫자를 두개씩 뽑아냄 
    # 겹치는 숫자는 없다
    list1 = random.sample(range(len(word1)), mutations)
    #range(len(word1)) 은 list
    new = ''
    # pos는 word1의0번부터끝까지
    for pos in range(len(word1)):
            #스페이스 넣어주기
        if not pos in list1:
                
            new += word1[pos]
        #pos이 list안에 있을떄
        #
        else: 
            #lower case올경우 따로 적어야됨
            #코드 미완성
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