a = int(input())

if a == 0:
    b = "no"
elif 1 <= a <= 5:
    b = "weak"
elif 6 <= a <= 30:
    b = "moderate"
else:
    b = "high"

print("There is", b, "risk of an allergic reaction at", a, "pollen per cubic metre.")