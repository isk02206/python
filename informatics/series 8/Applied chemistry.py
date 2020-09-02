# import string
# def isValid(symbol, chemical_name, length=None):
#     if length is None:
#         for i in symbol:
#             print(chemical_name.index('C'))
#             if i.lower() not in chemical_name.lower() and chemical_name.index(symbol[i]) > chemical_name.index(symbol[i+1]):
#                 return False
#         if symbol[0] == symbol[0].upper() and symbol[1:] == symbol[1:].lower() and set(symbol.lower()) - set(chemical_name.lower()) == set():
#             return True
#
#     else:
#
#         for i in symbol:
#
#             if i.lower() not in chemical_name.lower() and chemical_name.index(i.lower()) > chemical_name.index(symbol[i+1]):
#                 return False
#
#         if symbol[0] == symbol[0].upper() and symbol[1:] == symbol[1:].lower() and set(symbol.lower()) - set(chemical_name.lower()) == set() and len(symbol) == length:
#             return True
#     return False


# def isValid(symbol, chemical_name, length=None):
#     if symbol[0] != symbol[0].upper() or symbol[1:] != symbol[1:].lower() or set(symbol.lower()) - set(
#             chemical_name.lower()) != set():
#         return False
#
#     if length is None:
#         for j in symbol:
#             if j.lower() not in chemical_name.lower():
#                 return False
#
        # counter = 0
        # for i in range(len(symbol)):
        #
        #     if symbol[i].lower() in chemical_name.lower():
        #         position = chemical_name.lower().find(symbol[i].lower())
        #         print(symbol[i], position)
        #         if len(chemical_name) > 1:
        #             chemical_name = chemical_name[position+1:]
        #
        #         elif len(chemical_name) == 1:
        #             chemical_name = ''
        #
        #         counter += 1
        #         print(chemical_name, counter)
        #
        # if len(symbol) != counter:
        #     return False
#         #print(chemical_name.index(symbol[0]))
#
#
#     else:
#         for j in symbol:
#             if j.lower() not in chemical_name.lower():
#                 return False
#         for i in range(0, len(symbol)-1):
#             if chemical_name.lower().index(symbol[i].lower()) > chemical_name.lower().index(symbol[i+1].lower()):
#                 return False
#         #print(chemical_name.index(symbol[0].lower()))
#         if symbol[0] != symbol[0].upper() or symbol[1:] != symbol[1:].lower() or set(symbol.lower()) - set(chemical_name.lower()) != set() or len(symbol) != length:
#             return False
#
#     return True
#
# # def isValid(symbol, chemical_name, length=None):
# #     if symbol[0] != symbol[0].upper() or symbol[1:] != symbol[1:].lower():
# #         return False
# #     symbol = symbol.lower()
# #     chemical_name = chemical_name.lower()
# #     if
#
#
#     # for i in :
#     #
#     #     for j in chemical_name:
#     #
#     # if length is None:
#
#
#
# print(isValid('Zer', 'Zeddemorium'))
# print(isValid('Zer', 'Zeddemorium', 2))
# print(isValid('di', 'Zeddemorium'))
# print(isValid('El', 'Beryllium'))
# print(isValid('M', 'Bismuth', length=1))
# print(isValid('EM', 'Europium'))
# print(isValid('Ce', 'Arsenic', length=2))
# print(isValid('L=num', 'Molybdenum'))


def isValid(symbol, chemical_name, length=None):
    if symbol[0] != symbol[0].upper() or symbol[1:] != symbol[1:].lower():
        return False
    if length is None:
        length = len(symbol)
    if length != len(symbol):
        return False
    symbol = symbol.lower()
    chemical_name = chemical_name.lower()
    counter = 0
    for i in range(len(symbol)):

        if symbol[i].lower() in chemical_name.lower():
            position = chemical_name.lower().find(symbol[i].lower())
            #print(symbol[i], position)
            if len(chemical_name) > 1:
                chemical_name = chemical_name[position + 1:]

            elif len(chemical_name) == 1:
                chemical_name = ''

            counter += 1
            #print(chemical_name, counter)

    if len(symbol) != counter:
        return False
    return True

#
# print(isValid('Zer', 'Zeddemorium'))
# print(isValid('Zer', 'Zeddemorium', 2))
# print(isValid('di', 'Zeddemorium'))
# print(isValid('El', 'Beryllium'))
# print(isValid('M', 'Bismuth', length=1))
# print(isValid('EM', 'Europium'))
# print(isValid('Ce', 'Arsenic', length=2))
# print(isValid('L=num', 'Molybdenum'))


def symbols(chemical_name):
    result = set()
    counter = 0
    for i in chemical_name.lower():
        counter += 1
        for j in chemical_name[counter:].lower():
            #print(j)
            result.add(i.upper()+j)
            #print(result)
    return  result

# print(symbols('Iron'))
# print(symbols('Neon'))

def preference(chemical_name, last=None):
    sorting_chemical_name = sorted(list(symbols(chemical_name)))
    if last is None:
        last = False
    if last == True:
        return sorting_chemical_name[-1]
    else:
        return sorting_chemical_name[0]

print(preference('Iron'))
print(preference('Iron', last=True))
print(preference('Neon'))
print(preference('Neon', True))