with open('in.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

#result = 'zihwtxagifpbsnwleydukjmqv'
for current in data:
    for other in data:
        differ = 0
        r = ''
        # Compare the two
        for i in range(len(current)):
            if current[i] != other[i]:
                differ += 1
            else:
                r += current[i]
        if differ == 1:
            break
    else:
        continue
    break

print(r)