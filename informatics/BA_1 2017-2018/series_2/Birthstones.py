stone = str(input())

if stone == 'garnet':
    month = 'January'
if stone == 'amethyst':
    month = 'February'
if stone == 'bloodstone' or stone == 'aquamarine':
    month = 'March'
if stone == 'diamond' or stone == 'rock crystal':
    month = 'April'
if stone == 'emerald' or stone == 'chrysoprase':
    month = 'May'
if stone == 'pearl' or stone == 'moonstone' or stone == 'alexandrite':
    month = 'June'
if stone == 'ruby' or stone == 'carnelian':
    month = 'July'
if stone == 'sardonyx' or stone == 'spinel' or  stone == 'peridot':
    month = 'August'
if stone == 'sapphire':
    month = 'September'
if stone == 'opal' or stone == 'tourmaline':
    month = 'October'
if stone == 'topaz' or stone == 'citrine':
    month = 'November'
if stone == 'turquoise' or stone == 'zircon' or stone == 'tanzanite':
    month = 'December'

if stone == 'lapis lazuli':
    month = 'September or December'

print(stone,'is a birthstone of the month',month)