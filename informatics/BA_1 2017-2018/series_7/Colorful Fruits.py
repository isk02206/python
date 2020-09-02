def combine(color, fruits, amount=None):
    '''
    >>> colors = ['purple', 'yellow', 'green']
    >>> fruits = ('grape', 'banana', 'apple')
    >>> combine(colors, fruits)
    ['a purple grape', 'a green banana', 'a yellow apple']
    >>> combine(colors, fruits)
    ['a purple grape', 'a green apple', 'a yellow banana']
    >>> combine(colors, fruits)
    ['a purple apple', 'a yellow grape', 'a green banana']
    >>> combine(colors, fruits, amount=1)
    ['a purple grape']
    >>> combine(colors, fruits, amount=2)
    ['a yellow apple', 'a green banana']
    >>> combine(colors, fruits, amount=4)
    ['a yellow banana', 'a green grape', 'a purple apple']
    '''
    if amount == None:
        amout = 0
    for i in color, fruits:

