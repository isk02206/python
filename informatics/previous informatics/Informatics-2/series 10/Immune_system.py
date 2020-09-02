'''
Created on 2015. 12. 3.

@author: User
'''
class Organism:
    def __init__(self, file = None):
        list1 = []
        list2 = list()
        if file:
            reader = open(file, 'r').read().split()
            list1 = reader
            
        self.list1 = list1
        self.list2 = list2
        
    def isResistant(self, virus = None):
        
        virus = str(virus)
        
        if virus in self.list1:
            return True
        
        elif virus not in self.list1:
            self.list2.append(virus)
            print(self.list2)
            if self.list2.count(virus) < 3:
                return False
            else:
                return True
        
    def mutation(self, virus = None):
        
        virus = str(virus)
        list3 = []
        if str(virus) in self.list1:
            self.list1.remove(virus)
            
        if str(virus) in self.list2:
            for x in self.list2:
                if x != str(virus):
                    list3.append(x)
            self.list2 = list3
        
organism = Organism('immune_system.txt')
print(organism.isResistant(virus = 6))
print(organism.isResistant(virus = 6))
print(organism.isResistant(virus = 6))
print(organism.mutation(6))
print(organism.isResistant(6))