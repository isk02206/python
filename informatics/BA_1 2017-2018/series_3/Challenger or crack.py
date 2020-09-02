'''
Name: SungJoon Park
ID: 01514170
'''
n = int(input())

o = 0 #chall_point
c = 0 #crack_point

for i in range(n):
    cor = str(input()) #correct answer of question
    ans = str(input()) #challenger's answer of question
    cra = str(input()) #guess of result of crack
    if cor == ans and cra == 'correct': #crack guesses the correction of the challenger
        c += 1 #point for crack
        o += 1 #point for challenger
    if cor != ans and cra == 'wrong': #crack guesses the wrong of the challenger
        c += 1 #point for crack
    if cor == ans and cra == 'wrong': #challenger is correct challenger earns a point, but crack guesses wrong of the correction
        o += 1 #point for challenger


if c >= n/2 and c > o: #the condition for the crack to win. crack must score more than half of the number of question and crack must score more than the challenger.
    print('crack wins',c,'points against',o)
if o > c or c < n/2: # the condition for the challenger to win. challenger must score more than the crack or when the crack's score is less than the half of the question.
    print('challenger wins', o, 'points against', c)
if c == o and c > n/2: #the condition is a tie. both crack and challenger must have the same score and the crack must score higher than the half of the number of question.
    print('ex aequo: both contestants score',o,'points')
