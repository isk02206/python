def readMunicipalities(place):
    #make new dictionary
    dict1 = {} 
    #place�� text file�� ���� r =read \n means enter(go to next line)
    #�������� �����ϰ�츦 �����
    list1 = open(place, 'r').read().split('\n')[:-1]
    
    for area in list1:
        # \t = tap t�� �������� ������
        #list �ȿ� tap���� �����͵��� �� list �� ����
        list2 = area.split('\t')
        #()���� ,�� ��������  key �� value�� ���Ѵ�
        dict1.setdefault(list2[0], set()).add(list2[1])
        #�ݴ��� ��츦 �����ؼ� �ѹ��� ������
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