'''
Created on 2018. 7. 10.

@author: TaeWoo
'''

class Organism:
    
    def __init__(self, txt_file=None):
        
        # no text file given so empty list
        if txt_file is None:
            
            self.immune = []
        
        # text file given
        else:
            
            # open text file
            reader = open(txt_file, 'r')
            innate = reader.readlines()
            # close text file
            reader.close()
            
            # record
            self.immune = [int(i.strip()) for i in innate]
        
        self.antibodies = dict()
    
    def isResistant(self, virus):
        
        if virus in self.immune:
            
            return True
        
        else:
            
            if virus not in self.antibodies:
                
                self.antibodies[virus] = 1
                
            else:
                
                self.antibodies[virus] += 1
        
        if self.antibodies[virus] == 3:

            self.immune.append(virus)
            self.antibodies.pop(virus)

            return True
        
        return False
    
    def mutation(self, virus):
        
        if virus in self.immune:
            self.immune.pop(self.immune.index(virus))
        
        if virus in self.antibodies:
            self.antibodies.pop(virus)

            
            
        
        
    
    
    
organism = Organism('immune_system.txt')
print(organism.isResistant(virus=42))
organism.mutation(42)
print(organism.isResistant(virus=42))
print(organism.isResistant(virus=42))
print(organism.isResistant(virus=42))


