'''
difference_of_age = int(input())
years_after = int(input())
times_of_age = int(input()) 

age_of_mother = int()
age_of_son = int()

age_of_mother = age_of_son+(difference_of_age*12)
age_of_son = (difference_of_age/(times_of_age-1)-years_after)*12

print("The mother is", age_of_mother, "months old and her son", age_of_son, "months.")
'''
difference_of_age = int(input())
years_after = int(input())
times_of_age = int(input()) 

age_of_mother = int()
age_of_son = int()

age_of_mother = (difference_of_age/(times_of_age-1)-years_after)*12+difference_of_age*12
age_of_son = (difference_of_age/(times_of_age-1)-years_after)*12
round_1 = format(age_of_mother, '.0f')
round_2 = format(age_of_son, '.0f')

print("The mother is", round_1, "months old and her son", round_2, "months.")