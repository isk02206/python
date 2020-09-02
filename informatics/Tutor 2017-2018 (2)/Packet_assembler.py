'''
Created on 2018. 7. 4.

@author: TaeWoo
'''
from html.parser import incomplete

class Assembler:
    
    def __init__(self, text_file):
        
        # Make list containing each line of the text file
        reader = open(text_file, 'r')
        lines = reader.readlines()
        reader.close()
        
        # Construct empty dictionary
        self.packets = dict()
        
        # From list of lines, select each line and add it to the dictionary 
        for line in lines:
            
            # Cut line based on tab
            line = line.split('\t')
            # This is to remove '\n' from each line
            line[-1] = line[-1].strip()
            
            # If code is new in dictionary
            if line[0] not in self.packets:
                self.packets[line[0]] = [line[1:]]
                
            # If code already exist in dictionary
            else:
                self.packets[line[0]].append(line[1:])
        
    # m is the code
    def isComplete(self, m):
        
        if str(m) not in self.packets:
            
            return False
        
        packet_index = []
        check = int(self.packets[str(m)][0][1])

        for packet in self.packets[str(m)]:
            
            packet_index.append(int(packet[0]))
        
        if check == len(packet_index):
            
            return True
        
        else:
            
            return False
            
        
    def completeMessages(self):
        
        # Create empty set
        complete = set()
        
        for code in self.packets:
            
            information = self.packets[code]
            packet_index = sorted([int(packet[0]) for packet in information])
            check = int(information[0][1])
            
            if check == len(packet_index):
                complete.add(int(code))
            
        return complete
    
    def incompleteMessages(self):
        
        # Create empty dictionary
        incomplete = dict()
        
        for code in self.packets:
            
            information = self.packets[code]
            packet_index = sorted([int(packet[0]) for packet in information])
            check = int(information[0][1])
            
            if check != len(packet_index):
                incomplete[int(code)] = (int(len(packet_index)), check)
        
        return incomplete
    
    
    def message(self, code):
        
        complete = self.completeMessages()
        incomplete = self.incompleteMessages()
        
        # raise assertion error if code is incomplete
        assert code not in incomplete, 'incomplete message'
        # raise assertion error if code is invalid
        assert code in complete, 'incomplete message'
        
        # from self.packets bring packets that belong to the code and arrange in increasing order
        packets = sorted([int(packet[0]), packet[-1]] for packet in self.packets[str(code)])
        
        # make list containing each line of message format
        message = [str(packet[0]) + '. ' + packet[-1] for packet in packets]
        
        return '\n'.join(message)
        
a = Assembler('packets_02.txt')
print(a.completeMessages())
print(a.incompleteMessages())
print(a.isComplete(1234))