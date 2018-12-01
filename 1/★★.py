with open('input.txt', 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]

f, b, s, i = 0, {}, len(data), 0
while(1):
    if f in b: print(f); break
    b.update({f: 1})
    f += data[i]; i = (i + 1) % s
