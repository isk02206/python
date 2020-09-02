'''
Created on 2017. 6. 16.

@author: hayoung kim
'''
from curses.ascii import islower

class Diana:
    def __init__(self, text):
        self.text = text
        reader = open(text, 'r')
        data = reader.readlines()


    def trigraph(self, letter_1, letter_2):
        '''
        >>> diana.trigraph('Q', 'K')
        'Z'
        >>> diana.trigraph('t', 'f')
        'B'
        '''
        alphabet_order = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        self.letter_1 = alphabet_order[letter_1.lower()]
        self.letter_2 = alphabet_order[letter_2.lower()]
        order_plus = (25-self.letter_1-self.letter_2)
        
        #when answer is lower than 0, it doesn't match the alphabet order dictionary.
        if order_plus >= 0:
            order_plus = order_plus % 25
        else:
            order_plus = order_plus + 26
            
        alphabet_order_2 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
        answer = alphabet_order_2[order_plus]
        if letter_1 == islower:
            return answer.lower()
        else:
            return answer.upper()
            
                          
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        