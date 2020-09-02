class Panini:
    def __init__(self, collection):
        self.collection = collection
        if isinstance(self.collection, int):
            self.collection = [self.collection]
        if isinstance(self.collection, tuple):
            self.collection = list(self.collection)
        if isinstance(self.collection, set):
            self.collection = list(self.collection)
        assert (isinstance(self.collection, list) == True), str('invalid stickers')
        
        for c in self.collection:
            assert (isinstance(c, int) == True), str('invalid stickers')
    
    def __str__(self):
        if isinstance(self.collection, int or tuple or set):
            self.collection = list(self.collection)
            
        if self.collection == []:
            return None
        
        self.collection.sort()
        
        list_numbers = []
        for n in range(1,self.collection[-1]+1):
            list_numbers.append(int(n))
        
        non_numbers =[] 
        for n in list_numbers:
            if n not in self.collection:
                non_numbers.append(n)
        
        for o in non_numbers:
            if o not in self.collection:
                order = list_numbers.index(o)
                list_numbers[order] = ' '
        
        result = []
        total = []
        for n in list_numbers:
            if n == ' ':
                if result == []:
                    result = []
                    continue
                else:
                    total.append(result)
                    result = []
            else:
                result.append(n)
        total.append(result)
        
        group = ''
        for n in total:
            if len(n) == 1:
                group += str(n[0]) + ', '
            else:
                group += str(n[0])+ '-'+ str(n[-1]) + ', '
        group = group[:-2]
        return group
    
    def __repr__(self):
        if self.collection == []:
            return ''
        return self.__str__()
    
    def __add__(self, collection_add):
        if isinstance(collection_add.collection, int) == True:
            collection_add = collection_add
        else:
            collection_add = list(i for i in collection_add.collection)
        add_collection = Panini(set(self.collection + collection_add))
        return add_collection
    
    def __sub__(self, collection_sub):
        if isinstance(collection_sub.collection, int) == True:
            collection_sub = collection_sub
        else:
            collection_sub = sorted(list(set(list(i for i in collection_sub.collection))))
        collection_sub = Panini(list(i for i in self.collection if i not in collection_sub))
        return collection_sub

collection1 = Panini([1, 3, 4, 5, 6, 7, 9, 10, 11, 17, 19, 20])
print(Panini((15, 10)))