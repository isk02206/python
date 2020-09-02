a = str(input())
b = int(input())  # beat per minute
c = int(input())  # average life

beat = (b * 60 * 24 * 365 * c) / 10 ** 9

beat = format(beat, '.2f')

print(a, 'have', beat, 'billion heartbeats')