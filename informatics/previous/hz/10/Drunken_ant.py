'''
name : Ha Young Kim
student number : 01603259
'''

class DrunkenAnt:
    def __init__(self, text):
        reader = open(text, 'r')
        data = reader.readlines()
        data = ''.join(data).strip('\n').replace(' ', '').split('\n')
        #make the grid by using a list type
        list_reader = []
        for x in data:
            list_reader.append(list(x))
        #make the current position of the ant in the grid
        pos = (len(list_reader[0])-1,0)
        
        self.reader = list_reader
        self.pos = pos
        
    def position(self):
        #return the current position of the ant in the grid
        return self.pos
    

    def __repr__(self):
        #make the original form of grid(square n×n grid in the same format as used to store the original configuration of the grid in a text file.)
        group_1 = ''
        #lines
        for i in range(len(self.reader)):
            group_2 = ''
            #individual strings in lines
            for j in range(len(self.reader)):
                group_2 += self.reader[i][j] + ' '
            #tie individual strings and make new line
            group_1 += group_2.rstrip() + '\n'
        return group_1.rstrip()


    def __str__(self):
        #the direction symbol at the current location of the ant is preceded by an opening square bracket '[' and followed by a closing square bracket ']'.
        self.reader[self.pos[0]][self.pos[1]] = '['+self.reader[self.pos[0]][self.pos[1]]+']'
        
        group_3 = ''
        #lines
        for i in range(len(self.reader)):
            group_4 = ' '
            #individual strings in lines
            for j in range(len(self.reader)):
                #if the string does not contain bracket, make empty strings on both sides of the string.
                if len(self.reader[i][j]) == 3:
                    group_4 += self.reader[i][j]
                else:
                    group_4 += ' ' + self.reader[i][j] + ' '
            #if the string does not contain bracket, make empty string on left side of the string.
            if group_4[1] == '[':
                group_3 += group_4.lstrip() + '\n'
            else:
                group_3 += ' ' + group_4.lstrip() + '\n'
        #if the end string of the line contains bracket, it doesn't need empty string.
        if group_3[-2] == ']':
            group_3 = group_3.rstrip()
        else:
            group_3 = group_3.rstrip() + ' '
        return group_3
    
      
    def step(self):
        #make all characters to the same form.
        s = self.reader[self.pos[0]][self.pos[1]].replace('[','').replace(']','')
        #if there is a space to go to the right direction, change current string that contains bracket and current position also changed to the right.
        if s == '>':
            if self.pos[1] != len(self.reader) - 1:
                self.pos = (self.pos[0], self.pos[1]+1)
                self.reader[self.pos[0]][self.pos[1]-1] = 'v'
            else:
                self.reader[self.pos[0]][self.pos[1]] = 'v'
                self.pos = (self.pos[0], self.pos[1])
        #if there is a space to go to the left direction, change current string that contains bracket and current position also changed to the left.
        elif s == '<':
            if self.pos[1] != 0:
                self.pos = (self.pos[0], self.pos[1]-1)
                self.reader[self.pos[0]][self.pos[1]+1] = '^'
            else:
                self.reader[self.pos[0]][self.pos[1]] = '^'
                self.pos = (self.pos[0], self.pos[1])
        #if there is a space to go to the upper direction, change current string that contains bracket and current position also changed to the upper.
        elif s == '^':
            if self.pos[0] != 0:
                self.pos = (self.pos[0]-1, self.pos[1])
                self.reader[self.pos[0]+1][self.pos[1]] = '>'
            else:
                self.reader[self.pos[0]][self.pos[1]] = '>'
                self.pos = (self.pos[0], self.pos[1])
        #if there is a space to go to the lower direction, change current string that contains bracket and current position also changed to the lower.
        elif s == 'v':
            if self.pos[0] != len(self.reader) - 1:
                self.pos = (self.pos[0]+1, self.pos[1])
                self.reader[self.pos[0]-1][self.pos[1]] = '<'
            else:
                self.reader[self.pos[0]][self.pos[1]] = '<'
                self.pos = (self.pos[0], self.pos[1])
        
        return self.pos
    
    def steps(self):
        start = self.position()
        end = (0, len(self.reader) - 1)
        
        answer = []
        #until the start position and the end position are same, the function 'step' are ongoing. The function 'steps' have to gather all of these positions.
        while start != end:
            answer.append(start)
            start = self.step()
        return answer+[(0, len(self.reader)-1)]