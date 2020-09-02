class Panini:
    def __init__(self, sticker):
        self.sticker = sticker
        if type(self.sticker) == int:
            self.sticker = [self.sticker]
        if type(self.sticker) == tuple:
            self.sticker = list(self.sticker)
        if type(self.sticker) == set:
            self.sticker = list(self.sticker)
        assert (type(self.sticker) == list), str('invalid stickers')

        for c in self.sticker:
            assert (type(c) == int), str('invalid stickers')

    def __str__(self):
        if self.sticker == []:
            return None

        elif type(self.sticker) == int or tuple or set:
            self.sticker = list(self.sticker)
        self.sticker.sort()

        list_1 = []
        for i in range(1, self.sticker[-1] + 1):
            list_1.append(i)

        list_2 = []
        for j in list_1:
            if j not in self.sticker:
                list_2.append(j)

        for p in list_2:
            if p not in self.sticker:
                order = list_1.index(p)
                list_1[order] = ''

        list_3 = []
        list_4 = []
        for q in list_1:
            if q == '':
                if list_3 == []:
                    list_3 = []
                    continue
                else:
                    list_4.append(list_3)
                    list_3 = []
            else:
                list_3.append(q)
        list_4.append(list_3)

        result = ''
        for r in list_4:
            if len(r) != 1:
                result += str(r[0]) + '-' + str(r[-1]) + ', '
            elif len(r) == 1:
                result += str(r[0]) + ', '
        return result[0:-2].rstrip()

    def __repr__(self):
        if self.sticker == []:
            return ''
        return str(self)

    def __add__(self, add_sticker):
        if type(add_sticker.sticker) == int:
            add_sticker = add_sticker

        else:
            add_sticker = list(a for a in add_sticker.sticker)
        return Panini(set(self.sticker + add_sticker))

    def __sub__(self, sub_sticker):
        if type(sub_sticker) == int:
            sub_sticker = sub_sticker

        else:
            sub_sticker = sorted(list(set(list(s for s in sub_sticker.sticker))))
        return Panini(list(s for s in self.sticker if s not in sub_sticker))
