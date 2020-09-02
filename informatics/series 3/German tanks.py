m = int(input())

serial_number = [m]

while m > 0:

    m = int(input())
    if m > 0:
        serial_number.append(m)

#print(serial_number)
count_number = len(serial_number)
#print(count_number)
max_number = max(serial_number)
#print(max_number)

t = (((count_number + 1) * max_number) / count_number) - 1

print('The number of produced tanks is estimated to be', str(round(t)) + '.')