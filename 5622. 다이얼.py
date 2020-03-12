address = input()
addressList = list(address)
#print(address[0])
count = 0

for i in range(len(address)):
    if address[i] == "A" or address[i] == "B" or address[i] == "C":
        count += 3
    elif address[i] == "D" or address[i] == "E" or address[i] == "F":
        count += 4
    elif address[i] == "G" or address[i] == "H" or address[i] == "I":
        count += 5
    elif address[i] == "J" or address[i] == "K" or address[i] == "L":
        count += 6
    elif address[i] == "M" or address[i] == "N" or address[i] == "O":
        count += 7
    elif address[i] == "P" or address[i] == "Q" or address[i] == "R" or address[i] == "S":
        count += 8
    elif address[i] == "T" or address[i] == "U" or address[i] == "V":
        count += 9
    elif address[i] == "W" or address[i] == "X" or address[i] == "Y" or address[i] == "Z":
        count += 10

print(count)