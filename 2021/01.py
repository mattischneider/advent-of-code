with open("2021/01.txt", 'r') as f:
    d = [int(l) for l in f.readlines()]

print('part 1:', sum(1 for i in range(1, len(d)) if d[i] > d[i-1]))
print('part 2:', sum(1 for i in range(1, len(d))
      if sum(d[i:i+3]) > sum(d[i-1:i+2])))
