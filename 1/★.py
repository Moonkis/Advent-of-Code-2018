with open('input.txt', 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]
print(sum(data))