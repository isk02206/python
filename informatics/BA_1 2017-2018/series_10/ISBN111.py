class ISBN13:
    def __init__(self, code, length=1):
        assert len(str(code)) == 13, 'ISBN13-codes must have 13 numbers'
        assert str(code).isdigit(), 'ISBN13-codes must have 13 numbers'
        assert 1 <= length <= 5, 'ISBN13-codes is in between 1 and 5 numbers'

        self.code = code
        self.length = length

    def __str__(self):
        code = str(self.code)
        return '{}-{}-{}-{}'.format(
            code[:3],
            code[3:3 + self.length],
            code[3 + self.length:-1],
            code[-1]
        )

    def __repr__(self):
        return 'ISBN13({}, {})'.format(self.code, self.length)

    def isValid(self):
        code = str(self.code)
        answer = 0
        for i in range(12):
            if i % 2:
                answer += 3 * int(code[i])
            else:
                answer += int(code[i])
        answer = (10 - (answer % 10)) % 10
        return answer == int(code[12])

    def asISBN10(self):
        if not self.isValid() or str(self.code)[:3] == '979':
            return None
        else:
            code = str(self.code)[3:-1]
            answer = 0
            for i in range(9):
                answer += (i + 1) * int(code[i])
            answer %= 11
            if answer == 10:
                answer = 'X'
            else:
                answer = str(answer)
            return '{}-{}-{}'.format(
                code[:self.length],
                code[self.length:],
                answer
            )


if __name__ == '__main__':
    import doctest

    doctest.testmod()