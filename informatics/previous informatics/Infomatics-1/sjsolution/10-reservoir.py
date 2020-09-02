class Reservoir:
    
    def __init__(self, profile):
        
        self.profile = profile
        result = ''
        maximum = max(self.profile)
        while maximum != 0:
            
            for x in self.profile:
                if x >= maximum:
                    result += '#'
                else:
                    result += ' '
                    
            maximum -= 1
            result += '\n'
        if result[-1] == '\n':
            result = result[:-1]
            
        self.result = result
        
    def __str__(self):
        return self.result
    
    def fill(self):

        result_line = self.result.split('\n')
        result_fill = ''
        count = 0
        check = ''
        fill_count = 0
        
        for line in result_line:
            
            while count != len(line) -1:
                
                if line[count] == '#' and line.rfind('#') != count:            
                    check = line[count:line.rfind('#')+1]
                    fill_count += check.count(' ')
                    check = check.replace(' ','~')
                    line = line[:count] + check + line[line.rfind('#')+1:]
                    break
            
                count +=1
            
            result_fill += line + '\n'
            count = 0
            check = ''
        
        if result_fill[-1] == '\n':
            result_fill = result_fill[:-1]
        
        self.result =  result_fill
        self.fill_count = fill_count
        
        return self.fill_count
        
    def drain(self):
        
        count = 0
        for char in self.result:
            if char == '~':
                count += 1
        self.result = self.result.replace('~', ' ')
        return count
    
    def penetrate(self):
        
        self.result = self.result.replace('~',' ')
        penetrate = 0
        penetrate_result = ''
        
        for line in self.result.split('\n'):
            count = 0
            while count != len(line) - 1:
                if line[count] == '#':    
                    if line[count+1:].find('#') != -1:
                        
                        pos = line[count+1:].find('#')
                        
                        if not 0 in self.profile[count:count + 1 + pos]:
                            
                            penetrate += line[count:count+1+pos].count('~')
                            line = line[:count] + line[count:count+1+pos].replace(' ','~') + line[count+1+pos:]
                            
                        count += pos
                count += 1
        
            penetrate_result += line + '\n'
        
        if penetrate_result[-1] == '\n':
            penetrate_result= penetrate_result[:-1]
        
        self.result = penetrate_result
        
        ghent = 0
        for line2 in self.result.split('\n'):
            
            if line2.find('#') != line2.rfind('#'):
                
                ghent += line2[line2.find('#') : line2.rfind('#')].count(' ')
         
        return ghent
        
