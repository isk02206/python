'''
name : Ha Young Kim
student number : 01603259
'''

import random
class MadLibs:
    def __init__(self):
        #make set 'vocabulary' to add words by the function 'learn'
        self.vocabulary = {}
        
    def learn(self, n_1, n_2):
        #types of n_2 are all different and need to change all n_2 to a same form.
        if isinstance(n_2, str) == True:
            key, value = n_1.lower(), {n_2.lower()}
        else:
            n_2 = set(n_2)
            n_3 = []
            for n in n_2:
                n_3.append(str(n).lower())
            key, value = n_1.lower(), set(n_3)
        #to add one by one, method 'update' is needed if some values have a same key.
        if key in self.vocabulary:
            self.vocabulary[key].update(value)
        else:
            self.vocabulary[key] = value
    
    def suggest(self, k_1):
        #In case the given category does not occur as a key in the property vocabulary, the method must raise an AssertionError with the message unknown category.
        if k_1.lower() not in self.vocabulary:
            raise AssertionError ('unknown category')
        # If all letters contained in the given category are capitals, all letters in the selected word must also be converted into uppercase.
        if k_1[:].isupper():
            vocab = str(self.vocabulary[k_1.lower()]).replace('{','').replace('}','').replace("'","")
            #if the number of values >= 2, are needed to add one by one after changing into uppercase.
            vocab = vocab.split(', ')
            upper_list = []
            for v in vocab:
                v = v.upper()
                upper_list.append(v)
            return random.choice(upper_list)
        # If all letters contained in the given category are lowercase, all letters in the selected word must also be remained as lowercase.
        elif k_1[:].islower():
            vocab = str(self.vocabulary[k_1]).replace('{','').replace('}','').replace("'","")
            #if the number of values >= 2, are needed to add one by one after changing into lowercase.
            vocab = vocab.split(', ')
            lower_list = []
            for v in vocab:
                lower_list.append(v)
            return random.choice(lower_list)
        #If the first letter contained in the given category is a capital and all successive letters are lowercase letters, the first letter of the selected word must also be converted into uppercase.
        elif k_1[0].isupper() and k_1[1:].islower():
            vocab = str(self.vocabulary[k_1.lower()]).replace('{','').replace('}','').replace("'","")
            #if the number of values >= 2, are needed to add one by one after changing.
            vocab = vocab.split(', ')
            first_upper = []
            for v in vocab:
                v = v[0].upper() + v[1:]
                first_upper.append(v)
            return random.choice(first_upper)
    
    def fill(self, sentence):
        #split into individual words
        sentence = sentence.split(' ')
        
        result = ''
        #change words one by one
        for s in sentence:
            #forms of words are different. Some words have '_'.
            if s[0] == '_':
                s = s.split('_')
                p = s[1]
                #according to forms of words such as lowercase, uppercase and so on, methods are different.
                if p[:].islower():
                    p = self.suggest(p)
                    
                elif p[:].isupper():
                    p = self.suggest(p)
                    
                elif p[0].isupper() and p[1:].islower():
                    p = self.suggest(p)
                    p = p[0].upper() + p[1:]
                result+=str(p)+s[2]+' '
            #ties words to sentence
            else:
                result+=s+' '
        return result.rstrip()