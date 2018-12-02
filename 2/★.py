with open('in.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

x, y = 0,0
for line in data:
    table, two, three = [0] * 26, 0, 0
    for i in [ord(char) - 97 for char in line.lower()]:
        table[i] += 1
    for i in table:
        if i == 2:
            two = 1
        if i == 3:
            three = 1
        if two + three == 2:
            break
    x += two
    y += three

print(x * y)
    