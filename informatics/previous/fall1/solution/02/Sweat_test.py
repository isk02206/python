#read patient's age (in months)
age = int(input())

# read chloride concentration (in mmol/L)
concentration = int(input())

# make diagnose
if ((age <= 6 and concentration < 30) or(age > 6 and concentration < 40)):
    diagnose = 'very unlikely'
elif concentration < 60:
    diagnose = 'possible'
else:
    diagnose = 'likely'

# output diagnose
print('CF is {}'.format(diagnose))