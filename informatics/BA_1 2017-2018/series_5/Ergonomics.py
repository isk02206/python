def position(x):
    '''
    >>> row, col = position('K')
    >>> row
    0
    >>> col
    10
    >>> row, col = position('q')
    >>> row
    1
    >>> col
    3
    '''
    row_pos = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1}
    col_pos = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':0,'o':1,'p':2,'q':3,'r':4,'s':5,'t':6,'u':7,'v':8,'w':9,'x':10,'y':11,'z':12}
    y = x.lower()
    row = row_pos[y]
    col = col_pos[y]
    return row, col

def shift(a,b):
    '''
    >>> shift('K', 'q')
    8
    >>> shift('f', 'e')
    1
    '''
    a_row = position(a)[0]
    b_row = position(b)[0]
    a_col = position(a)[1]
    b_col = position(b)[1]
    x = abs(int(a_row)-int(b_row))
    y = abs(int(a_col)-int(b_col))
    return x+y

def ergonomics(x):
    '''
    >>> ergonomics('FEED')
    2
    >>> ergonomics('MAMA')
    36
    >>> ergonomics('feeders')
    5
    >>> ergonomics('layaway')
    67
    >>> ergonomics('disestablismentarianism')
    113
    >>> ergonomics('electroencephalographic')
    108
    '''
    shi = 0
    for i in range(len(x)-1):
        a = x[i]
        b = x[i+1]
        y = shift(a,b)
        shi += int(y)
    return shi
