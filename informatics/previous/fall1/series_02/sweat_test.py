
age = int(input())
chloride_level = int(input())

if age <= 6 :
    if chloride_level<=29:
        print("CF is very unlikely")
    elif chloride_level<=59:
        print("CF is possible")
    else:
        print("CF is likely")
if age > 6 :
    if chloride_level<=39:
        print("CF is very unlikely")
    elif chloride_level<=59:
        print("CF is possible")
    else:
        print("CF is likely")