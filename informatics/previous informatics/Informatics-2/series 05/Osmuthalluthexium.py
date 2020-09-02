class NameGenerator:
    def __init__(self):
        self.names = set()
        self.prefixes = set()
        self.triples = dict()
    def addName(self, name):
        # determine of the name exists of an upper case letter followed by two
        # or more lower case letters
        assert (len(name) >= 3 andname[0].isupper() andname[1:].islower()), 'invalid name'
        # remember names that were used to train the name generator
        self.names.add(name)
        # mark end of word by appending an underscore to the name
        name += '_'
        # add first three letters to the set of prefixes
        self.prefixes.add(name[:3])
        # add each bigram as a prefix for the next letter
        for i in range(1, len(name) - 2):
            prefix = name[i:i + 2]
            if prefix not in self.triples:
                self.triples[prefix] = {name[i + 2]}
            else:
                self.triples[prefix].add(name[i + 2])
    def addNames(self, filename):
        # traverse list of names in file and process each name by calling the
        # method addName with the name as an argument
        for name in open(filename, ¡¯r¡¯):
            self.addName(name.rstrip())
    def name(self):
        from random import choice
        # generate a new name until the name is different from all names that
        # were used to train the name generator
        name = None
        while not name or name in self.names:
            # choose a random prefix
            name = choice(list(self.prefixes))
            # extend name by choosing a random letter that can follow the
            # trailing bigram of the name, until an underscore has been chosen
            while name[-1] != ¡¯_¡¯:
                choices = list(self.triples[name[-2:]])
                name += choice(choices)[-1]
            # remove trailing underscore
            name = name[:-1]
        return name
if __name__ == ¡¯__main__¡¯:
    import doctest
    doctest.testmod()