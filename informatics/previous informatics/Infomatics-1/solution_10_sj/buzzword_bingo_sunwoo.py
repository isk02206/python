class BuzzBingo:
    def __init__(self, dgt, namelist):
        assert (dgt * dgt ==len(namelist)), "invalid card"
        self.namelist = namelist
        bingoboard = ''
        for x in range(len(namelist)):
            bingoboard += '-'
            if len(bingoboard.replace('\n', '')) % dgt == 0:
                bingoboard += '\n'
        self.bingoboard = bingoboard
        self.dgt = dgt
    
    def __str__(self):
        return self.bingoboard.strip('\n')
    
    def __repr__(self):
        return str(self)
    
    def cancelWord(self, word):
        dgt = self.dgt
        bingoboard = self.bingoboard
        bingoboard = bingoboard.replace('\n', '')
        bingoboard = list(bingoboard)
        namelist = self.namelist
        assert (word in namelist), "{} not found on card".format(word)
        
        counter = 0
        while True:
            if word == namelist[counter]:
                assert (bingoboard[counter] != 'x'),"{} was already cancelled".format(word)
                bingoboard[counter] = 'x'
                break
            counter += 1
            if counter == len(namelist):
                break
        mock = counter // dgt
        remain = counter % dgt 
        bingoboard2 = ''
        for x in bingoboard:
            bingoboard2 += x
            if len(bingoboard2.replace('\n', '')) % dgt == 0:
                bingoboard2 += '\n'
        self.bingoboard = bingoboard2
        return mock, remain
    
    def cancelWords(self, wordlist):
        dgt = self.dgt
        bingoboard = self.bingoboard
        bingoboard = bingoboard.replace('\n', '')
        bingoboard = list(bingoboard)
        namelist = self.namelist
        lis = []
    
        for word in wordlist:
            counter = 0
            while True:
                if word == namelist[counter]:
                    assert (bingoboard[counter] != 'x'),"{} was already cancelled".format(word)
                    bingoboard[counter] = 'x'
                    break
                counter += 1
                if counter == len(namelist):
                    break
            #row
            mock = counter // dgt
            #column
            remain = counter % dgt
            lis.append((mock, remain)) 
        bingoboard2 = ''
        for x in bingoboard:
            bingoboard2 += x
            if len(bingoboard2.replace('\n', '')) % dgt == 0:
                bingoboard2 += '\n'
        self.bingoboard = bingoboard2
        return lis
        
    def won(self):
        dgt = self.dgt
        bingoboard = self.bingoboard
        s = bingoboard.split('\n')
        s.remove('')
        for x in s:
            if '-' not in x:
                return True
        bingoboard = bingoboard.replace('\n', '')
        bingoboard = list(bingoboard)
        counter = 0
        while True:
            if bingoboard[counter] == 'x':
                checker = 0
                h = 0
                while True:
                    if bingoboard[counter + dgt * h] == 'x':
                        checker += 1
                    h += 1
                    if checker == dgt:
                        return True
                    if h == dgt :
                        break

            counter += 1
            if counter == dgt:
                break
            
        counter = 0
        checker = 0
        while True:
            if bingoboard[0  + (dgt + 1 * counter)] == 'x':
                checker += 1
            counter += 1 
            if counter == dgt:
                break
        if checker == dgt:
            return True
        return False