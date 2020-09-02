# read color and value of first playing card
color1 = input()
value1 = input()
# read color and value of second playing card
color2 = input()
value2 = input()
# determine color of the first playing card's mate
if color1 == 'spades':
    mate = 'clubs'
elif color1 == 'hearts':
    mate = 'diamonds'
elif color1 == 'clubs':
    mate = 'spades'
else:
    mate = 'hearts'
# determine whether or not the two cards are mates
mates = ''
if mate != color2 or value1 != value2:
    mates = 'not '
# output whether or not the two cards are mates
template = 'the {} of {} and the {} of {} are {}mates'
print(template.format(value1, color1, value2, color2, mates))