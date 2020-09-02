'''
Created on 2015. 12. 3.

@author: User
'''
read card properties
side = input() # which side is on top: color or value
card = input() # card description: text or digit
# read answer of a person on the question whether or not the card must be turned
answer = (input() == ’yes’)
# determine whether or not the card must be turned
if side == ’color’:
correct = (card != ’red’)
else:
correct = not bool(int(card) % 2)
# generate formatted output
print(
’{}: cards with {} {} must {}be turned.’.format(
’Correct’ if answer == correct else ’Wrong’,
side,
card,
’’ if correct else ’not ’
)
)
2.6 Darts
from math import sqrt, atan2, pi, degrees
# read position in Cartesian coordinates
x, y = float(input()), float(input())
# convert Cartesian coordinates into polar coordinates
eps = 1e-6
if abs(x) < eps and abs(y) < eps:
r, t = 0.0, 0.0
else:
r, t = sqrt(x ** 2 + y ** 2), atan2(y, x)
# some scores only depend on the radius r; in these cases there is not need to
# determine the index of the sector in which the dart is thrown
if r >= 170.0:
# darts outside the board get no score
score = 0
elif r < (12.7 / 2):
# bull’s eye
score = 50
elif r < (31.8 / 2):
# bull
score = 25
else:
5
# invert and shift angle in polar coordinates
sectors = 20
t = (pi / 2.0 + pi / sectors - t) % (2 * pi)
# compute index of sector
index = int(t * sectors / (2 * pi))
# basic score is one unit higher than index
score = index + 1
# correct score based on distance to center
if 107.0 - 9.6 < r < 107.0:
# triple ring
score *= 3
elif 170.0 - 9.6 < r < 170.0:
# double ring
score *= 2
# print the final score
print(score)
3 series 03
3.1 ISBN
# read the first digit of a ISBN-10 code
x1 = input()
while x1 != ’stop’:
# read the next digits and compute check digit
checkdigit = int(x1)
for i in range(2, 10):
checkdigit += i * int(input())
checkdigit %= 11
# test check digit
print(’OK’ if checkdigit == int(input()) else ’WRONG’)
# read first digit of next ISBN-10 code
x1 = input()
3.2 Con proofing
# flip a coin twice
coin1 = input()
coin2 = input()
# flip the coin twice again as long as the two outcomes are the same
while coin1 == coin2:
coin1 = input()
coin2 = input()
# determine which side wins
print(’{} wins’.format(coin1))
6
3.3 Visiting friends
# read day
day = int(input())
# initialize arrows
arrow1, arrow2, arrow3 = [True] * 3
# simulate visits on successive days
for _ in range(day):
# follow arrow1
if arrow1:
# follow arrow2
house = ’A’ if arrow2 else ’B’
# turn arrow2
arrow2 = not arrow2
else:
# follow arrow3
house = ’C’ if arrow3 else ’D’
# turn arrow3
arrow3 = not arrow3
# turn arrow1
arrow1 = not arrow1
print(house)
"""
There exists a solution that only requires a single line of code and no loops.
To understand the solution, you need to understand string indexing and make the
observation that there is a repetitive pattern in the order the villages are
visited on successive days:
A, C, B, D, A, C, B, D, A, C, B, D, A, C, B, D, ...
The one-line solution then becomes
print(’DACB’[int(input()) % 4])
"""
3.4 The frog prince
# math module defines the value e
import math
# read the number of frogs
frogs = int(input())
# determine the number of frogs that need to be evaluated first, before we
# really start selecting one of the frogs
frogs_sequence1 = math.ceil(frogs / math.e)
# determine maximal score of frogs in initial sequence; we do this using a for
# loop since we know in advance how many frogs need to be evaluated initially
# once we know the total number of frogs
max_score = float(input())
for _ in range(1, frogs_sequence1):
score = float(input())
if score > max_score:
max_score = score
7
# evaluate the remaining frogs until we find a frog having a higher score than
# all frogs in the initial sequence or until all frogs have been evaluated; we
# do this using a while loop since we do not know in advance whether we will
# stop evaluating early on or only after having seen all remaining frogs
score = float(input())
frog = frogs_sequence1 + 1
while frog < frogs and score < max_score:
score = float(input())
frog += 1
# output score of the last frog evaluated; either this is the first frog from
# the remaining sequence of frogs that had a higher score than all frogs in the
# list that was evaluated initially, or it is just the last frog in the sequence
print(score)
3.5 Babylonian method
# read value whose square root needs to be computed
s = float(input())
# read initial approximation of the square root
x1 = float(input())
if min(s, x1) <= 0.0:
print(’invalid input’)
else:
# output initial approximation of the square root
index = 0
print(’{}: {}’.format(index, x1))
# compute more accurate approximations according to Babylonian method;
# first part of the condition (index == 0) is needed because we need at
# least two successive approximations before we can evaluate the stop
# condition
while index == 0 or abs(x1 - x0) / x1 > 1e-15:
# increment index by 1
index += 1
# remember previous approximation as x0
x0 = x1
# compute new approximation as x1
x1 = 0.5 * (x0 + s / x0)
# output new approximation of the square root
print(’{}: {}’.format(index, x1))
3.6 Elevator paradox
# read information about the simulation
steps = int(input()) # number of steps in simulation
floor_start = int(input()) # index of floor where simulation starts
floor_top = int(input()) # index of top floor
direction = -1 if input() == ’v’ else 1 # initial direction of elevator
hour = int(input()) # time at start of simulation (hours)
minute = int(input()) # time at start of simulation (minutes)
verbose = input() == ’verbose’ # verbose output of information?
# simulation starts at given floor
8
floor = floor_start
# simulate successive steps of the elevator
for _ in range(steps):
# modify direction if elevator arrives at lobby or top floor
if floor == 0:
direction = 1
elif floor == floor_top:
direction = -1
# output information at the current floor
if verbose or floor == floor_start:
print(’{:02d}:{:02d} {} [{}]’.format(
hour,
minute,
floor,
’v’ if direction == -1 else ’ˆ’
))
# go to next floor
floor += direction
# step one minute forward in time
minute += 1
if minute == 60:
hour = (hour + 1) % 24
minute = 0
4 series 04
4.1 ISBN
# read first ISBN-10 code
code = input()
# read successive ISBN-10 codes until a line is read that only contains the word
# stop
while code != ’stop’:
# compute check digit
check_digit = int(code[0])
for i in range(2, 10):
check_digit += i * int(code[i - 1])
check_digit %= 11
# extract check digit from ISBN-10 code
x10 = code[9]
# check whether computed and extracted check digits are same
if (check_digit == 10 and x10 == ’X’) or x10 == str(check_digit):
print(’OK’)
else:
print(’WRONG’)
# read next ISBN-10 code
code = input()
4.2 Rorschach test
# read first line
line = input()
9
# while current line is not empty
while line:
# output line and the mirrored line
print(line + line[::-1])
# read next line
line = input()

4.6 Trevanion
import string
# either we are looking for the next punctuation mark, or we are looking for the
# third letter following the punctuation mark; we use a variable as a switch
# that indicates what we are currently looking for
findPunctuation = True
# find the secret message by traversing all characters of the given text from
# top to bottom and from left to right, each time appending the third letter
# following a punctuation mark to the secret message
lines, secret = int(input()), ’’
for _ in range(lines):
# read the next line (lines are processed from top to bottom)
line = input()
# traverse all characters in the line from left to right
for character in line:
if findPunctuation and character in string.punctuation:
# start looking for third character following punctuation mark
findPunctuation, letters = False, 0
elif not findPunctuation and character.isalpha():
# yet another letter found
letters += 1
11
# append third letter to the secret message and start looking for
# the next punctuation mark
if letters == 3:
secret += character
findPunctuation = True
# print the secret message (using lowercase letters only)
print(secret.lower())