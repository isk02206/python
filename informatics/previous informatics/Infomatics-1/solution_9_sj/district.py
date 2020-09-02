def readMunicipalities(place):
    #make new dictionary
    dict1 = {} 
    #place에 text file이 들어옴 r =read \n means enter(go to next line)
    #마지막이 빈줄일경우를 대비해
    list1 = open(place, 'r').read().split('\n')[:-1]
    
    for area in list1:
        # \t = tap t의 기준으로 나눈다
        #list 안에 tap으로 나눈것들을 또 list 로 만듬
        list2 = area.split('\t')
        #()에서 ,를 기준으로  key 와 value를 정한다
        dict1.setdefault(list2[0], set()).add(list2[1])
        #반대의 경우를 생각해서 한번더 적어줌
        dict1.setdefault(list2[1], set()).add(list2[0])
        
    return dict1
    
def searchMunicipalities(place, boroughs):
    
    set1 = set()
    
    for area in boroughs[place]:
        
        if len(boroughs[area]) > 2:
            
            set1.add(area)
            
    return set1

def compounds(boroughs):
    
    set1 = set()
    
    for key in boroughs.keys():
        
        series = searchMunicipalities(key, boroughs)
        
        for x in series:
            
            if '-' in x and x.split('-')[0] == key:
                
                set1.add(x)
                
    return set1


    
            

boroughs = readMunicipalities('vlaams_gewest.txt')
print(searchMunicipalities('Berchem', boroughs))
print(compounds(boroughs))