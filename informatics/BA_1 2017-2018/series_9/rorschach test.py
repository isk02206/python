def rorschach(text, rorschach=False):
    reader = open(text, 'r')
    lines = ''
    result = ''
    results = ''
    line = reader.readline()
    while line:
        lines = line[::-1]
        result = line + lines
        result = "".join(result.splitlines()) + "\n"
        results += result
        line = reader.readline()
    reader.close()

    if rorschach == False:
        print(results[:len(results) - 1])
    else:
        writer = open(rorschach, 'w')
        writer.write(results)
        writer.close()