def width(row):
    if len(row) == 1:
        row = list(row)
        result = row[0][0] + row[0][1]
        return result
    else:
        group = []
        row = list(row)
        for x in range(len(row)):
            group.append(row[x][0])
        for y in range(len(row)):
            if max(group) == row[y][0]:
                result = row[y][0] + row[y][1]
        return result


def line(row, endline=None):
    line = ''
    row = list(row)
    row.sort()
    line += ' ' * row[0][0]
    line += '#' * row[0][1]

    if len(row) == 1:
        if endline == None:
            return line
        else:
            while len(line) != endline:
                line += ' '
            return line

    if len(row) != 1:
        for x in range(1, len(row)):
            while len(line) != row[x][0]:
                line += ' '
            line += '#' * row[x][1]
        if endline == None:
            return line
        else:
            while len(line) != endline:
                line += ' '
            return line


def widthchecker(puzzle):
    reader = open(puzzle, 'r')
    widthchk = []

    lines = reader.readline()
    while lines:
        if ';' in lines:
            lines = lines.replace(';', ',')
            lines = (eval(lines))
            widthchk.append(width(lines))
        else:
            lines = [eval(lines)]
            widthchk.append(width(lines))
        lines = reader.readline()
    return max(widthchk)
    reader.close()


def nonogram(puzzle, solution):
    reader = open(puzzle, 'r')
    result = ''
    results = ''
    widthchk = widthchecker(puzzle)

    lines = reader.readline()
    while lines:
        if ';' in lines:
            lines = lines.replace(';', ',')
            lines = (eval(lines))
            result = line(lines, widthchk)
        else:
            lines = [eval(lines)]
            result = line(lines, widthchk)

        results = results + result + '\n'
        lines = reader.readline()
    reader.close()

    writer = open(solution, 'w')
    writer.write(results)
    writer.close()