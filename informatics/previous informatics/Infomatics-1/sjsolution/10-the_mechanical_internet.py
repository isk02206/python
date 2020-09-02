class Chappe:
    
    def __init__(self, file):
        assert isinstance(file, str)
        
        self.file = file
        
        reader = open(self.file,'r',encoding = 'utf-8')
        
        ghent = dict()
        list1 = []
            
        for line in reader:
                
            line = line.split('\t')    
            line[1] = line[1][:-1]
            list1 += [line]
            
        for x in list1:
            for y in list1:
                        
                ghent.setdefault(x[0],set()).add(x[1])
                ghent.setdefault(x[1],set()).add(x[0])
                    
                if x[0] == y[1]:
                    ghent[x[0]].add(y[0])
        
        self.network = ghent
        
        
    def neighbours(self, tower1):
            
        if not tower1 in self.network:
            raise (AssertionError( 'city not in network'))
        
        else:
            return self.network[tower1]
        
            
    def hubs(self, tower1, tower2):
        
        if tower2 not in self.network.keys() or tower1 not in self.network.keys():
        
            raise (AssertionError( 'city not in network'))
    
        else:
        
            U = [tower1]
            
            P = {tower1: 0}
            
            d = 0
            
            while tower2 not in P.keys():
    
                a = U.pop(0)
    
                nei = self.network[a]    
                    
                for x in nei:
                    
                    if not x in P.keys():
                        
                        d = P[a]+ 1
                        
                        P[x] = d
                        
                        U.append(x)
                    
                if U == []:
                    
                    return -1
            
            return P[tower2]
    
                
            
            
network = Chappe('chappe.txt')
print(network.hubs('Lille', 'Lille'))
print(network.neighbors('Londres'))