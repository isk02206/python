'''
name : Ha Young Kim
student number : 01603259
'''

#The input contains four integers a,b,n and t
a = int(input())
b = int(input())
n = int(input())
t = int(input())

#At the beginning of the first experiment, there is a single cell in the test tube.
first = 1
#list_1 = the list of gradually growing cells(experiment1) as time goes on
list_1 = [1]
#radiate the test tube for n seconds during the first experiment
for i in range (n):
    #if at a given point in time there are x cells in a test tube, one second later there are ax+b cells in the test tube.
    second = a*first + b
    list_1.append(second)
    #to calculate with a new number(the value of 'first' is changed.)
    first = second

#result_1 indicates how many cells the test tube contains at the end of the experiment
result_1 = list_1[len(list_1)-1]

#starting second
s = 0
#to obtain at least 'result_1' cells in the test tube
while t < result_1:
    #if at a given point in time there are x cells in a test tube, one second later there are ax+b cells in the test tube.
    t = a*t + b
    #to obtain an increasing value 's' with a loop(s:how many seconds s you will need to radiate the test tube so to obtain at least z cells in the test tube.
    s+=1

print('experiment #1:',result_1,'cells after',n,'seconds')
print('experiment #2:',t,'cells after',s,'seconds')